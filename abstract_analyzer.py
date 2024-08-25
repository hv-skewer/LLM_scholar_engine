import os
import pyautogui
import subprocess
import time
import keyboard
def analyze(raw,kw):
    #找到某个文件夹中最近下载的文件
    # 获取文件夹中所有文件的路径
    files = os.listdir('F:\\下载')

    # 根据文件的修改时间进行排序
    sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join('F:\\下载', x)))

    # 获取最晚修改的文件路径
    latest_file = os.path.join('F:\\下载', sorted_files[-1])
    

    # 打开智谱清言，分析文件内容
    def open_zhipuqingyan():
        # 打开智谱清言
        subprocess.Popen([r"D:\\software\\ChatGLM\\智谱清言.exe"])
        time.sleep(1)
        pyautogui.hotkey("alt+space+x")
        time.sleep(1)
        pyautogui.click(445,1350)
        # 等待文件选择对话框打开
        time.sleep(1)

        # 输入文件路径
        keyboard.write(latest_file)
        print(latest_file)
        time.sleep(1)
        # 按下回车键打开文件
        keyboard.press_and_release('enter')
        keyboard.press_and_release('enter')
        time.sleep(0.5)
        pyautogui.click(1330,1350)  # Replace with the actual coordinates of the Zhipuqingyan application
        time.sleep(0.5)
        modified_2=str(u"请根据以下提问：“")+str(raw)+str("”以及关键词：“")+str(kw)+str("”在我给出的附件文件中选出十篇最可能找到回答问题的相关内容的文章，并以列表的形式，按照可能性从高到低给出文件名，作为你的回答。请回答阿拉伯数字序号，并采用严格的python列表格式，如[1,2,3,4,5,6,7,8,9,10]。")
        keyboard.write(modified_2)
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(15)
        pyautogui.click(770,675)
        import pyperclip
        asset = pyperclip.paste()

    # 调用打开智谱清言函数
    open_zhipuqingyan()