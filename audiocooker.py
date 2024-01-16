import os, struct, time, pathlib,json
from datetime import datetime
from tkinter import filedialog
from subprocess import DEVNULL, STDOUT, run, call
def Menu():
    try:
        con =  json.load(open("config.json", "r"))
        volume = str(con["addVolume"])
        channeljson = int(con["channel"])
        modepcm = con["pcmMode"]
        modeopus = con["opusMode"]
        if channeljson == 1 or channeljson == 2:
            pass
        else:
            print('\n   Channel value failed. Channel was default into 2') 
            channeljson = 2
        getpcm = 0
        getopus = 0
        ffmpegPath = con["ffmpegPath"]
        vgaudioPath = str(con["nintendoVGAudioPath"])
        vgmstreamPath = str(con["vgmstreamPath"])
        def conjson1():
            try:
                datjs = open('config.json','w')
                print('Updating config...')
                datjs.write('''{
    "addVolume": ''')
                datjs.write(str(volume))
                datjs.write(''',    
    "version": 1.3,
    "pcmMode": "''')
                datjs.write(modepcm)
                datjs.write('''",
    "opusMode": "''')
                datjs.write(modeopus)
                datjs.write('''",
    "channel": ''')
                datjs.write(str(channeljson))
                datjs.write(''',
    "ffmpegPath": "''')
                datjs.write(ffmpegPath)
                datjs.write('''",
    "nintendoVGAudioPath": "''')
                datjs.write(vgaudioPath)
                datjs.write('''",
    "vgmstreamPath": "''')
                datjs.write(vgmstreamPath)
                datjs.write('''",
    "opusbitrate": ''')
                try:
                    opubitrate = con["opusbitrate"]
                except:
                    opubitrate = 256000
                datjs.write(str(opubitrate))
                datjs.write(''',
    "vorbisbitrate": ''')
                try:
                    vorbitrate = con["vorbisbitrate"]
                except:
                    vorbitrate = 320000
                datjs.write(str(vorbitrate))
                datjs.write(''',
    "pcmModeData":[
        {
            "id": 1,
            "pcmModeType": "normal",
            "pcmtitle": "Normal (JD2020-2022 Version)",
            "pcmHead": 72,
            "pcmHead1": 72,
            "pcmHead2": 2,
            "pcmHead3": 0,
            "pcmfmt": 56,
            "pcmfmt2": 16,
            "mark": false,
            "strg": false
        },
        {
            "id": 2,
            "pcmModeType": "oldVersion",
            "pcmtitle": "Old Version (JD2017-2019 Version)",
            "pcmHead": 74,
            "pcmHead1": 80,
            "pcmHead2": 2,
            "pcmHead3": 3,
            "pcmfmt": 56,
            "pcmfmt2": 16,
            "mark": false,
			"strg": false
        },
        {
            "id": 3,
            "pcmModeType": "titlepage",
            "pcmtitle": "JD TitlePage",
            "pcmHead": 2288,
            "pcmHead1": 2288,
            "pcmHead2": 4,
            "pcmHead3": 3,
            "pcmfmt": 80,
            "pcmfmt2": 18,
            "mark": true,
            "strg": true,
            "marklength": 2,
            "strglength": 2,
            "markdata":[
                {
                    "mark1":98,
                    "mark2":2182,
                    "strg1":2280,
                    "strg2":8,
                    "addinfohead1": 23789568,
                    "addinfohead2": 0,
                    "addinfohead3": 1,
                    "addinfohead4": 3145734,
                    "multiplieronaddinfo1": false,
                    "multiplieronaddinfo2": true,
                    "multiplieronaddinfo3": false,
                    "multiplieronaddinfo4": false,
                    "multiplier":[
                        {
                            "addinfo1": "mark1",
                            "addinfo2": "mark2",
                            "addinfo3": "strg1",
                            "addinfo4": "strg2"
                        }
                    ]
                }
            ]
        }
    ],
    "opusModeData":[
        {
            "id": 1,
            "opusModeType": "normal",
            "opusTitle": "Normal (JD2020-2022 Version)",
            "opusHead": 88,
            "opusHead2": 88,
            "opusHead3": 3,
            "opusHead4": 3,
            "opusfmt": 68,
            "opusfmt2": 16,
            "adinlength": 2,
            "adindata":[
                {
                    "adin1":84,
                    "adin2":4
                }
            ],
            "datatitlehead": 88,
            "16bitonInt32": false
        },
        {
            "id": 2,
            "opusModeType": "oldVersion",
            "opusTitle": "Old Version (JD2017-2019 Version)",
            "opusHead": 90,
            "opusHead2": 96,
            "opusHead3": 3,
            "opusHead4": 3,
            "opusfmt": 68,
            "opusfmt2": 18,
            "adinlength": 2,
            "adindata":[
                {
                    "adin1":86,
                    "adin2":4
                }
            ],
            "datatitlehead": 96,
            "16bitonInt32": true
        }
    ]

}''')
                datjs.close
                print('   Reopen the script again...')
                time.sleep(2)
                exit()
            except Exception as e:
                 print(str(e)) 
        for pcmitems in con["pcmModeData"]:
            if pcmitems["pcmModeType"] == modepcm:
                info = int(pcmitems["id"])
                pcmhead1 = int(pcmitems["pcmHead"])
                pcmhead2 = int(pcmitems["pcmHead1"])
                pcmhead3 = int(pcmitems["pcmHead2"])
                pcmhead4 = int(pcmitems["pcmHead3"])
                pcmfmt = int(pcmitems["pcmfmt"])
                pcmfmt2 = int(pcmitems["pcmfmt2"])
                markcount = 0
                strgcount = 0
                strgtitle = b''
                strgbyte = b''
                markbyte = b''
                marktitle = b''
                byteaddinfo =b''
                if pcmitems["mark"]:
                    marktitle = b'MARK'
                    marklength = int(pcmitems["marklength"])
                    markbyte = b''
                    while marklength > 0:
                                        markname = "mark"+str(marklength)
                                        markbyte = struct.pack("I",int(pcmitems["markdata"][0][markname]))+markbyte
                                        markcount+=1
                                        addinfo = markcount
                                        infomultplier = pcmitems["markdata"][0]["multiplier"][0]["addinfo"+str(addinfo)]
                                        if pcmitems["markdata"][0]["multiplieronaddinfo"+str(addinfo)]:
                                            multplytodatapcm = int((pcmitems["markdata"][0][infomultplier]-addinfo)/4)
                                            byteaddinfomutiply = struct.pack("I",int(pcmitems["markdata"][0]["addinfohead"+str(addinfo)]))
                                            byteaddinfo = byteaddinfo+(byteaddinfomutiply*multplytodatapcm)
                                        else:
                                            byteaddinfo = byteaddinfo+struct.pack("I",int(pcmitems["markdata"][0]["addinfohead"+str(addinfo)]))
                                        marklength = marklength - 1
                if pcmitems["strg"]:
                                        strgtitle = b'STRG'
                                        strglength = int(pcmitems["strglength"])
                                        strgbyte = b''
                                        while strglength > 0:
                                            strgname = "strg"+str(strglength)
                                            strgcount+=1
                                            strgbyte = struct.pack("I",int(pcmitems["markdata"][0][strgname]))+strgbyte
                                            addinfo = markcount+strgcount
                                            infomultplier = pcmitems["markdata"][0]["multiplier"][0]["addinfo"+str(addinfo)]
                                            if pcmitems["markdata"][0]["multiplieronaddinfo"+str(addinfo)]:
                                                multplytodatapcm = int((pcmitems["markdata"][0][infomultplier]-strgcount)/4)
                                                byteaddinfomutiply = struct.pack("I",int(pcmitems["markdata"][0]["addinfohead"+str(addinfo)]))*multplytodatapcm
                                                byteaddinfo = byteaddinfo+byteaddinfomutiply
                                            else:
                                                byteaddinfo = byteaddinfo+struct.pack("I",int(pcmitems["markdata"][0]["addinfohead"+str(addinfo)]))
                                            strglength = strglength - 1
                addinfobyte = byteaddinfo
                getpcm = 1
        for nopusitems in con["opusModeData"]:
            if nopusitems["opusModeType"] == modeopus:
                info = int(nopusitems["id"])
                opushead1 = int(nopusitems["opusHead"])
                opushead2 = int(nopusitems["opusHead2"])
                opushead3 = int(nopusitems["opusHead3"])
                opushead4 = int(nopusitems["opusHead4"])
                opusheadfmt = int(nopusitems["opusfmt"])
                opusheadfmt2 = int(nopusitems["opusfmt2"])
                adindatahead1 = int(nopusitems["adindata"][0]["adin1"])
                adindatahead2 = int(nopusitems["adindata"][0]["adin2"])
                datatitlehead = int(nopusitems["datatitlehead"])
                intbytehead = nopusitems["16bitonInt32"]
                getopus = 1
    except:
        current_time = datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%H-%M-%S')
        try:
            os.rename("config.json","config-old-"+formatted_time+".json")
            print("   Config Failed to read\n   Renew Config...")
        except:
            print('   Making Config...')
        datjs = open('config.json','w')
        datjs.write('''{
    "addVolume": 1,
    "version": 1.3,
    "pcmMode": "normal",
    "opusMode": "normal",
    "channel": 2,
    "ffmpegPath": "ffmpeg",
    "nintendoVGAudioPath": "VGAudioCli",
    "vgmstreamPath": "vgmstream",
    "opusbitrate": 256000,
    "vorbisbitrate": 320000,
    "pcmModeData":[
        {
            "id": 1,
            "pcmModeType": "normal",
            "pcmtitle": "Normal (JD2020-2022 Version)",
            "pcmHead": 72,
            "pcmHead1": 72,
            "pcmHead2": 2,
            "pcmHead3": 0,
            "pcmfmt": 56,
            "pcmfmt2": 16,
            "mark": false,
            "strg": false
        },
        {
            "id": 2,
            "pcmModeType": "oldVersion",
            "pcmtitle": "Old Version (JD2017-2019 Version)",
            "pcmHead": 74,
            "pcmHead1": 80,
            "pcmHead2": 2,
            "pcmHead3": 3,
            "pcmfmt": 56,
            "pcmfmt2": 16,
            "mark": false,
			"strg": false
        },
        {
            "id": 3,
            "pcmModeType": "titlepage",
            "pcmtitle": "JD TitlePage",
            "pcmHead": 2288,
            "pcmHead1": 2288,
            "pcmHead2": 4,
            "pcmHead3": 3,
            "pcmfmt": 80,
            "pcmfmt2": 18,
            "mark": true,
            "strg": true,
            "marklength": 2,
            "strglength": 2,
            "markdata":[
                {
                    "mark1":98,
                    "mark2":2182,
                    "strg1":2280,
                    "strg2":8,
                    "addinfohead1": 23789568,
                    "addinfohead2": 0,
                    "addinfohead3": 1,
                    "addinfohead4": 3145734,
                    "multiplieronaddinfo1": false,
                    "multiplieronaddinfo2": true,
                    "multiplieronaddinfo3": false,
                    "multiplieronaddinfo4": false,
                    "multiplier":[
                        {
                            "addinfo1": "mark1",
                            "addinfo2": "mark2",
                            "addinfo3": "strg1",
                            "addinfo4": "strg2"
                        }
                    ]
                }
            ]
        }
    ],
    "opusModeData":[
        {
            "id": 1,
            "opusModeType": "normal",
            "opusTitle": "Normal (JD2020-2022 Version)",
            "opusHead": 88,
            "opusHead2": 88,
            "opusHead3": 3,
            "opusHead4": 3,
            "opusfmt": 68,
            "opusfmt2": 16,
            "adinlength": 2,
            "adindata":[
                {
                    "adin1":84,
                    "adin2":4
                }
            ],
            "datatitlehead": 88,
            "16bitonInt32": false
        },
        {
            "id": 2,
            "opusModeType": "oldVersion",
            "opusTitle": "Old Version (JD2017-2019 Version)",
            "opusHead": 90,
            "opusHead2": 96,
            "opusHead3": 3,
            "opusHead4": 3,
            "opusfmt": 68,
            "opusfmt2": 18,
            "adinlength": 2,
            "adindata":[
                {
                    "adin1":86,
                    "adin2":4
                }
            ],
            "datatitlehead": 96,
            "16bitonInt32": true
        }
    ]

}''')
        print('   Reopen the script again...')
        time.sleep(2)
        exit()
    try:
        ver = float(con["version"])
    except:
        conjson1()
    if ver == 1.3:
        pass
    else:
        conjson1()
    for nopusitems1 in con["opusModeData"]:
        if nopusitems1["opusModeType"] == modeopus:
            title0 = str(nopusitems1["opusTitle"])
    for pcmitems1 in con["pcmModeData"]:
        if pcmitems1["pcmModeType"] == modepcm:
            title1 = str(pcmitems1["pcmtitle"])
    if getpcm == 0:
            namepcmMode = "Invalid pcm"
    elif(modepcm == "normal" or modepcm == "oldVersion" or modepcm == "titlepage"):
            namepcmMode = title1
    else:
            namepcmMode = str(title0+" (Custom Mode)")
    if getopus == 0:
            nameopusMode = "Invalid opus"
    elif(modeopus == "normal" or modeopus == "oldVersion"):
            nameopusMode = title0
    else:
            nameopusMode = str(title0+" (Custom Mode)")
    if channeljson == 1:
        txtchanneljson = "Channel Type: Mono"
    else:
        txtchanneljson = "Channel Type: Stereo"
    intvolumeset = int(con["addVolume"]*100)
    txtvolumeset = "Volume: "+ str(intvolumeset) + "%"
    try:
        bitrateopus = con["opusbitrate"]
        if bitrateopus < 0:
            bitrateopus = 92000
            print("   [Opus]: Invalid value. bitrate is set to 92000")
            bitrateopustxt = "Vorbis Audio Bitrate:Medium"
        elif bitrateopus < 64000:
            bitrateopustxt = "Opus Audio Bitrate: Low"
        elif bitrateopus < 192000:
            bitrateopustxt = "Opus Audio Bitrate: Medium"
        elif bitrateopus < 256000 or bitrateopus > 256000:
            bitrateopustxt = "Opus Audio Bitrate:High"
        elif bitrateopus == 256000:
            bitrateopustxt = "Opus Audio Bitrate: High (constant bitrate)"
    except:
        bitrateopus = 92000
        print("   [Opus]: Invalid key. bitrate is set to 92000")
        bitrateopustxt = "Vorbis Audio Bitrate:Medium"
    try:
        bitratevorbis = con["vorbisbitrate"]
        if bitratevorbis < 0:
            bitratevorbis = 128000
            print("   [Vorbis]: Invalid value. bitrate is set to 128000")
            bitratevorbistxt = "Vorbis Audio Bitrate:Medium"
        elif bitratevorbis < 92000:
            bitratevorbistxt = "Vorbis Audio Bitrate:Low"
        elif bitratevorbis < 192000:
            bitratevorbistxt = "Vorbis Audio Bitrate: Medium"
        elif bitratevorbis < 320000 or bitratevorbis > 320000:
            bitratevorbistxt = "Vorbis Audio Bitrate: High"
        elif bitratevorbis == 320000:
            bitratevorbistxt = "Vorbis Audio Bitrate: High (constant bitrate)"
        intbitratevorb = int(bitratevorbis/1000)
    except:
        bitratevorbis = 128000
        print("   [Vorbis]: Invalid key. bitrate is set to 128000")
        bitratevorbistxt = "Vorbis Audio Bitrate:Medium"
        intbitratevorb = int(bitratevorbis/1000)
    print('\n<------------------------------->\n\n\n Welcome to Just Dance Nx Audio Maker \n (Version 1.3)\n    Made by MicoPH  \n    If refresh. click Enter\n\n   Requirements:\n     FFMPEG - https://ffmpeg.org \n     VGMStream - Backup Audio (include in audiotools.zip)\n     VGAudio - for Nintendo Switch Opus (include in audiotools.zip)\n\n   PCM Mode: '+namepcmMode+" | Opus Mode: "+nameopusMode+"\n   "+txtchanneljson+" | "+txtvolumeset+"\n   "+bitrateopustxt+" | "+bitratevorbistxt+"\n\n     Choose the Options:\n     [1] Convert Audio to cooked nintendo opus file (commonly used in og games) (recommended for songs)\n     [2] Convert Audio to cooked pcm .wav format (recommended for amb and ui sfx)\n     [3] Convert Audio to Ogg\n     [4] Convert Back to WAV FILE(.wav.ckd to .wav)\n     [5] Help\n     [6] Changelog\n     [0] Exit\n\n")
    try:
        option = str(input("   Choose the option -----> "))
    except:
        pass
    if not option:
        Menu()
    try:
        intoption=int(option)
    except:
        print('\n     Use only numbers not letters/symbols')
        time.sleep(1)
        Menu()
    if(intoption == 0):
            time.sleep(2)
            exit()
    def O1():
        def Opt1():
            def Raki():
                if(os.path.isfile("temp/temp.lopus")):
                    print('   Encoding: '+ listfiles1)
                    opussize = os.path.getsize("temp/temp.lopus") 
                    with open("temp/temp.wav", "rb") as b:
                                b.read(12)
                                formattitle = b.read(4)
                                bitbyte = struct.unpack("I", b.read(4))[0] # if bytes is 16 means little bitbyte 
                                b.read(2)
                                channel = struct.unpack("H",b.read(2))[0]
                                riffdatainfo = b.read(12)
                                datatitle = b.read(4)
                                minidata = struct.unpack("I", b.read(4))[0]
                    with open("temp/temp.lopus", "rb") as f:
                        o1=f.read(8)
                        f.read(4)
                        o2=f.read(16)
                        f.read(4)
                        dataopus=f.read()
                        try:
                            opusenc = open(output+"\\" + audiofilename1 + ".wav.ckd", "wb")
                            opusenc.write(b'RAKI') # main header of opus raki file (4)
                            opusenc.write(struct.pack('I',11)) # audio version of raki
                            opusenc.write(b'Nx  Nx  ') # platform and encoding type of raki
                            opusenc.write(struct.pack('I',opushead1))
                            opusenc.write(struct.pack('I',opushead2))
                            opusenc.write(struct.pack('I',opushead3))
                            opusenc.write(struct.pack('I',opushead4))
                            opusenc.write(formattitle)
                            opusenc.write(struct.pack('I',opusheadfmt))
                            opusenc.write(struct.pack('I',opusheadfmt2)) 
                            opusenc.write(b'AdIn')
                            opusenc.write(struct.pack('I',adindatahead1))
                            opusenc.write(struct.pack('I',adindatahead2))
                            opusenc.write(datatitle)
                            opusenc.write(struct.pack('I',datatitlehead))
                            opusenc.write(struct.pack("I", opussize))  # Data size from this file (4)
                            opusenc.write(struct.pack('h',99))
                            opusenc.write(struct.pack("H",channel))
                            opusenc.write(riffdatainfo)
                            if intbytehead:
                                opusenc.write(struct.pack("H",0))
                            opusenc.write(struct.pack("I",int(minidata/((bitbyte*channel)/8)))) # total samples of raki format (4)
                            if intbytehead:
                                opusenc.write(struct.pack("H",0))
                                opusenc.write(struct.pack("I",0))
                            opusenc.write(o1)
                            opusenc.write(struct.pack("I", 512)) # change bytehead version
                            opusenc.write(o2)
                            opusenc.write(struct.pack("I", 120)) # change opushead version
                            opusenc.write(dataopus) # writes data from libopus file (depends of size of audio)
                            b.close
                            f.close
                            opusenc.close
                            outputres = output.replace('/','\\')+"\\"
                            print('   DONE: '+ outputres + os.path.splitext(listfiles1)[0] + ".wav.ckd "+' \n')
                        except:
                            print('   [ERROR]: The file used from another process\n')
            try:
                print("\n   Run Tkinter:\n   [NOTE]: If can't find filedialog. Minimize the window\n")
                outputaudiofile = filedialog.askopenfilenames(initialdir=pathlib.Path, title='Select the audio file', filetypes=(("Audio files (*.wav,*.opus,*.mp3,*.ogg)","*.wav *.opus *.mp3 *.ogg"),("All files","*.*")))
                if(not outputaudiofile):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        BadContinue()
                output = filedialog.askdirectory(initialdir=pathlib.Path,title="Select Location")
                if(not output):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        BadContinue()
                print('\n   Start Converting...\n')
                for listfiles in outputaudiofile:
                        listfiles1 = os.path.basename(listfiles)
                        if(".ogg" in listfiles or ".opus" in listfiles or ".mp3" in listfiles or ".wav" in listfiles):
                            # Other Audio process
                            try:
                                try:
                                    os.mkdir('temp')
                                except:
                                    pass
                                run((ffmpegPath), stdout=DEVNULL, stderr=STDOUT)
                                print('   Running FFMPEG to: '+ listfiles1)
                                os.system(ffmpegPath+' -y -i "'+listfiles+'" -f wav -bitexact -acodec pcm_s16le -ar 48000 -map_metadata -1 -ac '+str(channeljson)+' -loglevel quiet temp/temp.wav')
                                try:
                                    run(('VGAudioCli'), stdout=DEVNULL, stderr=STDOUT)
                                    print('   Running VGAudio: '+ listfiles1)
                                    call([vgaudioPath, 'temp/temp.wav', 'temp/temp.lopus', '--bitrate', str(bitrateopus), '--no-loop', '--opusheader','standard'],stdout=DEVNULL, stderr=STDOUT)
                                except:
                                    print("     [ERROR]: VGAudio (Nintendo opus) is not exist\n\n   1 missing")
                                    time.sleep(1)
                                    BadContinue()
                            except:
                                print("   [ERROR]: FFMPEG is not exist\n\n   1 missing")
                                time.sleep(1)
                                BadContinue()
                            audiofilename1 = os.path.splitext(listfiles1)[0]
                            Raki()
            except:
                pass
        def Opt2():
            def Raki():
                if(os.path.isfile("temp/temp.lopus")):
                    print('   Encoding: '+ filenameinfo)
                    opussize = os.path.getsize("temp/temp.lopus") 
                    with open("temp/temp.wav", "rb") as b:
                                b.read(12)
                                formattitle = b.read(4)
                                bitbyte = struct.unpack("I", b.read(4))[0] # if bytes is 16 means little bitbyte 
                                b.read(2)
                                channel = struct.unpack("H",b.read(2))[0]
                                riffdatainfo = b.read(12)
                                datatitle = b.read(4)
                                minidata = struct.unpack("I", b.read(4))[0]
                    with open("temp/temp.lopus", "rb") as f:
                        o1=f.read(8)
                        f.read(4)
                        o2=f.read(16)
                        f.read(4)
                        dataopus=f.read()
                        try:
                            with open(output,'wb') as opusenc:
                                opusenc.write(b'RAKI') # main header of opus raki file (4)
                                opusenc.write(struct.pack('I',11)) # audio version of raki
                                opusenc.write(b'Nx  Nx  ') # platform and encoding type of raki
                                opusenc.write(struct.pack('I',opushead1))
                                opusenc.write(struct.pack('I',opushead2))
                                opusenc.write(struct.pack('I',opushead3))
                                opusenc.write(struct.pack('I',opushead4))
                                opusenc.write(formattitle)
                                opusenc.write(struct.pack('I',opusheadfmt))
                                opusenc.write(struct.pack('I',opusheadfmt2)) 
                                opusenc.write(b'AdIn')
                                opusenc.write(struct.pack('I',adindatahead1))
                                opusenc.write(struct.pack('I',adindatahead2))
                                opusenc.write(datatitle)
                                opusenc.write(struct.pack('I',datatitlehead))
                                opusenc.write(struct.pack("I", opussize))  # Data size from this file (4)
                                opusenc.write(struct.pack('h',99))
                                opusenc.write(struct.pack("H",channel))
                                opusenc.write(riffdatainfo)
                                if intbytehead:
                                    opusenc.write(struct.pack("H",0))
                                opusenc.write(struct.pack("I",int(minidata/((bitbyte*channel)/8)))) # total samples of raki format (4)
                                if intbytehead:
                                    opusenc.write(struct.pack("H",0))
                                    opusenc.write(struct.pack("I",0))
                                opusenc.write(o1)
                                opusenc.write(struct.pack("I", 512)) # change bytehead version
                                opusenc.write(o2)
                                opusenc.write(struct.pack("I", 120)) # change opushead version # seperate code from datasize 
                                opusenc.write(dataopus) # writes data from libopus file (depends of size of audio)
                            b.close
                            f.close
                            opusenc.close
                            print('   DONE: '+output.replace('/','\\') +'\n')
                            time.sleep(1)
                        except Exception as e:
                            print('   [ERROR]: The file used from another process\n')
                            time.sleep(1)
            try:
                print("\n   Run Tkinter:\n   [NOTE]: If can't find filedialog. Minimize the window\n")
                audiofilename = filedialog.askopenfilename(initialdir=pathlib.Path, title='Select the audio file', filetypes=(("Audio files (*.wav,*.opus,*.mp3,*.ogg)","*.wav *.opus *.mp3 *.ogg"),("All files","*.*")))
                if(not audiofilename):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                    BadContinue()
                filenameinfo = os.path.basename(audiofilename)
                output = filedialog.asksaveasfilename(filetypes=[("Ubisoft RAKI",'*.wav.ckd')],initialdir=pathlib.Path,title="Select Location",initialfile=os.path.splitext(filenameinfo)[0]+'.wav.ckd')
                if(not output):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                    BadContinue()
                print('\n   Start Converting...\n')
                try:
                    os.mkdir('temp')
                except:
                    pass
                        # Other Audio process
                try:
                    run((ffmpegPath), stdout=DEVNULL, stderr=STDOUT)
                    print('   Running FFMPEG to: '+ filenameinfo)
                    os.system(ffmpegPath+' -y -i "' + audiofilename +  '"  -f wav -bitexact -acodec pcm_s16le -ar 48000 -ac '+str(channeljson)+' -filter:a "volume='+volume+'" -map_metadata -1 -loglevel quiet temp/temp.wav')
                    try:
                        run(('VGAudioCli'), stdout=DEVNULL, stderr=STDOUT)
                        print('   Running VGAudio: '+filenameinfo)
                        call([vgaudioPath, 'temp/temp.wav', 'temp/temp.lopus', '--bitrate', str(bitrateopus), '--no-loop', '--opusheader','standard'],stdout=DEVNULL, stderr=STDOUT)
                    except:
                        print("     [ERROR]: VGAudio (Nintendo opus) is not exist\n\n   1 missing")
                        time.sleep(1)
                        BadContinue()
                except Exception as e:
                    print("   [ERROR]: FFMPEG is not exist\n")
                    time.sleep(1)
                    BadContinue()
                audiofilename1 = os.path.splitext(output)[0]
                Raki()
            except:
                pass
        print('\n\n<------------------------------->\n\n   Encoding Type: Nintendo Opus\n     Header Type: '+nameopusMode+'\n   '+bitrateopustxt+'\n\n   What is your preferred option to convert?\n\n     [1] pick single file\n     [2] pick multiple files\n     [0] Back\n')
        try:
            opt12 = int(input("   Choose the option -----> "))
        except:
            print('     Invalid option')
            O1()
        if(opt12 == 1):
            Opt2()
        if(opt12 == 2):
            Opt1()
        if(opt12 == 0):
            Menu()
        if(opt12 > 2 or opt12 < 0):
            print('      Invalid numbers')
            O1()
        Continue()
    if(intoption == 1):
        if getopus == 1:
            O1()
        else:
            print('     Invalid Mode. reconfig the config.json')
            time.sleep(1)
            Menu()
    def O2():
        def Opt1():
            def Raki():
                    if(os.path.isfile("temp/temp.wav")):
                        print('   Encoding: '+ audiofilename1)
                        # open data from temp file
                        with open("temp/temp.wav", "rb") as f:
                            f.read(12)
                            formattitle = f.read(4)
                            bitbyte = f.read(4)
                            audioformat = f.read(2)
                            numofchannels = struct.unpack('h',f.read(2))[0]
                            riffend = f.read(12)
                            datatitle = f.read(4)
                            data = f.read(4)
                            audiofile = f.read()
                            #Checking when process
                            try:
                                denc = open(output+"\\" + audiofilename1 + ".wav.ckd", "wb")
                                denc.write(b'RAKI') # main header of this game
                                denc.write(struct.pack('I',11))
                                denc.write(b'Nx  pcm ')
                                denc.write(struct.pack('I',pcmhead1))
                                denc.write(struct.pack('I',pcmhead2))
                                denc.write(struct.pack('I',pcmhead3))
                                denc.write(struct.pack('I',pcmhead4))
                                denc.write(formattitle)
                                denc.write(struct.pack('I',pcmfmt))
                                denc.write(struct.pack('I',pcmfmt2))
                                denc.write(marktitle)
                                denc.write(markbyte)
                                denc.write(strgtitle)
                                denc.write(strgbyte)
                                denc.write(datatitle)
                                denc.write(struct.pack('I',pcmhead2))
                                denc.write(data) # important data chunk size from original audio # end header of audio file
                                denc.write(audioformat)
                                denc.write(struct.pack('h',numofchannels))
                                denc.write(riffend) # samplerate, byterate,blockAlign,bitspersample
                                denc.write(addinfobyte)
                                denc.write(audiofile) # whole data from original audio 
                                f.close
                                denc.close
                                print("   DONE: "+ output.replace('/','\\')+"\\" + audiofilename1 + ".wav.ckd")
                            except Exception as e:
                                print('   [ERROR]: The file used from another process\n')
            try:
                os.mkdir('temp/')
            except:
                pass
            try:
                print("\n   Run Tkinter:\n   [NOTE]: If can't find filedialog. Minimize the window\n")
                outputaudiofile = filedialog.askopenfilenames(initialdir=pathlib.Path, title='Select the audio file', filetypes=(("Audio files (*.wav,*.opus,*.mp3,*.ogg)","*.wav *.opus *.mp3 *.ogg"),("All files","*.*")))
                if(not outputaudiofile):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        BadContinue()
                output = filedialog.askdirectory(initialdir=pathlib.Path,title="Select Location")
                if(not output):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        BadContinue()
                print('\n   Start Converting...\n')
                for listfiles in outputaudiofile:
                    listfiles1 = os.path.basename(listfiles)
                    if(".ogg" in listfiles or ".opus" in listfiles or ".mp3" in listfiles or ".wav" in listfiles):
                        try:
                            os.mkdir('temp')
                        except:
                            pass
                        # Other Audio process
                        try:
                            run((ffmpegPath), stdout=DEVNULL, stderr=STDOUT)
                            print('   Running FFMPEG to: '+ listfiles1)
                            os.system(ffmpegPath+' -y -i "' + listfiles +  '"  -f wav -bitexact -acodec pcm_s16le -ar 48000 -ac '+str(channeljson)+' -filter:a "volume='+volume+'" -map_metadata -1 -loglevel quiet temp/temp.wav')
                        except:
                            print("   [ERROR]: FFMPEG is not exist\n\n   1 missing")
                            time.sleep(1)
                            BadContinue()
                        audiofilename1 = os.path.splitext(listfiles1)[0]
                        Raki()
            except:
                pass
        def Opt2():
            def Raki():
                    if(os.path.isfile("temp/temp.wav")):
                        print('   Encoding: '+ os.path.basename(audiofilename))
                        # open data from temp file
                        with open("temp/temp.wav", "rb") as f:
                            f.read(12)
                            formattitle = f.read(4)
                            bitbyte = f.read(4)
                            audioformat = f.read(2)
                            numofchannels = struct.unpack('h',f.read(2))[0]
                            riffend = f.read(12)
                            datatitle = f.read(4)
                            data = f.read(4)
                            audiofile = f.read()
                            #Checking when process
                            try:
                                with open(output,'wb') as denc:
                                    denc.write(b'RAKI') # main header of this game
                                    denc.write(struct.pack('I',11))
                                    denc.write(b'Nx  pcm ')
                                    denc.write(struct.pack('I',pcmhead1))
                                    denc.write(struct.pack('I',pcmhead2))
                                    denc.write(struct.pack('I',pcmhead3))
                                    denc.write(struct.pack('I',pcmhead4))
                                    denc.write(formattitle)
                                    denc.write(struct.pack('I',pcmfmt))
                                    denc.write(struct.pack('I',pcmfmt2))
                                    denc.write(marktitle)
                                    denc.write(markbyte)
                                    denc.write(strgtitle)
                                    denc.write(strgbyte)
                                    denc.write(datatitle)
                                    denc.write(struct.pack('I',pcmhead2))
                                    denc.write(data) # important data chunk size from original audio # end header of audio file
                                    denc.write(audioformat)
                                    denc.write(struct.pack('h',numofchannels))
                                    denc.write(riffend) # samplerate, byterate,blockAlign,bitspersample
                                    denc.write(addinfobyte)
                                    denc.write(audiofile) # whole data from original audio 
                                f.close
                                denc.close
                                print("   DONE: " + output.replace('/','\\')+"\\"  + ".wav.ckd \n")
                            except Exception as e:
                                print('   [ERROR]: The file used from another process\n')
            try:
                os.mkdir('temp/')
            except:
                pass
            try:
                print("\n   Run Tkinter:\n   [NOTE]: If can't find filedialog. Minimize the window\n")
                audiofilename = filedialog.askopenfilename(initialdir=pathlib.Path, title='Select the audio file', filetypes=(("Audio files (*.wav,*.opus,*.mp3,*.ogg)","*.wav *.opus *.mp3 *.ogg"),("All files","*.*")))
                if(not audiofilename):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                    BadContinue()
                filenameinfo = os.path.basename(audiofilename)
                output = filedialog.asksaveasfilename(filetypes=[("Ubisoft RAKI",'*.wav.ckd')],initialdir=pathlib.Path,title="Select Location",initialfile=os.path.splitext(filenameinfo)[0]+'.wav.ckd')
                if(not output):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                    BadContinue()
                print('\n   Start Converting...\n')
                if(".ogg" in audiofilename or ".opus" in audiofilename or ".mp3" in audiofilename or ".wav" in audiofilename):
                        # Other Audio process
                        try:
                            os.mkdir('temp')
                        except:
                            pass
                        try:
                            run((ffmpegPath), stdout=DEVNULL, stderr=STDOUT)
                            print('   Running FFMPEG to: '+ os.path.basename(output))
                            os.system(ffmpegPath+' -y -i "' + audiofilename +  '"  -f wav -bitexact -acodec pcm_s16le -ar 48000 -ac '+str(channeljson)+' -filter:a "volume='+volume+'" -map_metadata -1 -loglevel quiet temp/temp.wav')
                        except:
                            print("   [ERROR]: FFMPEG is not exist\n\n   1 missing")
                            time.sleep(1)
                            BadContinue()
                        audiofilename1 = os.path.splitext(output)[0]
                        Raki()
            except Exception as e:
                print('     No file found')
        print('\n\n<------------------------------->\n\n   Encoding Type: RIFF WAVE (PCM)\n     Header Type: '+namepcmMode+'\n\n   What is your preferred option to convert?\n\n     [1] pick single file\n     [2] pick multiple files\n     [0] Back\n')
        try:
            opt12 = int(input("   Choose the option -----> "))
        except:
            print('     Invalid option')
            O2()
        if(opt12 == 1):
            Opt2()
        if(opt12 == 2):
            Opt1()
        if(opt12 == 0):
            Menu()
        if(opt12 > 2 or opt12 < 0):
            print('      Invalid numbers')
            O2()
        Continue()
    if(intoption == 2):
        if getpcm == 1:
            O2()
        else:
            print('     Invalid Mode. reconfig the config.json')
            time.sleep(1)
            Menu()
    def O3():
        def Opt1():
            try:
                print("\n   Run Tkinter:\n   [NOTE]: If can't find filedialog. Minimize the window\n")
                outputaudiofile = filedialog.askopenfilenames(initialdir=pathlib.Path, title='Select the audio file', filetypes=(("Audio files (*.wav,*.opus,*.mp3,*.ogg)","*.wav *.opus *.mp3 *.ogg"),("All files","*.*")))
                if(not outputaudiofile):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        BadContinue()
                output = filedialog.askdirectory(initialdir=pathlib.Path,title="Select Location")
                if(not output):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        BadContinue()
                print('\n   Start Converting...\n')
                for listfiles in outputaudiofile:
                    listfiles1 = os.path.basename(listfiles)
                    print('   Running FFMPEG to: '+ listfiles1)
                    if(".ogg" in listfiles or ".opus" in listfiles or ".mp3" in listfiles or ".wav" in listfiles):
                            # Other Audio process
                            try:
                                run((ffmpegPath), stdout=DEVNULL, stderr=STDOUT)
                                os.system(ffmpegPath+' -y -i "'+listfiles+'"  -acodec libvorbis -ar 48000 -b:a '+str(intbitratevorb)+'k -ac '+str(channeljson)+' -filter:a "volume='+volume+'" -map_metadata -1 -loglevel quiet "'+output+'\\'+os.path.splitext(listfiles1)[0]+'.ogg"')
                                print("   DONE: " + output.replace('/','\\')+"\\"+os.path.splitext(listfiles1)[0]+'.ogg \n')
                            except:
                                print("   [ERROR]: FFMPEG is not exist\n\n   1 missing")
                                time.sleep(1)
                                BadContinue()
                Continue()
            except:
                time.sleep(1)
                BadContinue()
        def Opt2():
            print("\n   Run Tkinter:\n   [NOTE]: If can't find filedialog. Minimize the window\n")
            audiofilename = filedialog.askopenfilename(initialdir=pathlib.Path, title='Select the audio file', filetypes=(("Audio files (*.wav,*.opus,*.mp3,*.ogg)","*.wav *.opus *.mp3 *.ogg"),("All files","*.*")))
            if(not audiofilename):
                print("   [FAILED]: Tkinter Cancelled")
                time.sleep(1)
                BadContinue()
            audiofilename1=os.path.basename(audiofilename)
            output = filedialog.asksaveasfilename(filetypes=[("Ogg Vorbis",'*.ogg')],initialdir=pathlib.Path,title="Select Location",initialfile=os.path.splitext(audiofilename1)[0]+".ogg")
            if(not output):
                print("   [FAILED]: Tkinter Cancelled")
                time.sleep(1)
                BadContinue()
            try:
                print('\n   Start Converting...\n')
                            # Other Audio process
                try:
                    run((ffmpegPath), stdout=DEVNULL, stderr=STDOUT)
                    print('   Running FFMPEG to: '+ os.path.basename(audiofilename))
                    os.system(ffmpegPath+' -y -i "' + audiofilename +  '"  -acodec libvorbis -ar 48000  -b:a '+str(intbitratevorb)+'k -ac '+str(channeljson)+' -filter:a "volume='+volume+'" -map_metadata -1 -loglevel quiet "'+output+'"')
                    print("   DONE: " + output.replace('/','\\') + "\n")
                except:
                    print("   [ERROR]: FFMPEG is not exist\n\n   1 missing")
                    time.sleep(1)
                    BadContinue()
                Continue()
            except:
                time.sleep(1)
                BadContinue()
        def O3():
            print('\n\n<------------------------------->\n\n   Convert Type: Ogg\n   '+bitratevorbistxt+'\n\n   What is your preferred option to convert?\n\n     [1] pick single file\n     [2] pick multiple files\n     [0] Back\n')
            try:
                opt12 = int(input("   Choose the option -----> "))
            except:
                print('     Invalid option')
                O3()
            if(opt12 == 1):
                Opt2()
            if(opt12 == 2):
                Opt1()
            if(opt12 == 0):
                Menu()
            if(opt12 > 2 or opt12 < 0):
                print('      Invalid numbers')
                O3()
        O3()
        Continue()
    if(intoption == 3):
        O3()
    if(intoption == 4):
        try:
            os.mkdir('outputback')
        except:
            pass
        def o6():
            print("\n\n<------------------------------->\n\n      Choose to application to use to convert\n\n       [1] Use VGMStream (recommended) (requires vgmstream)\n\n       [2] Uncook PCM Data (vgmstream not required)\n           [WARN]: Don't recommended this options because didn't supported to other encoding like opus\n\n       [0] Exit\n")
            try:
                optionforback = int(input('\n     Choose the options -----> '))
            except:
                print('     Invalid Option')
                o6()
            if(optionforback == 0):
                Menu()
            if(optionforback > 2 or optionforback < 0):
                print('     Invalid numbers')
                Menu()
            if(optionforback == 1):
                def Opt1():
                    print("\n   Run Tkinter:\n   [NOTE]: If can't find filedialog. Minimize the window\n")
                    outputaudiofile = filedialog.askopenfilenames(initialdir=pathlib.Path, title='Select the Ubisoft RAKI file', filetypes=(("Ubisoft RAKI",'*.wav.ckd'),("All files","*.*")))
                    print('\n   Start Converting...\n')
                    if(not outputaudiofile):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        BadContinue()
                    output = filedialog.askdirectory(initialdir=pathlib.Path,title="Select Location")
                    if(not output):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        BadContinue()
                    print('\n   Start Converting...\n')
                    for listfiles in outputaudiofile:
                        listfiles1 = os.path.basename(listfiles)
                        if(".ckd" in listfiles):
                            try:
                                run((vgmstreamPath), stdout=DEVNULL, stderr=STDOUT) # checks if you have vgmstream
                                print('\n   Converting back to original audio file: '+ os.path.splitext(listfiles1)[0])
                                call([vgmstreamPath, '-o', output+ os.path.splitext(listfiles1)[0], listfiles],stdout=DEVNULL, stderr=STDOUT) # main vgmstream commands
                            except Exception as e:
                                print('   [ERROR] VGMSTREAM was not exist\n ') # it says not found
                                time.sleep(1)
                                BadContinue()
                            print('   DONE: '+os.path.splitext(listfiles1)[0] +'\n')
                def Opt2():
                    print("\n   Run Tkinter:\n   [NOTE]: If can't find filedialog. Minimize the window\n")
                    outputaudiofile = filedialog.askopenfilename(initialdir=pathlib.Path, title='Select the Ubisoft RAKI file', filetypes=(("Ubisoft RAKI",'*.wav.ckd'),("All files","*.*")))
                    if(not outputaudiofile):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        BadContinue()
                    filenameinfo = os.path.basename(outputaudiofile)
                    output = filedialog.asksaveasfilename(filetypes=[("Wave Format",'*.wav')],initialdir=pathlib.Path,title="Select Location",initialfile=os.path.splitext(filenameinfo)[0]+'.wav')
                    if(not output):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        BadContinue()
                    print('\n   Start Converting...\n')
                    try:
                        run((vgmstreamPath), stdout=DEVNULL, stderr=STDOUT) # checks if you have vgmstream
                        print('\n   Converting back to original audio file: '+ os.path.splitext(os.path.basename(outputaudiofile))[0])
                        call([vgmstreamPath, '-o', output+"\\", outputaudiofile],stdout=DEVNULL, stderr=STDOUT) # main vgmstream commands
                    except Exception as e:
                        print('   [ERROR] VGMSTREAM was not exist\n ') # it says not found
                        time.sleep(1)
                        BadContinue()
                    print('   DONE: '+os.path.splitext(output)[0] +'\n')
                def O4():
                    print('\n\n<------------------------------->\n\n   Uncook Type:VGMStream\n\n   What is your preferred option to convert?\n\n     [1] pick single file\n     [2] pick multiple files\n     [0] Back\n')
                    try:
                        opt12 = int(input("   Choose the option -----> "))
                    except:
                        print('     Invalid option')
                        O4()
                    if(opt12 == 1):
                        Opt2()
                    if(opt12 == 2):
                        Opt1()
                    if(opt12 == 0):
                        o6()
                    if(opt12 > 2 or opt12 < 0):
                        print('      Invalid numbers')
                        O4()
                O4()
            if(optionforback == 2):
                def Opt1():
                    print("\n   Run Tkinter:\n   [NOTE]: If can't find filedialog. Minimize the window\n")
                    outputaudiofile = filedialog.askopenfilenames(initialdir=pathlib.Path, title='Select the audio file', filetypes=(("Ubisoft RAKI",'*.wav.ckd'),("All files","*.*")))
                    if(not outputaudiofile):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        BadContinue()
                    output = filedialog.askdirectory(initialdir=pathlib.Path,title="Select Location")
                    if(not output):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        BadContinue()
                    print('\n   Start Converting...\n')
                    for listfiles in outputaudiofile:
                        listfiles1 = os.path.basename(listfiles)
                        if(".ckd" in listfiles1):
                            with open(listfiles, "rb") as f:
                                print('\n   Uncook back to original audio file: '+ listfiles)
                                try:
                                    uselessbyte = f.read(12)
                                    pcmchecker = f.read(4) # checks if your file is pcm
                                except Exception as e:
                                     print(str(e))
                                if(pcmchecker== b'pcm '):
                                    uselessbyte = f.read(28)
                                    marksig = f.read(4)
                                    multiplier2 = 0
                                    if marksig == b'MARK':
                                            try:
                                                uselessbyte = f.read(4)
                                                multiplier = struct.unpack("i",f.read(4))[0]
                                                uselessbyte = f.read(8)
                                                multiplier3 = struct.unpack("i",f.read(4))[0]
                                                multiplier2 = int(multiplier+multiplier3+2)
                                                datatitle = f.read(4)
                                            except Exception as e:
                                                print("wrong wav file")
                                                time.sleep(1)
                                                BadContinue()
                                    else:
                                                datatitle = marksig
                                    uselessbyte = f.read(4)
                                    data = f.read(4)
                                    endriff = f.read(16) # header for riff data
                                    f.read(multiplier2)
                                    audiodata = f.read() # audio data
                                    try:
                                        encodeback = open(output+"\\" + os.path.splitext(listfiles1)[0], "wb")
                                        encodeback.write(b'RIFF')  # main title of riff
                                        encodeback.write(struct.pack("I",int(struct.unpack("I",data)[0]+36))) # whole file length
                                        encodeback.write(b'WAVEfmt ')
                                        encodeback.write(struct.pack("I",16)) # full header of riff
                                        encodeback.write(endriff)
                                        encodeback.write(datatitle) # data title
                                        encodeback.write(data)
                                        encodeback.write(audiodata)
                                        print('   DONE: '+os.path.splitext(listfiles1)[0] +'\n')
                                    except Exception as e:
                                        print('   [ERROR] This file is used from another process\n ')
                                else:
                                    print('   BAD FILE: "'+listfiles1+ '" this is not pcm file')
                        else:
                             print('   [ERROR]: This file '+ listfiles1+' is not .ckd')
                def Opt2():
                    print("\n   Run Tkinter:\n   [NOTE]: If can't find filedialog. Minimize the window\n")
                    outputaudiofile = filedialog.askopenfilename(initialdir=pathlib.Path, title='Select the audio file', filetypes=(("Ubisoft RAKI",'*.wav.ckd'),("All files","*.*")))
                    if(not outputaudiofile):
                        print("   [FAILED]: Tkinter Cancelled")
                        BadContinue()
                    filenameinfo = os.path.basename(outputaudiofile)
                    output = filedialog.asksaveasfilename(filetypes=[("Wave Format",'*.wav')],initialdir=pathlib.Path,title="Select Location",initialfile=os.path.splitext(filenameinfo)[0]+'.wav')
                    if(not output):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        BadContinue()
                    print('\n   Start Converting...\n')
                    with open(outputaudiofile, "rb") as f:
                                print('\n   Uncook back to original audio file: '+ os.path.splitext(filenameinfo)[0])
                                f.read(12)
                                pcmchecker = f.read(4) # checks if your file is pcm
                                if(pcmchecker== b'pcm '):
                                    f.read(28)
                                    marksig = f.read(4)
                                    multiplier2 = 0
                                    if marksig == b'MARK':
                                            try:
                                                f.read(4)
                                                multiplier = struct.unpack("i",f.read(4))[0]
                                                f.read(8)
                                                multiplier3 = struct.unpack("i",f.read(4))[0]
                                                multiplier2 = int(multiplier+multiplier3+2)
                                                datatitle = f.read(4)
                                            except Exception as e:
                                                print("wrong wav file")
                                                time.sleep(1)
                                                BadContinue()
                                    else:
                                        datatitle = marksig
                                    f.read(4)
                                    data = f.read(4)
                                    endriff = f.read(16) # header for riff data
                                    f.read(multiplier2)
                                    audiodata = f.read() # audio data
                                    try:
                                        encodeback = open(output, "wb")
                                        encodeback.write(b'RIFF')  # main title of riff
                                        encodeback.write(struct.pack("I",int(struct.unpack("I",data)[0]+36))) # whole file length
                                        encodeback.write(b'WAVEfmt ')
                                        encodeback.write(struct.pack("I",16)) # full header of riff
                                        encodeback.write(endriff)
                                        encodeback.write(datatitle) # data title
                                        encodeback.write(data)
                                        encodeback.write(audiodata)
                                        print('   DONE: '+os.path.splitext(outputaudiofile)[0] +'\n')
                                    except Exception as e:
                                        print('   [ERROR] This file is used from another process\n ')
                                else:
                                    print('   BAD FILE: "'+outputaudiofile+ '" this is not pcm file')
                def O5():
                    print('\n\n<------------------------------->\n\n   Uncook Type:Decrypt Cook Wave PCM File (bulit-in)\n\n    What is your preferred option to convert?\n\n     [1] pick single file\n     [2] pick multiple files\n     [0] Back\n')
                    try:
                        opt12 = int(input("   Choose the option -----> "))
                    except:
                        print('     Invalid option')
                        O5()
                    if(opt12 == 1):
                        Opt2()
                    if(opt12 == 2):
                        Opt1()
                    if(opt12 == 0):
                        o6()
                    if(opt12 > 2 or opt12 < 0):
                        print('      Invalid numbers')
                        O5()
                O5()
        o6()
        Continue()
    if(intoption == 5):
        print('\n\n<------------------------------->\n\n     Help:\n\n     Command 1/2/3 - Cook Wav to (wav.ckd or .ogg)\n       Requirements:\n          - Download and Install FFMPEG\n          - Requires VGAudio v.2.2.1 (include in audiotools.zip) - if you choose command 1 \n\n       How to use?:\n          Step 1: Make sure you have an audio file\n            Supported Formats: (*.wav,*.mp3,*.opus and *.ogg)\n          Step 2: Choose 1 or 2 or 3  and choose type of convert\n          Step 3: Waiting to encoding\n          Step 4: When done, your cooked audio was saved to your directory\n\n     Command 4 - Convert back using output file\n       Requirements:\n          - Install VGMSTREAM (include in audiotools.zip)\n\n\n       How to use?\n          Step 1: Make sure you have an cooked audio file (*.wav.ckd)\n          Step 2: Choose 4 and choose type of convert\n          Step 3: Waiting a few seconds to finish\n          Step 4: When done, your file was saved to your directory\n\n     How Audio Maker Works in Games:\n          PCM(wav) uses for ambs, ui sounds and ui music(pcm)\n          Nintendo(Libopus) uses for songs, ui music\n          Ogg uses for online music\n\n     How to config or change header on config.json?\n       1.Click config.json and choose your software to configure it(ex. Notepad):\n          Types of PCM to change header(pcmMode):\n            normal = Normal header in JD2020-2022\n            oldVersion = Old Header in JD2017-2019\n            titlepage = Just Dance TitlePage (with signature)\n\n          Types of cooked libopus to change header:\n            normal = Normal Header on JD2020-2022\n            oldVersion = Old Header on JD2017-2019\n     How to change bitrate:\n       Step 1: open config.json\n       Step 2: below on vgmstreamPath change value into bytes\n          (128000 = 128kb)\n\n       FAQ:\n          Q:Can i change the value in config.json?\n          A:Yes\n\n          Q:Is that supported from any platform?\n          A:maybe, for cooked pcm but opus didn'+"'"+'t supported for nx only\n\n          Q:is the format of nintendo opus the same as ffmpeg opus?\n          A:No, because the nintendo opus has a different structure\n\n          Q:What Nx means?\n          A:the codename on Nintendo Switch\n')
        time.sleep(1)
        BadContinue()
    if(intoption == 6):
        print('\n\n<------------------------------->\n\n   Changelog:\n     Version 1.0\n       - New Launch\n       - Improvement CLI\n       - Added Features (back to wav conversion using output)\n       - Add feature "Decrypt Data" from command 4 it does not required vgmstream\n       - Add feature "Convert Audio using nintendo opus" from Command 1 which may better than ogg compression. [Command 1]\n       - Add optional feature "Convert Audio To Ogg". [Command 3]\n\n     Version 1.1\n       - Add Config to configure the code\n       - Add single file on Command 4\n       - Adding Brackets in per window\n       - Add More audio codes on config\n\n          Ubisoft RAKI PCM Type:\n            Normal - New Header/used for ambs/used for ui\n            Old Version - Old Types of Header/used ui in jd2017-2019\n            TitlePage - Main titlepage in Just Dance\n\n          Ubisoft RAKI Nintendo Opus Types:\n            Normal - New Header/used for ambs/used for ui\n            Old Version - Old Types of Header/used ui in jd2017-2019\n\n       - Fix issues from input directory on Commmand 2\n       - Fix issues from Command 3\n       - Fix crash on changelog when exit\n       - Updated ReadMe\n       - Update Command 5\n\n     Version 1.2\n       - Change input folder convert type into multiple file\n       - Fix file names from input to output file name\n       - remove input, output and outputback folder\n\n     Version 1.3\n       - The info of the config are shown in main menu\n       - Add bitrate key in config\n       - Fix bug update\n       - Fix crash detects not pcm from multiple files on "Uncook PCM Data"\n       - Add Refresh Function on Menu\n')
        time.sleep(1)
        BadContinue()
    if(intoption > 6 or option < 0):
        print('\n     Invalid numbers!')
        Menu()
def Continue():
    try:
        os.remove('temp/temp.wav')
    except:
        pass
    input("   Press Enter to continue...")
    Menu()
def BadContinue():
    try:
        os.remove('temp/temp.wav')
    except:
        pass
    print('\n')
    input("   Press Enter to continue...")
    Menu()
Menu()
exit()