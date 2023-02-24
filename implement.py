import main
import scheduling
import add

def implement_main():
    # main.add_word()  # 英単語を入力してください: 
    #                  # その単語の意味を入力してください:
    #                  # appleを辞書に追加しました。
    main.save_wordbook()  # 単語帳を保存しました。
    main.load_wordbook()
    main.send_word()

def implement_scheduling():
    main.load_wordbook()
    scheduling.schedule_task()

def implement_add_new_word():
    main.load_wordbook()
    add.add_new_word()

def implement(option):
    if option == 'imp':
        implement()
    elif option == 'sche':
        implement_scheduling()
    elif option =='add':
        implement_add_new_word()

implement('sche')
# implement('add')

