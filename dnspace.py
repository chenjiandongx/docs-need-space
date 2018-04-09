#!/usr/bin/env python
# coding=utf-8

import os
import re
import argparse
import codecs

__VERSION__ = "0.1.0"


def get_parser():
    """
    解析命令行参数
    """
    parser = argparse.ArgumentParser(description="docs need space")
    parser.add_argument(
        "docs",
        metavar="DOCS",
        type=str,
        help="The docs you want to add a space",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="output file. default(cover input file)",
    )
    parser.add_argument(
        '-v',
        '--version',
        action='store_true',
        help='displays the current version of `space`')
    return parser


def command_line_runner():
    """
    执行命令行操作
    """
    parser = get_parser()
    args = vars(parser.parse_args())
    if args["version"]:
        print(__VERSION__)
        return

    if not args["docs"]:
        parser.print_help()
        return
    add_space(args["docs"], args["output"])


def add_space(docs, output=None):
    """
    中英之间新增空格

    :param docs: 操作文档
    """
    if os.path.exists(docs):
        _left = re.compile(r"([a-zA-Z0-9)])([\u4e00-\u9fa5])")
        _right = re.compile(r"([\u4e00-\u9fa5])([a-zA-Z0-9\[])")
        with codecs.open(docs, "r", encoding="utf-8") as f:
            result = re.sub(
                _right, r"\1 \2", re.sub(_left, r"\1 \2", f.read())
            )
        if output is None:
            output = docs
        with codecs.open(output, 'w+', encoding="utf-8") as f:
            f.write(result)

    else:
        raise OSError("File does not exist!")


if __name__ == "__main__":
    command_line_runner()
