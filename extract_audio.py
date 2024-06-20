
#import all dependencies
import moviepy.editor as mp,time
import os
from pathlib import Path
import concurrent.futures,multiprocessing,threading

#variable to store the output folder path
folder_path='Output/'

#function to store the video path of all videos in a list
def get_file_path(folder_path):
    file_path_list=os.listdir(folder_path)
    for i,j in enumerate(file_path_list):
        file_path_list[i]=f'Output/{j}/{j}.mp4'
    return file_path_list

#function to extract the audio from the given video file path
def extract_audio(file_path):
    try:
        video=mp.VideoFileClip(file_path)
        #save the audio file in the designated video folder
        video.audio.write_audiofile(f'{file_path[0:-4]}.wav')
    except Exception as e:
        print(e)

#function to extract audio for all the video files in serial
def serial_audio_extraction(file_path_list):
    t1=time.perf_counter()

    for i in file_path_list:
        extract_audio(i)
    t2=time.perf_counter()
    print('Time taken to extract audio in serial(secs):',round(t2-t1,2))


#instance of the get_file_path function
file_path_list=get_file_path(folder_path)



if __name__=='__main__':
    serial_audio_extraction(file_path_list)
