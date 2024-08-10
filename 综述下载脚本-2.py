import webbrowser
from urllib.parse import quote

print("请输入提示词：")
word = input()

# 使用quote函数确保提示词是URL编码的
encoded_word = quote(word)

# 构建必应搜索的URL
bing_url = f"http://search.cnki.net/search.aspx?q={encoded_word}"

# 使用默认浏览器打开必应搜索结果
webbrowser.open(bing_url)
