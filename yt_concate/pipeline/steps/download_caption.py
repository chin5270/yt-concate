import sys
sys.path.append('./')
import os
import time
from threading import Thread

import yt_dlp
from vtt_to_srt.vtt_to_srt import ConvertDirectories
from yt_concate.settings import CAPTIONS_DIR
from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.steps.step import StepException
import logging



class DownloadCaptions(Step):

    def process(self, data, inputs,utils):
   
        ydl_opts = {
            'writesubtitles': True,
            'writeautomaticsub': True,
            'skip_download': True,
            'subtitleslangs': ['en'],
            'outtmpl': './downloads/captions/%(id)s.%(ext)s'
        }
      
        for yt in data:
            if utils.caption_file_exist(yt):
                # print("Skip downloading subtitles.")
                logging.debug("Skip downloading subtitles.")
                continue
            # 更改下載的路徑
            video_id = yt.id
            ydl_opts['outtmpl'] = f'./downloads/captions/{video_id}.%(ext)s'
        
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([yt.url])

            # CAPTIONS_DIR的vtt字幕轉換成srt
            recursive = False
            convert_file = ConvertDirectories(CAPTIONS_DIR, recursive, "utf-8")
            convert_file.convert()
            # CAPTIONS_DIR檔案裡只要有.vtt就刪除掉
        for root, dirs, files in os.walk(CAPTIONS_DIR):
                for file in files:
                    if file.endswith(".vtt"): 
                        vtt_file_path = os.path.join(root, file)
                        os.remove(vtt_file_path)
                        print("Deleted:", vtt_file_path)
        return data