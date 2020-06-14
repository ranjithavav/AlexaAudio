#!/usr/bin/env python3
import subprocess
c = open("url","r")
a = 97
for x in c.readlines():
    s = chr(a)
    command1 = "youtube-dl", x, "-f","bestaudio[ext=m4a]","--output", s+".m4a"
    command2 = "ffmpeg", "-y", "-i",s+".m4a", "-ar", "16000", "-ab", "48k", "-codec:a", "libmp3lame", "-ac", "1",  s+".mp3"
    command3 = "rm",s+".m4a"
    subprocess.call(command1, shell=False)
    subprocess.call(command2, shell=False)
    subprocess.call(command3, shell=False)
    print(x)
    a = a +1
