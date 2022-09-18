# EasyTest

#2019-7-22
线上体验地址：http://47.96.182.173:8000(服务器到期，已失效)
主要修改为前后端分离的方式，部分功能做了修改，代码未上传（暂时不会有了）


# 
个人自研的自动化测试平台，借鉴了部分HttpRunner的思想和部分代码，主要实现了项目管理、签名方式管理、接口管理、用例管理和测试计划的制定和运行等主要功能，其它的编辑修改都没做，现在只相当于完成了一个Demo吧。
## 环境：
                Python 3.6.3
                Django 2.0.1
                Pymysql 0.8.0
                Requests 2.18.4
## 主要功能

## 项目签名管理：
                项目签名方式的增删改查
		 
## 项目管理
  项目的增删改查，可以选择对应的签名方式
		 
### 接口管理
     接口的增删改查
     
### 测试环境管理
     测试环境的增删改查，方便执行的时候快速切换测试环境
		 
### 用例管理
     测试用例的增删改查，单个用例调试
		 
### 用例增加
一个用例中可以有多个接口　<br>
用例中用$符号来定义变量，用来多个接口之间参数的传递 <br>
如：<br>
    登录接口　url: /login  data: {"phonenum": "13599999999", "password":"123456"}  登录成功后,　返回userid <br>
		查询客户信息接口　url: /userinfo/$phonenum  data: {"userid": $userid} <br>
这里首先需要定义一个$phonenum变量，执行的时候，会自动在上下文中查找到phonenum的值为13599999999,并将$phonenum的值替换，执行时，查询客户信息      接口的url会变成/userinfo/1359999999  <br>
由于userid是登录接口返回的参数，所以在登录接口这一步需要添加一个提取参数userid,然后执行的时候会自动取值并替换 <br>

### 测试计划管理
计划的增删改查<br>
计划制定，可以根据项目选择多个用例，主要用来批量执行用例<br>
执行方式包括普通的执行和定时执行（暂时未做），执行完成后，可以查看测试报告 <br>

### 联系我　QQ:317808643
由于之前在公司已经用tornado实现过一次，除了上面部分，还包括定时任务，用户管理，权限管理，数据库监控，不方便放出来（有少部分别人的代码），这次用django又实现一次, 所以代码和前端都比较随意。
