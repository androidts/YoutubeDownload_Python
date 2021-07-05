from __future__ import unicode_literals
import youtube_dl

url = input("Enter Url :")

ydl_opt = {
    'format': 'bestaudio/best' #for Audio 
}

print("1. Video download 2. Audio download")
option  = int(input("Enter option"))

# for Youtube video download
if(option == 1):
    res = input("Enter resolution ex:- 1080p")

    ydl_opts = {
    'format': 'bestvideo[height<='+res+']+bestaudio[ext=m4a]/best[height<=1080]'#for video
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

elif(option == 2):
    with youtube_dl.YoutubeDL(ydl_opt) as ydl:
        ydl.download([url])


 
    

    



   

