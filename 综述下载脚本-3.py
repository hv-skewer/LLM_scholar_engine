import webbrowser
from urllib.parse import quote

print("请输入提示词：")
word = input()

# 使用quote函数确保提示词是URL编码的
encoded_word = quote(word)

# 知网搜索的基础URL和参数（根据你的URL格式）
base_url = "https://kns.cnki.net/kns8s/defaultresult/index?"
params = "korder=SU"

# 构建完整的知网搜索URL
# 注意：这里我移除了crossids参数，因为它可能对于每个用户是唯一的。
# 如果需要这个参数，请从你自己的搜索会话中获取。
cnki_url = f"{base_url}{params}&kw={encoded_word}"

# 使用默认浏览器打开知网搜索结果
webbrowser.open(cnki_url)
