from fileinput import filename
from time import strftime
import datetime
import mutagen
import subprocess
import os

def GrabVideoInformation(YTURL): # Prints and writes a file (if requested)
    viddata = 'User Name       - ' + YTURL.author + '\nUser Channel ID - ' + YTURL.channel_id + '\nVideo Title     - ' + YTURL.title + '\nVideo Views     - ' + str(YTURL.views) + '\nUpload Date     - ' + datetime.date(YTURL.publish_date.year, YTURL.publish_date.month, YTURL.publish_date.day).strftime("%d %B %Y") + '\nAge Restricted  - ' + str(YTURL.age_restricted) + '\nVideo Time (S)  - ' + str(YTURL.length) + '\nVideo Time (M)  - ' + str(int((YTURL.length)/60)) + '\nDescription_______ \n' + YTURL.description
    print(viddata) # prints viddata variable
    ask = input('Do you want to print to a .TXT file (y/n)? ') # takes input to ask if they want to write it to a text file
    if ask == 'y':
        info1 = open(YTURL.title + ' Video Information.txt', "w") #creates text file
        info1.write(viddata) #writes data to file
        info1.close #closes the instance
    else:
        exit()

def DownloadVideo(YTURL): # video downloader code
    fn  = input('Please enter a filename (note: will add .mp4/.mp3) or (press n to use YouTube Title)? ') # asks for a filename
    if fn == 'n':
        fn = YTURL.title
    VideoTitle = input('Enter Title or (type "n" to use YouTube Title)? ') 
    VideoAuthor = YTURL.author # sets channel name to a local variable
    if VideoTitle == 'n': # checks if user said no and uses YouTube Title
        VideoTitle = YTURL.title
    if '- Topic' in VideoAuthor: # if youtube channel is a Topic Channel or cotains it at the end 
        VideoAuthor = str(VideoAuthor[:-8])  
    selection = input('5 - HD/720p - MP4\n4 - 480p - MP4\n3 - 360p - MP4 \n2 - 240p - MP4 \n1 - 144p - MP4 \n0 - Audio - MP3 ')
    try:# downloads video
        if selection == '5':
            YTURL.streams.get_by_resolution('720p').download(filename=str(fn + '.mp4'))
        elif selection == '4':
            YTURL.streams.get_by_resolution('480p').download(filename=str(fn + '.mp4'))
        elif selection == '3':
            YTURL.streams.get_by_resolution('360p').download(filename=str(fn + '.mp4'))
        elif selection == '2':
            YTURL.streams.get_by_resolution('240p').download(filename=str(fn + '.mp4'))
        elif selection == '1': 
            YTURL.streams.get_by_resolution('144p').download(filename=str(fn + '.mp4'))
        elif selection == '0':
            YTURL.streams.get_audio_only().download(filename='tempy.mp3')

            subprocess.run(["ffmpeg", "-loglevel", "0", "-i", "tempy.mp3", fn + ".mp3"])
            os.remove('tempy.mp3')
        if int(selection) >= 1:
            filen = str(fn + '.mp4')
        elif int(selection) == 0:
            filen = str(fn + '.mp3')
        with open(filen, 'r+b') as file:
            mediafile = mutagen.File(filen, easy=True)
            mediafile['title'] = VideoTitle
            mediafile['artist'] = VideoAuthor
            mediafile.save(file)   
 
    except AttributeError: # if video fails sends this error message
            print('Error: Downloading. Please Try Lower The Resoulution (if video)')
 
