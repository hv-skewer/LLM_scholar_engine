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


wait = WebDriverWait(driver, 20)  # 创建WebDriverWait对象，最大等待时间为20秒
checkbox = wait.until(EC.presence_of_element_located((By.ID, 'selectCheckAll1')))  # 等待并找到全选按钮
checkbox.click()  # 点击全选按钮
# 查找并点击“导出与分析”按钮
dropdown_analysis_btns = wait.until(EC.presence_of_element_located((By.ID, "batchOpsBox")))
wait = WebDriverWait(driver, 1)
dropdown_analysis_btns = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#batchOpsBox > li:nth-child(2)")))  # 使用CSS选择器查找“导出与分析”按钮容器


# 查找并点击“导出选项”中的第二层菜单（如果需要）
export_literature = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#batchOpsBox > li:nth-child(2) > ul > li.export > i")))
export_literature.click()

# 查找并点击“EndNote”导出链接
endnote_export_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#batchOpsBox > li:nth-child(2) > ul > li.export > ul > li:nth-child(9) > a")))  # 使用CSS选择器查找EndNote导出链接
driver.execute_script("arguments[0].scrollIntoView(true);", endnote_export_link)
# 检查页面中是否存在iframe

endnote_export_link.click()
