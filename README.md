# A Tool of copying data to notion database easily

## **requirements:** \
keyboard           0.13.5 \
pyperclip          1.8.2 \
PyYAML             6.0 \
requests           2.28.1 \
win10toast         0.9

## **usage:**  \
1. read https://developers.notion.com/docs/getting-started and get your integration work on your notion database.
2. continue to get your page_id
3. make a config.yaml in the project's folder, its context likes:
```
notion:
  token: "your_integration_secret_token"
  page_id: "your page id"
  database_id: "your database id"
  blocks_id: "your blocks_id(always same as page id)"
  version: !!str 2022-06-28
```
4. run s2c.py. Broswer and copy(ctrl+c) the text your want to save. Then press alt+2 to send it. A windows notification will display for a while.