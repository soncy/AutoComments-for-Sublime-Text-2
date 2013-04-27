Sublime Text2 一键添加注释插件
=============

一键(默认快捷键，osx：command+shif+/，其他: ctrl+shift+/)自动为js，css和py文件开始增加一段注释，如下：

	/*
     * Created with Sublime Text 2.
	 * User: song.chen
	 * Date: 2013-03-29
	 * Time: 12:00:41
	 * Contact: song.chen@qunar.com
	 */

 
目前只支持js,css,py后缀的文件

### 安装

可以通过下面两种方式安装  

1. 到你的Sublime Text2 的Packages目录下，运行   
    
        git clone git://github.com/soncy/AutoComments-for-Sublime-Text-2.git

2. 直接下载zip包，解压到Packages目录.

Packages目录所在位置:

* Windows: %APPDATA%\Sublime Text 2
* OS X: ~/Library/Application Support/Sublime Text 2
* Linux: ~/.config/sublime-text-2

### 配置

Preferences -> Package Settings -> AutoComments

配置文件格式：

    {
        "user": "soncy",
        "contact": "http://www.qifendi.com"
    }