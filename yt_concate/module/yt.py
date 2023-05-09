import os

from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR

class Yt:
    def __init__(self,url):
        self.url = url
        self.id = self.get_video_id(self.url)
        self.caption_fillepath = self.get_caption_filepath()
        self.video_fillepath = self.get_video_filepath()
        self.captions = None
       

    @staticmethod
    def get_video_id(url):
        return url.split('=')[-1]
    
    def get_caption_filepath(self):
        return os.path.join(CAPTIONS_DIR,self.id+'.en.srt')
    def get_video_filepath(self):
        return os.path.join(VIDEOS_DIR,self.id+'txt')