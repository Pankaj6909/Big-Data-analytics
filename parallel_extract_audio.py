#import everything from download_videos.py
from extract_audio import*


#function to extrat the audio for all the video files in parallel using threadpoolexecutor
def parallel_thread_pool_runner(file_list):

    t1=time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract_audio,file_list)
    t2=time.perf_counter()
    #print the time taken to extract the audio
    print(f'Time taken to extract audio using ThreadPoolExecutor:{round(t2-t1,2)}')

#function to extrat the audio for all the video files in parallel using processpoolexecutor
def parallel_process_pool_runner(file_list):
    t1=time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(extract_audio,file_list)
    t2=time.perf_counter()
    #print the time taken to extract the audio
    print(f'Time taken to extract audio using ProcessPoolExecutor:{round(t2-t1,2)}')


#function to extract the audio from all the video files in parallel using multiprocessing.Pool
def parallel_multiprocesserrunner(file_list):
    
    t1=time.perf_counter()
    with multiprocessing.Pool() as executor:
        executor.map(extract_audio,file_list)
    t2=time.perf_counter()
    #print the time taken to extract the audio
    print(f'Time taken to extract audio using multiprocessing:{round(t2-t1,2)}')

#function to extract the audio from all the video files in parallel using threads
def Parallel_threadrunner(file_list):

    t1=time.perf_counter()

    #create and start threads
    threads=[]

    for i in file_list:
        thread=threading.Thread(target=extract_audio,args=(i,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()   

    t2=time.perf_counter()
    #print the time taken to extract the audio
    print(f'Time taken to extract audio using Threads:{round(t2-t1,2)}')




#instance of the get_file_path function
file_path_list=get_file_path(folder_path)

if __name__=='__main__':

    parallel_thread_pool_runner(file_path_list)
    parallel_process_pool_runner(file_path_list)
    parallel_multiprocesserrunner(file_path_list)
    Parallel_threadrunner(file_path_list)