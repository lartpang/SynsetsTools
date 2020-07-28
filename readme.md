# SynsetsTools

[[中文文档](./readme_zh.md)]

## Introduction

A toolkit for the site <https://synsets.net> that consults synonyms and antonyms and it will continue to be updated later.

Introduction to the website:
> Use synsets to find synonyms and antonyms.
> There are 68 more common languages, with vocabularies of at least 10,000 terms.
> About 90% of the world's population natively speaks one of these languages or the core languages.
> This list also includes some languages that are historical (such as Latin) or constructed (such as Esperanto).
> Much of our knowledge comes from the Internet, the free multilingual dictionary.
> This gives us information about synonyms, antonyms, translations of concepts into hundreds of languages, 
> and multiple labeled word senses for many words.

## Usage

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
