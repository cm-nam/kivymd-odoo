from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.base import EventLoop
from kivymd.uix.navigationdrawer import NavigationLayout

class MainNavigationLayout(NavigationLayout):
    _panel_disable = True
    token = None

    def to_page(self, page):
        self.ids.screen_manager.current = page

    def enable_drawer(self):
        self.ids.toolbar.left_action_items.append(['menu', lambda x: self.toggle_nav_drawer()])

class Main(MDApp):
    def __init__(self):
        MDApp.__init__(self)
        self.theme_cls.primary_palette = 'LightGreen'

    def on_start(self):
        EventLoop.window.bind(on_keyboard=self.hook_key)

    def hook_key(self, window, key, *args):
        if key == 27:
            self.root.ids.screen_manager.current = "screen_login"
            prev = self.root.ids["screen_manager"].current_screen
            print(prev)
            return True

Main().run()