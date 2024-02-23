# **Just Dance Audio Cooker**
- [MicoPH](https://github.com/MicoPH/)
## Requirements

---
- `FFMPEG` -  ffmpeg.org - [Link](https://ffmpeg.org)
* `VGMStream` - Backup Audio (include in `audiotools.zip`)
* `VGAudio` - for Nintendo Switch _Opus_ (include in `audiotools.zip`) 

---

## FAQ

#### Q: Can i change the value in `config.json`?

_A: Yes_

#### Q: Is that supported from any platform?

_A: maybe, for cooked pcm but opus didn't supported for nx only_

#### Q:is the format of nintendo opus the same as ffmpeg opus?

_A:No, because the nintendo opus has a different structure_

#### Q:What Nx means?

_A:the codename on Nintendo Switch_


## Changelog

[Expand](https://github.com/MicoPH/Just-Dance-Nx-Audio-Cooker/blob/main/changelog.md)

---
## Supported Formats
- `.ogg` - Ogg Vorbis
- `.opus` - .opus (ffmpeg)
- `.wav` - pcm
- `.mp3` - MPEG

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

- `256kbps` is the constant _bitrate_ in `opus`
- `320kbps` is the constant _bitrate_ in `vorbis`


### Available Modes
|Cook Format| Available Header (config)|
|:-----|:------|
|pcm (.wav) | `normal` `oldVersion` `titlepage`|
|Nintendo _opus_ | `normal` `oldVersion`|

### Note
In Version 1.5.0 config are available now in Settings _Command 7_

---
### How Audio Cooker Works in Games:
|Cook Format| Descrption|
|:------|:-----|
|pcm (.wav)|this is only for amb, ui(sfx) and ui(pcm)|
|Nintendo _opus_|(Most recommended) (for songs only)|
|Ogg|uses for online music|

----
## Infos
`audiocooker` works in _Just Dance 2019_ to _Just Dance 2022_ (Nintendo Switch). I haven't tested if it will work in _Just Dance 2017_ and _Just Dance 2018_
