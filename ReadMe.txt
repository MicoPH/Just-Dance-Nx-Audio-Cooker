Just Dance Audio Cooker
MicoPH


Requirements:
     FFMPEG - https://ffmpeg.org
     VGMStream - Backup Audio (include in audiotools.zip)
     VGAudio - for Nintendo Switch Opus (include in audiotools.zip)

Bitrate Value: 128kb = 128000
Available Mode: pcm - normal, oldVersion, titlepage
                opus - normal, oldVersion


Supported Formats:
     Ogg - Ogg Vorbis
     Opus - .opus (ffmpeg)
     Wave - pcm
     Mp3 - MPEG


[5] Help
     Command 1/2/3 - Cook Wav to (wav.ckd or .ogg)
       Requirements:
          - Download and Install FFMPEG
          - Requires VGAudio v.2.2.1 (include in audiotools.zip) - if you choose command 1

       How to use?:
          Step 1: Make sure you have an audio file
            Supported Formats: (*.wav,*.mp3,*.opus and *.ogg)
          Step 2: Choose 1 or 2 or 3  and choose type of convert
          Step 3: Waiting to encoding
          Step 4: When done, your cooked audio was saved to your directory

     Command 4 - Convert back using output file
       Requirements:
          - Install VGMSTREAM (include in audiotools.zip)


       How to use?
          Step 1: Make sure you have an cooked audio file (*.wav.ckd)
          Step 2: Choose 4 and choose type of convert
          Step 3: Waiting a few seconds to finish
          Step 4: When done, your file was saved to your directory

     How Audio Maker Works in Games:
          PCM(wav) uses for ambs, ui sounds and ui music(pcm)
          Nintendo(Libopus) uses for songs, ui music
          Ogg uses for online music

     How to config or change header on config.json?
       1.Click config.json and choose your software to configure it(ex. Notepad):
          Types of PCM to change header(pcmMode):
            normal = Normal header in JD2020-2022
            oldVersion = Old Header in JD2017-2019
            titlepage = Just Dance TitlePage (with signature)

          Types of cooked libopus to change header:
            normal = Normal Header on JD2020-2022
            oldVersion = Old Header on JD2017-2019
     How to change bitrate:
       Step 1: open config.json
       Step 2: below on vgmstreamPath change value into bytes
          (128kbps = 128000)

       FAQ:
          Q:Can i change the value in config.json?
          A:Yes

          Q:Is that supported from any platform?
          A:maybe, for cooked pcm but opus didn't supported for nx only

          Q:is the format of nintendo opus the same as ffmpeg opus?
          A:No, because the nintendo opus has a different structure

          Q:What Nx means?
          A:the codename on Nintendo Switch


[6] Changelog
   Changelog:
     Version 1.0
       - New Launch
       - Improvement CLI
       - Added Features (back to wav conversion using output)
       - Add feature "Decrypt Data" from command 4 it does not required vgmstream
       - Add feature "Convert Audio using nintendo opus" from Command 1 which may better than ogg compression. [Command 1]
       - Add optional feature "Convert Audio To Ogg". [Command 3]

     Version 1.1
       - Add Config to configure the code
       - Add single file on Command 4
       - Adding Brackets in per window
       - Add More audio codes on config

          Ubisoft RAKI PCM Type:
            Normal - New Header/used for ambs/used for ui
            Old Version - Old Types of Header/used ui in jd2017-2019
            TitlePage - Main titlepage in Just Dance

          Ubisoft RAKI Nintendo Opus Types:
            Normal - New Header/used for ambs/used for ui
            Old Version - Old Types of Header/used ui in jd2017-2019

       - Fix issues from input directory on Commmand 2
       - Fix issues from Command 3
       - Fix crash on changelog when exit
       - Updated ReadMe
       - Update Command 5

     Version 1.2
       - Change input folder convert type into multiple file
       - Fix file names from input to output file name
       - remove input, output and outputback folder

     Version 1.3
       - The info of the config are shown in main menu
       - Add bitrate key in config
       - Fix bug update
       - Fix crash detects not pcm from multiple files on "Uncook PCM Data"
       - Add Refresh Function on Menu


How Audio Maker Works in Games:
	PCM(wav) uses for ambs, ui sounds and ui music(pcm)
	Nintendo(Libopus) uses for songs, ui music
	Ogg uses for online music