from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# 创建WebDriverWait对象，并明确指定最大等待时间为10秒
wait = WebDriverWait(driver, 10)

try:
    # 等待直到EndNote导出链接变得可点击
    endnote_export_link = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[exporttype='EndNote']"))
    )
    # 点击EndNote导出链接
    endnote_export_link.click()
except TimeoutException:
    print("Element not clickable within the given time frame!")