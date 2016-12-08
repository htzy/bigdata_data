# 需求
想学习大数据等知识，一个一个找资料太麻烦，想爬取文字、图片、视频等资料学习。
要求：
1、主流专业的大数据学习平台、爬取文字、pdf、word、图片、视频等资料；
2、关键字：
java、scala、docker、spark、hadoop、play*、
||
基础、应用、实际、解析、笔记、核心、处理、入门、原理（进一步知识分层）

# install software
### develop environment
ubuntu 16.04, python-2.7.12, pip-9.0.1, scrapy-0.25.0

### install command
```shell
$ pip install --upgrade pip
$ wget http://launchpadlibrarian.net/109052632/python-support_1.0.15_all.deb
$ sudo dpkg -i python-support_1.0.15_all.deb
# 把Scrapy签名的GPG密钥添加到APT的钥匙环中
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7
# create /etc/apt/sources.list.d/scrapy.list 
$ echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | sudo tee /etc/apt/sources.list.d/scrapy.list
# install scrapy-latest
$ sudo apt-get update && sudo apt-get install scrapy-0.25

# create project
$ scrapy startproject bigdata

# try to use Selector in Shell
$ scrapy shell "www.baidu.com"
# use exit() or ctrl-D to exit
>>>exit()
```
```python
# ignore web site contains 'window', '线下','预告', '报名地址'
```



# references
[demo code from scrapy in github](https://github.com/scrapy/dirbot)

# tools
[firepath in mozilla](https://addons.mozilla.org/en-us/firefox/addon/firepath/)
[xpath-checker in mazilla](https://addons.mozilla.org/zh-cn/firefox/addon/xpath-checker/)
