import pyautogui
import keyboard
import time
import subprocess
import ast
import os
program_path=r"D:\\software\\ChatGLM\\智谱清言.exe"
def fileputin(true_asset):
    #统计true_asset中的文件数量
    file_num=len(true_asset)
    files = os.listdir('F:\\下载')

    # 根据文件的修改时间进行排序
    sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join('F:\\下载', x)))

    latest_files = [os.path.join('F:\\下载', sorted_files[-i]) for i in range(1, file_num + 1)]
    pyautogui.click(445,1350)
# 打印获取的文件路径
    for file in latest_files:
        keyboard.write(file+'space')


def generate_ct(raw,asset):
    """
    根据输入的字符串生成关键词列表。
    
    参数:
    raw (str): 输入的字符串
    
    返回:
    list: 关键词列表
    """
    # 打开大模型智谱清言的界面
    # 假设我们已经知道如何打开该程序
    # 这里使用 pyautogui 模拟鼠标点击和键盘输入
    string1=u"请根据以下提问：“"
    string2=u"”，从我附加的文件中读取相关内容，并进行引用，生成回答。"
    modified_1=str(string1)+str(raw)+str(string2)
    true_asset=ast.literal_eval(asset)
    subprocess.Popen([program_path])
    time.sleep(2)  # 等待程序打开
#    keyboard.press("alt+space")
#    time.sleep(0.5)
#    keyboard.press("x")
#    time.sleep(1) 快捷键导致程序异常卡顿，注释掉
    pyautogui.click(540,110)
    time.sleep(1)
    pyautogui.click(540,110)
    time.sleep(1)
    # 输入提问内容
    pyautogui.click(1330,1330)  # 选中聊天框
    time.sleep(0.5)
    keyboard.write(modified_1)
    fileputin(true_asset)
    # 等待大模型智谱清言生成回答
    time.sleep(15)  # 假设需要等待5秒
    
    # 获取回答内容
    # 这里假设回答内容出现在特定位置，可以使用 pyautogui 截图并 OCR 识别
    # 或者直接复制回答内容
    pyautogui.click(770,675)  # 假设回答内容在屏幕左上角
    time.sleep(1)
    
    # 从剪贴板获取回答内容