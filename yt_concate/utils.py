import sys
sys.path.append('./')
import os


from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import OUTPUT_DIR




class Utils:
    def __init__(self):
        pass

    def create_dir(self):
        os.makedirs(DOWNLOADS_DIR,exist_ok=True)
        os.makedirs(VIDEOS_DIR,exist_ok=True)
        os.makedirs(CAPTIONS_DIR,exist_ok=True)
        os.makedirs(OUTPUT_DIR,exist_ok=True)

    def get_video_list_filepath(self,channel_id):
        return os.path.join(DOWNLOADS_DIR,channel_id+'.txt')

    def get_video_list_exist(self,channel_id):
        path = os.path.join(DOWNLOADS_DIR,channel_id+'.txt')
        return os.path.exists(path) and os.path.getsize(path) > 0
    
    # @staticmethod
    # def get_video_id(url):
    #     return url.split('=')[-1]
    
    def caption_file_exist(self,yt):
        path = yt.caption_fillepath
        return os.path.exists(path) and os.path.getsize(path) > 0
    def video_file_exist(self,yt):
        path = yt.video_fillepath 
        return os.path.exists(path) and os.path.getsize(path) > 0
    
    def get_output_filepath(self,channel_id,search_word):
        filename = channel_id+'_'+search_word + '.mp4'
        return os.path.join( OUTPUT_DIR,filename)