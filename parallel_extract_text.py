#impor everything from extract_text.py
from extract_text import*

#function to extract text in parallel using the extract_text function and multiprocessing
def parallel_extract_text(file_list):
    t1=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as e:
        futures1=[e.submit(chunk_audio_and_extract_text,j,files[i]) for i,j in enumerate(file_list)]
        for future in concurrent.futures.as_completed(futures1 ):
            future.result()
    t2=time.perf_counter()
    print(f'Time taken to extract text in parallel using multiprocessing:{t2-t1}')

#function to extract text in parallel using the extract_text function and threads
def parallel_extract_text_using_threads(file_list):
    t1=time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as e:
        futures1=[e.submit(chunk_audio_and_extract_text,j,files[i]) for i,j in enumerate(file_list)]
        for future in concurrent.futures.as_completed(futures1 ):
            future.result()
    t2=time.perf_counter()
    print(f'Time taken to extract text in parallel using threads:{t2-t1}')


if __name__=='__main__':
    parallel_extract_text(file_list)
    parallel_extract_text_using_threads(file_list)