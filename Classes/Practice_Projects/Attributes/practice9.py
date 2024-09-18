'''
Custom Fallback for Missing Attributes
Create a class Config with a method get_setting(). Use getattr() with a default value to retrieve a setting from the class,
returning 'Not Set' if the setting is missing.
'''
from executing.executing import get_setter


class Config:
    def __init__(self):
        self.setting_1 = 'enabled'
        self.setting_2 = 'disabled'

    def get_setting(self, setting_name):
        return getattr(self, setting_name, 'Not Set')

Conf = Config()
print(Conf.get_setting('setting_1'))
print(Conf.get_setting('setting_3'))
print(Conf.get_setting('setting_2'))
print(Conf.get_setting('setting_4'))
