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

### Version 1.5.0
- [Removed Folder] Removed outputback folder in main app
- [Improved Option] in Help and Changelog
- [Add feature] Add Settings
- [Improved feature] Detects missing app when open
- [Improved ffmpeg request] Change ffmpeg os.system to subprocess
- [Update Feature] Last minor version

### Version 1.5.1
- [Improvement Print] Improve Print Console in Settings
- [Bug Fixes] Fixed VGAudio input temp not found
- [Settings] Volume numbers are now divided to 100 in config and change 2 option in path environment
- [Custom Value Settings] Fixed bug in custom volume and gets back in pressing enter in 3 times same as change bitrate
- [Exit Bug] Fixed bug the from exit
- [Old Config] Old config.json from 1.0 are now updated
- [App Wrong Detector] in FFMPEG, VGMStream and VGAudio are now detected to file if your requirements is wrong