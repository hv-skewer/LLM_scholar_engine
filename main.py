import pyautogui as pg
from keyword_generator import *
from abstract_download import *
from abstract_analyzer import *
from downloader import *
from output_generator import *
raw=input("请输入问题：")
kw=generate_kw(raw) #根据问题生成关键词
absurl=scriptdownload(kw) #根据关键词下载摘要
asset=analyze(raw,kw) #根据问题和关键词生成下载列表
download(asset,absurl,kw) #根据列表下载文章
generate_ct(raw,asset) #根据问题和文章列表生成回答
#pg.click(709,895) #关闭窗口