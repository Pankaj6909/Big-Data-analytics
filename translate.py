#import all dependencies
from textblob import TextBlob
from deep_translator import GoogleTranslator
import time,concurrent.futures,os
from text_file_path import*


#function to translate text from the input file and save the translated text in a different file
def translate_text(file_name,path):
    with open(file_name,'r') as file:
        text=file.read()
    try:
        translated=GoogleTranslator(source='en',target='es')
        translated_text = (translated.translate(text))
        
        with open(f'Output/{path}/translated text.txt','w',encoding='utf-8') as file:
            file.write(translated_text)
    except Exception as e:
        print(e)

#instance of t he get_file_path function
file_name,path1=get_file_path(Output_folder)

#function to run the translate_text function in serial
def serial_translate():
    t1=time.perf_counter()
    for i,j  in enumerate(file_name):
        translate_text(j,path1[i])
    t2=time.perf_counter()
    print(f'Time taken to translate text in serial(secs):{round(t2-t1,2)}')



if __name__=='__main__':
    serial_translate()
