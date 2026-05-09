# Macast macOS Apple Silicon 本地打包指南

## 环境要求

- **macOS**: 12.0 Monterey 或更高版本
- **芯片**: Apple Silicon (M1/M2/M3) - arm64
- **Python**: 3.12 (推荐)
- **Xcode Command Line Tools**: 已安装

---

## 步骤 1: 安装依赖

### 1.1 安装 Homebrew (如未安装)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 1.2 安装必要工具
```bash
# 安装 Python 3.12
brew install python@3.12

# 安装 create-dmg (用于生成 DMG 安装包)
brew install create-dmg

# 安装 gettext (用于编译翻译文件)
brew install gettext
```

### 1.3 确保使用 Python 3.12
```bash
# 检查 Python 版本
python3 --version  # 应显示 3.12.x

# 如需要，链接 Python 3.12
export PATH="/opt/homebrew/opt/python@3.12/bin:$PATH"
```

---

## 步骤 2: 克隆代码

```bash
# 克隆您的 fork
git clone https://github.com/smkuse/Macast.git
cd Macast

# 切换到适配后的代码分支
git checkout main  # 或包含 Apple Silicon 适配的分支
```

---

## 步骤 3: 安装 Python 依赖

```bash
# 创建虚拟环境（推荐）
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements/darwin.txt
pip install py2app
```

---

## 步骤 4: 下载 mpv (Apple Silicon 版本)

```bash
# 创建 bin 目录
mkdir -p bin

# 下载 mpv 最新版 (包含 Apple Silicon 支持)
curl -L -o mpv-latest.tar.gz \
  "https://laboratory.stolendata.net/~djinn/mpv_osx/mpv-latest.tar.gz"

# 解压 mpv
tar --strip-components 2 -C bin -xzvf mpv-latest.tar.gz \
  mpv.app/Contents/MacOS

# 验证 mpv 架构
file bin/mpv  # 应显示 "arm64" 或 "universal"
```

---

## 步骤 5: 编译翻译文件

```bash
for file in i18n/*/LC_MESSAGES/macast.po; do
    dir=$(dirname "$file")
    msgfmt -o "$dir/macast.mo" "$file"
    echo "Compiled: $file"
done
```

---

## 步骤 6: 构建 App

```bash
# 使用 py2app 构建 arm64 版本
python3 setup_py2app.py py2app --arch=arm64

# 将 mpv 复制到 App Bundle
cp -R bin dist/Macast.app/Contents/Resources/

# 验证 App 架构
file dist/Macast.app/Contents/MacOS/Macast
# 应显示: Mach-O 64-bit executable arm64
```

---

## 步骤 7: 创建 DMG 安装包

```bash
# 读取版本号
VERSION=$(cat macast/.version)

# 创建 DMG
create-dmg \
  --window-pos 200 120 \
  --window-size 800 400 \
  --icon-size 100 \
  --icon "Macast.app" 200 190 \
  --hide-extension "Macast.app" \
  --app-drop-link 600 185 \
  --volname "Macast-v${VERSION}-arm64 Installer" \
  "Macast-MacOS-arm64-v${VERSION}.dmg" \
  "dist/"
```

---

## 步骤 8: 验证构建结果

```bash
# 检查 DMG 文件
ls -lh Macast-MacOS-arm64-v*.dmg

# 挂载 DMG 测试
open Macast-MacOS-arm64-v*.dmg

# 检查 App 签名/公证状态 (可选)
codesign -dv --verbose=4 dist/Macast.app
```

---

## 完整一键脚本

创建 `build_macos.sh`:

```bash
#!/bin/bash
set -e

echo "=== Macast macOS Apple Silicon 构建脚本 ==="

# 检查环境
if [[ $(uname -m) != "arm64" ]]; then
    echo "警告: 当前不是 arm64 架构，构建的 App 可能无法在 Apple Silicon 上原生运行"
fi

# 安装依赖
echo "[1/6] 安装依赖..."
pip install -r requirements/darwin.txt
pip install py2app

# 下载 mpv
echo "[2/6] 下载 mpv..."
if [ ! -d "bin" ]; then
    mkdir -p bin
    curl -L -o mpv-latest.tar.gz "https://laboratory.stolendata.net/~djinn/mpv_osx/mpv-latest.tar.gz"
    tar --strip-components 2 -C bin -xzvf mpv-latest.tar.gz mpv.app/Contents/MacOS
    rm mpv-latest.tar.gz
fi

# 编译翻译
echo "[3/6] 编译翻译文件..."
for file in i18n/*/LC_MESSAGES/macast.po; do
    dir=$(dirname "$file")
    msgfmt -o "$dir/macast.mo" "$file"
done

# 构建 App
echo "[4/6] 构建 App..."
python3 setup_py2app.py py2app --arch=arm64
cp -R bin dist/Macast.app/Contents/Resources/

# 创建 DMG
echo "[5/6] 创建 DMG..."
VERSION=$(cat macast/.version)
if command -v create-dmg &> /dev/null; then
    create-dmg \
      --window-pos 200 120 \
      --window-size 800 400 \
      --icon-size 100 \
      --icon "Macast.app" 200 190 \
      --hide-extension "Macast.app" \
      --app-drop-link 600 185 \
      --volname "Macast-v${VERSION}-arm64 Installer" \
      "Macast-MacOS-arm64-v${VERSION}.dmg" \
      "dist/"
    echo "[6/6] 构建完成: Macast-MacOS-arm64-v${VERSION}.dmg"
else
    echo "[6/6] 构建完成 (无 DMG): dist/Macast.app"
    echo "提示: 安装 create-dmg 可生成 DMG 安装包"
fi
```

赋予执行权限并运行:
```bash
chmod +x build_macos.sh
./build_macos.sh
```

---

## 常见问题

### Q1: 提示 "No module named 'rumps'"
```bash
pip install rumps pyperclip
```

### Q2: py2app 构建失败
```bash
# 清理缓存后重试
rm -rf build dist
python3 setup_py2app.py py2app --arch=arm64
```

### Q3: mpv 无法运行
确保下载的是 Apple Silicon 版本:
```bash
file bin/mpv
# 应包含 arm64，而不是仅 x86_64
```

### Q4: App 打开后闪退
检查日志:
```bash
# 查看系统日志
log stream --predicate 'process == "Macast"' --level debug

# 或从终端运行查看错误
./dist/Macast.app/Contents/MacOS/Macast
```

---

## 输出文件

构建成功后，您将得到:
- `dist/Macast.app` - 可直接运行的 App
- `Macast-MacOS-arm64-v{VERSION}.dmg` - 安装包 (如安装了 create-dmg)

---

*最后更新: 2025-01-09*
