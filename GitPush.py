# coding=utf-8

import os
import requests
import time
import GitPushApi
import subprocess
import requests
localtime = time.asctime( time.localtime(time.time()) )

def send_message(title, desp):
    wx = GitPushApi.WeChat()
    # wx_hr = GitPushApihr.WeChat()
    wx.send_data(title+desp)
    # wx_hr.send_data(title+desp)
    print("title = >" + title)
    print("desp = >" + desp)

print ("\n开始更新项目\n")
cozy=os.popen("export http_proxy=127.0.0.1:10808 ; export https_proxy=127.0.0.1:10808 ; git -C /docker/cozy pull").read()

showcozy = os.popen("git -C /docker/cozy show | sed -n '5p'").read()
def cozyjd():
    if 'Already' in cozy:
        print (str(localtime)+"\ncozy已经是最新的了\n")
    elif 'Fast-forward' in cozy:
        send_message(title=str(localtime)+'\n<a href=\"https://github.com/cozy-labs/cozy-desktop">cozy-labs/cozy-desktop仓库更新概览</a>\n'+"########################\n"+str(showcozy)+"########################\n" , desp=str(cozy)) 
    else :
        print (str(localtime)+"\ncozy更新错误稍后再试\n")

if __name__ == '__main__':
    cozyjd()
