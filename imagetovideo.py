import argparse
import cv2
import numpy as np
import glob



class ImageToVideo:
    def __init__(self, output):
        self.output = output

    def generate_frames(self, input, fps):
        frame_array = []
        for filename in glob.glob(r'/home/administrator/Documents/dl/final-multilabel-v1/images/*.jpg'):
            print(filename)
            #get each files as array
            img = cv2.imread(filename,1)
            height, width, layers = img.shape
            size = (width,height)
    
    		#append image array
            frame_array.append(img)

        out = cv2.VideoWriter(self.output,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

        for i in range(len(frame_array)):
    		# writing to a image array
            out.write(frame_array[i])
        out.release()




ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True)
ap.add_argument("-o", "--output", required=True)
args = vars(ap.parse_args())

input = args["input"]
output = args["output"]

fps = 0.5

# Create ImageToVideo Class object
image_to_video = ImageToVideo(output)
image_to_video.generate_frames(input, fps)