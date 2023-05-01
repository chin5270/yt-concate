import sys
sys.path.append('./')
import os

import yt_dlp
from vtt_to_srt.vtt_to_srt import ConvertDirectories
from yt_concate.settings import CAPTIONS_DIR
from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.steps.step import StepException



class DownloadCaptions(Step):

    def process(self, data, inputs,utils):

        ydl_opts = {
            'writesubtitles': True,
            'writeautomaticsub': True,
            'skip_download': True,
            'subtitleslangs': ['en'],
            'outtmpl': './downloads/captions/%(title)s.%(ext)s' }
        
        for url in data:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            recursive = False
            convert_file = ConvertDirectories(CAPTIONS_DIR, recursive, "utf-8")
            convert_file.convert()
            
        for root, dirs, files in os.walk(CAPTIONS_DIR):
                for file in files:
                    if file.endswith(".vtt"):
                        vtt_file_path = os.path.join(root, file)
                        os.remove(vtt_file_path)
                        print("Deleted:", vtt_file_path)


            