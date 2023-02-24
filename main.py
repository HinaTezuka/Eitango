import pandas as pd
import os
import requests
import random
import datetime
import schedule

# LINE NotifyのURL/トークン
url = "https://notify-api.line.me/api/notify"
token = "ix4qUjCubaFBoDIWkjekWhscIIwN0rCC4SlJnf4x1l9"

# デスクトップのパスを取得する
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# 単語帳辞書
wordbook = {}

# 新しい単語と意味を辞書に追加する関数
def add_word():
    word = input("英単語を入力してください: ")
    meaning = input("その単語の意味を入力してください: ")
    wordbook[word] = meaning
    print(f"{word}を辞書に追加しました。")

# 単語帳をCSVファイルに書き込む関数
def save_wordbook():
    df = pd.DataFrame.from_dict(wordbook, orient='index', columns=['意味'])
    file_path = os.path.join(desktop_path, 'wordbook.csv')  # ファイルパスをDesktopに設定する
    df.to_csv(file_path, encoding='utf_8_sig')
    print("単語帳を保存しました。")

# 単語帳をCSVファイルから読み込む関数
def load_wordbook():
    global wordbook
    try:
        file_path = os.path.join(desktop_path, 'wordbook.csv')  # ファイルパスをDesktopに設定する
        df = pd.read_csv(file_path, index_col=0)
        wordbook = df.to_dict()['意味']
        print("単語帳を読み込みました。")
    except FileNotFoundError:
        print("単語帳が存在しません。")
        

# 毎日0時に2つの英単語をLINEに送信する関数
def send_word():
    now = datetime.datetime.now()
    # if now.hour == 2 and now.minute == 4:
    words = random.sample(list(wordbook.keys()), 2)
    word_url1 = f'https://ejje.weblio.jp/content/{words[0]}'
    word_url2 = f'https://ejje.weblio.jp/content/{words[1]}'
    message = f"今日の英単語は {words[0]} と {words[1]} だよ!\n" + f"{words[0]}の意味は" + word_url1 + " " + f"{words[1]}の意味は" + word_url2
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'message': message}
    requests.post(url, headers=headers, params=payload) 

