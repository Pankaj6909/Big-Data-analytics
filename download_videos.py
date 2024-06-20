
#import all the dependencies 

import threading, time
from pytube import YouTube
import datetime

#create mutex and semaphore locks
mutex_lock=threading.Lock()
semaphore_lock=threading.Semaphore(5)


#variable to store the path to the file containing the url for the videos
url_file='video_urls.txt'

# function to read the urls from the file and save it in a list
def read_urls(file_name):
    urls=[]
    with open(file_name,'r') as file:
        for line in file:
            urls.append(line)
    return urls

#function to download the videos from the url and add the log into the log file
def download_videos_and_log(threadID,url):

    #aquire semaphore lock
    semaphore_lock.acquire()

    yt=YouTube(url)
    stream=yt.streams.get_highest_resolution()
    print(f'Thread {threadID} downloading video:{yt.title}')


   #download the video in the desired folder 
    try:
        stream.download(output_path=f'Output/{yt.title}' ,filename=f'{yt.title}.mp4')
        print(f' Thread {threadID} successfully downloaded video:{yt.title}')
    
    #if any error,write into the logfile with 'download:False' and print the error on the screen
    except Exception as e:

        #aquring mutex lock
        mutex_lock.acquire()
        #open the logfile to write the log
        with open('log_file.txt','a') as logfile:
            today=datetime.datetime.now()
            date_time= today.strftime("%H:%M %d-%m-%Y")
            logfile.write(f'Timestamp:{date_time},URL:{url},Thread_ID: Thread {threadID},download:{False}\n')
            
        #print the exception to the screen
            print(e)

    #if no error, write to the logfile with 'download:True'
    else:
        #aquiring mutex lock    
        mutex_lock.acquire()
        #open the logfile to write the log
        with open('log_file.txt','a') as logfile:
            today=datetime.datetime.now()
            date_time= today.strftime("%H:%M %d-%m-%Y")
            logfile.write(f'Timestamp:{date_time},URL:{url},Thread_ID: Thread {threadID},download:{True}\n')

    #finally,release mutex and semaphore locks
    finally:
        mutex_lock.release()
        semaphore_lock.release()

#function to download the videos serially
def serial_downloader():
    t1=time.perf_counter()
    url=read_urls(url_file)
    for i in url:
        download_videos_and_log(threadID=1,url=i)

    t2=time.perf_counter()
    print(f'Time taken to download the videos serially(secs):{round(t2-t1,2)}')



if __name__=='__main__':
    (serial_downloader())
    


    