import requests
import time
from collections import Counter
import json


numbers = "1234567890 "
for i in numbers:
  for j in numbers:
    for k in numbers:
      for l in numbers:
        for m in numbers:
          for n in numbers:
            for o in numbers:
              for p in numbers:
                id = i + j + k + l + m + n + o + p
                try:
                  req = requests.get(f"https://api.scratch.mit.edu/studios/{id}").json()
                  json.dumps(req)
                  time.sleep(0.5)
                  title = req['title']
                  desc = req['description']
                  cnt = Counter()
                  words = desc.split()
                  for word in words:
                    cnt[word]
                  file = open("data.json", "a")
                  res = {"title": title, "keywords": cnt}
                  file.write(res)
                  file.close()
                  print(res)
                except:
                  print(f"{id} isn't on Scratch")
