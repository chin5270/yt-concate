import sys
sys.path.append('./')
import os
from pprint import pprint

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import CAPTIONS_DIR


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTIONS_DIR):
            with open(os.path.join(CAPTIONS_DIR,caption_file) ,'r')as f:
                captions = {}
                time_line = False
                time = None
                caption = None
                for line in f:
                    if '-->' in line:
                        time_line = True
                        time = line.strip()
                        continue
                    if time_line:
                        caption = line.strip() 
                        time_line = False
                        captions[caption] = time
            data[caption_file] = captions
        pprint(data)
        return data