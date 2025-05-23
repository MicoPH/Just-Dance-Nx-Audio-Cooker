# **Just Dance Nx Audio Cooker**

## Credits
- [MicoPH](https://github.com/MicoPH/)
- [MZommer](https://github.com/MZommer) - UbiArtPY (few codes have in this script)


## Requirements

---
- [FFMPEG](https://ffmpeg.org) -  ffmpeg.org - [Link](https://ffmpeg.org)
- [VGMStream](https://github.com/vgmstream/vgmstream) - Backup Audio
- [VGAudio](https://github.com/Thealexbarney/VGAudio) - for Nintendo Switch _Opus_ (Note: This Released Version of VGAudio is outdated)

---

## FAQ

#### Q: Can i change the value in `config.json`?

_A: Yes_

#### Q: Is that supported from any platform?

_A: maybe, for cooked pcm but opus didn't supported for nx only_

#### Q:is the format of nintendo opus the same as default opus?

_A:No, because the nintendo opus has a different codes_

#### Q:What Nx means?

_A:the codename on Nintendo Switch_


## Changelog

[Expand](https://github.com/MicoPH/Just-Dance-Nx-Audio-Cooker/blob/main/changelog.md)

---
## Supported Formats
- `.ogg` - Ogg Vorbis
- `.opus` - .opus (ffmpeg)
- `.wav` - Wave (PCM)
- `.mp3` - MPEG Layer 3

---

## Configs Tutorial
### Bitrate Value:
| Bit rate (_kilobytes_) | Config value (_bytes_)|
| :-----| :----------------- |
|64kbps | 64000
|92kbps | 92000
|128kbps | 128000
|256kbps | 256000 
|320kbps | 320000

- `256kbps` is the default _bitrate_ in `opus`
- `320kbps` is the default _bitrate_ in `vorbis`


### Available Modes
|Ubisoft Raki Format| Available Header (config)|
|:-----|:------|
|pcm (.wav) | `default` `header2` `titlepage`|
|Nintendo _opus_ | `default` `header2`|

### Note
In Version 1.5.0 config are available now in Settings _Command 7_

---
### How Just Dance Audio Cooker Works in Games:
|Cook Format| Descrption|
|:------|:-----|
|pcm (.wav)|UI only but not for songs|
|Nintendo _opus_|Most recommended|
|Ogg|Most of mods have use it for easier methods|

----
## Infos & Facts
`audiocooker` works in _Just Dance 2019_ to _Just Dance 2022_ (Nintendo Switch). I haven't tested if it will work in _Just Dance 2017_ and _Just Dance 2018_. This tool is a type of `UbiArt` and format called `Ubisoft RAKI` and Thanks to [MZommer](https://github.com/MZommer)
