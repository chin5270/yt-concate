import sys
sys.path.append('./')
import argparse
import getopt
import logging

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
from log import config_logging

# channel_id = 'UCucWV7tlbw5f9DYjicgEX_g'
# search_word = 'pictures'


def print_usage():
    print("python main.py -c channel_id> -s <search_word> -l <limit> -log<logging_level>" )

def main():

    channel_id = ''
    search_word = ''
    limit = 30
    logging_level = logging.WARNING

    short_options = 'hc:s:l:g:'
    long_options = 'help channel_id= search_word= limit= logging_level='.split()

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
            print( 'channel id ='+ channel_id)
        elif opt in ("-s", "--search_word"):
            search_word = arg
            print('search word = '+ search_word)
        elif opt in ("-l", "--limit"):
            limit = int(arg)
            print('video limt = '+ str(limit))
        elif opt in ("-g", "logging_level"):
            logging_level = arg

    if not channel_id or not search_word:
       print_usage()
       sys.exit(2)

    if logging_level == 'DEBUG':
        logging_level=logging.DEBUG

    elif logging_level == 'INFO':
         logging_level=logging.INFO

    elif logging_level == 'WARNING':
        logging_level=logging.WARNING

    elif logging_level == 'ERROR':
        logging_level=logging.ERROR
        
    elif logging_level == 'CRITICAL':
        logging_level=logging.CRITICAL
    else:
        print_usage()
        sys.exit(2)



    inputs = {
        'channel_id' : channel_id,
        'search_word':search_word,
        'limit':limit,
        'logging level':logging_level
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
    config_logging(logging_level)
    utils = Utils()

    p = Pipeline(steps)
    p.run(inputs,utils)

if __name__ =="__main__":
    main()
