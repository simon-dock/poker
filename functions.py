import addition_participants as ad_par

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
        
        players_number = ad_par.input_players_number()

        name_data = ad_par.input_players_name(players_number)

        Redo_Flag = ad_par.confirm_players(name_data)

        if Redo_Flag == True:
            print("Redo the players settings.")
        
            

#ポーカーの管理をする
def manage_poker():
    End_Flag = True
    data = []
    while(End_Flag):

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