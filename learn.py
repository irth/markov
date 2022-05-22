#!/usr/bin/env python3
import json
import pathlib
import sys 

corpus_file = pathlib.Path(sys.argv[1])
output_file = pathlib.Path(sys.argv[2])


corpus = []
with corpus_file.open() as f:
    for line in f.read().splitlines():
        for word in line.split():
            corpus.append(word.strip().lower())
        corpus += ["@@STOP@@"]

previous_word = corpus[0]

counts = {}

for word in corpus:
    if previous_word not in counts:
        counts[previous_word] = {}
    if word not in counts[previous_word]:
        counts[previous_word][word] = 0
    counts[previous_word][word] += 1
    previous_word = word

del(counts["@@STOP@@"])

with output_file.open('w') as f:
    json.dump(counts, f)

