#!/usr/bin/env python
# -*- coding: utf-8 -*-
import CaboCha
import sys

noun1 = [sys.argv[1]]
noun2 = [sys.argv[2]]
nouns = noun1 + noun2
if nouns[1] == 'No-Text-Found':
    del nouns[1]
sentence = sys.argv[3]

def get_word(tree, chunk):
    surface = ''
    for i in range(chunk.token_pos, chunk.token_pos + chunk.token_size):
        token = tree.token(i)
        features = token.feature.split(',')
        if features[0] == '名詞':
            surface += token.surface
        elif features[0] == '形容詞':
            surface += features[6]
            break
        elif features[0] == '動詞':
            surface += features[6]
            break
    return surface

# 主語と述語を取り出す
def get_subject_and_object(line):
    cp = CaboCha.Parser('-f1')
    tree = cp.parse(line)
    chunk_dic = {}
    chunk_id = 0
    for i in range(0, tree.size()):
        token = tree.token(i)
        if token.chunk:
            chunk_dic[chunk_id] = token.chunk
            chunk_id += 1

    tuples = []
    for chunk_id, chunk in chunk_dic.items():
        if chunk.link > 0:
            from_surface =  get_word(tree, chunk)
            to_chunk = chunk_dic[chunk.link]
            to_surface = get_word(tree, to_chunk)
            tuples.append((from_surface, to_surface))
    return tuples

# 主語-述語、主語-動詞など、文章構造における様々なパターンを取り出す
if __name__ == '__main__' :
    tuples = get_subject_and_object(sentence)
    for t in tuples:
        for noun in nouns:
            try:
                t.index(noun)
                print(t[0])
                print(t[1])
            except ValueError:
                next
