#import all dependencies
import spacy,nltk
import os
from nrclex import NRCLex
import time,concurrent.futures
from text_file_path import*


nlp = spacy.load("en_core_web_sm")
nltk.download('punkt')


#function to extract emotions from text 
def extract_emotions(file_name,file1):
    #open and read text file

    with open(file_name,'r') as file:
        text=file.read()
    try:
        doc=nlp(text)
        full_text = ' '.join([sent.text for sent in doc.sents])

        emotion=NRCLex(full_text)
        #open the file to write the analysis
        with open(f'Output/{file1}/Emotions.txt','w',encoding='utf-8') as file:
            file.write(f"Detected Emotions and Frequencies:/n{emotion.affect_frequencies}")
    except Exception as e:
        print(e)

#an instance of the get_file_path function  
file_path1,files1=get_file_path(Output_folder)

#function to run the extract_emotions function in serial
def serial_emotions():
    t1=time.perf_counter()
    for i,j in enumerate(file_path1):
        extract_emotions(j,files1[i])
    t2=time.perf_counter()
    print(f'Time taken to extract emotions in serial(secs):{round(t2-t1,2)}')



if __name__=='__main__':
    serial_emotions()

