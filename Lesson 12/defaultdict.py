# d = {"apple": 1, "banana": 23, "cherry": 4}

# print(d["orange"])
from collections import defaultdict

# it performs the same as the ordinary dict, but it won't crash if key doesn't exit
d = defaultdict(str)
d["apple"] = 1
d["banana"] = 23
d["cherry"] = 4
print(d["orange"])

