import os,time
import datetime
from pathlib import Path
import concurrent.futures,multiprocessing,threading
from download_videos import*
from extract_audio import*
from extract_emotions import* 
from extract_text import*
from extract_sentiment import*
from translate import* 
from parallel_download import*
from parallel_extract_audio import*
from parallel_extract_emotions import* 
from parallel_extract_text import*
from parallel_extract_sentiment import*
from parallel_translate import* 

def serial_main():
    t1=time.perf_counter()
    serial_downloader()
    serial_audio_extraction(file_path_list)
    serial_text_extraction(file_list)
    serial_sentiment()
    serial_translate()
    serial_emotions()

    t2=time.perf_counter()
    print(f'Total time taken for all tasks in serial:{round(t2-t1,2)}')

def parallel_main():
    t1=time.perf_counter()
    parallel_ThreadPoolDownloader()
    parallel_process_pool_runner(file_path_list)#not sure if this is the best option
    parallel_extract_text_using_threads(file_list)#not sure if this is the best option
    parallel_sentiment_threads()
    parallel_translate_threads()
    parallel_emotions_threads()
    t2=time.perf_counter()
    print(f'Total time taken for all  tasks using multiprocessing and threading:{round(t2-t1,2)}')
 






if __name__=='__main__':
    serial_main()
    parallel_main()


