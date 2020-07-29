
# Import the required module for text  
# to speech conversion 
from gtts import gTTS 

  
# This module is imported so that we can  
# play the converted audio 

import os 

import pytesseract as tess
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from PIL import Image

import pyautogui
import time

x=1
while x<2:
    pyautogui.screenshot("Z:/PROJECT/BLIND/New folder/image.png")
    x+=1
    
    time.sleep(160)
    
    
    img = Image.open("image.png")
    text = tess.image_to_string(img, lang = 'eng')
      
    # Language in which you want to convert 
    
    language = 'en'
    
      
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    
    myobj = gTTS(text=text, lang=language, slow=False) 
    
      
    # Saving the converted audio in a mp3 file named 
    # welcome  
    
    myobj.save("welcome.mp3") 
    
      
    # Playing the converted file 
    
    os.system("welcome.mp3")
      
    # The text that you want to convert to audio 



