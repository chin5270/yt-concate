import sys
sys.path.append('./')

from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.get_all_video import GetVideoList

channel_id = 'UCudk4X86eRN6H2psDpP2LFg'


def main():
    inputs = {
        'channel_id' : channel_id,
        }

    steps = [
        GetVideoList(),
    ]
    
    p = Pipeline(steps)
    p.run(inputs)

if __name__ =="__main__":
    main()