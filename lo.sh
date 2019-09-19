#!/bin/sh

read -p '追加するログ: ' MESSAGE
python /Users/kei/business-git/git/original-logging/lo.py -m $MESSAGE
