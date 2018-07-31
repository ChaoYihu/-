# 主要的库依赖

requests

base64(python自带)

opencv-python

requests库可以直接通过pip安装,opencv-python模块在安装前要先升级一下setuptools才能通过pip安装,建议选择国内的pip镜像源,安装速度快.

# 关于Face++ API的申请

首先进入Face++的官方网站,然后申请一个账号,登录账号后进入Face++的用户控制台,在左侧的选择栏里选择应用管理->API Key 左上角有一个创建API Key的按钮,点击,申请一个试用的API Key即可.然后将得到的API Key与API Secret填入到Face_Core.py和Face_Analyze.py的两个对应的变量中,再运行main.py就可以使用了.