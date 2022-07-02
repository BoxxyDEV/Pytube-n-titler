from pytube import *
from YT_functions import *

def on_progress(stream, chunk, bytes_remaining):
    progress_string = f' {round(100 - bytes_remaining / stream.filesize *100, 0)}'
    print(str(progress_string) + '% complete')

while(True): # loops
    print('=====================Boxuga Video Downloader=====================') # title
    option1 = input('Select an Option \n 1 - Video Information \n 2 - Download Video \n 3 - Quit Program ') # asks question and grabs answer
    if option1 == '3':
        exit()
    URL = input('Please YT URL? ')
    video = YouTube(URL, on_progress_callback=on_progress)
    if option1 == '1':
        GrabVideoInformation(video)
    elif option1 == '2':
        DownloadVideo(video)
   
    print('=========Boxuga==========')
    print('=========Title===========')
    print(YouTube(URL).title)
    print('=========Length==========')
    print(str(int(YouTube(URL).length/60)) + ' Minutes')
    print('=========Channel=========')
    print(YouTube(URL).author)
