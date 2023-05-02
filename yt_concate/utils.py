import sys
sys.path.append('./')
import os
from yt_dlp import YoutubeDL

from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR




class Utils:
    def __init__(self):
        pass

    def create_dir(self):
        os.makedirs(DOWNLOADS_DIR,exist_ok=True)
        os.makedirs(VIDEOS_DIR,exist_ok=True)
        os.makedirs(CAPTIONS_DIR,exist_ok=True)

    @staticmethod
    def get_video_id(url):
        return url.split('=')[-1]
    

    def caption_file_exist(self,url):
        path = os.path.join(CAPTIONS_DIR,self.get_video_id(url)+ '.en.srt')
        return os.path.exists(path) and os.path.getsize(path) > 0