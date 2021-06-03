import json, os

def saveInfo(name, time):
    """Lưu tên, thời gian phá đảo."""
    with open(os.path.join("data", "data.txt"), 'a') as file:
        data = (name, time)
        json.dump(data, file)
        file.write('\n')

#viết info vào file text