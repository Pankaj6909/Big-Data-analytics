#import all dependencies
from textblob import TextBlob
import os
import multiprocessing,concurrent.futures,threading
import time
from text_file_path import*

#function to extract sentiments using Textblob
def extract_sentiment(file_name,path):

    try:
        #open a file to read the text and save it in a variable
        with open(file_name,'r') as file:
            text=file.read()
        blob=TextBlob(text)

        #open a file and write the sentiment analysis of the text
        with open(f'Output/{path}/Sentiment analysis.txt','w') as file:
            file.write(f'Sentiment:\nPolarity:{blob.sentiment.polarity}\nSubjectiviy:{blob.sentiment.subjectivity}')
    except Exception as e:
        print(e)


#instance of the get_file_path function 
file_name,path1=get_file_path(Output_folder)

#function to run the extract_sentiment function in serial
def serial_sentiment():
    t1=time.perf_counter()
    for i,j in enumerate(file_name):
        extract_sentiment(j,path1[i])
    t2=time.perf_counter()
    print(f'Time taken to extract sentiments in Serial(secs):{round(t2-t1,2)}')



if __name__=='__main__':
    serial_sentiment()

