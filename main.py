import pyautogui as pg
from keyword_generator import *
from abstract_download import *
from abstract_analyzer import *
from downloader import *
from output_generator import *
raw=input("请输入问题：")
kw=generate_kw(raw)
kw="大学生 学习兴趣 培养"
absurl=scriptdownload(kw)
asset=analyze(raw,kw)
download(asset,absurl,kw)
#generate_ct(asset)
#pg.click(709,895)