import main

# 新しい単語を辞書に追加
def add_new_word():
    main.load_wordbook()
    main.add_word()
    main.save_wordbook()

