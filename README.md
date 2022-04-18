# flypy_dictionary

>全拼转小鹤双拼Python脚本+Rime词库脚本

## 为什么有这个Repo？

最近使用gboard的时候，想整理自己的双拼词库，打算分为私人词库和常用公共词库，私人词库可以通过自己使用习惯导出，然而通过网络上找到的公共词库都是全拼词库，所以打算转换成小鹤双拼可以使用的词库。这是一个非常简单的小脚本，但是竟然在网上没看到对小鹤双拼进行支持的词库，可能还是双拼用户比较少的缘故。

当然这个脚本不止支持gboard，你可以通过修改initials和finals对照表重新运行，得到符合你输入习惯的词库；也可以通过定制输出的line格式，定制符合对应输入法的dictionary文件。

## Repo中文件介绍

1. `搜狗标准词库.scel`：搜狗网上下载的标准词库。
2. `dictionary.txt`：深蓝词库转换上述词库得到的文件。
3. `finals1.txt`：常规韵母对照表。
4. `finals2.txt`：没声母的那些字韵母对照表。
5. `initials.txt`：声母对照表。
6. `todouble.py`：主要完成生成词典的脚本。
7. `dictionary_rime.txt`：添加支持生成Rime的词库啦。
8. `torime.py`：生成rime词库的小脚本。

## todoble.py使用

安装好Python环境后，只需要部署好`pypinyin`即可：

```cmd
python -m pip install pypinyin
```

然后到此文件夹运行：
```cmd
cd \path\to\this\folder
python .\todouble.py
```

最后生成的`dictionary_new.txt`要用`notepad++`转换一下格式：

`编辑 > 文档格式转换 > 转换为UNIX（LF）`

添加Rime词库支持了~
```cmd
cd \path\to\this\fold
python .\torime.py
```

生成的`dictionary_rime.txt`可以直接使用：
`右键单击Rime图标 > 用户词典管理 > 点击<luna_pinyin> > 点击<导入文本码表>`

## 一些链接

> 不太熟悉Python，所以基本都是一些Python基本语法。

- [pypinyin](https://github.com/mozillazg/python-pinyin#id6)
- [pypinyin api](https://pypinyin.readthedocs.io/zh_CN/master/api.html)
- [python 字符串连接函数](https://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p14_combine_and_concatenate_strings.html)
- [python for loop](https://www.w3schools.com/python/python_for_loops.asp)
- [python readline](https://www.runoob.com/python/file-readline.html)
- [python openfile](https://www.w3schools.com/python/python_file_open.asp)
- [python open preferred method](https://stackoverflow.com/questions/11555468/how-should-i-read-a-file-line-by-line-in-python)
- [python while loop](https://www.w3schools.com/python/python_while_loops.asp)
- [python write append mode](https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/)
- [encoding error](https://blog.csdn.net/lqzdreamer/article/details/76549256)
- [python line text split](https://www.w3schools.com/python/ref_string_split.asp)
- [python function syntax](https://www.w3schools.com/python/python_functions.asp)
- [python case syntax](https://cloud.tencent.com/developer/article/1540890)
- [python if syntax](https://www.w3schools.com/python/python_conditions.asp)
- [python dictionary](https://www.runoob.com/python/python-dictionary.html)
- [pypi pypinyin](https://pypi.org/project/pypinyin/)
- [text to dict](https://devenum.com/how-to-convert-text-file-to-a-dictionary-in-python/)
- [conda create python env](https://blog.csdn.net/lyy14011305/article/details/59500819)
- [pypinyin CSDN](https://cuiqingcai.com/6519.html)
- [flypy声母韵母对照](https://www.douban.com/note/720180447/?_i=01764579blmLOJ,01926889blmLOJ)  补充了个ve，否则报错。
- [notepad++转换格式](http://shouce.jb51.net/notepad_book/npp_func_windows_unix_mac.html)

## 其他

最后我把自己生成的gboard可以直接导入使用的压缩包放release，第一版，可能会有错误。
补充Rime支持，词库文件放release里，标签打第二版吧。
