'''
Author      :   Saqib Ullah Siddiqui
Date        :   02-March-2020
Objective   :   Convert Images (.jpg,.jpeg and .png) into Vido file

Usage       :   python imagetovideo.py -i /home/administrator/Documents/dl/images 
                            -o /home/administrator/Documents/dl/images/video.avi 
                            -f 20                
'''


import argparse
import cv2
import numpy as np
import os


class ImageToVideo:
    def __init__(self, output):
        self.output = output

    def generate_frames(self, input, fps):
        frame_array = []
        for filename in os.listdir(input):
            print(filename)
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                #create each file name
                img = cv2.imread(input+"/"+filename,1)
                height, width, layers = img.shape
                size = (width,height)    
                #append image array
                frame_array.append(img)

        out = cv2.VideoWriter(self.output,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

        for i in range(len(frame_array)):
    		# writing to a image array
            out.write(frame_array[i])
        out.release()


# Define Argument Parser for the script
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True)
ap.add_argument("-o", "--output", required=True)
ap.add_argument("-f", "--fps", required=True)
args = vars(ap.parse_args())

# Set user parameters
input = args["input"]
output = args["output"]
fps = args["fps"]

# Create ImageToVideo Class object
image_to_video = ImageToVideo(output)
image_to_video.generate_frames(input, fps)
