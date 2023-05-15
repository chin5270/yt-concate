import sys
sys.path.append('./')
from pprint import pprint

from yt_concate.pipeline.steps.step import Step
from yt_concate.module.found import Found

class Search(Step):
    def process(self, data, inputs, utils):
        search_word = inputs['search_word']
        found = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt,caption,time)
                    found.append(f)
        pprint(len(found))
        return found