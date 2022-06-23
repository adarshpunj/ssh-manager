from setuptools import setup

APP = ['app.py']
DATA_FILES = ['preferences.json','utils.py']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'ssh-manager.icns',
    'plist': {
        'CFBundleShortVersionString': '1.0.0',
        'LSUIElement': True,
    },
    'packages': ['rumps']
}

setup(
    app=APP,
    name='SSH Manager',
    py_modules=['utils'],
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['rumps']
)
