import players_addfunc as add_play
import manage_addfunc as add_mana
import random

#プログラムの起動メッセージ
def display_massege_start():
    print("#####################")
    print("")
    print("start Tool of Poker")
    print("")
    print("#####################")
    print("")


#参加者のデータリストを作成する
def make_players_data():
    
    print("Set up the players.")

    Redo_Flag = True

    while(Redo_Flag):

        print("Enter the number of players.")

        players_number = add_play.input_players_number()

        name_data = add_play.input_players_name(players_number)

        Redo_Flag = add_play.confirm_players(name_data)

        if Redo_Flag == True:
            print("Redo the players settings.")

    print("Players setup is finished.")
    print("")

    return name_data


#ゲームの設定を行う
def make_game_setting():

    print("Set up the game.")
    print("Enter the amount for small blind.")

    Correct_Flag = True

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box.isnumeric():
            small_blind = int(tmp_box)
            Correct_Flag = False
        else:
            print("Please enter the number.")

    print("Small blind is ", small_blind)
    print("Game setup is finished.")
    print("")

    return small_blind

        
            

#ポーカーの管理をする
#1 2 0 2 4 4
#0 2 0 0

#0 1 2 2 2 0
#2 2 
def manage_poker(name_data, small_blind):

    print("GAME START")

    players_number = len(name_data)

    dealer = add_mana.select_dealerbutton(players_number, name_data)

    End_Flag = True
    cip_data = []
    data = []
    while(End_Flag):

        #プリフロップ
        #pre-flop()

        #フロップ
        #flop()

        #ターン
        #turn()

        #リバー
        #river()

        entered_char = input()
        print("The character entered is ",entered_char)
        data.append(entered_char)   

        if entered_char == "q":
            End_Flag = False

    print(data)

#戦績を精算
def calculate_result():
    pass

#結果を表示する
def display_result():
    pass

#結果をテキストファイルに出力する
def export_reult():
    pass