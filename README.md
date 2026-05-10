<img align="center" src="macast_slogan.png" alt="slogan" height="auto"/>

# Macast

[![build](https://img.shields.io/github/actions/workflow/status/smkuse/Macast/build-macast.yaml?branch=main&label=build)](https://github.com/smkuse/Macast/actions/workflows/build-macast.yaml)
[![release](https://img.shields.io/github/v/release/smkuse/Macast?label=latest%20release)](https://github.com/smkuse/Macast/releases/latest)
[![mac](https://img.shields.io/badge/platform-macOS%2015.0%2B%20(Tahoe)-lightgrey?logo=Apple)](https://github.com/smkuse/Macast/releases/latest)
[![license](https://img.shields.io/github/license/smkuse/Macast)](LICENSE)

> **⚠️ Note: This is a fork of [xfangfang/Macast](https://github.com/xfangfang/Macast).**
> 
> The original project is no longer maintained and doesn't work on latest macOS. This fork includes:
> - Native support for **macOS 26 Tahoe (Apple Silicon M-series)**
> - Updated Python dependencies to latest versions
> - Replaced deprecated `netifaces` with `netifaces-plus`
> - Fixed py2app packaging issues
> - Updated CI/CD with GitHub Actions for automatic DMG builds
> - **Platform support: macOS only (Apple Silicon)**

[中文说明](README_ZH.md)

A menu bar application using mpv as **DLNA Media Renderer**. You can push videos, pictures or musics from your mobile phone to your computer.

---

## 📥 Download

### macOS (Apple Silicon)

**Download from [Releases](https://github.com/smkuse/Macast/releases/latest)**

| File | Description |
|------|-------------|
| `Macast-MacOS-arm64-*.dmg` | DMG installer for Apple Silicon (M1/M2/M3/M4) |
| `*.sha256` | SHA256 checksum file |

**System Requirements:**
- macOS 15.0 Sequoia or later (macOS 26 Tahoe recommended)
- Apple Silicon Mac (M1/M2/M3/M4)

---

## 📦 Installation

### Option 1: Download DMG (Recommended)

1. Go to [Releases](https://github.com/smkuse/Macast/releases/latest)
2. Download `Macast-MacOS-arm64-*.dmg`
3. Open the DMG file
4. Drag `Macast.app` to Applications folder

### Option 2: Install via pip

```shell
pip install macast
macast-gui  # or macast-cli
```

### Option 3: Build from source

Please refer to: [macOS Build Guide](MACOS_BUILD_GUIDE.md)

---

## 🚀 Usage

After opening this app, a small icon will appear in the **menu bar**, then you can push your media files from a DLNA client (such as your phone) to your Mac.

### Supported DLNA Clients
- iOS: nPlayer, Infuse, etc.
- Android: BubbleUPnP, VLC, etc.
- Windows: Windows Media Player
- Other DLNA/UPnP compatible apps

---

## ⚙️ Features

- **DLNA Media Renderer**: Receive media from any DLNA client
- **MPV Integration**: High-quality video playback
- **Menu Bar App**: Lightweight, runs in background
- **Multi-language Support**: English, Chinese, Finnish, Italian

---

## 🔧 Development

See [Development Guide](docs/Development.md) for build instructions.

---

## 📄 License

This project is licensed under GPL-3.0 - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Credits

- Original project by [xfangfang](https://github.com/xfangfang)
- DLNA implementation based on [coherence](https://github.com/coherence-project/coherence)
