#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MeCab
import sys

str = sys.argv[1]
mecab = MeCab.Tagger("mecabrc")
mecab.parse("")

# MeCabを使って形態素解析を行い、名詞と分かっている単語を文章中から二つ抜き出す
# 後に、それら名詞と文章全体を照らし合わせる作業を行う
def ma_parse(sentence, filter="名詞"):
  node = mecab.parseToNode(sentence)
  while node:
    if node.feature.startswith(filter):
      yield node.surface
    node = node.next

if __name__ == "__main__":
  num = 0
  for word in ma_parse(str):
      if (num > 2):
          break
      print(word)
      num += 1
