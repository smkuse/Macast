# Macast

[![build](https://img.shields.io/github/actions/workflow/status/smkuse/Macast/build-macast.yaml?branch=main&label=build)](https://github.com/smkuse/Macast/actions/workflows/build-macast.yaml)
[![release](https://img.shields.io/github/v/release/smkuse/Macast?label=latest%20release)](https://github.com/smkuse/Macast/releases/latest)
[![mac](https://img.shields.io/badge/platform-macOS%2015.0%2B%20(Tahoe)-lightgrey?logo=Apple)](https://github.com/smkuse/Macast/releases/latest)
[![license](https://img.shields.io/github/license/smkuse/Macast)](LICENSE)

> **⚠️ 注意：此仓库是原项目 [xfangfang/Macast](https://github.com/xfangfang/Macast) 的 Fork。**
> 
> 由于原项目已长期未更新，无法在最新的 macOS 系统上正常运行，故在此 Fork 基础上做了以下改动以继续使用：
> - 原生支持 **macOS 26 Tahoe (Apple Silicon M 系列芯片)**
> - 升级所有 Python 依赖到最新版本
> - 使用 `netifaces-plus` 替代已停止维护的 `netifaces`
> - 修复 py2app 打包后 .app 播放视频后无响应的问题
> - 升级 CI/CD (GitHub Actions)，自动构建并发布 DMG
> - **平台支持：仅支持 macOS (Apple Silicon)**

[English](README.md)

一个使用 mpv 作为 **DLNA 媒体渲染器** 的菜单栏应用。你可以将手机上的视频、图片或音乐推送到 Mac 上播放。

---

## 📥 下载

### macOS (Apple Silicon)

**从 [Releases](https://github.com/smkuse/Macast/releases/latest) 下载**

| 文件 | 说明 |
|------|------|
| `Macast-MacOS-arm64-*.dmg` | Apple Silicon (M1/M2/M3/M4) 安装包 |
| `*.sha256` | SHA256 校验和文件 |

**系统要求：**
- macOS 15.0 Sequoia 或更高版本（推荐 macOS 26 Tahoe）
- Apple Silicon Mac (M1/M2/M3/M4)

---

## 📦 安装

### 方式一：下载 DMG（推荐）

1. 访问 [Releases](https://github.com/smkuse/Macast/releases/latest) 页面
2. 下载 `Macast-MacOS-arm64-*.dmg`
3. 打开 DMG 文件
4. 将 `Macast.app` 拖入应用程序文件夹

### 方式二：通过 pip 安装

```shell
pip install macast
macast-gui  # 或 macast-cli
```

### 方式三：从源码构建

请参考：[macOS 构建指南](MACOS_BUILD_GUIDE.md)

---

## 🚀 使用方法

打开应用后，菜单栏会出现一个小图标，然后你就可以从 DLNA 客户端（如手机）将媒体文件推送到 Mac 上播放。

### 支持的 DLNA 客户端
- iOS: nPlayer、Infuse 等
- Android: BubbleUPnP、VLC 等
- Windows: Windows Media Player
- 其他 DLNA/UPnP 兼容应用

---

## ⚙️ 功能特性

- **DLNA 媒体渲染器**：接收来自任何 DLNA 客户端的媒体
- **MPV 集成**：高质量视频播放
- **菜单栏应用**：轻量级，后台运行
- **多语言支持**：英语、中文、芬兰语、意大利语

---

## 🔧 开发

构建说明请参考 [开发指南](docs/Development.md)。

---

## 📄 许可证

本项目采用 GPL-3.0 许可证 - 详情请见 [LICENSE](LICENSE) 文件。

---

## 🙏 致谢

- 原项目作者 [xfangfang](https://github.com/xfangfang)
- DLNA 实现基于 [coherence](https://github.com/coherence-project/coherence)
