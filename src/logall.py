import requests
import json
from datetime import datetime
import re

history_url = "https://slack.com/api/channels.history"
users_url = "https://slack.com/api/users.list"
token = "token"
users_token = "token"
channel_id = "channel id"

def getUsers():
    payload = {
        "token": users_token
    }
    response = requests.get(users_url, params=payload)
    json_data = response.json()
    users = json_data["members"]
    usersMap = {}
    userNamesMap = {}
    for i in users:
        usersMap[i["id"]] = i["real_name"]
        userNamesMap[i["real_name"]] = i["name"]
    return usersMap, userNamesMap
def main():
    payload = {
        "token": token,
        "channel": channel_id
        }
    response = requests.get(history_url, params=payload)
    json_data = response.json()
    messages = json_data["messages"]
    usersList, userNamesList = getUsers()
    count = 0
    list = []
    for i in messages:
        parseFloat = float(i["ts"])
        time = datetime.fromtimestamp(parseFloat)
        count += 1
        nl = "\n"
        with open('out.txt', mode='a') as f:
            f.write(('【No.】' + str(count)) + nl)
            f.write('【USER ID】' + i["user"] + nl)
            f.write('【DISPLAY NAME】' + str(usersList[i["user"]]).replace("[", "").replace("]", "") + nl)
            f.write('【ACCOUNT ID】' + str(userNamesList[str(usersList[i["user"]])]) + nl)
            f.write('【DATE】' + str(time) + nl)
            f.write('【MESSAGES】' + i["text"] + nl)
            f.write('--------------------------------------------------------------------------------' + nl)
        with open("raw.txt", mode="a") as f:
if __name__ == '__main__':
    main()