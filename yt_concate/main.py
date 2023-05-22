import sys
sys.path.append('./')
import getopt

from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.Preflight import Preflight
from yt_concate.pipeline.steps.get_all_video import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYt
from yt_concate.pipeline.steps.download_caption import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_video import DownloadVideos
from yt_concate.pipeline.steps.edit_video import EditVideo
from yt_concate.utils import Utils

# channel_id = 'UCucWV7tlbw5f9DYjicgEX_g'
# search_word = 'pictures'

def print_usage():
    print("python main.py -c channel_id> -s <search_word>")
def main():
    channel_id = ''
    search_word = ''
    short_options = 'hc:s:'
    long_options = 'help channel_id= search_word='.split()

    try:
        opts, args = getopt.getopt(sys.argv[1:], short_options, long_options)
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
           print_usage()
        elif opt in ("-c", "--channel_id"):
            channel_id = arg
            print( channel_id)
        elif opt in ("-s", "--search_word"):
            search_word = arg
            print(search_word)
    if not channel_id or not search_word:
       print_usage()
       sys.exit(2)
    inputs = {
        'channel_id' : channel_id,
        'search_word':search_word,
        'limit':30,
        }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYt(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideo(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs,utils)

if __name__ =="__main__":
    main()
