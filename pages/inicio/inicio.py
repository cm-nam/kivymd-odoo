from pages.base import BaseScreen

from kivymd.uix.list import OneLineListItem
import requests

class PageInicio(BaseScreen):
    def on_enter(self, *args):
        headers = {"Authorization": f"Bearer {self.root_nav.token}"}
        req = requests.get("http://192.168.1.55:8000/res.users/", headers=headers)
        json = req.json()
        for user in json['data']:
            item = OneLineListItem(text=user['name'])
            self.ids.list.add_widget(item)