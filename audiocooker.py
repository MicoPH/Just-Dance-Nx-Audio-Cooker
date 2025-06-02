# All Python Modules
import os, struct, time, pathlib, json
from datetime import datetime
from tkinter import filedialog
from tkinter import *
from subprocess import DEVNULL, STDOUT, run
def CmdClear(ifclear:bool):
    if ifclear:
        os.system('cls')
# Main function
def Menu():
    intoption=0
    datefilename=datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    notchan=""
    noteopus=""
    notevorb=""
    newjson={'version': 2.0, 'cmdclear': True, 'addVolume': 1, 'pcmMode': 0, 'opusMode': 0, 'channel': 2, 'ffmpegPath': 'ffmpeg', 'VGAudioPath': 'VGAudioCli', 'vgmstreamPath': 'vgmstream', 'opusbitrate': 256000, 'vorbisbitrate': 320000, 'pcmModeData': [{'pcmTitle': 'Default', 'pcmHead': 72, 'pcmHead1': 72, 'pcmHead2': 2, 'pcmHead3': 0, 'pcmfmt': 56, 'pcmfmt2': 16, 'mark': False, 'strg': False}, {'pcmTitle': 'Header 2', 'pcmHead': 74, 'pcmHead1': 80, 'pcmHead2': 2, 'pcmHead3': 3, 'pcmfmt': 56, 'pcmfmt2': 16, 'mark': False, 'strg': False}, {'pcmTitle': 'JD TitlePage', 'pcmHead': 2288, 'pcmHead1': 2288, 'pcmHead2': 4, 'pcmHead3': 3, 'pcmfmt': 80, 'pcmfmt2': 18, 'mark': True, 'strg': True, 'marklength': 2, 'strglength': 2, 'markdata': [{'mark1': 98, 'mark2': 2182, 'strg1': 2280, 'strg2': 8, 'addinfohead1': 23789568, 'addinfohead2': 0, 'addinfohead3': 1, 'addinfohead4': 3145734, 'multiplieronaddinfo1': False, 'multiplieronaddinfo2': True, 'multiplieronaddinfo3': False, 'multiplieronaddinfo4': False, 'multiplier': [{'addinfo1': 'mark1', 'addinfo2': 'mark2', 'addinfo3': 'strg1', 'addinfo4': 'strg2'}]}]}], 'opusModeData': [{'opusTitle': 'Default', 'opusHead': 88, 'opusHead2': 88, 'opusHead3': 3, 'opusHead4': 3, 'opusfmt': 68, 'opusfmt2': 16, 'adinlength': 2, 'adindata': [{'adin1': 84, 'adin2': 4}], 'datatitlehead': 88, '16bitonInt32': False}, {'opusTitle': 'Header 2', 'opusHead': 90, 'opusHead2': 96, 'opusHead3': 3, 'opusHead4': 3, 'opusfmt': 68, 'opusfmt2': 18, 'adinlength': 2, 'adindata': [{'adin1': 86, 'adin2': 4}], 'datatitlehead': 96, '16bitonInt32': True}]}

    # Loads JSON
    try:
        con=json.load(open("config.json", "r")) # Reads config file
        volume=str(con["addVolume"])
        channeljson=int(con["channel"])
        newjson["addVolume"]=float(volume)

        if channeljson<1 or channeljson>2: # if channel is less than 0 and more than 2 was default into 2
            notchan='\n   Channel value failed. Channel was default into 2'
            channeljson=2
        newjson["channel"]=channeljson


        modepcm=con["pcmMode"]
        modeopus=con["opusMode"]
        getpcm=False
        getopus=False
        newjson["opusMode"]=modeopus
        newjson["pcmMode"]=modepcm


        # Third Party Programs Path
        ffmpegPath=con["ffmpegPath"]
        try:
            vgaudioPath=str(con["VGAudioPath"])
        except:
            vgaudioPath=str("VGAudioCli")
        vgmstreamPath=str(con["vgmstreamPath"])
        newjson["ffmpegPath"]=ffmpegPath
        newjson["VGAudioPath"]=vgaudioPath
        newjson['vgmstreamPath']=vgmstreamPath


        # Update function
        def setdataconfig():
            try:
                datjs=open('config.json','w')
                print('Updating config...')
                datjs.write(json.dumps(newjson,indent=4))
                datjs.close
            except:
                pass

        # PCM items that write value
        try:
            pcmhead1=int(con["pcmModeData"][modepcm]["pcmHead"])
            pcmhead2=int(con["pcmModeData"][modepcm]["pcmHead1"])
            pcmhead3=int(con["pcmModeData"][modepcm]["pcmHead2"])
            pcmhead4=int(con["pcmModeData"][modepcm]["pcmHead3"])
            pcmfmt=int(con["pcmModeData"][modepcm]["pcmfmt"])
            pcmfmt2=int(con["pcmModeData"][modepcm]["pcmfmt2"])
            namepcmMode=str(con["pcmModeData"][modepcm]["pcmTitle"])
            markcount=0
            strgcount=0
            strgtitle=b''
            strgbyte=b''
            markbyte=b''
            marktitle=b''
            byteaddinfo =b''

            # This is signatures from titlepage (beta)
            if con["pcmModeData"][modepcm]["mark"]:
                marktitle=b'MARK'
                marklength=int(con["pcmModeData"][modepcm]["marklength"])
                markbyte=b''
                while marklength>0:
                    markname="mark"+str(marklength)
                    markbyte=struct.pack("I",int(con["pcmModeData"][modepcm]["markdata"][0][markname]))+markbyte
                    markcount+=1
                    addinfo=markcount
                    infomultplier=con["pcmModeData"][modepcm]["markdata"][0]["multiplier"][0]["addinfo"+str(addinfo)]
                    if con["pcmModeData"][modepcm]["markdata"][0]["multiplieronaddinfo"+str(addinfo)]:
                        multplytodatapcm=int((con["pcmModeData"][modepcm]["markdata"][0][infomultplier]-addinfo)/4)
                        byteaddinfomutiply=struct.pack("I",int(con["pcmModeData"][modepcm]["markdata"][0]["addinfohead"+str(addinfo)]))
                        byteaddinfo=byteaddinfo+(byteaddinfomutiply*multplytodatapcm)
                    else:
                        byteaddinfo=byteaddinfo+struct.pack("I",int(con["pcmModeData"][modepcm]["markdata"][0]["addinfohead"+str(addinfo)]))
                    marklength=marklength - 1
            if con["pcmModeData"][modepcm]["strg"]:
                strgtitle=b'STRG'
                strglength=int(con["pcmModeData"][modepcm]["strglength"])
                strgbyte=b''
                while strglength>0:
                    strgname="strg"+str(strglength)
                    strgcount+=1
                    strgbyte=struct.pack("I",int(con["pcmModeData"][modepcm]["markdata"][0][strgname]))+strgbyte
                    addinfo=markcount+strgcount
                    infomultplier=con["pcmModeData"][modepcm]["markdata"][0]["multiplier"][0]["addinfo"+str(addinfo)]
                    if con["pcmModeData"][modepcm]["markdata"][0]["multiplieronaddinfo"+str(addinfo)]:
                        multplytodatapcm=int((con["pcmModeData"][modepcm]["markdata"][0][infomultplier]-strgcount)/4)
                        byteaddinfomutiply=struct.pack("I",int(con["pcmModeData"][modepcm]["markdata"][0]["addinfohead"+str(addinfo)]))*multplytodatapcm
                        byteaddinfo=byteaddinfo+byteaddinfomutiply
                    else:
                        byteaddinfo=byteaddinfo+struct.pack("I",int(con["pcmModeData"][modepcm]["markdata"][0]["addinfohead"+str(addinfo)]))
                    strglength=strglength - 1
            addinfobyte=byteaddinfo
            getpcm=True
        except:
            pass

        # Opus items that write value
        try:
            opushead1=int(con["opusModeData"][modeopus]["opusHead"])
            opushead2=int(con["opusModeData"][modeopus]["opusHead2"])
            opushead3=int(con["opusModeData"][modeopus]["opusHead3"])
            opushead4=int(con["opusModeData"][modeopus]["opusHead4"])
            opusheadfmt=int(con["opusModeData"][modeopus]["opusfmt"])
            opusheadfmt2=int(con["opusModeData"][modeopus]["opusfmt2"])
            adindatahead1=int(con["opusModeData"][modeopus]["adindata"][0]["adin1"])
            adindatahead2=int(con["opusModeData"][modeopus]["adindata"][0]["adin2"])
            datatitlehead=int(con["opusModeData"][modeopus]["datatitlehead"])
            intbytehead=con["opusModeData"][modeopus]["16bitonInt32"]
            nameopusMode=str(con["opusModeData"][modeopus]["opusTitle"])
            getopus=True
        except:
            pass
                
        # Update Version
        try:
            ver=float(con["version"])
        except:
            newjson['cmdclear']=True
            setdataconfig()
            return 11
        if ver==2.0:
            newjson["pcmModeData"]=con["pcmModeData"]
            newjson["opusModeData"]=con["opusModeData"]
        else:
            if ver<2.0:
                if "normal" in str(modepcm):
                    newjson['pcmMode']=0
                if "normal" in str(modeopus):
                    newjson['opusMode']=0
                if "oldHeader" in str(modeopus):
                    newjson['opusMode']=1
                if "oldHeader" in str(modepcm):
                    newjson['pcmMode']=1
                if "titlepage" in str(modepcm):
                    newjson['pcmMode']=2
                newjson['cmdclear']=True
            setdataconfig()
            return 10
        # Bitrate Auto
        try:
            int(con["vorbisbitrate"])
        except:
            con["vorbisbitrate"]=0
        try:
            int(con["opusbitrate"])
        except:
            con["opusbitrate"]=0
        cmdclear=bool(con["cmdclear"])
        newjson['cmdclear']=cmdclear
        newjson['vorbisbitrate']=con["vorbisbitrate"]
        newjson['opusbitrate']=con["opusbitrate"]
    # JSON Error by error strings, integer, boolean and float and dissarrange of object and array.
    except Exception as e:
        print(str(e))
        time.sleep(4)
        try:
            run(["copy", 'config.json', "config-old-"+datefilename+".json"], stdout=DEVNULL, stderr=STDOUT, shell=TRUE)
            print("   Config Failed to read\n   Renew Config...")
        except:
            print('   Making Config...')
        datjs=open('config.json','w')
        datjs.write(json.dumps(newjson,indent='\t'))
        return 1


    # LibOpus items that shows in configs by opusmode
    if not getopus:
        nameopusMode="Invalid opus"


    # PCM items that shows in configs by pcmmode
    if not getpcm:
        namepcmMode="Invalid pcm"


    # Channels that shows in configs  
    if channeljson==1:
        txtchanneljson="Channel Type: Mono"
    elif channeljson==2:
        txtchanneljson="Channel Type: Stereo"
    else:
        txtchanneljson="Channel Type: Surround"


    # Volumes that values and shows in configs 
    intvolumeset=int(con["addVolume"]*100)
    txtvolumeset="Volume: "+ str(intvolumeset) + "%"


    # Bitrate from opus that shows in configs
    try:
        bitrateopus=con["opusbitrate"]
        if bitrateopus<0:
            bitrateopus=92000
            noteopus="\n   [WARNING]: Invalid value. Libopus bitrate is set to 92000"
            bitrateopustxt="Opus Audio Bitrate: Medium - "+str(int(bitrateopus/1000))+'kb'
        elif bitrateopus==0:
            bitrateopustxt="Opus Audio Bitrate: Auto"
        elif bitrateopus<64000:
            bitrateopustxt="Opus Audio Bitrate: Low - "+str(int(bitrateopus/1000))+'kb'
        elif bitrateopus<192000:
            bitrateopustxt="Opus Audio Bitrate: Medium - "+str(int(bitrateopus/1000))+'kb'
        elif bitrateopus<256000 or bitrateopus>256000:
            bitrateopustxt="Opus Audio Bitrate: High - "+str(int(bitrateopus/1000))+'kb'
        elif bitrateopus==256000:
            bitrateopustxt="Opus Audio Bitrate: Default - "+str(int(bitrateopus/1000))+'kb'
    except:
        bitrateopus=92000
        noteopus="\n   [WARNING]: Invalid key. Libopus bitrate is set to 92000"
        bitrateopustxt="Vorbis Audio Bitrate: Medium"
    
    # Bitrate from ogg vorbis that shows in configs
    try:
        bitratevorbis=con["vorbisbitrate"]
        intbitratevorb=int(bitratevorbis/1000)
        if bitratevorbis<0:
            bitratevorbis=128000
            notevorb="   [WARNING]: Invalid value. Ogg Vorbis bitrate is set to 128000"
            bitratevorbistxt="Vorbis Audio Bitrate: Medium - "+str(intbitratevorb)+'kb'
        elif bitratevorbis==0:
            bitratevorbistxt="Vorbis Audio Bitrate: Auto"
        elif bitratevorbis<92000:
            bitratevorbistxt="Vorbis Audio Bitrate: Low - "+str(intbitratevorb)+'kb'
        elif bitratevorbis<192000:
            bitratevorbistxt="Vorbis Audio Bitrate: Medium - "+str(intbitratevorb)+'kb'
        elif bitratevorbis<320000 or bitratevorbis>320000:
            bitratevorbistxt="Vorbis Audio Bitrate: High - "+str(intbitratevorb)+'kb'
        elif bitratevorbis==320000:
            bitratevorbistxt="Vorbis Audio Bitrate: Default - "+str(intbitratevorb)+'kb'
    except:
        bitratevorbis=128000
        notevorb="\n   [WARNING]: Invalid key. Ogg Vorbis bitrate is set to 128000"
        intbitratevorb=int(bitratevorbis/1000)
        bitratevorbistxt="Vorbis Audio Bitrate: Medium"+str(intbitratevorb)+'k'


    # Third Party Programs that shows in configs
    missingcnt=0
    # FFMPEG
    ffmpegmisdesc=""
    vgaudiomisdesc=""
    vgmstreammisdesc=""
    try:
        run((ffmpegPath), stdout=DEVNULL, stderr=STDOUT)
        ffmpeg=True
    except:
        ffmpeg=False
        ffmpegmisdesc="\n     FFMPEG - Convert Audio to WAVE Format"
        missingcnt+=1
    # VGAudio
    try:
        run((vgaudioPath), stdout=DEVNULL, stderr=STDOUT)
        vgaudio=True
    except:
        vgaudio=False
        vgaudiomisdesc="\n     VGAudio - Convert Audio to Libopus format (Note: Github release is outdated so don't work on libopus)"
        missingcnt+=1
    # VGMStream
    try:
        vgmstream=True
        run((vgmstreamPath), stdout=DEVNULL, stderr=STDOUT)
    except:
        vgmstream=False
        vgmstreammisdesc="\n     VGMSTREAM - Convert back to WAVE "
        missingcnt+=1
    # Missing Info
    if not ffmpeg or not vgmstream or not vgaudio:
        missing='\n\n   Requirements (not found):     '+ffmpegmisdesc+vgaudiomisdesc+vgmstreammisdesc+'\n   '+str(missingcnt)+" missing"
    else:
        missing="\n\n   All Requirements found"

    # Extract Wave from FFMPEG
    def Extract_WAV_FFMPEG(inputfile):
        print('     Running FFMPEG to: '+os.path.basename(inputfile))
        run([ffmpegPath,'-y','-i',inputfile,'-f','wav','-bitexact','-ar','48000','-ac',str(channeljson),'-filter:a','volume='+volume,'-map_metadata','-1',os.getcwd()+'\\temp\\temp.wav'],stdout=DEVNULL, stderr=STDOUT)
        if not os.path.isfile(os.getcwd()+'\\temp\\temp.wav'):
            print('\n       [ERROR]: Temp not found\n\n')
            return False
        else:
            return True
    # RAKI PCM Writer
    def Raki_PCM_write(inputfile:str,output:str,ambintro:bool,inputambfile:str):
        try:
            if ambintro:
                print('     Encoding: '+ os.path.basename(inputambfile))
                pcm_file=open("temp/temp_intro.wav", "rb")
            else:
                print('     Encoding: '+ os.path.basename(inputfile))
                pcm_file=open("temp/temp.wav", "rb")
            pcm_file.read(12)
            formattitle=pcm_file.read(4)
            pcm_file.read(4)
            audioformat=pcm_file.read(2)
            numofchannels=struct.unpack('h',pcm_file.read(2))[0]
            riffend=pcm_file.read(12)
            datatitle=pcm_file.read(4)
            data=pcm_file.read(4)
            audiofile=pcm_file.read()
            raki_pcm=open(output, "wb")
            raki_pcm.write(b'RAKI') 
            raki_pcm.write(struct.pack('I',11))
            raki_pcm.write(b'Nx  pcm ')
            raki_pcm.write(struct.pack('I',pcmhead1))
            raki_pcm.write(struct.pack('I',pcmhead2))
            raki_pcm.write(struct.pack('I',pcmhead3))
            raki_pcm.write(struct.pack('I',pcmhead4))
            raki_pcm.write(formattitle)
            raki_pcm.write(struct.pack('I',pcmfmt))
            raki_pcm.write(struct.pack('I',pcmfmt2))
            raki_pcm.write(marktitle)
            raki_pcm.write(markbyte)
            raki_pcm.write(strgtitle)
            raki_pcm.write(strgbyte)
            raki_pcm.write(datatitle)
            raki_pcm.write(struct.pack('I',pcmhead2))
            raki_pcm.write(data) 
            raki_pcm.write(audioformat)
            raki_pcm.write(struct.pack('h',numofchannels))
            raki_pcm.write(riffend) 
            raki_pcm.write(addinfobyte)
            raki_pcm.write(audiofile)  
            pcm_file.close
            raki_pcm.close
            outputres=output.replace('/','\\')
            print(fileSize(inputfile,outputres))
        except Exception as e:
            print('       [ERROR] An unexpected error : '+ str(e)+'\n')
            time.sleep(1)
    # Libopus Conv
    def VGAudio_Libopus(inputfile:str,ambintro:bool):
        if ambintro:
            print('     Running VGAudio: Audio')
        else:
            print('     Running VGAudio: '+os.path.basename(inputfile))
        if bitrateopus==0:
            run([vgaudioPath, os.getcwd()+'\\temp\\temp.wav', os.getcwd()+'\\temp\\temp.lopus', '--no-loop', '--opusheader','standard'],stdout=DEVNULL, stderr=STDOUT)
        else:
            run([vgaudioPath, os.getcwd()+'\\temp\\temp.wav', os.getcwd()+'\\temp\\temp.lopus', '--bitrate', str(bitrateopus), '--no-loop', '--opusheader','standard'],stdout=DEVNULL, stderr=STDOUT)
        if not os.path.isfile(os.getcwd()+'\\temp\\temp.lopus'):
            print('\n       [ERROR]: Temp_Libopus not found\n     Please check the version VGAudio (Github release is outdated) or Wrong VGAudio\n')
            return False
        else:
            return True
    # RAKi Libopus Writer
    def Raki_Libopus_write(inputfile:str,output:str,ambintro:bool):
        try:
            if ambintro:
                print('     Encoding: Audio')
                pcm_file=open("temp/temp_full.wav", "rb")
            else:
                print('     Encoding: '+ os.path.basename(inputfile))
                pcm_file=open("temp/temp.wav", "rb")
            pcm_file.read(12)
            formattitle=pcm_file.read(4)
            bitbyte=struct.unpack("I", pcm_file.read(4))[0]
            pcm_file.read(2)
            channel=struct.unpack("H",pcm_file.read(2))[0]
            riffdatainfo=pcm_file.read(12)
            datatitle=pcm_file.read(4)
            minidata=struct.unpack("I", pcm_file.read(4))[0]
            lopus_file=open("temp/temp.lopus", "rb")
            write1=lopus_file.read(8)
            lopus_file.read(4)
            o2=lopus_file.read(16)
            lopus_file.read(4)
            dataopus=lopus_file.read()
            raki_libopus=open(output, "wb")
            raki_libopus.write(b'RAKI') 
            raki_libopus.write(struct.pack('I',11)) 
            raki_libopus.write(b'Nx  Nx  ') 
            raki_libopus.write(struct.pack('I',opushead1))
            raki_libopus.write(struct.pack('I',opushead2))
            raki_libopus.write(struct.pack('I',opushead3))
            raki_libopus.write(struct.pack('I',opushead4))
            raki_libopus.write(formattitle)
            raki_libopus.write(struct.pack('I',opusheadfmt))
            raki_libopus.write(struct.pack('I',opusheadfmt2)) 
            raki_libopus.write(b'AdIn')
            raki_libopus.write(struct.pack('I',adindatahead1))
            raki_libopus.write(struct.pack('I',adindatahead2))
            raki_libopus.write(datatitle)
            raki_libopus.write(struct.pack('I',datatitlehead))
            raki_libopus.write(struct.pack("I", os.path.getsize("temp/temp.lopus")))  
            raki_libopus.write(struct.pack('h',99))
            raki_libopus.write(struct.pack("H",channel))
            raki_libopus.write(riffdatainfo)
            if intbytehead:
                raki_libopus.write(struct.pack("H",0))
            raki_libopus.write(struct.pack("I",int(minidata/((bitbyte*channel)/8)))) 
            if intbytehead:
                raki_libopus.write(struct.pack("H",0))
                raki_libopus.write(struct.pack("I",0))
            raki_libopus.write(write1)
            raki_libopus.write(struct.pack("I", 512)) 
            raki_libopus.write(o2)
            raki_libopus.write(struct.pack("I", 120))
            raki_libopus.write(dataopus) 
            pcm_file.close
            lopus_file.close
            raki_libopus.close
            outputres=output.replace('/','\\')
            print(fileSize(inputfile,outputres))
        except Exception as e:
            print('       [ERROR] An unexpected error : '+ str(e)+'\n')
            time.sleep(1)
    # Ogg Vorbis Writer
    def OGG_FFMPEG(inputfile:str, output:str):
        print('     Running FFMPEG to: '+ os.path.basename(inputfile))
        if bitratevorbis==0:
            run([ffmpegPath,'-y','-i',inputfile,'-acodec','libvorbis','-ar','48000','-ac',str(channeljson),'-filter:a','volume='+volume,'-map_metadata','-1',output],stdout=DEVNULL, stderr=STDOUT)
        else:
            run([ffmpegPath,'-y','-i',inputfile,'-acodec','libvorbis','-ar','48000','-b:a',str(intbitratevorb)+'k','-ac',str(channeljson),'-filter:a','volume='+volume,'-map_metadata','-1',output],stdout=DEVNULL, stderr=STDOUT)
        if not os.path.isfile(output):
            print('       [ERROR]: Ogg not found. Wrong FFMPEG')
        else:
            outputres=output.replace('/','\\')
            print(fileSize(inputfile, outputres))
    # Extract wav.ckd File
    def VGM_Run(inputfile:str,output:str):
        basenamefile=os.path.basename(inputfile)
        print('     Converting back to original audio file: '+ basenamefile)
        run([vgmstreamPath, '-o', output, inputfile],stdout=DEVNULL, stderr=STDOUT) 
        if not os.path.isfile(output):
            print('\n       [ERROR]: VGMStream is not recognized')
            Continue()
        outputres=output.replace('/','\\')
        print(fileSize(inputfile,outputres))
    # Extract wav.ckd file (pcm only)
    def Experimental_Raki_PCM_to_RIFF_PCM(inputfile:str, output:str):
        basenamefile=os.path.basename(inputfile)
        print('     Uncook back to original audio file: '+ basenamefile)
        try:  
            pcm_file=open(inputfile, "rb")
            pcm_file.read(12)
            pcmchecker=pcm_file.read(4)
            if(pcmchecker==b'pcm '):
                pcm_file.read(28)
                marksig=pcm_file.read(4)
                multiplier2=0
                sig=0
                if marksig==b'MARK':
                    pcm_file.read(20)
                    datatitle=pcm_file.read(4)
                    sig=1
                else:
                    datatitle=marksig
                pcm_file.read(4)
                data=pcm_file.read(4)
                if sig==1:
                    multiplier2=int(os.path.getsize(inputfile)-(struct.unpack("I",data)[0]+96))
                endriff=pcm_file.read(16) 
                pcm_file.read(multiplier2)
                audiodata=pcm_file.read() 
                encodeback=open(output, "wb")
                encodeback.write(b'RIFF')  # main title of riff
                encodeback.write(struct.pack("I",int(struct.unpack("I",data)[0]+36))) # whole file length
                encodeback.write(b'WAVEfmt ')
                encodeback.write(struct.pack("I",16)) # full header of riff
                encodeback.write(endriff)
                encodeback.write(datatitle) # data title
                encodeback.write(data)
                encodeback.write(audiodata)
                outputres=output.replace('/','\\')
                print(fileSize(inputfile,outputres))
            else:
                if pcmchecker==b'Nx  ':
                    print('       WRONG FILE: "'+basenamefile+'" detected Cooked(Libopus) file')
                else:
                    print('       BAD FILE: "'+basenamefile+ '" Undetected')
        except Exception as e:
            print('       [ERROR] An unexpected error : '+ str(e)+'\n')
            time.sleep(1)

    def FFMPEG_Splitter(miliseconds):
        run([ffmpegPath,'-y','-ss',str(miliseconds)+'s','-i',os.getcwd()+'\\temp\\temp.wav',os.getcwd()+'\\temp\\temp_full.wav'],stdout=DEVNULL, stderr=STDOUT)
        run([ffmpegPath,'-y','-ss','0ms','-t',str(miliseconds),'-i',os.getcwd()+'\\temp\\temp.wav',os.getcwd()+'\\temp\\temp_intro.wav'],stdout=DEVNULL, stderr=STDOUT)
        if not os.path.isfile(os.getcwd()+'\\temp\\temp_full.wav') and os.path.isfile(os.getcwd()+'\\temp\\temp_intro.wav'):
            print('\n       [ERROR]: Temp not completed. Wrong ffmpeg\n\n')
            return False
        else:
            return True
    # Print
    CmdClear(cmdclear)
    print('\n Welcome to Just Dance Nx Audio Maker \n (Version 2.0.0)'+notchan+noteopus+notevorb+missing+'\n\n   RAKI_PCM Header: '+namepcmMode+" | RAKI_Libopus Header: "+nameopusMode+"\n   "+txtchanneljson+" | "+txtvolumeset+"\n   "+bitrateopustxt+" | "+bitratevorbistxt+"\n\n   Select the Options:\n     Recommended Options:\n       [1] Convert Audio to cooked Libopus file (Recommeneded to more efficient than vorbis)\n       [2] Convert Audio to cooked pcm wave format (only for ambs and user interface)\n       [3] Ubiart Audio/Amb Cutter (for unsynchronize audio\n\n     Other Options:\n       [4] Convert Audio to Ogg\n       [5] Convert Back to WAV FILE(.wav.ckd to .wav)\n       [6] Help\n       [7] Changelog\n       [8] Settings\n       [0] Exit\n\n")

    # Main Option
    option=str(input("   Select the option -----> "))
    if not option:
        return 11
    try:
        intoption=int(option)
        if(intoption==11):
            intoption=12
    except:
        print('\n     Use only numbers not letters/symbols')
        time.sleep(1)
        intoption=11

    # Tkinter Strings
    windowtitle1='Select the audio file'
    audiofiletypes1="*.wav *.opus *.mp3 *.ogg *.mkv *.mp4 *.webm *.mpg *.3gp *.flac *.avi *.mov *.wmv *.aac *.m4a *.mid *.mpg *.mpeg *.ogv"
    titleaudiofiletypes1="Audio/Video files (*.wav,*.opus,*.mp3,*.ogg and video w/audio)"

    # Tkinter Windows
    def TKWin_Multi(windowtitle:str,titleaudiofiletypes:str,audiofiletypes:str):
        print("\n   Run Tkinter:\n")
        openwindow=Tk()
        openwindow.title('')
        input_audiofile=filedialog.askopenfilenames(initialdir=pathlib.Path, title=windowtitle, filetypes=((titleaudiofiletypes,audiofiletypes),("All files","*.*")))
        try:
            openwindow.destroy()
        except:
            pass
        return input_audiofile
    def TKWin_Single(windowtitle:str,titleaudiofiletypes:str,audiofiletypes:str):
        print("\n   Run Tkinter:\n")
        openwindow=Tk()
        openwindow.title('')
        input_audiofile=filedialog.askopenfilename(initialdir=pathlib.Path, title=windowtitle, filetypes=((titleaudiofiletypes,audiofiletypes),("All files","*.*")))
        try:
            openwindow.destroy()
        except:
            pass
        return input_audiofile
    def TKWin_SaveFile(filename:str,titlefiletypes:str,filetypes:str):
        openwindow=Tk()
        openwindow.title('')
        output=filedialog.asksaveasfilename(filetypes=[(titlefiletypes,filetypes)],initialdir=pathlib.Path,title="Select Location",initialfile=filename)
        try:
            openwindow.destroy()
        except:
            pass
        return output
    def TKWin_Directory():
        openwindow=Tk()
        openwindow.title('')
        output=filedialog.askdirectory(initialdir=pathlib.Path,title="Select Location")
        try:
            openwindow.destroy()
        except:
            pass
        return output

    # create Temp
    def createTemp():
        try:
            os.mkdir('temp')
        except:
            pass

    # raki_libOpus option
    def Option1():
        CmdClear(cmdclear)
        
        def Multiple_files():
            input_audiofile=TKWin_Multi(windowtitle1,titleaudiofiletypes1,audiofiletypes1)
            if(not input_audiofile):
                print("   [FAILED]: Tkinter Cancelled")
                time.sleep(1)
            else:
                print('   Input files: ')
                for lstinfo in input_audiofile:
                    print('     '+os.path.basename(lstinfo))
                output=TKWin_Directory()
                print('   Directory: '+os.path.basename(output))
                if(not output):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                else:
                    createTemp()
                    print('\n   Converting...\n')
                    for listfiles in input_audiofile:
                        if(os.path.isfile(output+"/"+os.path.splitext(os.path.basename(listfiles))[0]+".wav.ckd")):
                            print('   File: "'+os.path.basename(listfiles)+'"')
                            overwritteninput=str(input("   Are you sure that file will be overwritten (y or n)? "))
                            if overwritteninput=="y" or overwritteninput=="Y":
                                if Extract_WAV_FFMPEG(listfiles):
                                    pass
                                    if VGAudio_Libopus(listfiles,False):
                                        Raki_Libopus_write(listfiles,output+"/"+os.path.splitext(os.path.basename(listfiles))[0]+".wav.ckd",False)
                            else:
                                print('   The file: "'+os.path.basename(listfiles)+'" was canceled')
                        else:
                            if Extract_WAV_FFMPEG(listfiles):
                                pass
                                if VGAudio_Libopus(listfiles,False):
                                    Raki_Libopus_write(listfiles,output+"/"+os.path.splitext(os.path.basename(listfiles))[0]+".wav.ckd",False)

        def Single_files():
            input_audiofile=TKWin_Single(windowtitle1,titleaudiofiletypes1,audiofiletypes1)
            if(not input_audiofile):
                print("   [FAILED]: Tkinter Cancelled")
                time.sleep(1)
            else:
                filenameinfo=os.path.basename(input_audiofile)
                print('     Input file: '+filenameinfo)
                output=TKWin_SaveFile(os.path.splitext(filenameinfo)[0]+'.wav.ckd',"Ubisoft RAKI",'*.wav.ckd')
                if(not output):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                else:
                    print('     Output file: '+os.path.basename(output))
                    print('\n   Converting...\n')
                    createTemp()
                    if Extract_WAV_FFMPEG(input_audiofile):
                        pass
                        if VGAudio_Libopus(input_audiofile,False):
                            Raki_Libopus_write(input_audiofile,output,False)
        print('\n   Encoding Type: RAKI (Libopus)\n     Header Type: '+nameopusMode+'\n   '+bitrateopustxt+'\n\n   What is your preferred option to convert?\n\n     [1] pick single file\n     [2] pick multiple files\n     [0] Back\n')
        try:
            InputFunction1=int(input("   Choose the option -----> "))
            if(InputFunction1==1):
                Single_files()
                Continue()
            if(InputFunction1==2):
                Multiple_files()
                Continue()
            if(InputFunction1==0):
                pass
            if(InputFunction1>2 or InputFunction1<0):
                CmdClear(cmdclear)
                print('      Invalid value')
                Option1()
        except:
            print('     Invalid value')
            Option1()

    # raki_pcm16 option
    def Option2():
        CmdClear(cmdclear)
        def Multiple_files():
            input_audiofile=TKWin_Multi(windowtitle1,titleaudiofiletypes1,audiofiletypes1)
            if(not input_audiofile):
                print("   [FAILED]: Tkinter Cancelled")
                time.sleep(1)
            else:
                print('   Input files: ')
                for lstinfo in input_audiofile:
                    print('     '+os.path.basename(lstinfo))
                output=TKWin_Directory()
                if(not output):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                else:
                    print('   Directory: '+os.path.basename(output))
                    print('\n   Converting...\n')
                    createTemp()
                    for listfiles in input_audiofile:
                        if(os.path.isfile(output+"/"+os.path.splitext(os.path.basename(listfiles))[0]+".wav.ckd")):
                            print('   File: "'+os.path.basename(listfiles)+'"')
                            overwritteninput=str(input("   Are you sure that file will be overwritten (y or n)? "))
                            if overwritteninput=="y" or overwritteninput=="Y":
                                if Extract_WAV_FFMPEG(listfiles):
                                    Raki_PCM_write(listfiles,output+"/"+os.path.splitext(os.path.basename(listfiles))[0]+".wav.ckd",False,'')
                            else:
                                print('   The file: "'+os.path.basename(listfiles)+'" was canceled')
                        else:
                            if Extract_WAV_FFMPEG(listfiles):
                                Raki_PCM_write(listfiles,output+"/"+os.path.splitext(os.path.basename(listfiles))[0]+".wav.ckd",False,'')

        def Single_files():
            input_audiofile=TKWin_Single(windowtitle1,titleaudiofiletypes1,audiofiletypes1)
            if(not input_audiofile):
                print("   [FAILED]: Tkinter Cancelled")
                time.sleep(1)
            else:
                filenameinfo=os.path.basename(input_audiofile)
                print('     Input file: '+filenameinfo)
                output=TKWin_SaveFile(os.path.splitext(filenameinfo)[0]+'.wav.ckd',"Ubisoft RAKI",'*.wav.ckd')
                if(not output):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                    Continue()
                else:
                    print('     Output file: '+os.path.basename(output))
                    print('\n   Converting...\n')
                    createTemp()
                    if Extract_WAV_FFMPEG(input_audiofile):
                        Raki_PCM_write(input_audiofile,output,False,'')


        print('\n   Encoding Type: RAKI (PCM)\n     Header Type: '+namepcmMode+'\n\n   What is your preferred option to convert?\n\n     [1] pick single file\n     [2] pick multiple files\n     [0] Back\n')
        try:
            InputFunction1=int(input("   Choose the option -----> "))
            if(InputFunction1==1):
                Single_files()
                Continue()
            if(InputFunction1==2):
                Multiple_files()
                Continue()
            if(InputFunction1==0):
                pass
            if(InputFunction1>2 or InputFunction1<0):
                print('      Invalid value')
                Option2()
        except:
            print('     Invalid value')
            Option2()
            
    # Vorbis option
    def Option3():
        def Multiple_files():
            input_audiofile=TKWin_Multi(windowtitle1,titleaudiofiletypes1,audiofiletypes1)
            if(not input_audiofile):
                print("   [FAILED]: Tkinter Cancelled")
                time.sleep(1)
            else:
                print('   Input files: ')
                for lstinfo in input_audiofile:
                    print('     '+os.path.basename(lstinfo))
                output=TKWin_Directory()
                if(not output):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                else:
                    print('   Directory: '+os.path.basename(output))
                    print('\n   Converting...\n')
                    for listfiles in input_audiofile:
                        basenamefile=os.path.basename(listfiles)
                        if(os.path.isfile(output+"/"+os.path.splitext(os.path.basename(listfiles))[0]+".ogg")):
                            print('   File: "'+os.path.basename(listfiles)+'"')
                            overwritteninput=str(input("   Are you sure that file will be overwritten (y or n)? "))
                            if overwritteninput=="y" or overwritteninput=="Y":
                                if(listfiles==output+'\\'+os.path.splitext(basenamefile)[0]+'.ogg'):
                                    print("   [FAILED]: Same file detected")
                                elif(".ogg" in listfiles or ".opus" in listfiles or ".mp3" in listfiles or ".wav" in listfiles):
                                    OGG_FFMPEG(listfiles, output+'\\'+os.path.splitext(basenamefile)[0]+'.ogg')
                                else:
                                    createTemp()
                                    if Extract_WAV_FFMPEG(listfiles):
                                        OGG_FFMPEG(os.getcwd()+'\\temp\\temp.wav',output+'\\'+os.path.splitext(basenamefile)[0]+'.ogg')
                            else:
                                print('   The file: "'+os.path.basename(listfiles)+'" was canceled')
                        else:
                            if(listfiles==output+'\\'+os.path.splitext(basenamefile)[0]+'.ogg'):
                                print("   [FAILED]: Same file detected")
                            elif(".ogg" in listfiles or ".opus" in listfiles or ".mp3" in listfiles or ".wav" in listfiles):
                                OGG_FFMPEG(listfiles, output+'\\'+os.path.splitext(basenamefile)[0]+'.ogg')
                            else:
                                createTemp()
                                if Extract_WAV_FFMPEG(listfiles):
                                    OGG_FFMPEG(os.getcwd()+'\\temp\\temp.wav',output+'\\'+os.path.splitext(basenamefile)[0]+'.ogg')
        def Single_files():
            input_audiofile=TKWin_Single(windowtitle1,titleaudiofiletypes1,audiofiletypes1)
            if(not input_audiofile):
                print("   [FAILED]: Tkinter Cancelled")
                time.sleep(1)
            else:
                basenamefile=os.path.basename(input_audiofile)
                print('     Input file: '+basenamefile)
                output=TKWin_SaveFile(basenamefile,"Ogg Vorbis","*.ogg")
                print('     Output file: '+os.path.basename(output))
                if(not output):
                    print("   [FAILED]: Tkinter Cancelled")
                    time.sleep(1)
                else:
                    print('\n   Converting...\n')
                    createTemp()
                    if(input_audiofile==output):
                        print("   [FAILED]: Same file detected")
                        time.sleep(1)
                    elif(".ogg" in input_audiofile or ".opus" in input_audiofile or ".mp3" in input_audiofile or ".wav" in input_audiofile):
                        OGG_FFMPEG(input_audiofile,output)
                    else:
                        if Extract_WAV_FFMPEG(input_audiofile):
                            OGG_FFMPEG(os.getcwd()+'\\temp\\temp.wav',output)

        CmdClear(cmdclear)
        print('\n   Convert Type: Ogg\n   '+bitratevorbistxt+'\n\n   What is your preferred option to convert?\n\n     [1] pick single file\n     [2] pick multiple files\n     [0] Back\n')
        try:
            InputFunction1=int(input("   Choose the option -----> "))
            if(InputFunction1==1):
                Single_files()
                Continue()
            if(InputFunction1==2):
                Multiple_files()
                Continue()
            if(InputFunction1==0):
                pass
            if(InputFunction1>2 or InputFunction1<0):
                print('      Invalid value')
                Option3()
        except:
            print('     Invalid value')
            Option3()

    # JD Audio/Amb Cutter option
    def Option11():
        CmdClear(cmdclear)
        print('\n   JDU Audio/Amb Cutter (for unsync audio) \n\n     Header Type (Libopus): '+nameopusMode+'\n       '+bitrateopustxt+'\n     Header Type (PCM): '+namepcmMode+'\n')
        musictrk=TKWin_Single('Select the musictrack file','Musictrack (_musictrack.tpl.ckd)','*_musictrack.tpl.ckd')
        mapname=os.path.basename(musictrk)
        if not musictrk:
            print("   [FAILED]: Tkinter Cancelled")
            time.sleep(1)
        else:
            try:
                jsonmusictrk=json.load(open(musictrk,'r'))
                startbeat=int(jsonmusictrk['COMPONENTS'][0]['trackData']['structure']['startBeat'])
                if startbeat<0:
                    print('     Unsynchronized Detected')
                    startbeat=startbeat*-1
                elif startbeat==0:
                    print('     DONE: This Musictrack file is completely synchronized. Please select the option on Menu')
                    Continue()
                    return
                else:
                    print('     Unsynchronized Detected')
                    startbeat=startbeat
                markers=int(jsonmusictrk['COMPONENTS'][0]['trackData']['structure']['markers'][startbeat])
                markers=markers/48000
            except Exception as e:
                print('     JSON Error: '+str(e))
                Continue()
                return
            input_audiofile=TKWin_Single('Select the (unsynchronized) audio file','Ogg Vorbis/Opus (*.ogg, *opus)','*.ogg *.opus')
            if not input_audiofile:
                print("   [FAILED]: Tkinter Cancelled")
                time.sleep(1)
                return
            print('     Input file: '+input_audiofile)
            full_audiofile=TKWin_SaveFile(mapname.lower()[:len(mapname)-19]+'.wav.ckd',"Ubisoft RAKI (Audio)",'*.wav.ckd')
            if not full_audiofile:
                print("   [FAILED]: Tkinter Cancelled")
                time.sleep(1)
                return
            print('     Audio file: '+full_audiofile)
            amb_audiofile=TKWin_SaveFile('amb_'+mapname.lower()[:len(mapname)-19]+'_intro.wav.ckd',"Ubisoft RAKI (amb intro)",'*.wav.ckd')
            if not amb_audiofile:
                print("   [FAILED]: Tkinter Cancelled")
                time.sleep(1)
                return
            else:
                print('     Amb Intro file: '+amb_audiofile)
                print('\n   Converting...\n')
                createTemp()
                if Extract_WAV_FFMPEG(input_audiofile):
                    if FFMPEG_Splitter(markers):
                        if VGAudio_Libopus(os.getcwd()+'\\temp\\temp_full.wav',True):
                            Raki_Libopus_write(os.getcwd()+'\\temp\\temp_full.wav',full_audiofile,True)
                            Raki_PCM_write(os.getcwd()+'\\temp\\temp_intro.wav',amb_audiofile,True,input_audiofile)
                            Continue()


    # Option 1 - Exit
    if(intoption==0 or intoption==11):
        pass
    # Option 1 - to RAKI_Libopus
    elif(intoption==1):
        if not ffmpeg and not vgaudio:
            print('     FFMPEG and VGAudio is missing')
            time.sleep(1)
        elif not ffmpeg:
            print('     FFMPEG is missing')
            time.sleep(1)
        elif not vgaudio:
            print('     VGAudio is missing')
            time.sleep(1)
        elif getopus:
            Option1()
        else:
            print('     Invalid Mode.')
            time.sleep(1)
    # Option 2 - to RAKI_PCM
    elif(intoption==2):
        if not ffmpeg:
            print('     FFMPEG is missing')
            time.sleep(1)
        elif getpcm:
            Option2()
        else:
            CmdClear(cmdclear)
            print('     Invalid Mode.')
            time.sleep(1)

    # Option 3 - JDU Audio to Amb Cutter
    elif(intoption==3):
        if not ffmpeg and not vgaudio:
            print('     FFMPEG and VGAudio is missing')
            time.sleep(1)
        elif not ffmpeg:
            print('     FFMPEG is missing')
            time.sleep(1)
        elif not vgaudio:
            print('     VGAudio is missing')
            time.sleep(1)
        elif getopus:
            Option11()
        else:
            print('     Invalid Mode.')
            time.sleep(1)
    
    # Option 4 - Ogg Vorbis
    elif(intoption==4):
        if not ffmpeg:
            print('     FFMPEG not found')
            time.sleep(1)
        else:
            Option3()

    # Option 5 - Conversion back to wav
    elif(intoption==5):

        # raki to wav option
        def Option6():
            CmdClear(cmdclear)
            print("\n       Options:\n\n       [1] Use VGMStream (recommended) (requires vgmstream)\n\n       [2] Bulit-in (RAKI-PCM Only) (experimental)\n\n       [0] Exit\n")
            try:
                optionforback=int(input('\n     Input here -----> '))
            except:
                print('     Invalid value')
                Option6()
            if(optionforback==0):
                pass
            elif(optionforback==1):
                def Multiple_files():
                    input_audiofile=TKWin_Multi('Select the Ubisoft RAKI file',"Ubisoft RAKI",'*.wav.ckd')
                    if(not input_audiofile):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                    else:
                        print('   Input files: ')
                        for lstinfo in input_audiofile:
                            print('     '+os.path.basename(lstinfo))
                        output=TKWin_Directory()
                        if(not output):
                            print("   [FAILED]: Tkinter Cancelled")
                            time.sleep(1)
                        else:
                            print('   Directory: '+os.path.basename(output))
                            print('\n   Converting...\n')
                            for listfiles in input_audiofile:
                                if(os.path.isfile(output+"/"+os.path.splitext(os.path.basename(listfiles))[0])):
                                    print('   File: "'+os.path.basename(listfiles)+'"')
                                    overwritteninput=str(input("   Are you sure that file will be overwritten (y or n)? "))
                                    if overwritteninput=="y" or overwritteninput=="Y":
                                        VGM_Run(listfiles, output+"\\"+ os.path.splitext(os.path.basename(listfiles))[0])
                                    else:
                                        print('   The file: "'+os.path.basename(listfiles)+'" was canceled')
                                else:
                                    VGM_Run(listfiles, output+"\\"+ os.path.splitext(os.path.basename(listfiles))[0])
                def Single_files():
                    input_audiofile=TKWin_Single('Select the Ubisoft RAKI file',"Ubisoft RAKI",'*.wav.ckd')
                    if(not input_audiofile):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                    else:
                        filenameinfo=os.path.basename(input_audiofile)
                        print('     Input file: '+filenameinfo)
                        output=TKWin_SaveFile(os.path.splitext(filenameinfo)[0],"Wave Format",'*.wav')
                        if(not output):
                            print("   [FAILED]: Tkinter Cancelled")
                            time.sleep(1)
                        else:
                            print('     Output file: '+os.path.basename(output))
                            print('\n   Converting...\n')
                            VGM_Run(input_audiofile,output)
                def Option4():
                    CmdClear(cmdclear)
                    print('\n   Uncook Type: VGMStream\n\n   What is your preferred option to convert?\n\n     [1] pick single file\n     [2] pick multiple files\n     [0] Back\n')
                    try:
                        InputFunction1=int(input("   Choose the option -----> "))
                    except:
                        print('     Invalid value')
                        Option4()
                    if(InputFunction1==1):
                        Single_files()
                        Continue()
                    if(InputFunction1==2):
                        Multiple_files()
                        Continue()
                    if(InputFunction1==0):
                        Option6()
                    if(InputFunction1>2 or InputFunction1<0):
                        print('      Invalid value')
                        Option4()
                if not vgmstream:
                    print('     VGMStream not found')
                    time.sleep(1)
                    pass
                else:
                    Option4()
            elif(optionforback==2):
                def Multiple_files():
                    input_audiofile=TKWin_Multi(windowtitle1,"Ubisoft RAKI",'*.wav.ckd')
                    if(not input_audiofile):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                    else:
                        print('   Input files: ')
                        for lstinfo in input_audiofile:
                            print('     '+os.path.basename(lstinfo))
                        output=TKWin_Directory()
                        if(not output):
                            print("   [FAILED]: Tkinter Cancelled")
                            time.sleep(1)
                        else:
                            print('   Directory: '+os.path.basename(output))
                            print('\n   Converting...\n')
                            for listfiles in input_audiofile:
                                if(os.path.isfile(output+"/"+os.path.splitext(os.path.basename(listfiles))[0])):
                                    print('   File: "'+os.path.basename(listfiles)+'"')
                                    overwritteninput=str(input("   Are you sure that file will be overwritten (y or n)? "))
                                    if overwritteninput=="y" or overwritteninput=="Y":
                                        Experimental_Raki_PCM_to_RIFF_PCM(listfiles,output+"\\" + os.path.splitext(os.path.basename(listfiles))[0])
                                    else:
                                        print('   The file: "'+os.path.basename(listfiles)+'" was canceled')
                                else:
                                    Experimental_Raki_PCM_to_RIFF_PCM(listfiles,output+"\\" + os.path.splitext(os.path.basename(listfiles))[0])
                def Single_files():
                    input_audiofile=TKWin_Single(windowtitle1,"Ubisoft RAKI",'*.wav.ckd')
                    if(not input_audiofile):
                        print("   [FAILED]: Tkinter Cancelled")
                        time.sleep(1)
                    else:
                        filenameinfo=os.path.basename(input_audiofile)
                        print('     Input file: '+filenameinfo)
                        output=TKWin_SaveFile(os.path.splitext(filenameinfo)[0],"Wave Format",'*.wav')
                        if(not output):
                            print("   [FAILED]: Tkinter Cancelled")
                            time.sleep(1)
                        else:
                            print('     Output file: '+os.path.basename(output))
                            print('\n   Converting...\n')
                            Experimental_Raki_PCM_to_RIFF_PCM(input_audiofile,output)
                def Option5():
                    CmdClear(cmdclear)
                    print('\n   Uncook Type: Bulit-in (RAKI-PCM Only) (experimental)\n\n    What is your preferred option to convert?\n\n     [1] pick single file\n     [2] pick multiple files\n     [0] Back\n')
                    try:
                        InputFunction1=int(input("   Choose the option -----> "))
                        if(InputFunction1==1):
                            Single_files()
                            Continue()
                        elif(InputFunction1==2):
                            Multiple_files()
                            Continue()
                        elif(InputFunction1==0):
                            Option6()
                        else:
                            print('      Invalid value')
                            Option5()
                    except:
                        print('      Invalid value')
                        Option5()
                Option5()
            else:
                print('     Invalid value')
                Option6()
        Option6()

    # Option 6 - Help
    elif(intoption==6):
        CmdClear(cmdclear)
        def Helpers(helper):
            if helper==1:
                print('''     Options 1/2/3 - Cook Wav to (wav.ckd or .ogg)
        Requirements:
            - FFMPEG
            - VGAudio

        How to use?:
            Step 1: Make sure you have an audio file
                Supported Formats: (*.wav,*.mp3,*.opus and *.ogg and video w/audio)
            Step 2: Choose 1 or 2 or 3  and choose type of convert
            Step 3: Waiting...
            Step 4: When done, your cooked audio was saved to your directory''')
            elif helper==2:
                print('''     Command 4 - Convert back using output file
        Requirements:
            - VGMStream


        How to use?
            Step 1: Make sure you have an cooked audio file (*.wav.ckd)
            Step 2: Choose 4 and choose type of convert
            Step 3: Waiting a few seconds to finish
            Step 4: When done, your file was saved to your directory''')
            elif helper==3:
                print('''     Steps to change header?
        Step 1: open config.json
        Step 2: For pcmMode and opusMode keys are based to list arrays
                default --> 0
                header 2 --> 1
        
        Steps to change bitrate:
        Step 1: open config.json
        Step 2: For opusbitrate and vorbisbitrate keys
            Bitrate Value (in kbps) --> 128 kb
            Config Value --> 128000''')
            elif helper==4:
                print('''       FAQ:
        Q:Can i change the value in config.json?
        A:Yes

        Q:Is that supported from any platform?
        A:maybe, for cooked pcm but opus didn't supported for nx only

        Q:is the format of Libopus the same as main opus?
        A:No, because the Libopus has a different structure

        Q:What Nx means?
        A:the codename on Nintendo Switch''')
            else:
                print('Invalid value')
                time.sleep(1)
                CmdClear(cmdclear)
                Option7()
            time.sleep(1)
            input('    Press Enter to go Help...')
            CmdClear(cmdclear)
            Option7()

        # Help Option
        def Option7():
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
                if helper==0:
                    pass
                elif not helper>4 or helper<0:
                    CmdClear(cmdclear)
                    Helpers(helper)
                else:
                    print('   Invalid value')
                    time.sleep(1)
                    CmdClear(cmdclear)
                    Option7()
            except:
                print(' Invalid value')
                time.sleep(1)
                CmdClear(cmdclear)
                Option7()
        Option7()

    # Option 7 - Changelog
    elif(intoption==7):
        CmdClear(cmdclear)
        def Changelogs(changever):
            if changever==1:
                print('''     Version 1.0
       - [Main] New Launch
       - [Update Print] Improvement CLI
       - [Added Feature] Added (back to wav conversion using output)
       - [Added Feature] Added Feature "Decrypt Data" from command 4 it does not required vgmstream
       - [Added Feature] Added Feature "Convert Audio using Libopus" from Command 1 which may better than ogg compression. [Command 1]
       - [Optional Feature] Add "Convert Audio To Ogg". [Command 3]''')
            elif changever==2:
                print('''     Version 1.1
       - [Added Feature] Add Config to configure the code
       - [Added Feature] Add single file on Command 4
       - [Added Feature] Adding Brackets in per window
       - [Added Feature] Add More audio codes on config''')
            elif changever==3:
                print('''     Version 1.2
       - [Change] Change input folder convert type into multiple file
       - [Bug Fixed] Fix file names from input to output file name
       - [Removed Feature] remove input, output and outputback folder''')
            elif changever==4:
                print('''     Version 1.3
       - [Update Info] The info of the config are shown in main menu
       - [Added Feature] Add bitrate key in config
       - [Bug Fixed] Fix bug update
       - [Bug Fixed] Fix crash detects not pcm from multiple files on "Uncook PCM Data"
       - [Added Feature] Add Refresh Function on Menu''')
            elif changever==5:
                print('''     Version 1.4.0 - The New Patch Version
       - [Version Feature] New Patch Version
          There was a patch version, if there is a bug again, it will be released again, it will not be in the minor version
       - [Improved Feature] Add input/output info
       - [Bug fixed] Fix missing window in tkinter
       - [Update Print] Update Print (it is no longer messy anymore)''')
            elif changever==6:
                print('''     Version 1.4.1
       - [Removed Bug] Fixed Double ".wav" extension on Command 4
       - [Removed Feature] Fixed .ogg input from tkinter(file dialog) on Command 3
       - [Improved Feature] Add size on the result file
       - [Fixed Bug] Fixed Code on VGMStream
       - [Improved Script] Fixed the far spaced on this script
       - [Fixed Bug] Added reminder to know a file alredy exists on multple files''')
            elif changever==7:
                print('''     Version 1.5.0
       - [Removed Folder] Removed outputback folder in main app
       - [Improved Option] in Help and Changelog
       - [Added Feature] Add Settings
       - [Improved feature] Detects missing app when open
       - [Improved ffmpeg request] Change ffmpeg os.system to subprocess''')
            elif changever==8:
                print('''     Version 1.5.1
       - [Improved Print] Improve Print Console in Settings
       - [Bug Fixed] Fixed VGAudio input temp not found
       - [Settings] Volume numbers are now divided to 100 in config and change 2 option in path environment
       - [Custom Value Settings] Fixed bug in custom volume and gets back in pressing enter in 3 times same as change bitrate
       - [Exit Bug] Fixed bug the from exit
       - [Old Config] Old config.json from 1.0 are now updated
       - [App Wrong Detector] in FFMPEG, VGMStream and VGAudio are now detected to file if your requirements is wrong''')
            elif (changever==9):
                print('''     Version 2.0.0
            Major Changes:
       - [Added Feature] Added filesize difference the previous
       - [Added Feature] Added audiotrimmer amb.
            This feature is perfect convert your ambs from JDNEXT to JDU
       - [Added Feature] Added Video file support on tkinter
       - [Skip Exit] When changed config in Settings are fixed
       - [JSON] The pcmMode and opusMode keys are removed and change into number of arrays
                (Default header --> 0)
                (Header 2 --> 1)
       - [Added Feature] Added cmdClear on config and settings. "True" by default

            Minor Changes:
       - [Fully deleted outputback] from the previous version the folder outputback is always shown is now deleted from this script
       - [Backup Config] The filename of the config backup file has fixed datetime format which is includes day format
       - [Change header info] Changed title name
                Normal - Default
                Old Header - Header 2
       - [Bug Fixed] From some Activity input invalid number exception is hidden
       - [Updated JSON Keys] Updated other JSON Keys''')
            time.sleep(1)
            input('    Press Enter to go Changelog...')
            CmdClear(cmdclear)
            Option8()
        def Option8():
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
       [9] Version v2.0.0
       [0] Menu''')
            try:
                num=int(input('   Select a version that updates the application --> '))
                if num==0:
                    pass
                elif not num>9 or num<0:
                    CmdClear(cmdclear)
                    Changelogs(num)
                else:
                    print('   Invalid value')
                    time.sleep(1)
                    CmdClear(cmdclear)
                    Option8()
            except:
                print('   Invalid value')
                time.sleep(1)
                CmdClear(cmdclear)
                Option8()
        Option8()

    # Option 8 - Settings
    elif(intoption==8):
        vorbitrate=con["vorbisbitrate"]
        opubitrate=con["opusbitrate"]
        CmdClear(cmdclear)

        # Settings Function
        def Settings(nbrs):
            CmdClear(cmdclear)
            # Bitrate Settings
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
                        CmdClear(cmdclear)
                        if mode=="opus":
                            print('\n     Custom Bitrate:\n     Limit: (12000 (12kbps) to 920000 (920kbps))\n\n     '+bitrateopustxt+'\n\n      Press Enter '+str(press01)+' times to back\n')
                        else:
                            print('\n     Custom Bitrate:\n     Limit: (12000 (12kbps) to 920000 (920kbps))\n\n     '+bitratevorbistxt+'\n\n      Press Enter '+str(press01)+' times to back\n')
                        strbitbyte=str(input('    Input here from bytes --> '))
                        if not strbitbyte:
                            press01-=1
                            if press01==0:
                                Activity1(mode)
                                exit()
                            Func(nbrs,mode,press01)
                        try:
                            bitbyte=int(strbitbyte)
                        except:
                            time.sleep(1)
                            print('     Invalid value')
                            Func(nbrs,mode,3)
                        if bitbyte<12000 or bitbyte>920000:
                            print('     [Note]: Maximum bytes')
                            Func(nbrs,mode,3)
                    elif(nbrs==0):
                        Option10()
                    else:
                        print('     Invalid value')
                        time.sleep(1)
                        CmdClear(cmdclear)
                        Activity1(mode)
                    if mode=="opus":
                        newjson['opusbitrate']=bitbyte
                        setdataconfig()
                    elif mode=="vorbis":
                        newjson['vorbisbitrate']=bitbyte
                        setdataconfig()
                def Activity1(mode):
                    press01=3
                    CmdClear(cmdclear)
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
                        Func(nbrs,mode,press01)
                    except:
                        print('     Invalid value')
                        time.sleep(1)
                        CmdClear(cmdclear)
                        Activity1(mode)
                def Option10():
                    CmdClear(cmdclear)
                    print('''    \n     Choose Bitrate Type:
        
        '''+bitrateopustxt+''' | '''+bitratevorbistxt+'''

        [1] RAKI_Libopus
        [2] Ogg Vorbis
        [0] Back
        ''')
                    try:
                        nbrs = int(input('       Choose the bitrate type here --> '))
                        if nbrs==1:
                            Activity1("opus")
                        elif nbrs==2:
                            Activity1("vorbis")
                        elif nbrs==0:
                            CmdClear(cmdclear)
                            Option9()
                        else:
                            print('     Invalid value')
                            time.sleep(1)
                            CmdClear(cmdclear)
                            Option10()
                    except:
                        print(' Invalid value')
                        Option10()
                Option10()
            
            # Changing of Program Path Settings
            elif(nbrs==2):
                def Func(num):
                    ffmpegPath=con['ffmpegPath']
                    vgaudioPath=con['VGAudioPath']
                    vgmstreamPath=con['vgmstreamPath']
                    if num==1:
                        ffmpegPath=TKWin_Single('Change FFMPEG Path',"Programs","*.exe")
                        if not ffmpegPath:
                            Option10()
                        else:
                            newjson['ffmpegPath']=ffmpegPath
                            setdataconfig()
                    elif num==2:
                        vgaudioPath=TKWin_Single('Change VGAudio Path',"Programs","*.exe")
                        if not vgaudioPath:
                            Option10()
                        else:
                            newjson['VGAudioPath']=vgaudioPath
                            setdataconfig()
                    elif num==3:
                        vgmstreamPath=TKWin_Single('Change VGMStream Path',"Programs","*.exe")
                        if not vgmstreamPath:
                            Option10()
                        else:
                            newjson['vgmstreamPath']=vgmstreamPath
                            setdataconfig()
                    elif num==0:
                        CmdClear(cmdclear)
                        Option9()
                    else:
                        print('     Invalid Number')
                        time.sleep(1)
                        Option10()
                def Option10():
                    CmdClear(cmdclear)
                    print('''\n     Select the program:
            [1] FFMPEG
            [2] VGAudio
            [3] VGMStream
            [0] Back''')
                    try:
                        nbrs=int(input('    Select the program here --> '))
                        Func(nbrs)
                    except:
                        print('     Invalid value')
                        Option10()
                Option10()
            
            # Channel Settings
            elif(nbrs==3):
                def Func(nbrs):
                    if(nbrs==1 or nbrs==2):
                        print('     Applying...')
                        newjson['channel']
                        setdataconfig()
                    elif(nbrs==0):
                        CmdClear(cmdclear)
                        Option9()
                    else:
                        print('     Invalid value')
                        time.sleep(1)
                        CmdClear(cmdclear)
                        Option10()
                def Option10():
                    nbrs=2
                    CmdClear(cmdclear)
                    print('''\n    Choose Channels:
                          
            '''+txtchanneljson+'''
        [1] Mono
        [2] Stereo
        [0] Back''')
                    try:
                        nbrs=int(input('    Choose option here -> '))
                        Func(nbrs)
                    except:
                        print('     Invalid value')
                        time.sleep(1)
                        CmdClear(cmdclear)
                        Option10()
                Option10()

            # Volume Settings
            elif(nbrs==4):
                CmdClear(cmdclear)
                volumestr=int(volume)*100
                def Func(nbrs,press01):
                    if(nbrs==1):
                        print('     Applying...')
                        newjson['addVolume']=1
                        setdataconfig()
                    elif(nbrs==2):
                        print('     Applying...')
                        newjson['addVolume']=.75
                        setdataconfig()
                    elif(nbrs==3):
                        print('     Applying...')
                        newjson['addVolume']=.5
                        setdataconfig()
                    elif(nbrs==4):
                        print('     Applying...')
                        newjson['addVolume']=.25
                        setdataconfig()
                    elif(nbrs==5):
                        print('     Applying...')
                        newjson['addVolume']=0
                        setdataconfig()
                    elif(nbrs==6):
                        CmdClear(cmdclear)
                        print('\n     Custom Volume:\n     Limit: (0 to 500%)\n\n     Main Volume: '+str(volumestr)+'%\n\n      Press Enter '+str(press01)+' times to back\n')
                        strvol=str(input('     Input volume here(Limit: 500%) ----> '))
                        if not strvol:
                            press01-=1
                            if press01==0:
                                Option10()
                                exit()
                            Func(nbrs,press01)
                        try:
                            strvol1=int(strvol)
                        except:
                            time.sleep(1)
                            print('     Invalid value')
                            Func(nbrs,3)
                        if strvol1>500 or strvol1<0:
                            print('     Limit numbers!!!')
                            time.sleep(0.5)
                            Func(nbrs,3)
                        else:
                            newjson['addVolume']=float(strvol/100)
                            setdataconfig()
                    elif(nbrs==0):
                        CmdClear(cmdclear)
                        Option9()
                    else:
                        print('     Invalid value')
                        time.sleep(1)
                        CmdClear(cmdclear)
                        Option10()
                def Option10():
                    press01=3
                    CmdClear(cmdclear)
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
                        Func(nbrs,press01)
                    except:
                        print('     Invalid value')
                        time.sleep(1)
                        Option10()
                Option10()

            # Modes settings
            elif(nbrs==5):
                CmdClear(cmdclear)
                def Func(nbrs):

                    # Modes from raki_libOpus settings
                    if nbrs==1:
                        CmdClear(cmdclear)
                        def Activity2(nbrs,max):
                            if(nbrs==0):
                                CmdClear(cmdclear)
                                Option10()
                            elif(nbrs<0 or nbrs>max):
                                print('     Invalid value')
                                Activity1()
                            else:
                                newjson['opusMode']=nbrs
                                setdataconfig()
                        def Activity1():
                            CmdClear(cmdclear)
                            print('''\n    Choose Mode from Cooked Opus:
        Main Mode: '''+nameopusMode+'''
''')
                            num=0
                            for opusinput in con["opusModeData"]:
                                num+=1
                                print('        ['+str(num)+'] '+opusinput["opusTitle"])
                            print('        [0] Back')
                            try:
                                nbrs=int(input('    Choose the mode here --> '))
                                Activity2(nbrs,num)
                            except:
                                print('     Invalid value')
                                Activity1()
                        Activity1()

                    # Modes from raki_pcm16 settings
                    elif nbrs==2:
                        CmdClear(cmdclear)
                        def Activity2(nbrs,max):
                            if(nbrs==0):
                                CmdClear(cmdclear)
                                Option10()
                            elif(nbrs<0 or nbrs>max):
                                print('     Invalid value')
                                Activity1()
                            else:
                                newjson['opusMode']=nbrs
                                setdataconfig()
                        def Activity1():
                            CmdClear(cmdclear)
                            print('''\n    Choose Mode from Cooked PCM:
        Main Mode: '''+namepcmMode+'''
''')
                            num=0
                            for pcminput in con["pcmModeData"]:
                                num+=1
                                print('        ['+str(num)+'] '+pcminput["pcmTitle"])
                            print('        [0] Back')
                            try:
                                nbrs=int(input('    Choose the mode here --> '))
                                Activity2(nbrs,num)
                            except:
                                print('     Invalid value')
                                Activity1()
                        Activity1()
                    elif nbrs==0:
                        CmdClear(cmdclear)
                        Option9()
                    else:
                        print('     Invalid value')
                        time.sleep(1)
                        CmdClear(cmdclear)
                        Option10()
                def Option10():
                    print('''
            Choose Mode Audio Type:
        [1] Cooked Opus
        [2] Cooked PCM
        [0] Back''')
                    try:
                        nbrs=int(input('    Input the mode type here --> '))
                        Func(nbrs)
                    except:
                        print('     Invalid value')
                        time.sleep(1)
                        CmdClear(cmdclear)
                        Option10()
                Option10()
            elif(nbrs==6):
                if cmdclear:
                    newjson['cmdclear']=False
                    setdataconfig()
                else:
                    newjson['cmdclear']=True
                    setdataconfig()
            elif(nbrs==0):
                pass
            else:
                print('     Invalid value')
                time.sleep(1)
                CmdClear(cmdclear)
                Option9()
        def Option9():
            print('''
    Settings: '''+'''
    Settings(JSON) Version: '''+str(ver)+'''
        [1] Change Bitrate
        [2] Change Path Environment
        [3] Channels
        [4] Volume
        [5] Mode''')
            if cmdclear:
                print('        [6] Remove Clear Screen')
            else:
                print('        [6] Clear Screen')
            print('        [0] Back')
            try:
                modeopt=int(input('   Choose the option --> '))
                Settings(modeopt)
            except:
                print('     Invalid value')
                time.sleep(1)
                CmdClear(cmdclear)
                Option9()
        Option9()

    # Invalid value
    else:
        print('\n     Invalid value!')
        time.sleep(1)
    return intoption

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
        os.remove('temp\\temp_intro.wav')
    except:
        pass
    try:
        os.remove('temp\\temp_full.wav')
    except:
        pass
    try:
        os.rmdir('temp')
    except:
        pass
    try:
        keytocontinue=input("   Press Enter to go Menu...")
    except:
        pass


#This info shows the comparison of a file
def fileSize(inputfile:str,output:str):
    filepathsize=os.path.getsize(inputfile)
    if filepathsize<1000000:
        filepathsizevalue="%.2f"%round(filepathsize/1024, 2)
        bfrfilepathtxt=str(filepathsizevalue)+" KB"
    elif filepathsize<1000000000:
        filepathsizevalue="%.2f"%round(filepathsize/1024000, 2)
        bfrfilepathtxt=str(filepathsizevalue)+" MB"
    else:
        filepathsizevalue="%.2f"%round(filepathsize/1024000000, 2)
        bfrfilepathtxt=str(filepathsizevalue)+" GB"
    filepathsize=os.path.getsize(output)
    if filepathsize<1000000:
        filepathsizevalue="%.2f"%round(filepathsize/1024, 2)
        filepathtxt=str(filepathsizevalue)+" KB"
    elif filepathsize<1000000000:
        filepathsizevalue="%.2f"%round(filepathsize/1024000, 2)
        filepathtxt=str(filepathsizevalue)+" MB"
    else:
        filepathsizevalue="%.2f"%round(filepathsize/1024000000, 2)
        filepathtxt=str(filepathsizevalue)+" GB"
    if filepathsize>os.path.getsize(inputfile):
        compressratio="%.2f"%round(((filepathsize-os.path.getsize(inputfile))/os.path.getsize(inputfile))*100,2)
        if compressratio=="0.00":
            compressratio="0.01"
        compresstext=compressratio+"%"+" larger"
    elif filepathsize==os.path.getsize(inputfile):
        compresstext="equal file size"
    else:
        compressratio="%.2f"%round(((os.path.getsize(inputfile)-filepathsize)/filepathsize)*100,2)
        if compressratio=="0.00":
            compressratio="0.01"
        compresstext=compressratio+"%"+" smaller"
    return '       DONE: '+output+' \n       Size: '+bfrfilepathtxt+' --> '+filepathtxt+' ('+compresstext+' than previous file'+')\n'

def loopMenu():
    NumMenu=Menu()
    if NumMenu==0:
        pass
    elif NumMenu==10:
        time.sleep(3)
        loopMenu()
    else:
        loopMenu()
loopMenu()