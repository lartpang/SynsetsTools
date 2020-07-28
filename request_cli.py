# -*- coding: utf-8 -*-
# @Time    : 2020/7/23
# @Author  : Lart Pang
# @Email   : lartpang@163.com
# @File    : request_cli.py
# @Project : RequestSynsets
# @GitHub  : https://github.com/lartpang
from pprint import pprint

import requests
import argparse
import re
import json

LANGUAGES = [
    "en",
    "fr",
    "it",
    "de",
    "es",
    "ru",
    "pt",
    "nl",
    "el",
    "hu",
    "pl",
    "ro",
    "sv",
    "tr",
    "uk",
    "da",
    "fi",
    "no",
    "et",
    "cs",
    "sl",
    "zh",
    "ja",
    "ko",
    "hi",
    "bn",
    "ar",
    "fa",
    "th",
    "vi",
    "ur",
]

my_parser = argparse.ArgumentParser(
    description="Request synsets.net from the command-line interface.",
    epilog="Enjoy the program! :)",
    allow_abbrev=False,
)
my_parser.version = "1.0.0"
my_parser.add_argument("-v", "--version", action="version")
my_parser.add_argument(
    "--lang",
    type=str,
    default="en",
    choices=LANGUAGES,
    required=True,
    help="the language you want to use",
)
my_parser.add_argument(
    "--word",
    type=str,
    default="hello",
    required=True,
    help="the work you want to search",
)


def convert_answer_text_to_dict(answer_text: str) -> dict:
    key_list = re.findall(r"<b>(.+?)</b>", answer_text)
    value_list = re.findall(r"</b>(.+?)<br>", answer_text)
    key_list = [x.strip() for x in key_list]
    value_list = [x.strip() for x in value_list]
    return {k: v for k, v in zip(key_list, value_list)}


def main():
    args = my_parser.parse_args()
    target_url = f"https://synsets.net/{args.lang}/{args.word}.html?from=api"
    request_headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    }
    request_obj = requests.get(target_url, headers=request_headers, verify=False)
    html = request_obj.text
    useful_json_str = re.findall(
        r'<script type="application/ld\+json">([\s\S]*?)</script>', html
    )
    striped_json_str = re.sub(r"[\r\n\t]", "", useful_json_str[0])
    target_anwser_dict = json.loads(striped_json_str)

    for answer_dict in target_anwser_dict["mainEntity"]:
        test_to_dict = convert_answer_text_to_dict(
            answer_dict["acceptedAnswer"]["text"]
        )
        answer_dict["acceptedAnswer"].update({"text": test_to_dict})
    pprint(target_anwser_dict)


if __name__ == "__main__":
    main()
