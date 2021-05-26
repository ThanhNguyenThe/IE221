import json, os

def saveInfo(name, time):
    with open(os.path.join("data", "data.txt"), 'a') as file:
        data = (name, time)
        json.dump(data, file)
        file.write('\n')
