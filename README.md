<div align="center">

<img src="src/refrata/resources/brand/icon-256.png" alt="Cine60" width="112" height="112">

# Cine60

**A video and music player on the VLC engine, with smooth motion at 60 fps.**

[Download](https://github.com/adrianobbarcelos/Cine60/releases/latest) · [Report a problem](https://github.com/adrianobbarcelos/Cine60/issues/new/choose) · [Changelog](CHANGELOG.md) · [Português](README.pt-BR.md)

</div>

Cine60 is a fork of [Refrata](https://github.com/LucsLabsStudios/refrata) by LucsLabs Studios, under the same
GPL-3.0 license. Most of the program comes from it.

## What Cine60 adds

- A **Picture panel** in the player (`G`): smooth motion, detail and light boost, presets. `V` turns smooth
  motion on and off; `Shift+V` switches the preset.
- **Smooth motion** timed by when each frame was displayed, with scene cuts found in dark scenes too.
- **A faster first start**: VLC's plugin cache stays valid in any time zone.
- **Controls that hide** when the mouse rests.

## What comes from Refrata

VLC's formats and protocols, the library, subtitles (AI ones included), equalizer, picture-in-picture,
casting and 14 languages.

## Known problems

- With very fast camera moves, parts of the picture may tear while smooth motion is on.
- True HDR output is off: with Windows HDR on it darkened SDR video. HDR video is converted to SDR.
- The installer has no Windows code signature: SmartScreen may warn about an unknown publisher.
- No Linux version is published; only the tests run on Linux.

## Install

Windows 10 or 11, 64-bit: [download](https://github.com/adrianobbarcelos/Cine60/releases/latest) `Cine60-Setup-<version>.exe`, which needs no
administrator rights, or `Cine60-<version>-portable.zip`, which needs no installation. Updates are accepted
only with the Cine60 Ed25519 signature.

## Build

The [build workflow](.github/workflows/build.yml) is the recipe used for releases. More in
[docs/development.md](docs/development.md) (inherited from Refrata).

## License

[GPL-3.0](LICENSE). Refrata © LucsLabs Studios. Bundles libVLC (VideoLAN, LGPL 2.1+) and Qt for Python
(LGPL 3). VLC is a trademark of VideoLAN; Cine60 is independent of it and of LucsLabs Studios.
