'''
tuling123.com注册
替换key
运行.py，扫描登录

windows下直接运行即可

linux
nohup python run.py &

之后手动打开二维码扫描或者使用一些方式让二维码在命令行显示。
'''

import requests
import itchat
import random

# Devin
# KEY = 'd6a29b9bd7bd40bcaedbf26b5010a050'
# userid='Devin'

# devin
KEY='ed9538da22024cf98776c4aeede166eb'
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'devin',
        # 'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    # robots=['1','2','3']
    # reply = get_response(msg['Text'])+random.choice(robots)
    reply = get_response(msg['Text'])
    return reply or defaultReply

# itchat.auto_login(enableCmdQR=True)
itchat.auto_login(hotReload=True,enableCmdQR=2)
# itchat.auto_login(enableCmdQR=1)
itchat.run()