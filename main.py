import pandas as pd   
import requests   
import os
import openai
import urllib.request     
import cv2
import numpy as np
import glob             
from pytrends.request import TrendReq
import moviepy.editor
import random
from instagrapi import Client
import shutil
from instapy_cli import client
import ffmpeg
import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import *


pytrend = TrendReq()




# Get Google Hot Trends data
df = pytrend.trending_searches()

image_name = random.choice(df[0])


openai.api_key = ""

for i in range(15):
    response = openai.Image.create(
      prompt="{}".format(image_name),
      n=1,
      size="1024x1024"

    )
    image_url = response['data'][0]['url']
    urllib.request.urlretrieve("{}".format(image_url), "{}{}.jpg".format(image_name, i))



src_dir = "/mnt/c/Images/"
dst_dir = "/mnt/c/Images/im/"
for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
    shutil.copy(jpgfile, dst_dir)


path = "/mnt/c/Images/im/"
out_path = "/mnt/c/Images"
out_video_name = 'video.mp4'
out_video_full_path = out_path+out_video_name

pre_imgs = os.listdir(path)
# print(pre_imgs)
img = []

for i in pre_imgs:
    i = path+i
    # print(i)
    img.append(i)
    img.append(i)
    img.append(i)
    img.append(i)
    img.append(i)

# print(img)

cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')

frame = cv2.imread(img[0])
size = list(frame.shape)
del size[2]
size.reverse()
# print(size)

video = cv2.VideoWriter(out_video_name, cv2_fourcc, 4, size) #output video name, fourcc, fps, size

for i in range(len(img)): 
    video.write(cv2.imread(img[i]))

video.release()





dir = "/mnt/c/Images/music/"
filename = random.choice(os.listdir(dir))
print(filename)
path = os.path.join(dir, filename)


my_clip = moviepy.editor.VideoFileClip("/mnt/c/Images/video.mp4")  # .resize( (1080,1920) )
clip_duration = my_clip.duration

audio_background = moviepy.editor.AudioFileClip(path).set_duration(clip_duration)
print(audio_background)
final_audio = moviepy.editor.CompositeAudioClip([audio_background])
final_clip = my_clip.set_audio(final_audio)
final_clip.write_videofile("new_video.mp4")
