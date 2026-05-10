# Macast 开发指南

> **注意：本项目仅支持 macOS (Apple Silicon)。**

## 环境要求

- **macOS**: 15.0 Sequoia 或更高版本（推荐 macOS 26 Tahoe）
- **芯片**: Apple Silicon (M1/M2/M3/M4) - arm64
- **Python**: 3.12+（推荐 3.13 或 3.14）
- **Xcode Command Line Tools**: 已安装

---

## 开发环境配置

### 1. 克隆代码

```shell
git clone https://github.com/smkuse/Macast.git
cd Macast
```

### 2. 下载 mpv

```shell
wget https://laboratory.stolendata.net/~djinn/mpv_osx/mpv-latest.tar.gz
mkdir -p bin && tar --strip-components 2 -C bin -xzvf mpv-latest.tar.gz mpv.app/Contents/MacOS
```

### 3. 安装依赖

```shell
# 创建虚拟环境（推荐）
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements/darwin.txt
```

### 4. 运行调试

```shell
python Macast.py
```

---

## 打包发布

### 使用 py2app 打包

```shell
# 安装 py2app
pip install py2app

# 构建 arm64 版本
python setup_py2app.py py2app --arch=arm64

# 复制 mpv 到 App Bundle
cp -R bin dist/Macast.app/Contents/Resources/

# 验证
open dist
```

### 创建 DMG 安装包

```shell
# 安装 create-dmg
brew install create-dmg

# 创建 DMG
VERSION=$(cat macast/.version)
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

## 项目结构

```
Macast/
├── macast/                 # 核心模块
│   ├── gui.py             # GUI 界面 (rumps)
│   ├── macast.py          # 主应用逻辑
│   ├── server.py          # HTTP 服务器
│   ├── ssdp.py            # SSDP 发现服务
│   ├── protocol.py        # DLNA 协议实现
│   ├── renderer.py        # 渲染器基类
│   ├── plugin.py          # 插件系统
│   ├── utils.py           # 工具函数
│   └── xml/               # DLNA XML 描述文件
├── macast_renderer/        # 渲染器实现
│   └── mpv.py             # MPV 播放器渲染器
├── i18n/                   # 国际化翻译文件
├── requirements/           # 依赖文件
│   └── darwin.txt         # macOS 依赖
├── Macast.py              # 应用入口
├── setup.py               # pip 安装配置
└── setup_py2app.py        # py2app 打包配置
```

---

## 常见问题

### Q1: 提示 "No module named 'rumps'"

```shell
pip install rumps pyperclip
```

### Q2: py2app 构建失败

```shell
# 清理缓存后重试
rm -rf build dist
python setup_py2app.py py2app --arch=arm64
```

### Q3: mpv 无法运行

确保下载的是 Apple Silicon 版本:

```shell
file bin/mpv
# 应包含 arm64，而不是仅 x86_64
```

### Q4: App 打开后闪退

检查日志:

```shell
# 查看系统日志
log stream --predicate 'process == "Macast"' --level debug

# 或从终端运行查看错误
./dist/Macast.app/Contents/MacOS/Macast
```

---

## 详细构建指南

完整的构建步骤请参考 [macOS 构建指南](../MACOS_BUILD_GUIDE.md)。

---

*最后更新: 2026-05-10*
