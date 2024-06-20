from extract_emotions import* 

#function to run the extract_emotions function in parallel using threads
def parallel_emotions_threads():
    t1=time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as e:
        futures1=[e.submit(extract_emotions,j,files1[i]) for i,j in enumerate(file_path1)]
        concurrent.futures.wait(futures1)
    for future in concurrent.futures.as_completed(futures1):
        future.result()

    t2=time.perf_counter()
    print(f'Time taken to extract emotions in parallel using threads:{t2-t1}')

#function to run the extract_emotions function in parallel using multiprocessing
def parallel_emotions_multiprocessing():
    t1=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as e:
        futures1=[e.submit(extract_emotions,j,files1[i]) for i,j in enumerate(file_path1)]
        concurrent.futures.wait(futures1)
    for future in concurrent.futures.as_completed(futures1):
        future.result()

    t2=time.perf_counter()
    print(f'Time taken to extract emotions in parallel using multiprocessing:{t2-t1}')

if __name__=='__main__':

    parallel_emotions_threads()
    parallel_emotions_multiprocessing()
