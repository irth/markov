#!/usr/bin/env python3
import json
import pathlib
import random
import sys

counts_file = pathlib.Path(sys.argv[1])
length = int(sys.argv[2])

with counts_file.open() as f:
    counts = json.load(f)

words = []

words.append(random.choice(list(counts.keys())))

while len(words) < length:
    possibilities = []
    weights = []

    for word, weight in counts[words[-1]].items():
        possibilities.append(word)
        weights.append(weight)


    choice = random.choices(possibilities, weights=weights, k=1)
    if choice[0] == "@@STOP@@":
        break
    words.append(choice[0])

print(" ".join(words))

    
