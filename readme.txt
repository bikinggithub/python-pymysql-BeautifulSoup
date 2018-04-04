本项目是使用python+BeautifulSoup+pymysql采集参考消息网站的实例。

1、安装python 当前项目版本为3.6

2、安装本次项目使用包含的模块，可直接使用命令 pip install 模块名称
   本次使用的模块包括：requests 、BeautifulSoup、pymysql。
   本项目中包含的部分模块为python内置模块，可跳过安装

3、本项目包含三个模块，数据库操作模块（自己封装的），采集首页程序，采集内容页程序

4、采集内容页时，可配置是否将内容中的图片保存到本地，如果开启到本地，
   请确认项目根目录下的upload目录有可读可写权限。本次项目仅在windows下测试通过，尚未在linux环境中运行。

5、数据库脚本见项目根目录下的spidernews.sql


