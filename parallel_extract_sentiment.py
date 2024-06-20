
#import everythong from extract_sentiment.py
from extract_sentiment import*


#function to run the extract_sentiment function in parallel using threads
def parallel_sentiment_threads():
    t1=time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as e:
        futures1=[e.submit(extract_sentiment,j,path1[i]) for i,j in enumerate(file_name)]
        for future in concurrent.futures.as_completed(futures1):
            future.result()

    t2=time.perf_counter()
    print(f'Time taken to extract sentiments in parallel using threads:{t2-t1}')

#function to run the extract_sentiment function in parallel using multiprocessing
def parallel_sentiment_multiprocssing():
    t1=time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as e:
        futures1=[e.submit(extract_sentiment,j,path1[i]) for i,j in enumerate(file_name)]
        for future in concurrent.futures.as_completed(futures1):
            future.result()

    t2=time.perf_counter()
    print(f'Time taken to extract sentiments in parallel using multiprocessing:{t2-t1}')


if __name__=='__main__':
    parallel_sentiment_threads()
    parallel_sentiment_multiprocssing()