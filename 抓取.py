

# 获取当前微信客户端
from wxauto import wxauto

#前提是安装了wxauto库，需要挂梯子下载安装，指令为pip install wxauto

wx = wxauto.WeChat()

# 获取会话列表
wx.GetSessionList()


###############################
# 1、获取默认窗口聊天信息
###############################
# 函数名称：get_default_window_messages
# 函数功能：获取并打印默认窗口中的所有消息
# 说明：该函数首先获取当前窗口中的所有消息，并打印每条消息的发送者和内容。然后加载更多消息，并再次打印所有消息的发送者和内容。
# 注意：该代码片段中的wx模块和方法是假设存在的，实际使用时需要根据实际情况进行调整。
###############################
def get_default_window_messages():
    # 获取当前窗口中的所有消息
    # 默认是微信窗口当前选中的窗口
    # 输出当前聊天窗口聊天消息
    msgs = wx.GetAllMessage()
    # 遍历所有消息并打印发送者和内容
    for msg in msgs:
        print('%s : %s' % (msg[0], msg[1]))

    # 加载更多消息
    # 获取更多聊天记录
    wx.LoadMoreMessage()
    # 再次获取所有消息
    msgs = wx.GetAllMessage()
    # 遍历新获取的消息并打印发送者和内容
    for msg in msgs:
        print('%s : %s' % (msg[0], msg[1]))


#if __name__ == '__main__':
get_default_window_messages()

