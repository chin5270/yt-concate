import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')


# 創建資料夾
DOWNLOADS_DIR = 'downloads'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR,'videos')
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')
OUTPUT_DIR = 'outputs'
