import pyautogui
import keyboard
import time
import subprocess
program_bath=r"D:\\software\\ChatGLM\\智谱清言.exe"
def generate_kw(raw):
    """
    根据输入的字符串生成关键词列表。
    
    参数:
    raw (str): 输入的字符串
    
    返回:
    list: 关键词列表
    """
    print(raw)
    # 打开大模型智谱清言的界面
    # 假设我们已经知道如何打开该程序
    # 这里使用 pyautogui 模拟鼠标点击和键盘输入
    string1=u"请根据以下提问：“"
    string2=u"”生成1-3个关键词，用于直接复制粘贴，并在中国知网上搜索可能找到相关参考资料的论文。关键词之间以空格隔开。请用不超过三个关键词回答，答案唯一。"
    modified_1=str(string1)+str(raw)+str(string2)
    subprocess.Popen([program_bath])
    time.sleep(2)  # 等待程序打开
    keyboard.press("alt+space")
    time.sleep(0.5)
    keyboard.press("x")
    time.sleep(1)
    pyautogui.click(540,110)
    time.sleep(1)
    pyautogui.click(540,110)
    time.sleep(1)
    # 输入提问内容
    pyautogui.click(1330,1330)  # 选中聊天框
    time.sleep(0.5)
    keyboard.write(modified_1)
    pyautogui.press('enter')
    print(modified_1)
    # 等待大模型智谱清言生成回答
    time.sleep(15)  # 假设需要等待5秒
    
    # 获取回答内容
    # 这里假设回答内容出现在特定位置，可以使用 pyautogui 截图并 OCR 识别
    # 或者直接复制回答内容
    pyautogui.click(770,675)  # 假设回答内容在屏幕左上角
    time.sleep(1)
    
    # 从剪贴板获取回答内容
    import pyperclip
    keywords = pyperclip.paste()
    
    return keywords