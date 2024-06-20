from translate import*

#function to run the translate_text function in parallel using threads
def parallel_translate_threads():
    t1=time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as e:
        futures1=[e.submit(translate_text,j,path1[i]) for i,j in enumerate(file_name)]
        for future in concurrent.futures.as_completed(futures1):
            future.result()
    t2=time.perf_counter()
    print(f'Time taken to translate text in parallel using threads:{t2-t1}')

#function to run the translate_text function in parallel using multiprocessing
def parallel_translate_multiprocessing():
    t1=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as e:
        futures1=[e.submit(translate_text,j,path1[i]) for i,j in enumerate(file_name)]
        for future in concurrent.futures.as_completed(futures1):
            future.result()

    t2=time.perf_counter()
    print(f'Time taken to translate text in parallel using multiprocessing:{t2-t1}')

if __name__=='__main__':
    parallel_translate_threads()
    parallel_translate_multiprocessing()