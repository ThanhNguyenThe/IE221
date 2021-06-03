from operator import attrgetter, itemgetter
from pygame import key, time
import json, os

def top3():
    """sort top3 người chơi pro nhất."""
    with open(os.path.join("data", "data.txt"), 'r') as file_in:
        lst = []
        for line in file_in:
            lst.append(line.rstrip())
    list = [json.loads (s) for s in lst]
    list.sort(key=lambda x: x[1])
    return list[0:3]

#mở file và sort top 3