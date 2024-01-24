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
- <span style="color:#4ae75d">[Feature]</span> New Launch
- <span style="color:#21dde2">[Update Print]</span> Improvement CLI
- <span style="color:#4ae75d">[Feature]</span> Added (back to wav conversion using output)
- <span style="color:#4ae75d">[Feature]</span> Add  `Decrypt Data` from _command 4_ it does not required vgmstream
- <span style="color:#4ae75d">[Feature]</span> Add  `Convert Audio using nintendo opus` from _Command 1_ which may better than ogg compression. _Command 1_
- <span style="color:#4ae7ab">[Optional Feature]</span> Add `Convert Audio To Ogg`. _Command 3_

### Version 1.1
- <span style="color:#4ae75d">[Feature]</span> Add Config to configure the code
- <span style="color:#4ae75d">[Feature]</span> Add single file on _Command 4_
- <span style="color:#4ae75d">[Feature]</span> Adding Brackets in per window
- <span style="color:#4ae75d">[Feature]</span> Add More audio codes on config

          Ubisoft RAKI PCM Type:
            Normal - New Header/used for ambs/used for ui
            Old Version - Old Types of Header/used ui in jd2017-2019
            TitlePage - Main titlepage in Just Dance

          Ubisoft RAKI Nintendo Opus Types:
            Normal - New Header/used for ambs/used for ui
            Old Version - Old Types of Header/used ui in jd2017-2019>

- <span style="color:#f1f11f">[Bug Fixed]</span> Fix issues from input directory on Commmand 2
- <span style="color:#f1f11f">[Bug Fixed]</span> Fix issues from Command 3
- <span style="color:#f1f11f">[Bug Fixed]</span> Fix crash on changelog when exit
- <span style="color:#21dde2">[Update ReadMe]</span> Updated ReadMe
- <span style="color:#3de4c3">[Change]</span> Update Command 5

### Version 1.2
- <span style="color:#3de4c3">[Change]</span> Change  file picker convert type into multiple file
- <span style="color:#f1f11f">[Bug Fixed]</span> Fix file names from input to output file name
- <span style="color:#ed1b1c"> [Removed Feature]</span> remove input, output and outputback folder

### Version 1.3
- <span style="color:#21dde2">[Update Info]</span> The info of the config are shown in main menu
- <span style="color:#4ae75d">[Feature]</span> Add bitrate key in config
- <span style="color:#f1f11f">[Bug Fixed]</span> Fix bug update
- <span style="color:#f1f11f">[Bug Fixed]</span> Fix crash detects not pcm from multiple files on "Uncook PCM Data"
- <span style="color:#4ae75d">[Feature]</span> Add Refresh Function on Menu

### Version 1.4 
- <span style="color:#c53add">[Version Feature]</span> New Patch Version
   - There was a patch version, if there is a bug again, it will be released again, it will not be in the minor version
- <span style="color:#4ae75d">[Feature]</span> Add folde/directory base path info 
- <span style="color:#f1f11f">[Bug Fixed]</span> Fix missing window in tkinter
- <span style="color:#21dde2">[Update Print]</span> Update Print (it is no longer messy anymore)

### Version 1.4.2
- [Removed Bug] Fixed Double ".wav" extension on Command 4
- [Removed Feature] Fixed .ogg input from tkinter(file dialog) on Command 3
- [Add Feature] Add size on the result file
- [Fixed Bug] Fixed Code on VGMStream
- [Fixed Script] Fixed the far spaced on this script
- [Fixed Bug] Added reminder to know a file alredy exists on multple files

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
|pcm (.wav)|this is only for amb, ui(sfx) and ui(pcm)|
|Nintendo _opus_|(Most recommended) (for songs only)|
|Ogg|uses for online music|

----
## Infos
`audiocooker` works in _Just Dance 2019_ to _Just Dance 2022_ (Nintendo Switch). I haven't tested if it will work in _Just Dance 2017_ and _Just Dance 2018_
