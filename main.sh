#!/bin/bash

# 第一引数にディレクトリ名を入れる
DIR=${1}
if [ "$1" = "" ]
then
    echo "ディレクトリが選択されていません。"
    exit 1
fi

python3 ./${DIR}/code.py < ./${DIR}/input.txt
