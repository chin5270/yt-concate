import sys
sys.path.append('./')

from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.Preflight import Preflight
from yt_concate.pipeline.steps.get_all_video import GetVideoList
from yt_concate.pipeline.steps.download_caption import DownloadCaptions
from yt_concate.utils import Utils

channel_id = 'UCucWV7tlbw5f9DYjicgEX_g'


def main():
    inputs = {
        'channel_id' : channel_id,
        }

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions()
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs,utils)

if __name__ =="__main__":
    main()
