import mutagen
import colorama

def GrabMonthString(Month1): # proberly a better way to do this
    if Month1 == 1:
        return 'January'
    elif Month1 == 2:
        return 'Febuary'
    elif Month1 == 3:
        return 'March'
    elif Month1 == 4:
        return 'April'
    elif Month1 == 5:
        return 'May'
    elif Month1 == 6:
        return 'June'
    elif Month1 == 7:
        return 'July'
    elif Month1 == 8:
        return 'August'
    elif Month1 == 9:
        return 'September'
    elif Month1 == 10:
        return 'October'
    elif Month1 == 11:
        return 'November'
    elif Month1 == 12:
        return 'December'
    else:
        return 'Incorrect'

def GrabVideoInformation(YTURL): # Prints and writes a file (if requested)
    viddata = 'User Name       - ' + YTURL.author + '\nUser Channel ID - ' + YTURL.channel_id + '\nVideo Title     - ' + YTURL.title + '\nVideo Views     - ' + str(YTURL.views) + '\nUpload Date     - ' + str(YTURL.publish_date.day) + ' ' + GrabMonthString(YTURL.publish_date.month) + ' ' + str(YTURL.publish_date.year) + '\nAge Restricted  - ' + str(YTURL.age_restricted) + '\nVideo Time (S)  - ' + str(YTURL.length) + '\nVideo Time (M)  - ' + str(int((YTURL.length)/60)) + '\nDescription_______ \n' + YTURL.description
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
            YTURL.streams.get_audio_only().download(filename=str(fn + '.mp3')) 
    except AttributeError: # if video fails sends this error message
            print(colorama.Fore.RED + 'Error:' + colorama.Fore.WHITE + ' Downloading. Please Try Lower The Resoulution (if video)')
    if int(selection) >= 1:
        filen = str(fn + '.mp4')
    elif int(selection) == 0:
        filen = str(fn + '.mp3')
    with open(filen, 'r+b') as file:
        mediafile = mutagen.File(filen, easy=True)
        mediafile['title'] = VideoTitle
        mediafile['artist'] = VideoAuthor
        mediafile.save(file)   
