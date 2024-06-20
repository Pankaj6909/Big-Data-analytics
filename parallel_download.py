#import all the dependencies 

import concurrent.futures, time
from download_videos import*



#funtion to download the videos using ThreadPoolExecutor
def parallel_ThreadPoolDownloader():
    t1=time.perf_counter()
    
    url=read_urls(url_file)
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures1=[executor.submit(download_videos_and_log,i,u) for i,u in enumerate(url)]

    for future in concurrent.futures.as_completed(futures1):
        future.result()

    t2=time.perf_counter()
    print(f'time taken for downloading videos in parallel using threads:{round(t2-t1,2)}')




if __name__=='__main__':
    parallel_ThreadPoolDownloader()
