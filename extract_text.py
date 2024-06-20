#import all dependencies
import speech_recognition as sr,os
from pathlib import Path
import concurrent.futures,multiprocessing,threading
from pydub import AudioSegment
import time
from io import BytesIO


#function that returns two lists, one with all audio files and other list with their path
def get_file_path(Output_folder):
    file_path =os.listdir('Output/')
    files=file_path[:]
    file_path=[f'Output/{j}/{j}.wav' for j in (file_path)]

    return files,file_path

#recognizer instance
recognizer=sr.Recognizer()

#divide the audio into a list of chunks and extract text to save it in a file
def chunk_audio_and_extract_text(audio_path,file, chunk_length=60000):  # chunk_length in milliseconds
    
    audio = AudioSegment.from_wav(audio_path)
    length_audio = len(audio)
    #variable to savee the text from all the chunks of an audio
    whole_text=''

    for i, chunk in enumerate(range(0, length_audio, chunk_length)):
        #divide the audio in small chunks
        chunk_audio = audio[chunk:chunk + chunk_length] 
        chunk_io=BytesIO()
        #export the small files in the memory
        chunk_audio.export(chunk_io, format="wav")
        chunk_io.seek(0)

        #extract text from each chunk and add it to the variable whole_text
        try:
            with sr.AudioFile(chunk_io) as source:
                audio_data=recognizer.record(source)
                text=recognizer.recognize_google(audio_data)
                whole_text+=' ' + text
        #if error, print error to the screen
        except Exception as e:
            print(e)
        
    #variable for the output path
    output_path=audio_path[0:-3]+'txt'
    #open the text file to write the whole text to it
    with open(output_path,'w') as file:
        file.write(whole_text)
        print(f'text has been written to the file {output_path}')

#instance of the get_file_path function
files,file_list=get_file_path(get_file_path)
    
#function to extract text in serial
def serial_text_extraction(file_list):

    t1=time.perf_counter()
    
    for i,j  in enumerate(file_list):
        chunk_audio_and_extract_text(j,files[i])

    t2=time.perf_counter()
    print(f'Time taken to extract text in serial(secs):{round(t2-t1,2)}')
    

if __name__=='__main__':
    serial_text_extraction(file_list)
