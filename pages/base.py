from kivy.uix.screenmanager import Screen
from kivy.app import App

class BaseScreen(Screen):
    @property
    def root_nav(self):
        return App.get_running_app().root

    def logout(self, *args):
        self.root_nav.ids.toolbar.left_action_items = []
        self.root_nav.to_page("screen_login")