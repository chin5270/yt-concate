import sys
sys.path.append('./')
import os
from pytube import YouTube

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import VIDEOS_DIR

class DownloadVideos(Step):
    def process(self, data, inputs, utils):
       
       yt_set = set([found.yt for found in data])
       
    

       for yt in yt_set:
            url= yt.url
            if utils.video_file_exist(yt):
                print(f'found existing video file for {url} , skipping')
                continue
            YouTube(url).streams.get_highest_resolution().download(output_path= VIDEOS_DIR ,filename = yt.id + '.mp4')
         
      
