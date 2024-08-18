import pyautogui as pg
from .keyword_generator import generate_kw
from .abstract_download import scriptdownload
from .abstract_analyzer import analyze
from .downloader import download
from .output_generator import generate_ct
raw=input("请输入问题：")
kw=generate_kw(raw)
absurl=scriptdownload(kw)
asset=analyze(raw,kw)
download(asset,absurl,kw)
generate_ct(asset)
pg.click(709,895)