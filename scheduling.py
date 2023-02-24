import main
import schedule
import requests
import random
import datetime
from time import sleep

def schedule_task():
    # スケジュール登録（毎日0時に実行）
    schedule.every().day.at('00:00:00').do(main.send_word)

    while True:
        schedule.run_pending()
        sleep(1)
