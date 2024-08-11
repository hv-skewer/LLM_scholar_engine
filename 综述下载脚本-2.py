# 设置Edge选项（例如，无头模式）
edge_options = Options()
# edge_options.add_argument("--headless")  # 无界面运行，如果需要界面，可以注释掉这一行

# 指定EdgeDriver的路径
webdriver_service = Service('path/to/msedgedriver')

# 初始化webdriver
driver = webdriver.Edge(service=webdriver_service, options=edge_options)

# 打开网页
driver.get('https://kns.cnki.net/kns8s/defaultresult/index?crossids=YSTT4HG0...')

# 查找复选框元素
checkbox = driver.find_element(By.ID, 'selectCheckAll1')

# 点击复选框来勾选或取消勾选
checkbox.click()

# 根据需要执行其他操作...

# 关闭浏览器
driver.quit()