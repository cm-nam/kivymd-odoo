from kivy.properties import ObjectProperty
from pages.base import BaseScreen
from kivy.clock import Clock
import requests
from requests.auth import HTTPBasicAuth
from common import save_pickle_data

class PageLogin(BaseScreen):
    email = ObjectProperty()
    password = ObjectProperty()

    def set_focus(self, *args):
        self.email.focus = True

    def on_enter(self, *args):
        Clock.schedule_once(self.set_focus)

    def login_user(self):
        req = requests.post("http://192.168.1.55:8000/auth/", auth=HTTPBasicAuth(self.email.text, self.password.text))
        if req.status_code == 200:
            json = req.json()
            self.root_nav.token = json['access_token']
            self.root_nav.to_page("screen_inicio")
            self.root_nav.enable_drawer()

    def enable_menu(self, *args):
        menu = ["menu", lambda x: self.root_nav.toggle_nav_drawer()]
        self.root_nav.ids.toolbar.left_action_items.append(menu)