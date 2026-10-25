import json, re

def put(f, d): # file, data
  with open(f, "w") as t: # template
    json.dump(d, t, indent=2); t.close()

ws, exp = {}, r"\b\w+(?:['’_-]*\w+)*\b" # words, regular expression

with open("essay.txt", "r") as e: # essay
  lw = re.findall(exp, e.read().lower()); e.close() # listed words

for k in lw: # key
  if not k in ws.keys():
    ws[k] = lw.count(k)
    lw = [w for w in lw if w != k] # word

ws = {k: ws[k] for k in sorted(ws)}
put("words.json", ws)

ws = {k: ws[k] for k in sorted(ws, key=ws.get, reverse=True)}
put("counted_words.json", ws)

# time to complete -> 1:08:46.65
# date and time of official completion -> 2026-10-25 22:50:39.272880
# 21 lines of code
# 476 characters

''' #AI's model code (just for comparison)

import json, re

def put(f, d):
  with open(f, "w") as t:
    json.dump(d, t, indent=2)

exp = r"\b\w+(?:['’_-]\w+)*\b"
with open("essay.txt", "r") as e:
  lw = re.findall(exp, e.read().lower())

ws = {w: lw.count(w) for w in set(lw)}

sort_abc = {k: ws[k] for k in sorted(ws)}
put("words.json", sort_abc)

sort_freq = {k: ws[k] for k in sorted(ws, key=ws.get, reverse=True)}
put("counted_words.json", sort_freq)

# 17 lines of code
# 412 characters

'''