import os, struct, time, pathlib,json
from datetime import datetime
from tkinter import filedialog
from tkinter import *
from subprocess import DEVNULL, STDOUT, run, call
def Menu():
    os.system('cls')
    print('Loading...')
    notchan=""
    noteopus=""
    notevorb=""
    changing=0
    try:
        con=json.load(open("config.json", "r"))
        volume=str(con["addVolume"])
        channeljson=int(con["channel"])
        modepcm=con["pcmMode"]
        modeopus=con["opusMode"]
        if channeljson==1 or channeljson==2:
            pass
        else:
            notchan='\n   Channel value failed. Channel was default into 2'
            channeljson=2
        getpcm=0
        getopus=0
        ffmpegPath=con["ffmpegPath"]
        vgaudioPath=str(con["nintendoVGAudioPath"])
        vgmstreamPath=str(con["vgmstreamPath"])
        def conjson1(volume,modepcm,modeopus,channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,opubitrate,vorbitrate,settings):
            try:
                datjs=open('config.json','w')
                print('Updating config...')
                datjs.write('''{
    "addVolume": ''')
                datjs.write(str(volume))
                datjs.write(''',    
    "version": 1.5,
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
                if(settings==0):
                    try:
                        opubitrate=con["opusbitrate"]
                    except Exception as e:
                        print(str(e))
                        opubitrate=256000
                datjs.write(str(opubitrate))
                datjs.write(''',
    "vorbisbitrate": ''')
                if(settings==0):
                    try:
                        vorbitrate=con["vorbisbitrate"]
                    except:
                        vorbitrate=320000
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
            if pcmitems["pcmModeType"]==modepcm:
                info=int(pcmitems["id"])
                pcmhead1=int(pcmitems["pcmHead"])
                pcmhead2=int(pcmitems["pcmHead1"])
                pcmhead3=int(pcmitems["pcmHead2"])
                pcmhead4=int(pcmitems["pcmHead3"])
                pcmfmt=int(pcmitems["pcmfmt"])
                pcmfmt2=int(pcmitems["pcmfmt2"])
                markcount=0
                strgcount=0
                strgtitle=b''
                strgbyte=b''
                markbyte=b''
                marktitle=b''
                byteaddinfo =b''
                if pcmitems["mark"]:
                    marktitle=b'MARK'
                    marklength=int(pcmitems["marklength"])
                    markbyte=b''
                    while marklength>0:
                        markname="mark"+str(marklength)
                        markbyte=struct.pack("I",int(pcmitems["markdata"][0][markname]))+markbyte
                        markcount+=1
                        addinfo=markcount
                        infomultplier=pcmitems["markdata"][0]["multiplier"][0]["addinfo"+str(addinfo)]
                        if pcmitems["markdata"][0]["multiplieronaddinfo"+str(addinfo)]:
                            multplytodatapcm=int((pcmitems["markdata"][0][infomultplier]-addinfo)/4)
                            byteaddinfomutiply=struct.pack("I",int(pcmitems["markdata"][0]["addinfohead"+str(addinfo)]))
                            byteaddinfo=byteaddinfo+(byteaddinfomutiply*multplytodatapcm)
                        else:
                            byteaddinfo=byteaddinfo+struct.pack("I",int(pcmitems["markdata"][0]["addinfohead"+str(addinfo)]))
                        marklength=marklength - 1
                if pcmitems["strg"]:
                    strgtitle=b'STRG'
                    strglength=int(pcmitems["strglength"])
                    strgbyte=b''
                    while strglength>0:
                        strgname="strg"+str(strglength)
                        strgcount+=1
                        strgbyte=struct.pack("I",int(pcmitems["markdata"][0][strgname]))+strgbyte
                        addinfo=markcount+strgcount
                        infomultplier=pcmitems["markdata"][0]["multiplier"][0]["addinfo"+str(addinfo)]
                        if pcmitems["markdata"][0]["multiplieronaddinfo"+str(addinfo)]:
                            multplytodatapcm=int((pcmitems["markdata"][0][infomultplier]-strgcount)/4)
                            byteaddinfomutiply=struct.pack("I",int(pcmitems["markdata"][0]["addinfohead"+str(addinfo)]))*multplytodatapcm
                            byteaddinfo=byteaddinfo+byteaddinfomutiply
                        else:
                            byteaddinfo=byteaddinfo+struct.pack("I",int(pcmitems["markdata"][0]["addinfohead"+str(addinfo)]))
                        strglength=strglength - 1
                addinfobyte=byteaddinfo
                getpcm=1
        for nopusitems in con["opusModeData"]:
            if nopusitems["opusModeType"]==modeopus:
                info=int(nopusitems["id"])
                opushead1=int(nopusitems["opusHead"])
                opushead2=int(nopusitems["opusHead2"])
                opushead3=int(nopusitems["opusHead3"])
                opushead4=int(nopusitems["opusHead4"])
                opusheadfmt=int(nopusitems["opusfmt"])
                opusheadfmt2=int(nopusitems["opusfmt2"])
                adindatahead1=int(nopusitems["adindata"][0]["adin1"])
                adindatahead2=int(nopusitems["adindata"][0]["adin2"])
                datatitlehead=int(nopusitems["datatitlehead"])
                intbytehead=nopusitems["16bitonInt32"]
                getopus=1
    except:
        current_time=datetime.now()
        formatted_time=current_time.strftime('%Y-%m-%H-%M-%S')
        try:
            os.rename("config.json","config-old-"+formatted_time+".json")
            print("   Config Failed to read\n   Renew Config...")
        except:
            print('   Making Config...')
        datjs=open('config.json','w')
        datjs.write('''{
    "addVolume": 1,
    "version": 1.5,
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
        autobitupd=con["vorbisbitrate"]
    except:
        autobitupd=0
    try:
        autobitupd1=con["opusbitrate"]
    except:
        autobitupd1=0
    try:
        ver=float(con["version"])
    except:
        conjson1(volume,modepcm,modeopus,channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,autobitupd1,autobitupd,0)
    if ver==1.5:
        pass
    else:
        conjson1(volume,modepcm,modeopus,channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,autobitupd1,autobitupd,0)
    for nopusitems1 in con["opusModeData"]:
        if nopusitems1["opusModeType"]==modeopus:
            title0=str(nopusitems1["opusTitle"])
    for pcmitems1 in con["pcmModeData"]:
        if pcmitems1["pcmModeType"]==modepcm:
            title1=str(pcmitems1["pcmtitle"])
    if getpcm==0:
        namepcmMode="Invalid pcm"
    elif(modepcm=="normal" or modepcm=="oldVersion" or modepcm=="titlepage"):
        namepcmMode=title1
    else:
        namepcmMode=str(title0+" (Custom Mode)")
    if getopus==0:
        nameopusMode="Invalid opus"
    elif(modeopus=="normal" or modeopus=="oldVersion"):
        nameopusMode=title0
    else:
        nameopusMode=str(title0+" (Custom Mode)")
    if channeljson==1:
        txtchanneljson="Channel Type: Mono"
    else:
        txtchanneljson="Channel Type: Stereo"
    intvolumeset=int(con["addVolume"]*100)
    txtvolumeset="Volume: "+ str(intvolumeset) + "%"
    try:
        bitrateopus=con["opusbitrate"]
        if bitrateopus<0:
            bitrateopus=92000
            noteopus="\n   [Opus]: Invalid value. bitrate is set to 92000"
            bitrateopustxt="Opus Audio Bitrate: Medium"
        elif bitrateopus==0:
            bitrateopustxt="Opus Audio Bitrate: Auto"
        elif bitrateopus<64000:
            bitrateopustxt="Opus Audio Bitrate: Low"
        elif bitrateopus<192000:
            bitrateopustxt="Opus Audio Bitrate: Medium"
        elif bitrateopus<256000 or bitrateopus>256000:
            bitrateopustxt="Opus Audio Bitrate: High"
        elif bitrateopus==256000:
            bitrateopustxt="Opus Audio Bitrate: High (constant bitrate)"
    except:
        bitrateopus=92000
        noteopus="\n   [Opus]: Invalid key. bitrate is set to 92000"
        bitrateopustxt="Vorbis Audio Bitrate: Medium"
    try:
        bitratevorbis=con["vorbisbitrate"]
        if bitratevorbis<0:
            bitratevorbis=128000
            notevorb="   [Vorbis]: Invalid value. bitrate is set to 128000"
            bitratevorbistxt="Vorbis Audio Bitrate: Medium"
        elif bitratevorbis==0:
            bitratevorbistxt="Vorbis Audio Bitrate: Auto"
        elif bitratevorbis<92000:
            bitratevorbistxt="Vorbis Audio Bitrate: Low"
        elif bitratevorbis<192000:
            bitratevorbistxt="Vorbis Audio Bitrate: Medium"
        elif bitratevorbis<320000 or bitratevorbis>320000:
            bitratevorbistxt="Vorbis Audio Bitrate: High"
        elif bitratevorbis==320000:
            bitratevorbistxt="Vorbis Audio Bitrate: High (constant bitrate)"
        intbitratevorb=int(bitratevorbis/1000)
    except:
        bitratevorbis=128000
        notevorb="\n   [Vorbis]: Invalid key. bitrate is set to 128000"
        bitratevorbistxt="Vorbis Audio Bitrate: Medium"
        intbitratevorb=int(bitratevorbis/1000)
    missingcnt=0
    try:
        call((ffmpegPath), stdout=DEVNULL, stderr=STDOUT)
        ffmpeg=1
        ffmpegmisdesc="FFMPEG - Convert Audio to WAVE Format (found)"
    except:
        ffmpeg=0
        ffmpegmisdesc="FFMPEG - Convert Audio to WAVE Format (not found) - Visit in https://ffmpeg.org"
        missingcnt+=1
    try:
        call((vgaudioPath), stdout=DEVNULL, stderr=STDOUT)
        vgaudio=1
        vgaudiomisdesc="VGAudio - Convert WAVE to Nintendo opus format (found)"
    except:
        vgaudio=0
        vgaudiomisdesc="VGAudio - Convert WAVE to Nintendo opus format (not found) - extract the audiotools.zip"
        missingcnt+=1
    try:
        vgmstream=1
        call((vgmstreamPath), stdout=DEVNULL, stderr=STDOUT)
        vgmstreammisdesc="VGMSTREAM - Uncook back to WAVE (found)"
    except:
        vgmstream=0
        vgmstreammisdesc="VGMSTREAM - Uncook back to WAVE (not found) - extract the audiotools.zip"
        missingcnt+=1
    if ffmpeg==0 or vgmstream==0 or vgaudio==0:
        missing='\n   '+str(missingcnt)+" missing"
    else:
        missing=""
    os.system('cls')
    print('\n Welcome to Just Dance Nx Audio Maker \n (Version 1.5.1)\n    Made by MicoPH  \n    If refresh. click Enter'+notchan+noteopus+notevorb+'\n\n   Requirements:\n     '+ffmpegmisdesc+' \n     '+vgaudiomisdesc+'\n     '+vgmstreammisdesc+missing+'\n\n   PCM Mode: '+namepcmMode+" | Opus Mode: "+nameopusMode+"\n   "+txtchanneljson+" | "+txtvolumeset+"\n   "+bitrateopustxt+" | "+bitratevorbistxt+"\n\n     Choose the Options:\n     [1] Convert Audio to cooked nintendo opus file (Most recommended) (for songs only)\n     [2] Convert Audio to cooked pcm .wav format (this is only for amb, ui(sfx) and ui(pcm)\n     [3] Convert Audio to Ogg (optional feature)\n     [4] Convert Back to WAV FILE(.wav.ckd to .wav)\n     [5] Help\n     [6] Changelog\n     [7] Settings\n     [0] Exit\n\n")
    try:
        option=str(input("   Choose the option -----> "))
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
    if(intoption==0):
        time.sleep(2)
        exit()
    def O1():
        os.system('cls')
        def Opt1():
            def Raki(audiofilename1,listfiles1,listfiles):
                if(os.path.isfile("temp/temp.lopus")):
                    print('   Encoding: '+ listfiles1)
                    opussize=os.path.getsize("temp/temp.lopus") 
                    with open("temp/temp.wav", "rb") as b:
                        b.read(12)
                        formattitle=b.read(4)
                        bitbyte=struct.unpack("I", b.read(4))[0]
                        b.read(2)
                        channel=struct.unpack("H",b.read(2))[0]
                        riffdatainfo=b.read(12)
                        datatitle=b.read(4)
                        minidata=struct.unpack("I", b.read(4))[0]
                    with open("temp/temp.lopus", "rb") as f:
                        o1=f.read(8)
                        f.read(4)
                        o2=f.read(16)
                        f.read(4)
                        dataopus=f.read()
                        try:
                            opusenc=open(output+"\\" + audiofilename1 + ".wav.ckd", "wb")
                            opusenc.write(b'RAKI') 
                            opusenc.write(struct.pack('I',11)) 
                            opusenc.write(b'Nx  Nx  ') 
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
                            opusenc.write(struct.pack("I", opussize))  
                            opusenc.write(struct.pack('h',99))
                            opusenc.write(struct.pack("H",channel))
                            opusenc.write(riffdatainfo)
                            if intbytehead:
                                opusenc.write(struct.pack("H",0))
                            opusenc.write(struct.pack("I",int(minidata/((bitbyte*channel)/8)))) 
                            if intbytehead:
                                opusenc.write(struct.pack("H",0))
                                opusenc.write(struct.pack("I",0))
                            opusenc.write(o1)
                            opusenc.write(struct.pack("I", 512)) 
                            opusenc.write(o2)
                            opusenc.write(struct.pack("I", 120))
                            opusenc.write(dataopus) 
                            b.close
                            f.close
                            opusenc.close
                            outputres=output.replace('/','\\')+"\\"
                            filepathsize=os.path.getsize(listfiles)
                            if filepathsize<1000000:
                                filepathsizefloat=filepathsize/1024
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                bfrfilepathtxt=str(filepathsizefloatdec)+" KB"
                            elif filepathsize<1000000000:
                                filepathsizefloat=filepathsize/1024000
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                bfrfilepathtxt=str(filepathsizefloatdec)+" MB"
                            else:
                                filepathsizefloat=filepathsize/1024000000
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                bfrfilepathtxt=str(filepathsizefloatdec)+" GB"
                            filepathsize=os.path.getsize(output+"\\" + audiofilename1 + ".wav.ckd")
                            if filepathsize<1000000:
                                filepathsizefloat=filepathsize/1024
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                filepathtxt=str(filepathsizefloatdec)+" KB"
                            elif filepathsize<1000000000:
                                filepathsizefloat=filepathsize/1024000
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                filepathtxt=str(filepathsizefloatdec)+" MB"
                            else:
                                filepathsizefloat=filepathsize/1024000000
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                filepathtxt=str(filepathsizefloatdec)+" GB"
                            print('   DONE: '+ outputres + os.path.splitext(listfiles1)[0] + ".wav.ckd "+' \n     Size: '+bfrfilepathtxt+' --> '+filepathtxt+'\n')
                        except:
                            print('   [ERROR]: The file used from another process\n')
            try:
                print("\n   Run Tkinter:\n")
                openwindow=Tk()
                openwindow.title('')
                outputaudiofile=filedialog.askopenfilenames(initialdir=pathlib.Path, title='Select the audio file', filetypes=(("Audio files (*.wav,*.opus,*.mp3,*.ogg)","*.wav *.opus *.mp3 *.ogg"),("All files","*.*")))
                openwindow.destroy()
                if(not outputaudiofile):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                    Continue()
                print('   Input files: ')
                for lstinfo in outputaudiofile:
                    print('     '+os.path.basename(lstinfo))
                openwindow=Tk()
                openwindow.title('')
                output=filedialog.askdirectory(initialdir=pathlib.Path,title="Select Location")
                openwindow.destroy()
                print('   Directory: '+os.path.basename(output))
                if(not output):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                    Continue()
                    exit()
                print('\n   Start Converting...\n')
                for listfiles in outputaudiofile:
                    def startRun():
                        listfiles1=os.path.basename(listfiles)
                        if(".ogg" in listfiles or ".opus" in listfiles or ".mp3" in listfiles or ".wav" in listfiles):
                            try:
                                try:
                                    os.mkdir('temp')
                                except:
                                    pass
                                run((ffmpegPath), stdout=DEVNULL, stderr=STDOUT)
                                print('   Running FFMPEG to: '+ listfiles1)
                                call([ffmpegPath,'-y','-i',listfiles,'-f','wav','-bitexact','-ar','48000','-ac',str(channeljson),'-filter:a','volume='+volume,'-map_metadata','-1',os.getcwd()+'\\temp\\temp.wav'],stdout=DEVNULL, stderr=STDOUT)
                                if not os.path.isfile(os.getcwd()+'\\temp\\temp.wav'):
                                    print('\n     [ERROR]: Not recognized FFMPEG\n')
                                    Continue()
                                    exit()
                                try:
                                    run((vgaudioPath), stdout=DEVNULL, stderr=STDOUT)
                                    print('   Running VGAudio: '+ listfiles1)
                                    if bitrateopus==0:
                                        call([vgaudioPath, os.getcwd()+'\\temp\\temp.wav', os.getcwd()+'\\temp\\temp.lopus', '--no-loop', '--opusheader','standard'],stdout=DEVNULL, stderr=STDOUT)
                                    else:
                                        call([vgaudioPath, os.getcwd()+'\\temp\\temp.wav', os.getcwd()+'\\temp\\temp.lopus', '--bitrate', str(bitrateopus), '--no-loop', '--opusheader','standard'],stdout=DEVNULL, stderr=STDOUT)
                                except:
                                    print("     [ERROR]: VGAudio (Nintendo opus) is not initialized\n")
                                    time.sleep(1)
                                    Continue()
                                    exit()
                                if not os.path.isfile(os.getcwd()+'\\temp\\temp.lopus'):
                                    print('\n     [ERROR]: Not recognized VGAudio\n')
                                    Continue()
                                    exit()
                            except:
                                print("   [ERROR]: FFMPEG is not initialized\n")
                                time.sleep(1)
                                Continue()
                                exit()
                            Raki(os.path.splitext(listfiles1)[0],listfiles1,listfiles)
                    if(os.path.isfile(output+"/"+os.path.splitext(os.path.basename(listfiles))[0]+".wav.ckd")):
                        print('   File: "'+os.path.basename(listfiles)+'"')
                        overwritteninput=str(input("   Are you sure that file will be overwritten (y or n)? "))
                        if overwritteninput=="y" or overwritteninput=="Y":
                            startRun()
                        else:
                            print('   The file: "'+os.path.basename(listfiles)+'" was canceled')
                    else:
                        startRun()
            except:
                pass
        def Opt2():
            def Raki():
                if(os.path.isfile("temp/temp.lopus")):
                    print('   Encoding: '+ filenameinfo)
                    opussize=os.path.getsize("temp/temp.lopus") 
                    with open("temp/temp.wav", "rb") as b:
                        b.read(12)
                        formattitle=b.read(4)
                        bitbyte=struct.unpack("I", b.read(4))[0]  
                        b.read(2)
                        channel=struct.unpack("H",b.read(2))[0]
                        riffdatainfo=b.read(12)
                        datatitle=b.read(4)
                        minidata=struct.unpack("I", b.read(4))[0]
                    with open("temp/temp.lopus", "rb") as f:
                        o1=f.read(8)
                        f.read(4)
                        o2=f.read(16)
                        f.read(4)
                        dataopus=f.read()
                        try:
                            with open(output,'wb') as opusenc:
                                opusenc.write(b'RAKI') 
                                opusenc.write(struct.pack('I',11)) 
                                opusenc.write(b'Nx  Nx  ') 
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
                                opusenc.write(struct.pack("I", opussize))  
                                opusenc.write(struct.pack('h',99))
                                opusenc.write(struct.pack("H",channel))
                                opusenc.write(riffdatainfo)
                                if intbytehead:
                                    opusenc.write(struct.pack("H",0))
                                opusenc.write(struct.pack("I",int(minidata/((bitbyte*channel)/8)))) 
                                if intbytehead:
                                    opusenc.write(struct.pack("H",0))
                                    opusenc.write(struct.pack("I",0))
                                opusenc.write(o1)
                                opusenc.write(struct.pack("I", 512)) 
                                opusenc.write(o2)
                                opusenc.write(struct.pack("I", 120)) 
                                opusenc.write(dataopus) 
                            b.close
                            f.close
                            opusenc.close
                            outputres=output.replace('/','\\')
                            filepathsize=os.path.getsize(audiofilename)
                            if filepathsize<1000000:
                                filepathsizefloat=filepathsize/1024
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                bfrfilepathtxt=str(filepathsizefloatdec)+" KB"
                            elif filepathsize<1000000000:
                                filepathsizefloat=filepathsize/1024000
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                bfrfilepathtxt=str(filepathsizefloatdec)+" MB"
                            else:
                                filepathsizefloat=filepathsize/1024000000
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                bfrfilepathtxt=str(filepathsizefloatdec)+" GB"
                            filepathsize=os.path.getsize(outputres)
                            if filepathsize<1000000:
                                filepathsizefloat=filepathsize/1024
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                filepathtxt=str(filepathsizefloatdec)+" KB"
                            elif filepathsize<1000000000:
                                filepathsizefloat=filepathsize/1024000
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                filepathtxt=str(filepathsizefloatdec)+" MB"
                            else:
                                filepathsizefloat=filepathsize/1024000000
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                filepathtxt=str(filepathsizefloatdec)+" GB"
                            print('   DONE: '+ outputres +' \n     Size: '+bfrfilepathtxt+' --> '+filepathtxt+'\n')
                            time.sleep(1)
                        except Exception as e:
                            print('   [ERROR]: The file used from another process\n')
                            time.sleep(1)
            try:
                print("\n   Run Tkinter:\n")
                openwindow=Tk()
                openwindow.title('')
                audiofilename=filedialog.askopenfilename(initialdir=pathlib.Path, title='Select the audio file', filetypes=(("Audio files (*.wav,*.opus,*.mp3,*.ogg)","*.wav *.opus *.mp3 *.ogg"),("All files","*.*")))
                openwindow.destroy()
                if(not audiofilename):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                    Continue()
                    exit()
                filenameinfo=os.path.basename(audiofilename)
                print('   Input file: '+filenameinfo)
                openwindow=Tk()
                openwindow.title('')
                output=filedialog.asksaveasfilename(filetypes=[("Ubisoft RAKI",'*.wav.ckd')],initialdir=pathlib.Path,title="Select Location",initialfile=os.path.splitext(filenameinfo)[0]+'.wav.ckd')
                openwindow.destroy()
                if(not output):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                    Continue()
                print('   Save file: '+os.path.basename(output))
                print('\n   Start Converting...\n')
                try:
                    os.mkdir('temp')
                except:
                    pass
                try:
                    run((ffmpegPath), stdout=DEVNULL, stderr=STDOUT)
                    print('   Running FFMPEG to: '+ filenameinfo)
                    call([ffmpegPath,'-y','-i',audiofilename,'-f','wav','-bitexact','-ar','48000','-ac',str(channeljson),'-filter:a','volume='+volume,'-map_metadata','-1',os.getcwd()+'\\temp\\temp.wav'],stdout=DEVNULL, stderr=STDOUT)
                    if not os.path.isfile(os.getcwd()+'\\temp\\temp.wav'):
                        print('\n     [ERROR]: Not recognized FFMPEG\n')
                        Continue()
                        exit()
                    try:
                        run((vgaudioPath), stdout=DEVNULL, stderr=STDOUT)
                        print('   Running VGAudio: '+filenameinfo)
                        if bitrateopus==0:
                            call([vgaudioPath, os.getcwd()+'\\temp\\temp.wav', os.getcwd()+'\\temp\\temp.lopus', '--no-loop', '--opusheader','standard'],stdout=DEVNULL, stderr=STDOUT)
                        else:
                            call([vgaudioPath, os.getcwd()+'\\temp\\temp.wav', os.getcwd()+'\\temp\\temp.lopus', '--bitrate', str(bitrateopus), '--no-loop', '--opusheader','standard'],stdout=DEVNULL, stderr=STDOUT)
                    except:
                        print("     [ERROR]: VGAudio (Nintendo opus) is not initialized\n")
                        time.sleep(1)
                        Continue()
                        exit()
                    if not os.path.isfile(os.getcwd()+'\\temp\\temp.lopus'):
                        print('\n     [ERROR]: Not recognized VGAudio\n')
                        Continue()
                        exit()
                except Exception as e:
                    print("   [ERROR]: FFMPEG is not initialized\n")
                    time.sleep(1)
                    Continue()
                    exit()
                Raki()
            except:
                pass
        print('\n   Encoding Type: Nintendo Opus\n     Header Type: '+nameopusMode+'\n   '+bitrateopustxt+'\n\n   What is your preferred option to convert?\n\n     [1] pick single file\n     [2] pick multiple files\n     [0] Back\n')
        try:
            opt12=int(input("   Choose the option -----> "))
        except:
            print('     Invalid option')
            O1()
        if(opt12==1):
            Opt2()
        if(opt12==2):
            Opt1()
        if(opt12==0):
            Menu()
        if(opt12>2 or opt12<0):
            os.system('cls')
            print('      Invalid numbers')
            O1()
        Continue()
    if(intoption==1):
        if ffmpeg==0 and vgaudio==0:
            print('     FFMPEG and VGAudio is missing')
            time.sleep(1)
            Menu()
            exit()
        if ffmpeg==0:
            print('     FFMPEG not found')
            time.sleep(1)
            Menu()
            exit()
        if vgaudio==0:
            print('     VGAudio not found')
            time.sleep(1)
            Menu()
            exit()
        if getopus==1 and ffmpeg==1 and vgaudio==1:
            O1()
        else:
            print('     Invalid Mode. reconfig the config.json')
            time.sleep(1)
            Menu()
            exit()
    def O2():
        os.system('cls')
        def Opt1():
            def Raki(audiofilename1, listfiles):
                if(os.path.isfile("temp/temp.wav")):
                    print('   Encoding: '+ audiofilename1)
                    with open("temp/temp.wav", "rb") as f:
                        f.read(12)
                        formattitle=f.read(4)
                        f.read(4)
                        audioformat=f.read(2)
                        numofchannels=struct.unpack('h',f.read(2))[0]
                        riffend=f.read(12)
                        datatitle=f.read(4)
                        data=f.read(4)
                        audiofile=f.read()
                        try:
                            denc=open(output+"\\" + audiofilename1 + ".wav.ckd", "wb")
                            denc.write(b'RAKI') 
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
                            denc.write(data) 
                            denc.write(audioformat)
                            denc.write(struct.pack('h',numofchannels))
                            denc.write(riffend) 
                            denc.write(addinfobyte)
                            denc.write(audiofile)  
                            f.close
                            denc.close
                            outputres=output.replace('/','\\')
                            filepathsize=os.path.getsize(listfiles)
                            if filepathsize<1000000:
                                filepathsizefloat=filepathsize/1024
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                bfrfilepathtxt=str(filepathsizefloatdec)+" KB"
                            elif filepathsize<1000000000:
                                filepathsizefloat=filepathsize/1024000
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                bfrfilepathtxt=str(filepathsizefloatdec)+" MB"
                            else:
                                filepathsizefloat=filepathsize/1024000000
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                bfrfilepathtxt=str(filepathsizefloatdec)+" GB"
                            filepathsize=os.path.getsize(output+"\\" + audiofilename1 + ".wav.ckd")
                            if filepathsize<1000000:
                                filepathsizefloat=filepathsize/1024
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                filepathtxt=str(filepathsizefloatdec)+" KB"
                            elif filepathsize<1000000000:
                                filepathsizefloat=filepathsize/1024000
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                filepathtxt=str(filepathsizefloatdec)+" MB"
                            else:
                                filepathsizefloat=filepathsize/1024000000
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                filepathtxt=str(filepathsizefloatdec)+" GB"
                            print('   DONE: '+ outputres + os.path.splitext(listfiles1)[0] + ".wav.ckd "+' \n     Size: '+bfrfilepathtxt+' --> '+filepathtxt+'\n')
                        except Exception as e:
                            print('   [ERROR]: The file used from another process\n')
            try:
                os.mkdir('temp/')
            except:
                pass
            try:
                print("\n   Run Tkinter:\n")
                openwindow=Tk()
                openwindow.title('')
                outputaudiofile=filedialog.askopenfilenames(initialdir=pathlib.Path, title='Select the audio file', filetypes=(("Audio files (*.wav,*.opus,*.mp3,*.ogg)","*.wav *.opus *.mp3 *.ogg"),("All files","*.*")))
                openwindow.destroy()
                if(not outputaudiofile):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                    Continue()
                    exit()
                print('   Input files: ')
                for lstinfo in outputaudiofile:
                    print('     '+os.path.basename(lstinfo))
                openwindow=Tk()
                openwindow.title('')
                output=filedialog.askdirectory(initialdir=pathlib.Path,title="Select Location")
                openwindow.destroy()
                if(not output):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                    Continue()
                    exit()
                print('   Directory: '+os.path.basename(output))
                print('\n   Start Converting...\n')
                for listfiles in outputaudiofile:
                    listfiles1=os.path.basename(listfiles)
                    def startRun():
                        if(".ogg" in listfiles or ".opus" in listfiles or ".mp3" in listfiles or ".wav" in listfiles):
                            try:
                                os.mkdir('temp')
                            except:
                                pass
                            try:
                                run((ffmpegPath), stdout=DEVNULL, stderr=STDOUT)
                                print('   Running FFMPEG to: '+ listfiles1)
                                call([ffmpegPath,'-y','-i',listfiles,'-f','wav','-bitexact','-ar','48000','-ac',str(channeljson),'-filter:a','volume='+volume,'-map_metadata','-1',os.getcwd()+'\\temp\\temp.wav'],stdout=DEVNULL, stderr=STDOUT)
                            except:
                                print("   [ERROR]: FFMPEG is not initialized\n")
                                time.sleep(1)
                                Continue()
                                exit()
                            if not os.path.isfile(os.getcwd()+'\\temp\\temp.wav'):
                                print('\n     [ERROR]: Not recognized FFMPEG\n')
                                Continue()
                                exit()
                            audiofilename1=os.path.splitext(listfiles1)[0]
                            Raki(audiofilename1,listfiles)
                    if(os.path.isfile(output+"/"+os.path.splitext(os.path.basename(listfiles))[0]+".wav.ckd")):
                        print('   File: "'+os.path.basename(listfiles)+'"')
                        overwritteninput=str(input("   Are you sure that file will be overwritten (y or n)? "))
                        if overwritteninput=="y" or overwritteninput=="Y":
                            startRun()
                        else:
                            print('   The file: "'+os.path.basename(listfiles)+'" was canceled')
                    else:
                        startRun()
            except:
                pass
        def Opt2():
            def Raki():
                if(os.path.isfile("temp/temp.wav")):
                    print('   Encoding: '+ os.path.basename(audiofilename))
                    with open("temp/temp.wav", "rb") as f:
                        f.read(12)
                        formattitle=f.read(4)
                        f.read(4)
                        audioformat=f.read(2)
                        numofchannels=struct.unpack('h',f.read(2))[0]
                        riffend=f.read(12)
                        datatitle=f.read(4)
                        data=f.read(4)
                        audiofile=f.read()
                        try:
                            with open(output,'wb') as denc:
                                denc.write(b'RAKI') 
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
                                denc.write(data) 
                                denc.write(audioformat)
                                denc.write(struct.pack('h',numofchannels))
                                denc.write(riffend) 
                                denc.write(addinfobyte)
                                denc.write(audiofile)  
                            f.close
                            denc.close
                            outputres=output.replace('/','\\')
                            filepathsize=os.path.getsize(audiofilename)
                            if filepathsize<1000000:
                                filepathsizefloat=filepathsize/1024
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                bfrfilepathtxt=str(filepathsizefloatdec)+" KB"
                            elif filepathsize<1000000000:
                                filepathsizefloat=filepathsize/1024000
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                bfrfilepathtxt=str(filepathsizefloatdec)+" MB"
                            else:
                                filepathsizefloat=filepathsize/1024000000
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                bfrfilepathtxt=str(filepathsizefloatdec)+" GB"
                            filepathsize=os.path.getsize(outputres)
                            if filepathsize<1000000:
                                filepathsizefloat=filepathsize/1024
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                filepathtxt=str(filepathsizefloatdec)+" KB"
                            elif filepathsize<1000000000:
                                filepathsizefloat=filepathsize/1024000
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                filepathtxt=str(filepathsizefloatdec)+" MB"
                            else:
                                filepathsizefloat=filepathsize/1024000000
                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                filepathtxt=str(filepathsizefloatdec)+" GB"
                            print('   DONE: '+ outputres +' \n     Size: '+bfrfilepathtxt+' --> '+filepathtxt+'\n')
                        except Exception as e:
                            print('   [ERROR]: The file used from another process\n')
            try:
                os.mkdir('temp/')
            except:
                pass
            try:
                print("\n   Run Tkinter:\n")
                openwindow=Tk()
                openwindow.title('')
                audiofilename=filedialog.askopenfilename(initialdir=pathlib.Path, title='Select the audio file', filetypes=(("Audio files (*.wav,*.opus,*.mp3,*.ogg)","*.wav *.opus *.mp3 *.ogg"),("All files","*.*")))
                openwindow.destroy()
                if(not audiofilename):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                    Continue()
                    exit()
                filenameinfo=os.path.basename(audiofilename)
                print('   Input file: '+filenameinfo)
                openwindow=Tk()
                openwindow.title('')
                output=filedialog.asksaveasfilename(filetypes=[("Ubisoft RAKI",'*.wav.ckd')],initialdir=pathlib.Path,title="Select Location",initialfile=os.path.splitext(filenameinfo)[0]+'.wav.ckd')
                openwindow.destroy()
                if(not output):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                    Continue()
                    exit()
                print('   Save file: '+os.path.basename(output))
                print('\n   Start Converting...\n')
                if(".ogg" in audiofilename or ".opus" in audiofilename or ".mp3" in audiofilename or ".wav" in audiofilename):
                    try:
                        os.mkdir('temp')
                    except:
                        pass
                    try:
                        run((ffmpegPath), stdout=DEVNULL, stderr=STDOUT)
                        print('   Running FFMPEG to: '+ os.path.basename(output))
                        call([ffmpegPath,'-y','-i',audiofilename,'-f','wav','-bitexact','-ar','48000','-ac',str(channeljson),'-filter:a','volume='+volume,'-map_metadata','-1',os.getcwd()+'\\temp\\temp.wav'],stdout=DEVNULL, stderr=STDOUT)
                    except:
                        print("   [ERROR]: FFMPEG is not initialized\n")
                        time.sleep(1)
                        Continue()
                        exit()
                    if not os.path.isfile(os.getcwd()+'\\temp\\temp.wav'):
                        print('\n     [ERROR]: Not recognized FFMPEG\n')
                        Continue()
                        exit()
                    Raki()
            except Exception as e:
                print('     No file found'+str(e))
        print('\n   Encoding Type: RIFF WAVE (PCM)\n     Header Type: '+namepcmMode+'\n\n   What is your preferred option to convert?\n\n     [1] pick single file\n     [2] pick multiple files\n     [0] Back\n')
        try:
            opt12=int(input("   Choose the option -----> "))
        except:
            print('     Invalid option')
            O2()
        if(opt12==1):
            Opt2()
        if(opt12==2):
            Opt1()
        if(opt12==0):
            Menu()
        if(opt12>2 or opt12<0):
            print('      Invalid numbers')
            O2()
        Continue()
    if(intoption==2):
        if ffmpeg==0:
            print('     FFMPEG not found')
            time.sleep(1)
            Menu()
            exit()
        if getpcm==1:
            O2()
        else:
            os.system('cls')
            print('     Invalid Mode. reconfig the config.json')
            time.sleep(1)
            Menu()
    def O3():
        os.system('cls')
        def Opt1():
            try:
                print("\n   Run Tkinter:\n")
                openwindow=Tk()
                openwindow.title('')
                outputaudiofile=filedialog.askopenfilenames(initialdir=pathlib.Path, title='Select the audio file', filetypes=(("Audio files (*.wav,*.opus,*.mp3)","*.wav *.opus *.mp3"),("All files","*.*")))
                openwindow.destroy()
                if(not outputaudiofile):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                    Continue()
                    exit()
                print('   Input files: ')
                for lstinfo in outputaudiofile:
                    print('     '+os.path.basename(lstinfo))
                openwindow=Tk()
                openwindow.title('')
                output=filedialog.askdirectory(initialdir=pathlib.Path,title="Select Location")
                openwindow.destroy()
                if(not output):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                    Continue()
                    exit()
                print('   Directory: '+os.path.basename(output))
                print('\n   Start Converting...\n')
                for listfiles in outputaudiofile:
                    listfiles1=os.path.basename(listfiles)
                    def startRun():
                        print('   Running FFMPEG to: '+ listfiles1)
                        if(".ogg" in listfiles or ".opus" in listfiles or ".mp3" in listfiles or ".wav" in listfiles):
                            try:
                                run((ffmpegPath), stdout=DEVNULL, stderr=STDOUT)
                                if bitratevorbis==0:
                                    call([ffmpegPath,'-y','-i',listfiles,'-acodec','libvorbis','-ar','48000','-ac',str(channeljson),'-filter:a','volume='+volume,'-map_metadata','-1',output+'\\'+os.path.splitext(listfiles1)[0]+'.ogg'],stdout=DEVNULL, stderr=STDOUT)
                                else:
                                    call([ffmpegPath,'-y','-i',listfiles,'-acodec','libvorbis','-ar','48000','-b:a',str(intbitratevorb)+'k','-ac',str(channeljson),'-filter:a','volume='+volume,'-map_metadata','-1',output+'\\'+os.path.splitext(listfiles1)[0]+'.ogg'],stdout=DEVNULL, stderr=STDOUT)
                                if not os.path.isfile(output+'\\'+os.path.splitext(listfiles1)[0]+'.ogg'):
                                    Continue()
                                    exit()
                                outputres=output.replace('/','\\')+"\\"
                                filepathsize=os.path.getsize(listfiles)
                                if filepathsize<1000000:
                                    filepathsizefloat=filepathsize/1024
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    bfrfilepathtxt=str(filepathsizefloatdec)+" KB"
                                elif filepathsize<1000000000:
                                    filepathsizefloat=filepathsize/1024000
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    bfrfilepathtxt=str(filepathsizefloatdec)+" MB"
                                else:
                                    filepathsizefloat=filepathsize/1024000000
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    bfrfilepathtxt=str(filepathsizefloatdec)+" GB"
                                filepathsize=os.path.getsize(outputres + os.path.splitext(listfiles1)[0] + ".ogg")
                                if filepathsize<1000000:
                                    filepathsizefloat=filepathsize/1024
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    filepathtxt=str(filepathsizefloatdec)+" KB"
                                elif filepathsize<1000000000:
                                    filepathsizefloat=filepathsize/1024000
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    filepathtxt=str(filepathsizefloatdec)+" MB"
                                else:
                                    filepathsizefloat=filepathsize/1024000000
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    filepathtxt=str(filepathsizefloatdec)+" GB"
                                print('   DONE: '+ outputres + os.path.splitext(listfiles1)[0] + ".ogg "+' \n     Size: '+bfrfilepathtxt+' --> '+filepathtxt+'\n')
                            except:
                                print("   [ERROR]: FFMPEG is not initialized\n")
                                time.sleep(1)
                                Continue()
                                exit()
                    if(os.path.isfile(output+"/"+os.path.splitext(os.path.basename(listfiles))[0]+".ogg")):
                        print('   File: "'+os.path.basename(listfiles)+'"')
                        overwritteninput=str(input("   Are you sure that file will be overwritten (y or n)? "))
                        if overwritteninput=="y" or overwritteninput=="Y":
                            startRun()
                        else:
                            print('   The file: "'+os.path.basename(listfiles)+'" was canceled')
                    else:
                        startRun()
                Continue()
            except:
                time.sleep(1)
                Continue()
                exit()
        def Opt2():
            print("\n   Run Tkinter:\n")
            openwindow=Tk()
            openwindow.title('')
            audiofilename=filedialog.askopenfilename(initialdir=pathlib.Path, title='Select the audio file', filetypes=(("Audio files (*.wav,*.opus,*.mp3)","*.wav *.opus *.mp3"),("All files","*.*")))
            openwindow.destroy()
            if(not audiofilename):
                print("   [FAILED]: Tkinter Cancelled")
                time.sleep(1)
                Continue()
            audiofilename1=os.path.basename(audiofilename)
            print('   Input file: '+audiofilename1)
            openwindow=Tk()
            openwindow.title('')
            output=filedialog.asksaveasfilename(filetypes=[("Ogg Vorbis",'*.ogg')],initialdir=pathlib.Path,title="Select Location",initialfile=os.path.splitext(audiofilename1)[0]+".ogg")
            openwindow.destroy()
            print('   Save file: '+os.path.basename(output))
            if(not output):
                print("   [FAILED]: Tkinter Cancelled")
                time.sleep(1)
                Continue()
            try:
                print('\n   Start Converting...\n')
                try:
                    run((ffmpegPath), stdout=DEVNULL, stderr=STDOUT)
                    print('   Running FFMPEG to: '+ os.path.basename(audiofilename))
                    if bitratevorbis==0:
                        call([ffmpegPath,'-y','-i',audiofilename,'-acodec','libvorbis','-ar','48000','-ac',str(channeljson),'-filter:a','volume='+volume,'-map_metadata','-1',output],stdout=DEVNULL, stderr=STDOUT)
                    else:
                        call([ffmpegPath,'-y','-i',audiofilename,'-acodec','libvorbis','-ar','48000','-b:a',str(intbitratevorb)+'k','-ac',str(channeljson),'-filter:a','volume='+volume,'-map_metadata','-1',output],stdout=DEVNULL, stderr=STDOUT)
                    if not os.path.isfile(output):
                        Continue()
                        exit()
                    outputres=output.replace('/','\\')
                    filepathsize=os.path.getsize(audiofilename)
                    if filepathsize<1000000:
                        filepathsizefloat=filepathsize/1024
                        filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                        bfrfilepathtxt=str(filepathsizefloatdec)+" KB"
                    elif filepathsize<1000000000:
                        filepathsizefloat=filepathsize/1024000
                        filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                        bfrfilepathtxt=str(filepathsizefloatdec)+" MB"
                    else:
                        filepathsizefloat=filepathsize/1024000000
                        filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                        bfrfilepathtxt=str(filepathsizefloatdec)+" GB"
                    filepathsize=os.path.getsize(outputres)
                    if filepathsize<1000000:
                        filepathsizefloat=filepathsize/1024
                        filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                        filepathtxt=str(filepathsizefloatdec)+" KB"
                    elif filepathsize<1000000000:
                        filepathsizefloat=filepathsize/1024000
                        filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                        filepathtxt=str(filepathsizefloatdec)+" MB"
                    else:
                        filepathsizefloat=filepathsize/1024000000
                        filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                        filepathtxt=str(filepathsizefloatdec)+" GB"
                    print('   DONE: '+ outputres +' \n     Size: '+bfrfilepathtxt+' --> '+filepathtxt+'\n')
                except:
                    print("   [ERROR]: FFMPEG is not initialized\n")
                    time.sleep(1)
                    Continue()
                    exit()
                Continue()
            except:
                time.sleep(1)
                Continue()
        def O3():
            os.system('cls')
            print('\n   Convert Type: Ogg\n   '+bitratevorbistxt+'\n\n   What is your preferred option to convert?\n\n     [1] pick single file\n     [2] pick multiple files\n     [0] Back\n')
            try:
                opt12=int(input("   Choose the option -----> "))
            except:
                print('     Invalid option')
                O3()
            if(opt12==1):
                Opt2()
            if(opt12==2):
                Opt1()
            if(opt12==0):
                Menu()
            if(opt12>2 or opt12<0):
                print('      Invalid numbers')
                O3()
        O3()
        Continue()
    if(intoption==3):
        if ffmpeg==0:
            print('     FFMPEG not found')
            time.sleep(1)
            Menu()
            exit()
        O3()
    if(intoption==4):
        try:
            os.mkdir('outputback')
        except:
            pass
        def o6():
            os.system('cls')
            print("\n      Choose to application to use to convert\n\n       [1] Use VGMStream (recommended) (requires vgmstream)\n\n       [2] Uncook from Cooked PCM Data (RAKI-PCM Only) (vgmstream not required)\n\n       [0] Exit\n")
            try:
                optionforback=int(input('\n     Choose the options -----> '))
            except:
                print('     Invalid Option')
                o6()
            if(optionforback==0):
                Menu()
            if(optionforback>2 or optionforback<0):
                print('     Invalid numbers')
                Menu()
            if(optionforback==1):
                if vgmstream==0:
                    print('     VGMStream not found')
                    time.sleep(1)
                    Menu()
                def Opt1():
                    print("\n   Run Tkinter:\n")
                    openwindow=Tk()
                    openwindow.title('')
                    outputaudiofile=filedialog.askopenfilenames(initialdir=pathlib.Path, title='Select the Ubisoft RAKI file', filetypes=(("Ubisoft RAKI",'*.wav.ckd'),("All files","*.*")))
                    openwindow.destroy()
                    print('\n   Start Converting...\n')
                    if(not outputaudiofile):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        Continue()
                    print('   Input files: ')
                    for lstinfo in outputaudiofile:
                        print('     '+os.path.basename(lstinfo))
                    openwindow=Tk()
                    openwindow.title('')
                    output=filedialog.askdirectory(initialdir=pathlib.Path,title="Select Location")
                    openwindow.destroy()
                    if(not output):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        Continue()
                    print('   Directory: '+os.path.basename(output))
                    print('\n   Start Converting...\n')
                    for listfiles in outputaudiofile:
                        listfiles1=os.path.basename(listfiles)
                        def startRun():
                            if(".ckd" in listfiles):
                                try:
                                    run((vgmstreamPath), stdout=DEVNULL, stderr=STDOUT) 
                                    print('   Converting back to original audio file: '+ os.path.splitext(listfiles1)[0])
                                    call([vgmstreamPath, '-o', output+"\\"+ os.path.splitext(listfiles1)[0], listfiles],stdout=DEVNULL, stderr=STDOUT) 
                                except Exception as e:
                                    print('   [ERROR]: VGMStream was not initialized\n ') 
                                    time.sleep(1)
                                    Continue()
                                if not os.path.isfile(output+"\\"+ os.path.splitext(listfiles1)[0]):
                                    print('\n     [ERROR]: VGMStream is not recognized')
                                    Continue()
                                    exit()
                                outputres=output.replace('/','\\')
                                filepathsize=os.path.getsize(listfiles)
                                if filepathsize<1000000:
                                    filepathsizefloat=filepathsize/1024
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    bfrfilepathtxt=str(filepathsizefloatdec)+" KB"
                                elif filepathsize<1000000000:
                                    filepathsizefloat=filepathsize/1024000
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    bfrfilepathtxt=str(filepathsizefloatdec)+" MB"
                                else:
                                    filepathsizefloat=filepathsize/1024000000
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    bfrfilepathtxt=str(filepathsizefloatdec)+" GB"
                                filepathsize=os.path.getsize(outputres+"\\" + os.path.splitext(listfiles1)[0])
                                if filepathsize<1000000:
                                    filepathsizefloat=filepathsize/1024
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    filepathtxt=str(filepathsizefloatdec)+" KB"
                                elif filepathsize<1000000000:
                                    filepathsizefloat=filepathsize/1024000
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    filepathtxt=str(filepathsizefloatdec)+" MB"
                                else:
                                    filepathsizefloat=filepathsize/1024000000
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    filepathtxt=str(filepathsizefloatdec)+" GB"
                                print('   DONE: '+ outputres + os.path.splitext(listfiles1)[0] +' \n     Size: '+bfrfilepathtxt+' --> '+filepathtxt+'\n')
                        if(os.path.isfile(output+"/"+os.path.splitext(os.path.basename(listfiles))[0])):
                            print('   File: "'+os.path.basename(listfiles)+'"')
                            overwritteninput=str(input("   Are you sure that file will be overwritten (y or n)? "))
                            if overwritteninput=="y" or overwritteninput=="Y":
                                startRun()
                            else:
                                print('   The file: "'+os.path.basename(listfiles)+'" was canceled')
                        else:
                            startRun()
                def Opt2():
                    print("\n   Run Tkinter:\n")
                    openwindow=Tk()
                    openwindow.title('')
                    outputaudiofile=filedialog.askopenfilename(initialdir=pathlib.Path, title='Select the Ubisoft RAKI file', filetypes=(("Ubisoft RAKI",'*.wav.ckd'),("All files","*.*")))
                    openwindow.destroy()
                    if(not outputaudiofile):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        Continue()
                    filenameinfo=os.path.basename(outputaudiofile)
                    print('   Input file: '+filenameinfo)
                    openwindow=Tk()
                    openwindow.title('')
                    output=filedialog.asksaveasfilename(filetypes=[("Wave Format",'*.wav')],initialdir=pathlib.Path,title="Select Location",initialfile=os.path.splitext(filenameinfo)[0])
                    openwindow.destroy()
                    if(not output):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        Continue()
                    print('   Save file: '+os.path.basename(output))
                    print('\n   Start Converting...\n')
                    try:
                        run((vgmstreamPath), stdout=DEVNULL, stderr=STDOUT) 
                        print('   Converting back to original audio file: '+ os.path.splitext(os.path.basename(outputaudiofile))[0])
                        call([vgmstreamPath, '-o', output, outputaudiofile],stdout=DEVNULL, stderr=STDOUT)
                        if not os.path.isfile(output):
                            print('\n     [ERROR]: VGMStream is not recognized\n') 
                            Continue()
                            exit()
                        outputres=output.replace('/','\\')
                        filepathsize=os.path.getsize(outputaudiofile)
                        if filepathsize<1000000:
                            filepathsizefloat=filepathsize/1024
                            filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                            bfrfilepathtxt=str(filepathsizefloatdec)+" KB"
                        elif filepathsize<1000000000:
                            filepathsizefloat=filepathsize/1024000
                            filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                            bfrfilepathtxt=str(filepathsizefloatdec)+" MB"
                        else:
                            filepathsizefloat=filepathsize/1024000000
                            filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                            bfrfilepathtxt=str(filepathsizefloatdec)+" GB"
                        filepathsize=os.path.getsize(outputres)
                        if filepathsize<1000000:
                            filepathsizefloat=filepathsize/1024
                            filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                            filepathtxt=str(filepathsizefloatdec)+" KB"
                        elif filepathsize<1000000000:
                            filepathsizefloat=filepathsize/1024000
                            filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                            filepathtxt=str(filepathsizefloatdec)+" MB"
                        else:
                            filepathsizefloat=filepathsize/1024000000
                            filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                            filepathtxt=str(filepathsizefloatdec)+" GB"
                        print('   DONE: '+ outputres +' \n     Size: '+bfrfilepathtxt+' --> '+filepathtxt+'\n')
                    except Exception as e:
                        print('   [ERROR] VGMSTREAM was not initialized\n ') 
                        time.sleep(1)
                        Continue()
                def O4():
                    os.system('cls')
                    print('\n   Uncook Type:VGMStream\n\n   What is your preferred option to convert?\n\n     [1] pick single file\n     [2] pick multiple files\n     [0] Back\n')
                    try:
                        opt12=int(input("   Choose the option -----> "))
                    except:
                        print('     Invalid option')
                        O4()
                    if(opt12==1):
                        Opt2()
                    if(opt12==2):
                        Opt1()
                    if(opt12==0):
                        o6()
                    if(opt12>2 or opt12<0):
                        print('      Invalid numbers')
                        O4()
                O4()
            if(optionforback==2):
                def Opt1():
                    print("\n   Run Tkinter:\n")
                    openwindow=Tk()
                    openwindow.title('')
                    outputaudiofile=filedialog.askopenfilenames(initialdir=pathlib.Path, title='Select the audio file', filetypes=(("Ubisoft RAKI",'*.wav.ckd'),("All files","*.*")))
                    openwindow.destroy()
                    if(not outputaudiofile):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        Continue()
                    print('   Input files: ')
                    for lstinfo in outputaudiofile:
                        print('     '+os.path.basename(lstinfo))
                    openwindow=Tk()
                    openwindow.title('')
                    output=filedialog.askdirectory(initialdir=pathlib.Path,title="Select Location")
                    openwindow.destroy()
                    if(not output):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        Continue()
                    print('   Directory: '+os.path.basename(output))
                    print('\n   Start Converting...\n')
                    for listfiles in outputaudiofile:
                        listfiles1=os.path.basename(listfiles)
                        def startRun(outputaudiofile):
                            if(".ckd" in listfiles1):
                                with open(listfiles, "rb") as f:
                                    print('   Uncook back to original audio file: '+ listfiles)
                                    try:
                                        f.read(12)
                                        pcmchecker=f.read(4) 
                                    except Exception as e:
                                        print(str(e))
                                    if(pcmchecker==b'pcm '):
                                        f.read(28)
                                        marksig=f.read(4)
                                        multiplier2=0
                                        sig=0
                                        if marksig==b'MARK':
                                            try:
                                                f.read(20)
                                                datatitle=f.read(4)
                                                sig=1
                                            except Exception as e:
                                                print("wrong wav file")
                                                time.sleep(1)
                                                Continue()
                                        else:
                                            datatitle=marksig
                                        f.read(4)
                                        data=f.read(4)
                                        if sig==1:
                                            multiplier2=int(os.path.getsize(outputaudiofile)-(struct.unpack("I",data)[0]+96))
                                        endriff=f.read(16) 
                                        f.read(multiplier2)
                                        audiodata=f.read() 
                                        try:
                                            encodeback=open(output+"\\" + os.path.splitext(listfiles1)[0], "wb")
                                            encodeback.write(b'RIFF')  # main title of riff
                                            encodeback.write(struct.pack("I",int(struct.unpack("I",data)[0]+36))) # whole file length
                                            encodeback.write(b'WAVEfmt ')
                                            encodeback.write(struct.pack("I",16)) # full header of riff
                                            encodeback.write(endriff)
                                            encodeback.write(datatitle) # data title
                                            encodeback.write(data)
                                            encodeback.write(audiodata)
                                            outputres=output.replace('/','\\')
                                            filepathsize=os.path.getsize(listfiles)
                                            if filepathsize<1000000:
                                                filepathsizefloat=filepathsize/1024
                                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                                bfrfilepathtxt=str(filepathsizefloatdec)+" KB"
                                            elif filepathsize<1000000000:
                                                filepathsizefloat=filepathsize/1024000
                                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                                bfrfilepathtxt=str(filepathsizefloatdec)+" MB"
                                            else:
                                                filepathsizefloat=filepathsize/1024000000
                                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                                bfrfilepathtxt=str(filepathsizefloatdec)+" GB"
                                            filepathsize=os.path.getsize(outputres+"\\" + os.path.splitext(listfiles1)[0])
                                            if filepathsize<1000000:
                                                filepathsizefloat=filepathsize/1024
                                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                                filepathtxt=str(filepathsizefloatdec)+" KB"
                                            elif filepathsize<1000000000:
                                                filepathsizefloat=filepathsize/1024000
                                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                                filepathtxt=str(filepathsizefloatdec)+" MB"
                                            else:
                                                filepathsizefloat=filepathsize/1024000000
                                                filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                                filepathtxt=str(filepathsizefloatdec)+" GB"
                                            print('   DONE: '+ outputres + os.path.splitext(listfiles1)[0] +' \n     Size: '+bfrfilepathtxt+' --> '+filepathtxt+'\n')
                                        except Exception as e:
                                            print('   [ERROR] This file is used from another process\n ')
                                    else:
                                        if pcmchecker==b'Nx  ':
                                            print('   WRONG FILE: "'+listfiles1+'" detects Cooked(Nintendo opus) file')
                                        else:
                                            print('   BAD FILE: "'+listfiles1+ '" Undetected file or not pcm')
                            else:
                                print('   [ERROR]: This file '+ listfiles1+' is not .ckd')
                        if(os.path.isfile(output+"/"+os.path.splitext(os.path.basename(listfiles))[0]+".wav")):
                            print('   File: "'+os.path.basename(listfiles)+'"')
                            overwritteninput=str(input("   Are you sure that file will be overwritten (y or n)? "))
                            if overwritteninput=="y" or overwritteninput=="Y":
                                startRun(outputaudiofile)
                            else:
                                print('   The file: "'+os.path.basename(listfiles)+'" was canceled')
                        else:
                            startRun(listfiles)
                def Opt2():
                    print("\n   Run Tkinter:\n")
                    openwindow=Tk()
                    openwindow.title('')
                    outputaudiofile=filedialog.askopenfilename(initialdir=pathlib.Path, title='Select the audio file', filetypes=(("Ubisoft RAKI",'*.wav.ckd'),("All files","*.*")))
                    openwindow.destroy()
                    if(not outputaudiofile):
                        print("   [FAILED]: Tkinter Cancelled")
                        Continue()
                    filenameinfo=os.path.basename(outputaudiofile)
                    print('   Input file: '+filenameinfo)
                    openwindow=Tk()
                    openwindow.title('')
                    output=filedialog.asksaveasfilename(filetypes=[("Wave Format",'*.wav')],initialdir=pathlib.Path,title="Select Location",initialfile=os.path.splitext(filenameinfo)[0]+'.wav')
                    openwindow.destroy()
                    if(not output):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                        Continue()
                    print('   Save file: '+os.path.basename(output))
                    print('\n   Start Converting...\n')
                    with open(outputaudiofile, "rb") as f:
                        print('   Uncook back to original audio file: '+ os.path.splitext(filenameinfo)[0])
                        f.read(12)
                        pcmchecker=f.read(4) 
                        if(pcmchecker==b'pcm '):
                            f.read(28)
                            marksig=f.read(4)
                            multiplier2=0
                            sig=0
                            if marksig==b'MARK':
                                try:
                                    f.read(20)
                                    datatitle=f.read(4)
                                    sig=1
                                except Exception as e:
                                    print("wrong wav file")
                                    time.sleep(1)
                                    Continue()
                            else:
                                datatitle=marksig
                            f.read(4)
                            data=f.read(4)
                            if sig==1:
                                multiplier2=int(os.path.getsize(outputaudiofile)-(struct.unpack("I",data)[0]+96))
                            endriff=f.read(16) 
                            f.read(multiplier2)
                            audiodata=f.read() 
                            try:
                                encodeback=open(output, "wb")
                                encodeback.write(b'RIFF')  # main title of riff
                                encodeback.write(struct.pack("I",int(struct.unpack("I",data)[0]+36))) # whole file length
                                encodeback.write(b'WAVEfmt ')
                                encodeback.write(struct.pack("I",16)) # full header of riff
                                encodeback.write(endriff)
                                encodeback.write(datatitle) # data title
                                encodeback.write(data)
                                encodeback.write(audiodata)
                                outputres=outputaudiofile.replace('/','\\')
                                filepathsize=os.path.getsize(outputaudiofile)
                                if filepathsize<1000000:
                                    filepathsizefloat=filepathsize/1024
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    bfrfilepathtxt=str(filepathsizefloatdec)+" KB"
                                elif filepathsize<1000000000:
                                    filepathsizefloat=filepathsize/1024000
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    bfrfilepathtxt=str(filepathsizefloatdec)+" MB"
                                else:
                                    filepathsizefloat=filepathsize/1024000000
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    bfrfilepathtxt=str(filepathsizefloatdec)+" GB"
                                filepathsize=os.path.getsize(outputres)
                                if filepathsize<1000000:
                                    filepathsizefloat=filepathsize/1024
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    filepathtxt=str(filepathsizefloatdec)+" KB"
                                elif filepathsize<1000000000:
                                    filepathsizefloat=filepathsize/1024000
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    filepathtxt=str(filepathsizefloatdec)+" MB"
                                else:
                                    filepathsizefloat=filepathsize/1024000000
                                    filepathsizefloatdec="%.2f" % round(filepathsizefloat, 2)
                                    filepathtxt=str(filepathsizefloatdec)+" GB"
                                print('   DONE: '+ outputres +' \n     Size: '+bfrfilepathtxt+' --> '+filepathtxt+'\n')
                            except Exception as e:
                                print('   [ERROR] This file is used from another process\n ')
                        else:
                            if pcmchecker==b'Nx  ':
                                print('   WRONG FILE: "'+outputaudiofile+'" detects Cooked(Nintendo opus) file')
                            else:
                                print('   BAD FILE: "'+outputaudiofile+ '" Undetected file or not pcm')
                def O5():
                    os.system('cls')
                    print('\n   Uncook Type:Decrypt Cook Wave PCM File (bulit-in)\n\n    What is your preferred option to convert?\n\n     [1] pick single file\n     [2] pick multiple files\n     [0] Back\n')
                    try:
                        opt12=int(input("   Choose the option -----> "))
                    except:
                        print('     Invalid option')
                        O5()
                    if(opt12==1):
                        Opt2()
                    if(opt12==2):
                        Opt1()
                    if(opt12==0):
                        o6()
                    if(opt12>2 or opt12<0):
                        print('      Invalid numbers')
                        O5()
                O5()
        o6()
        Continue()
    if(intoption==5):
        os.system('cls')
        def Helpers(helper):
            if helper==1:
                print('''     Command 1/2/3 - Cook Wav to (wav.ckd or .ogg)
        Requirements:
            - Download and Install FFMPEG
            - Requires VGAudio v.2.2.1 (include in audiotools.zip) - if you choose command 1

        How to use?:
            Step 1: Make sure you have an audio file
                Supported Formats: (*.wav,*.mp3,*.opus and *.ogg)
            Step 2: Choose 1 or 2 or 3  and choose type of convert
            Step 3: Waiting to encoding
            Step 4: When done, your cooked audio was saved to your directory''')
            if helper==2:
                print('''     Command 4 - Convert back using output file
        Requirements:
            - Install VGMSTREAM (include in audiotools.zip)


        How to use?
            Step 1: Make sure you have an cooked audio file (*.wav.ckd)
            Step 2: Choose 4 and choose type of convert
            Step 3: Waiting a few seconds to finish
            Step 4: When done, your file was saved to your directory''')
            if helper==3:
                print('''     How to config or change header on config.json?
        1.Click config.json and choose your software to configure it(ex. Notepad):
            Types of PCM to change header(pcmMode):
                normal=Normal header in JD2020-2022
                oldVersion=Old Header in JD2017-2019
                titlepage=Just Dance TitlePage (with signature)

            Types of cooked libopus to change header:
                normal=Normal Header on JD2020-2022
                oldVersion=Old Header on JD2017-2019
        How to change bitrate:
        Step 1: open config.json
        Step 2: below on vgmstreamPath change value into bytes
            (128000=128kb)''')
            if helper==4:
                print('''       FAQ:
        Q:Can i change the value in config.json?
        A:Yes

        Q:Is that supported from any platform?
        A:maybe, for cooked pcm but opus didn't supported for nx only

        Q:is the format of nintendo opus the same as ffmpeg opus?
        A:No, because the nintendo opus has a different structure

        Q:What Nx means?
        A:the codename on Nintendo Switch''')
            if (helper>4 or helper<0):
                print('Wrong option')
                time.sleep(1)
                os.system('cls')
                O7()
            if (helper==0):
                time.sleep(1)
                Menu()
        def O7():
            print('\n   Help: ')
            print('''
        [1] How to cook wav to (wav.ckd or .ogg)
        [2] How to uncook wav.ckd to (.wav)
        [3] How to use config.json
        [4] FAQ's
        [0] Back
    ''')
            try:
                helper=int(input('    Choose something helpful find out --> '))
            except:
                print(' Invalid option')
                os.system('cls')
                O7()
            if helper==0 or helper>4 or helper<0:
                pass
            else:
                os.system('cls')
            print('\n')
            Helpers(helper)
            time.sleep(1)
            input('    Press Enter to go Help...')
            os.system('cls')
            O7()
        O7()
    if(intoption==6):
        os.system('cls')
        def Changelogs(changever):
            if changever==1:
                print('''     Version 1.0
       - [Main] New Launch
       - [Update Print] Improvement CLI
       - [Add Feature] Added (back to wav conversion using output)
       - [Add Feature] Add feature "Decrypt Data" from command 4 it does not required vgmstream
       - [Add Feature] Add feature "Convert Audio using nintendo opus" from Command 1 which may better than ogg compression. [Command 1]
       - [Optional Feature] Add "Convert Audio To Ogg". [Command 3]''')
            if changever==2:
                print('''     Version 1.1
       - [Add Feature] Add Config to configure the code
       - [Add Feature] Add single file on Command 4
       - [Add Feature] Adding Brackets in per window
       - [Add Feature] Add More audio codes on config

          Ubisoft RAKI PCM Type:
            Normal - New Header/used for ambs/used for ui
            Old Version - Old Types of Header/used ui in jd2017-2019
            TitlePage - Main titlepage in Just Dance

          Ubisoft RAKI Nintendo Opus Types:
            Normal - New Header/used for ambs/used for ui
            Old Version - Old Types of Header/used ui in jd2017-2019''')
            if changever==3:
                print('''     Version 1.2
       - [Change] Change input folder convert type into multiple file
       - [Bug Fixed] Fix file names from input to output file name
       - [Removed Feature] remove input, output and outputback folder''')
            if changever==4:
                print('''     Version 1.3
       - [Update Info] The info of the config are shown in main menu
       - [Add Feature] Add bitrate key in config
       - [Bug Fixed] Fix bug update
       - [Bug Fixed] Fix crash detects not pcm from multiple files on "Uncook PCM Data"
       - [Add Feature] Add Refresh Function on Menu''')
            if changever==5:
                print('''     Version 1.4.0 - The New Patch Version
       - [Version Feature] New Patch Version
          There was a patch version, if there is a bug again, it will be released again, it will not be in the minor version
       - [Improved Feature] Add input/output info
       - [Bug fixed] Fix missing window in tkinter
       - [Update Print] Update Print (it is no longer messy anymore)''')
            if changever==6:
                print('''     Version 1.4.1
       - [Removed Bug] Fixed Double ".wav" extension on Command 4
       - [Removed Feature] Fixed .ogg input from tkinter(file dialog) on Command 3
       - [Improved Feature] Add size on the result file
       - [Fixed Bug] Fixed Code on VGMStream
       - [Improved Script] Fixed the far spaced on this script
       - [Fixed Bug] Added reminder to know a file alredy exists on multple files''')
            if changever==7:
                print('''     Version 1.5.0
       - [Removed Folder] Removed outputback folder in main app
       - [Improved Option] in Help and Changelog
       - [Add feature] Add Settings
       - [Improved feature] Detects missing app when open
       - [Improved ffmpeg request] Change ffmpeg os.system to subprocess''')
            if changever==8:
                print('''     Version 1.5.1
       - [Improvement Print] Improve Print Console in Settings
       - [Bug Fixes] Fixed VGAudio input temp not found
       - [Settings] Volume numbers are now divided to 100 in config and change 2 option in path environment
       - [Custom Value Settings] Fixed bug in custom volume and gets back in pressing enter in 3 times same as change bitrate
       - [Exit Bug] Fixed bug the from exit
       - [Old Config] Old config.json from 1.0 are now updated
       - [App Wrong Detector] in FFMPEG, VGMStream and VGAudio are now detected to file if your requirements is wrong''')
            if (changever>8 or changever<0):
                print('Wrong option')
                time.sleep(1)
                os.system('cls')
                O8()
            if (changever==0):
                time.sleep(1)
                Menu()
        def O8():
            print('  Changelog: ')
            print('''     Choose the Version:
       [1] Version v1.0
       [2] Version v1.1
       [3] Version v1.2
       [4] Version v1.3
       [5] Version v1.4.0 - New Patch Version
       [6] Version v1.4.1
       [7] Version v1.5.0
       [8] Version v1.5.1
       [0] Menu''')
            try:
                num=int(input('   Select a version that updates the application --> '))
            except:
                print('Invalid option')
                time.sleep(1)
                os.system('cls')
                O8()
            if num==0 or num>8 or num<0:
                pass
            else:
                os.system('cls')
            print('\n')
            Changelogs(num)
            time.sleep(1)
            input('    Press Enter to go Changelog...')
            os.system('cls')
            O8() 
        O8()
    if(intoption==7):
        vorbitrate=con["vorbisbitrate"]
        opubitrate=con["opusbitrate"]
        os.system('cls')
        def Options(nbrs):
            os.system('cls')
            if(nbrs==1):
                def Func(nbrs,mode,press01):
                    if(nbrs==1):
                        bitbyte=0
                    elif(nbrs==2):
                        bitbyte=32000
                    elif(nbrs==3):
                        bitbyte=64000
                    elif(nbrs==4):
                        bitbyte=128000
                    elif(nbrs==5):
                        bitbyte=256000
                    elif(nbrs==6):
                        bitbyte=320000
                    elif(nbrs==7):
                        os.system('cls')
                        if mode=="opus":
                            print('\n     Custom Bitrate:\n     Limit: (12000 (12kbps) to 920000 (920kbps))\n\n     '+bitrateopustxt+'\n\n      Press Enter '+str(press01)+' times to back\n')
                        else:
                            print('\n     Custom Bitrate:\n     Limit: (12000 (12kbps) to 920000 (920kbps))\n\n     '+bitratevorbistxt+'\n\n      Press Enter '+str(press01)+' times to back\n')
                        strbitbyte=str(input('    Input here from bytes --> '))
                        if not strbitbyte:
                            press01-=1
                            if press01==0:
                                GoFunc(mode)
                                exit()
                            Func(nbrs,mode,press01)
                        try:
                            bitbyte=int(strbitbyte)
                        except:
                            time.sleep(1)
                            print('     [ERROR]: Invalid option')
                            Func(nbrs,mode,3)
                        if bitbyte<12000 or bitbyte>920000:
                            print('     [Note]: Maximum bytes')
                            Func(nbrs,mode,3)
                    elif(nbrs==0):
                        O10()
                    else:
                        print('     [ERROR]: Invalid option')
                        time.sleep(1)
                        os.system('cls')
                    if mode=="opus":
                        conjson1(volume,modepcm,modeopus,channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,bitbyte,vorbitrate,1)
                    elif mode=="vorbis":
                        conjson1(volume,modepcm,modeopus,channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,opubitrate,bitbyte,1)
                def GoFunc(mode):
                    press01=3
                    os.system('cls')
                    if mode=="opus":
                        print('''    Choose the bitrate here (in cooked opus):

    '''+bitrateopustxt+'''
    (Note: 192k = 192000)
    [1] Auto
    [2] 32000 (Low)
    [3] 96000 (Medium)
    [4] 128000 (Mild High)
    [5] 256000 (High) (exact bitrate)
    [6] 320000 (High)
    [7] Custom
    [0] Back
    ''')
                    if mode=="vorbis":
                        print('''\n    Choose the bitrate here (in vorbis):

    '''+bitratevorbistxt+'''
    (Note: 192k = 192000)
    [1] Auto
    [2] 32000 (Low)
    [3] 96000 (Medium)
    [4] 128000 (Mild High)
    [5] 256000 (High)
    [6] 320000 (High) (exact bitrate)
    [7] Custom
    [0] Back
    ''')
                    try:
                        nbrs=int(input('    Choose the choices here --> '))
                    except:
                        print('     [ERROR]: Invalid option')
                        time.sleep(1)
                        os.system('cls')
                        GoFunc(mode)
                    Func(nbrs,mode,press01)
                def O10():
                    os.system('cls')
                    print('''    \n     Choose Bitrate Type:
        
        '''+bitrateopustxt+''' | '''+bitratevorbistxt+'''

        [1] Cooked Opus
        [2] Ogg
        [0] Back
        ''')
                    try:
                        nbrs = int(input('       Choose the bitrate type here --> '))
                    except:
                        print(' [ERROR]: Invalid option')
                        O10()
                    if nbrs==1:
                        GoFunc("opus")
                    elif nbrs==2:
                        GoFunc("vorbis")
                    elif nbrs==0:
                        os.system('cls')
                        O9()
                    else:
                        print('     [ERROR]: Invalid option')
                        time.sleep(1)
                        os.system('cls')
                        O10()
                O10()
            elif(nbrs==2):
                def Func(num):
                    ffmpegPath=con['ffmpegPath']
                    vgaudioPath=con['nintendoVGAudioPath']
                    vgmstreamPath=con['vgmstreamPath']
                    if num==1:
                        ffmpegPath=filedialog.askopenfilename(initialdir=pathlib.Path, title='Change FFMPEG Enviromental Path', filetypes=(("Programs","*.exe"),("All files","*.*")))
                        if not ffmpegPath:
                            O10()
                        conjson1(volume,modepcm,modeopus,channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,opubitrate,vorbitrate,1)
                    elif num==2:
                        vgaudioPath=filedialog.askopenfilename(initialdir=pathlib.Path, title='Change VGAudio Enviromental Path', filetypes=(("Programs","*.exe"),("All files","*.*")))
                        if not vgaudioPath:
                            O10()
                        conjson1(volume,modepcm,modeopus,channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,opubitrate,vorbitrate,1)
                    elif num==3:
                        vgmstreamPath=filedialog.askopenfilename(initialdir=pathlib.Path, title='Change VGMStream Enviromental Path', filetypes=(("Programs","*.exe"),("All files","*.*")))
                        if not vgmstreamPath:
                            O10()
                        conjson1(volume,modepcm,modeopus,channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,opubitrate,vorbitrate,1)
                    elif num==0:
                        os.system('cls')
                        O9()
                    else:
                        print('     [ERROR]: Invalid number')
                        O10()
                def O10():
                    os.system('cls')
                    print('''\n     Choose Path Environment Type:
            [1] FFMPEG
            [2] VGAudio
            [3] VGMStream
            [0] Back''')
                    try:
                        nbrs=int(input('    Choose the path environment here --> '))
                        Func(nbrs)
                    except Exception as e:
                        print('     [ERROR]: Invalid option'+str(e))
                        O10()
                O10()
            elif(nbrs==3):
                def Func(nbrs):
                    if(nbrs==1 or nbrs==2):
                        print('     Applying...')
                        conjson1(volume,modepcm,modeopus,str(nbrs),ffmpegPath,vgaudioPath,vgmstreamPath,opubitrate,vorbitrate,1)
                    elif(nbrs==0):
                        os.system('cls')
                        O9()
                    else:
                        print('     [ERROR]: Invalid option')
                        time.sleep(1)
                        os.system('cls')
                        O10()
                def O10():
                    os.system('cls')
                    print('''\n    Choose Channels:
                          
            '''+txtchanneljson+'''
        [1] Mono
        [2] Stereo
        [0] Back''')
                    try:
                        nbrs=int(input('    Choose option here -> '))
                    except:
                        print('     [ERROR]: Invalid option')
                        time.sleep(1)
                        os.system('cls')
                        O10()
                    Func(nbrs)
                O10()
            elif(nbrs==4):
                os.system('cls')
                volumestr=int(volume)*100
                def Func(nbrs,press01):
                    if(nbrs==1):
                        strvol=100
                        print('     Applying...')
                        conjson1(str(strvol/100),modepcm,modeopus,channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,opubitrate,vorbitrate,1)
                    elif(nbrs==2):
                        strvol=75
                        print('     Applying...')
                        conjson1(str(strvol/100),modepcm,modeopus,channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,opubitrate,vorbitrate,1)
                    elif(nbrs==3):
                        strvol=50
                        print('     Applying...')
                        conjson1(str(strvol/100),modepcm,modeopus,channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,opubitrate,vorbitrate,1)
                    elif(nbrs==4):
                        strvol=25
                        print('     Applying...')
                        conjson1(str(strvol/100),modepcm,modeopus,channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,opubitrate,vorbitrate,1)
                    elif(nbrs==5):
                        strvol=0
                        print('     Applying...')
                        conjson1(str(strvol/100),modepcm,modeopus,channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,opubitrate,vorbitrate,1)
                    elif(nbrs==6):
                        os.system('cls')
                        print('\n     Custom Volume:\n     Limit: (0 to 500%)\n\n     Main Volume: '+str(volumestr)+'%\n\n      Press Enter '+str(press01)+' times to back\n')
                        strvol=str(input('     Input volume here(Limit: 500%) ----> '))
                        if not strvol:
                            press01-=1
                            if press01==0:
                                O10()
                                exit()
                            Func(nbrs,press01)
                        try:
                            strvol1=int(strvol)
                        except:
                            time.sleep(1)
                            print('     [ERROR]: Invalid option')
                            Func(nbrs,3)
                        if strvol1>500 or strvol1<0:
                            print('     Limit numbers!!!')
                            time.sleep(0.5)
                            Func(nbrs,3)
                        else:
                            conjson1(str(strvol1/100),modepcm,modeopus,channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,opubitrate,vorbitrate,1)
                    elif(nbrs==0):
                        os.system('cls')
                        O9()
                    else:
                        print('     [ERROR]: Invalid option')
                        time.sleep(1)
                        os.system('cls')
                        O10()
                def O10():
                    press01=3
                    os.system('cls')
                    print('''\n        Select Volume Input:
            Main Volume: '''+str(volumestr)+'''%
        [1] 100%
        [2] 75%
        [3] 50%
        [4] 25%
        [5] 0% (muted)
        [6] Custom
        [0] Back''')
                    try:
                        nbrs=int(input('        Choose the option --> '))
                    except:
                        print('     [ERROR]: Invalid option')
                        time.sleep(1)
                        O10()
                    Func(nbrs,press01)
                O10()
            elif(nbrs==5):
                os.system('cls')
                def Func(nbrs):
                    if nbrs==1:
                        os.system('cls')
                        def Func01(nbrs):
                            if(nbrs==1):
                                conjson1(volume,modepcm,"normal",channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,opubitrate,vorbitrate,1)
                            elif(nbrs==2):
                                conjson1(volume,modepcm,"oldVersion",channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,opubitrate,vorbitrate,1)
                            elif(nbrs==0):
                                os.system('cls')
                                O10()
                            else:
                                print('     [ERROR]: Invalid option')
                                GoFunc()
                        def GoFunc():
                            os.system('cls')
                            print('''\n    Choose Mode from Cooked Opus:
        Main Mode: '''+nameopusMode+'''

        [1] New Mode (JD2020-22)
        [2] Old Mode (JD2017-19)
        [0] Back''')
                            try:
                                nbrs=int(input('    Choose the mode here --> '))
                            except:
                                print('     [ERROR]: Invalid option')
                                GoFunc()
                            Func01(nbrs)
                        GoFunc()
                    elif nbrs==2:
                        os.system('cls')
                        def Func01(nbrs):
                            if(nbrs==1):
                                conjson1(volume,"normal",modeopus,channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,opubitrate,vorbitrate,1)
                            elif(nbrs==2):
                                conjson1(volume,"oldVersion",modeopus,channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,opubitrate,vorbitrate,1)
                            elif(nbrs==3):
                                conjson1(volume,"titlepage",modeopus,channeljson,ffmpegPath,vgaudioPath,vgmstreamPath,opubitrate,vorbitrate,1)
                            elif(nbrs==0):
                                os.system('cls')
                                O10()
                            else:
                                print('     [ERROR]: Invalid option')
                                GoFunc()
                        def GoFunc():
                            os.system('cls')
                            print('''\n    Choose Mode from Cooked PCM:
        Main Mode: '''+namepcmMode+'''
                                  
        [1] New Mode (JD2020-22)
        [2] Old Mode (JD2017-19)
        [3] JD Titlepage w/signature (Beta)
        [0] Back''')
                            try:
                                nbrs=int(input('    Choose the mode here --> '))
                            except:
                                print('     [ERROR]: Invalid option')
                                GoFunc()
                            Func01(nbrs)
                        GoFunc()
                    elif nbrs==0:
                        os.system('cls')
                        O9()
                    else:
                        print('     [ERROR]: Invalid option')
                        time.sleep(1)
                        os.system('cls')
                        O10()
                def O10():
                    print('''
            Choose Mode Audio Type:
        [1] Cooked Opus
        [2] Cooked PCM
        [0] Back''')
                    try:
                        nbrs=int(input('    Input the mode type here --> '))
                    except:
                        os.system('cls')
                        O10()
                    Func(nbrs)
                O10()
            elif(nbrs==0):
                Menu()
            else:
                print('     [ERROR]: Invalid option')
                time.sleep(1)
                os.system('cls')
                O9()
        def O9():
            print('''
    Settings: '''+'''
    Settings(JSON) Version: '''+str(ver)+'''
        [1] Change Bitrate
        [2] Change Path Environment
        [3] Channels
        [4] Volume
        [5] Mode
        [0] Back to Menu''')
            try:
                modeopt=int(input('   Choose the option --> '))
            except:
                print('     [ERROR]: Invalid option')
                time.sleep(1)
                os.system('cls')
                O9()
            Options(modeopt)
        O9()
    if(intoption>7 or intoption<0):
        print('\n     Invalid numbers!')
        Menu()
def Continue():
    try:
        os.remove('temp\\temp.wav')
    except:
        pass
    try:
        os.remove('temp\\temp.lopus')
    except:
        pass
    try:
        os.rmdir('temp')
    except:
        pass
    input("   Press Enter to go Menu...")
    Menu()
Menu()