from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import TimeoutException
import webbrowser
from urllib.parse import quote

print("请输入提示词：")
word = input()

# 使用quote函数确保提示词是URL编码的
encoded_word = quote(word)

# 知网搜索的基础URL和参数（根据你的URL格式）
# 初始化WebDriver
base_url = "https://kns.cnki.net/kns8s/defaultresult/index?"
params = "korder=SU"

# 构建完整的知网搜索URL
# 注意：这里我移除了crossids参数，因为它可能对于每个用户是唯一的。
# 如果需要这个参数，请从你自己的搜索会话中获取。
cnki_url = f"{base_url}{params}&kw={encoded_word}"
driver = webdriver.Edge()
driver.get(cnki_url)
#
wait = WebDriverWait(driver, 20)
checkbox = wait.until(EC.presence_of_element_located((By.ID, 'selectCheckAll1')))
# 点击全选按钮
checkbox.click()

# 创建WebDriverWait对象，并明确指定最大等待时间为10秒



# 查找"导出与分析"的元素并模拟鼠标悬停
dropdown_analysis_btns = wait.until(EC.presence_of_element_located((By.ID, "batchOpsBox")))
wait = WebDriverWait(driver, 1)
dropdown_analysis_btns = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "icon-d")))
wait = WebDriverWait(driver, 1)
dropdown_analysis_btns.click()
export_literature = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "export")))
wait = WebDriverWait(driver, 1)
dropdown_analysis_btns = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "secondUl")))
wait = WebDriverWait(driver, 1)
dropdown_analysis_btns.click()
# 等待"EndNote"的元素出现并模拟鼠标悬停
endnote_export_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[exporttype='EndNote']")))
endnote_export_link.click()

# 完成后关闭浏览器