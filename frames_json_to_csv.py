#!/usr/bin/env python
import json, sys

loaded = json.load(open(sys.argv[1]))

cols = ['id']
i = 0

for frame in loaded['frames']:
    for key, value in frame.items():
        if key not in cols:
            cols.append(key)

print(",".join([str(s) for s in cols]))

for frame in loaded['frames']:
    i = i+1
    row = [0] * len(cols)
    row[0] = i
    for key, value in frame.items():
        row[cols.index(key)] = value
    print(",".join([str(s) for s in row]))

