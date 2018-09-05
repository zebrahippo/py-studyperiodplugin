# py-studyperiodplugin

## 功能：驾校科目一自动挂学时

主要是方便已经学过理论的同学挂学时，不用每隔15分钟输一个验证数字。<br>
没学过理论的童鞋还是乖乖的去学习。。<br><br>

## 运行环境
python2.7<br>
selenium-3.14.0<br>
Firefox 61.0.2(64位)<br>
geckodriver-v0.20.1-win64<br><br>

## 1、前提准备
1.1 安装python<br>
1.2 安装Firefox浏览器<br>
1.3下载geckodriver(是Firefox的官方webdriver)<br><br>

## 2、Python安装selenium
pip 安装命令：pip install selenium<br>

## 3、 下载安装geckodriver
下载地址https://github.com/mozilla/geckodriver/releases<br>
选择合适的版本，我是下载的geckodriver-v0.20.1-win64.zip，解压完记得把geckodriver.exe复制到studyperiodplugin.py所在目录下。<br><br>

## 4、使用方法
python2.7 studyperiodplugin.py<br><br>
4.1会弹出浏览器，记下验证码，下一步会用到，切换到命令行窗口；<br>
4.2命令行窗口会要求输入用户名、密码、验证码，就按正常登录网站的信息来填就好，没错，验证码就是4.1弹出的浏览器页面上的那个验证码，然后回车会自动登录，全程不用管浏览器，也不要去操作浏览器；<br>
4.3最后就不用管了，可以去干别的事了，等挂完4小时学时程序会关掉浏览器并退出。<br>
