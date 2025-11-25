import os
import requests

class PushPlus:
    def __init__(self):
        self.token = os.environ.get("PUSHPLUS_TOKEN")

    def send(self, title, content):
        if not self.token:
            print("PushPlus token not found.")
            return
        
        url = "https://www.pushplus.plus/send"
        data = {
            "token": self.token,
            "title": title,
            "content": content,
            "template": "txt"
        }

        resp = requests.post(url, json=data)
        print("PushPlus response:", resp.text)
