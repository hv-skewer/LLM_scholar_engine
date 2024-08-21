import pyautogui as pg
from .keyword_generator import KeywordGenerator
from .abstract_download import AbstractDownload
from .abstract_analyzer import AbstractAnalyzer
from .downloader import Downloader
from .output_generator import OutputGenerator
raw=input("请输入问题：")
kw=generate_kw(raw)
absurl=scriptdownload(kw)
#asset=analyze(raw,kw)
#download(asset,absurl,kw)
#generate_ct(asset)
#pg.click(709,895)