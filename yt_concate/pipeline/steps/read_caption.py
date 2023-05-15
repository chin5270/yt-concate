import sys
sys.path.append('./')

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import CAPTIONS_DIR


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if not utils.caption_file_exist(yt):
                continue

            captions = {}
            with open(yt.caption_fillepath,'r')as f:
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
            yt.captions = captions
            
        return data