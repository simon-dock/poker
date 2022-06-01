import addition_participants as ad_par

def display_massege_start():#プログラムの起動メッセージ
    print("#####################")
    print("")
    print("start Tool of Poker")
    print("")
    print("#####################")
    print("")

def make_participants_data():#参加者のデータリストを作成
    
    print("Set up the participants.")
    print("Please enter the number of participants.")

    ad_par.input_particpants_number()


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