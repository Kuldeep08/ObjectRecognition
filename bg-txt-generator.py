import urllib.request
import sys
sys.path.append('/usr/local/lib/python3.5/site-packages')
import cv2
import numpy as np
import os


def create_pos_n_neg():
    for file_type in ['pos']:
        
        for img in os.listdir(file_type):

            if file_type == 'pos':
                os.system("opencv_createsamples -img "+str(img)+ " -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 2024")
                #line = file_type+'/'+img+' 1 0 0 50 50\n'
                #with open('info.dat','a') as f:
                   # f.write(line)


            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)

create_pos_n_neg()
