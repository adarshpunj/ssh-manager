import json

class Preferences(dict):__getattr__ = dict.get

with open('./preferences.json','r') as f:
    __preferences__ = Preferences(json.load(f))