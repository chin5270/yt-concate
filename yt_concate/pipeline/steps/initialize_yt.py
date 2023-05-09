import sys
sys.path.append('./')

from yt_concate.pipeline.steps.step import Step
from yt_concate.module.yt import Yt

# 在這裡整理data的資料，將Yt實例，讓後續pipeline裡的step可以很好的使用class Yt
class InitializeYt(Step):
    def process(self, data, inputs, utils):
        return  [ Yt(url) for url in data]