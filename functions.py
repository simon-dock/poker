
def display_massege_start():#プログラムの起動メッセージ
    print("start Tool of Poker")


def make_entrant_list():#参加者のデータリストを作成
    pass


def manage_poker():#ポーカーの管理をする

    End_Flag = True
    data = []
    while(End_Flag):

        entered_char = input()
        print("The character entered is ",entered_char)
        data.append(entered_char)   

        if entered_char == "q":
            End_Flag = False

    print(data)


def calculate_result():#戦績を精算
    pass


def display_result():#結果を表示する
    pass


def export_reult():#結果をテキストファイルに出力する
    pass