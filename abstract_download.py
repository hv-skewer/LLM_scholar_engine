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
def scriptdownload():
    service = Service()

    # 提示用户输入关键词
    print("请输入提示词：")
    word = input()
    # 使用quote函数对用户输入的关键词进行URL编码
    encoded_word = quote(word)

    # 设置知网搜索的基础URL和固定参数
    base_url = "https://kns.cnki.net/kns8s/defaultresult/index?"
    params = "korder=SU"

    # 构建完整的知网搜索URL
    cnki_url = f"{base_url}{params}&kw={encoded_word}"

    # 初始化Chrome浏览器
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # 最大化窗口
    driver = webdriver.Chrome(service=service)
    driver.get(cnki_url)  # 打开知网搜索页面
    ActionChains(driver).scroll_by_amount(0,600).perform()
    # 等待页面加载，直到全选按钮出现
    wait = WebDriverWait(driver, 20)  # 创建WebDriverWait对象，最大等待时间为20秒
    checkbox = wait.until(EC.presence_of_element_located((By.ID, 'selectCheckAll1')))  # 等待并找到全选按钮
    checkbox.click()  # 点击全选按钮

    # 查找并点击“导出与分析”按钮
    dropdown_analysis_btns = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#batchOpsBox > li:nth-child(2)")))  # 使用CSS选择器查找“导出与分析”按钮容器
    dropdown_analysis_btns.click()  # 点击“导出与分析”按钮
    # 查找并点击“导出选项”中的第二层菜单（如果需要）
    export_literature = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#batchOpsBox > li:nth-child(2) > ul > li.export > i")))
    export_literature.click()
    # 查找并点击“EndNote”导出链接
    time.sleep(1)
    endnote_export_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#batchOpsBox > li:nth-child(2) > ul > li.export > ul > li:nth-child(7)")))  # 使用CSS选择器查找EndNote导出链接
    endnote_export_link.click()  # 点击EndNote导出链接
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    export=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#result > ul > div > label:nth-child(9)")))
    export.click()
    export=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#result > ul > div > label:nth-child(11)")))
    export.click()
    export=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#result > ul > div > div > ul")))
    export.click()
    export=wait.until(EC.presence_of_element_located((By.ID, "litotxt")))
    export.click()
    time.sleep(5)