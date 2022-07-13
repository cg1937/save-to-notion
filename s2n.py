from time import sleep
import requests
import pyperclip
from win10toast import ToastNotifier
from datetime import datetime
import keyboard
import yaml

# use yaml package to parse the config.yml
with open('config.yml', 'r') as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.FullLoader)

TOKEN = config['notion']['token']
notion_version = config['notion']['version']
blocks_id = config['notion']['blocks_id']


headers = {
    'Authorization': 'Bearer ' + TOKEN,
    'Content-Type': 'application/json',
    'Notion-Version': notion_version,
}


def get_clipboard_data():
    return pyperclip.paste()


def show_notification(title, msg):
    toast = ToastNotifier()
    toast.show_toast(title, msg, duration=2, threaded=True)


def save2notion(clip_text):
    json_data = {
        'children': [
            {
                'object': 'block',
                'type': 'paragraph',
                'paragraph': {
                    'rich_text': [
                        {
                            'type': 'text',
                            'text': {
                                'content': clip_text,
                            },
                        },
                    ],
                },
            }
        ],
    }
    response = requests.patch(
        'https://api.notion.com/v1/blocks/' + blocks_id + '/children', headers=headers, json=json_data)
    print(response)


def auto_function():
    """ One of your functions to be executed by a combination """
    print('Simulate Ctrl C')
    sleep(0.1)
    print('get clipboard data')
    clip_text = get_clipboard_data()
    print(clip_text)
    clip_text += ' ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('save to notion')
    save2notion(clip_text)
    show_notification('Clipboard', 'Saved to Notion Successfully')


if __name__ == '__main__':
    keyboard.add_hotkey('alt+2', auto_function)
    keyboard.wait()
