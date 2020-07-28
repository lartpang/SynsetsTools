# SynsetsTools

## 简介

查询近义词反义词的网站<https://synsets.net>的一个工具集，后续还可能会继续更新。

网站简介：
> 使用同义词集查找同义词和反义词。还有68种更常见的语言，至少有10,000个词汇。
> 世界上大约90%的人口的母语或核心语言都被包含在这里。
> 这个列表还包括一些历史语言(如拉丁语)或构造语言(如世界语)。
> 我们的很多知识都来自互联网——免费的多语种词典。
> 这为我们提供了关于同义词、反义词、在数百种语言中概念的翻译，以及许多单词的多个标记词义的信息。

## 使用

* python==3.8.3
* requests==2.24.0

```shell script
$ python request_cli.py --help
usage: request_cli.py [-h] [-v] --lang {en,fr,it,de,es,ru,pt,nl,el,hu,pl,ro,sv,tr,uk,da,fi,no,et,cs,sl,zh,ja,ko,hi,bn,ar,fa,th,vi,ur} --word WORD

Request synsets.net from the command-line interface.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --lang {en,fr,it,de,es,ru,pt,nl,el,hu,pl,ro,sv,tr,uk,da,fi,no,et,cs,sl,zh,ja,ko,hi,bn,ar,fa,th,vi,ur}
                        the language you want to use
  --word WORD           the work you want to search

Enjoy the program! :)
```
