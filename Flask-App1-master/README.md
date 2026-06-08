 **项目部署教程** 
一、通过git clone url 去拉取代码（之前拉过代码使用git pull获取更新即可）
二、用Pycharm将拉取的项目打开
1.python依赖包：
pip install flask flask-wtf flask-sqlalchemy flask-login passlib
pip install email-validator
pip install flask
pip install pymysql
pip install requests bs4
pip3 install html5lib
pip install flask_bootstrap
2.数据脚本（创建数据库数据表）
创建数据库：
CREATE DATABASE stat
USE stat
创建用户表
CREATE TABLE USER(
		id INTEGER PRIMARY KEY AUTO_INCREMENT,
		username VARCHAR(50) UNIQUE,
		email VARCHAR(100)UNIQUE,
		password_hash VARCHAR(200)
		)
3.确认代码中python路径下config.py文件中的数据库配置信息
 SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/stat'
4.执行run.py去启动Web项目(或者在控制台执行指令python run.py 启动项目)

 **开发教程** 
一、项目结构
python
      ---control
      ---model
web
     ---static
     ---templates
该项目结构基于Flask框架（MVT模式）
开发步骤：
（1）将与用户交互的html页面放至templates路径下（如果html页面涉及第三方CSS样式及js，将CSS、js文件放至static路径下）。
（2）如果系统功能涉及到与数据库交互，则在model路径下创建与数据表对应的模型（类）。
（3）如果页面动态加载需要调用路由或者用户在页面中执行了某个动作去调用对应的路由，则在control路径下新建一个.py文件，将对应路由执行的代码写入其中。


**新增商品销量分析功能**
1.通过需求分析及功能分析新建商品销量数据表
CREATE TABLE goods(
	a INT PRIMARY KEY,
	b INT,
	c INT 
	)
//插入一条模拟的数据
INSERT into goods VALUES(5,15,3)
