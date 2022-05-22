#!/usr/bin/env python3
import json
import pathlib
import sys 

corpus_file = pathlib.Path(sys.argv[1])
output_file = pathlib.Path(sys.argv[2])

with corpus_file.open() as f:
    corpus = f.read()

previous_word = corpus[0]

counts = {}

for word in corpus.split():
    word = word.strip().lower()
    if previous_word not in counts:
        counts[previous_word] = {}
    if word not in counts[previous_word]:
        counts[previous_word][word] = 0
    counts[previous_word][word] += 1
    previous_word = word

with output_file.open('w') as f:
    json.dump(counts, f)

