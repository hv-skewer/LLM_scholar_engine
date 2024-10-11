import requsts
from bs4 import BeautifulSoup
import os
import pyautogui
import ast
import time
from selenium import webdriver  # 导入Selenium中的webdriver模块，用于控制浏览器
from selenium.webdriver.common.by import By  # 导入By模块，用于定位元素
from selenium.webdriver.common.keys import Keys  # 导入Keys模块，用于模拟键盘输入
from selenium.webdriver.support.ui import WebDriverWait  # 导入WebDriverWait模块，用于显式等待
from selenium.webdriver.support import expected_conditions as EC  # 导入expected_conditions模块，用于设置等待条件
from selenium.common.exceptions import TimeoutException  # 导入TimeoutException，用于处理超时异常
from selenium.webdriver.chrome.service import Service  # 导入Service模块，用于Chrome服务
from selenium.webdriver.chrome.options import Options  # 导入Options模块，用于配置Chrome选项
from selenium.webdriver.common.action_chains import ActionChains
from urllib.parse import quote  # 导入quote函数，用于URL编码
from selenium.webdriver.chrome.service import Service
def download(asset,absurl,kw):
    #asset应该是列表形式，包含文件编号
    #absurl是网页地址
    #kw是关键字
    service = Service()
    true_asset=ast.literal_eval(asset)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # 最大化窗口
    driver = webdriver.Chrome(service=service)
    driver.get(absurl)  # 打开知网搜索页面
    wait = WebDriverWait(driver, 20)  # 创建WebDriverWait对象，最大等待时间为20秒
    for doc in true_asset:
        location=f".result-table-list > tbody > tr:nth-child("+str(doc) +f") > .seq > input"
        checkbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, location)))  # 等待并找到全选按钮
        checkbox.click()
    #批量下载
    driver.execute_script("window.scrollTo(0, 0);")  # 滚动到页面顶部
    download_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bulkdownload export")))  # 等待并找到下载按钮
    download_btn.click()

    # 等待下载完成
    time.sleep(60)
