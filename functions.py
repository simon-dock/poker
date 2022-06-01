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
    print("Enter the number of participants.")

    participants_number = ad_par.input_particpants_number()

    name_data = []

    for i in range(participants_number):
        if i == 0:
            print("Enter the name of the first person.")
        else:
            print("Eenter the name of the person to your left.")

        name = input()
        name_data.append(name)
    
    print(name_data)
            

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