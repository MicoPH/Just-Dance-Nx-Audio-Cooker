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

### Version 1.0
- New Launch
- Improvement CLI
- Added Features (back to wav conversion using output)
- Add feature `Decrypt Data` from command 4 it does not required vgmstream
- Add feature `Convert Audio using nintendo opus` from Command 1 which may better than ogg compression. _Command 1_
- Add optional feature `Convert Audio To Ogg`. _Command 3_

### Version 1.1
- Add Config to configure the code
- Add single file on _Command 4_
- Adding Brackets in per window
- Add More audio codes on config
    ### Ubisoft RAKI PCM Type:
        Normal - New Header/used for ambs/used for ui
        Old Version - Old Types of Header/used ui in jd2017-2019
        TitlePage - Main titlepage in Just Dance

    ### Ubisoft RAKI Nintendo Opus Types:
        Normal - New Header/used for ambs/used for ui
        Old Version - Old Types of Header/used ui in jd2017-2019

- Fix issues from input directory on Commmand 2
- Fix issues from Command 3
- Fix crash on changelog when exit
- Updated ReadMe
- Update Command 5

### Version 1.2
- Change input folder convert type into multiple file
- Fix file names from input to output file name
- remove input, output and outputback folder

### Version 1.3
- The info of the config are shown in main menu
- Add bitrate key in config
- Fix bug update
- Fix crash detects not pcm from multiple files on "Uncook PCM Data"
- Add Refresh Function on Menu

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

---
### How Audio Maker Works in Games:
|Cook Format| Descrption|
|:------|:-----|
|pcm (.wav)|use for ambs, ui sounds and ui music(pcm)|
|Nintendo _opus_|uses for songs, ui music|
|Ogg|uses for online music|

----
## Infos
`audiomaker` works in _Just Dance 2019_ to _Just Dance 2022_ (Nintendo Switch). I haven't tested if it will work in _Just Dance 2017_ and _Just Dance 2018_
