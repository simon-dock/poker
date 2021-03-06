import common_function as com
import players_addfunc as add_play
import manage_addfunc as add_mana
import numpy as np
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

    sb_value = com.check_data_int()

    print("Small blind is ", sb_value)
    print("Game setup is finished.")
    print("")

    return sb_value

        
            

#ポーカーの管理をする
#cip_dataの中身
#データサイズ[]][参加人数＋１]
#[j][0]=1,プリフロップ、2,フロップ、3,ターン、4,リバーの開始を示す
#       次の0以外の数字が来るまでそのラウンド
#       5,[j][1]にそのゲームの勝者の添字が入ることを示す
#[j][1~n]=対応するプレイヤーの掛け金　０の場合チェックorフォールド
#データがない要素には0 読み出しは専用のプログラムを作成予定
#具体例 3人の場合
#[1, 1, 2, 2], [j][0]に１　ここからプリフロップ　sbが1 bbが2　buttonが2コール
#[0, 1, 2, -1], [j][0]に０　プリフロップのデータ　sbが1コール　bbが4にレイズ　buttonがフォールド
#[0, 2, 0, -1], [j][0]に０　プリフロップのデータ　sbが2コール　
#[2, 0, 0, -1], [j][0]に２　フロップのデータ sb bb　ともにチェック
#[3, 2, 2, -1], [j][0]に３　ターンのデータ　sbが2ベット　bbが2コール
#[4, 2, 4, -1],
#[0, 2, 0, -1],
#[5, 1, 0, 0], [j][0]に５　[j][1]に勝者の添字　つまり sbの勝ちだった
def manage_poker(name_data, sb_value):

    print("--------------------")
    print("GAME START")

    players_number = len(name_data)

    dealer = add_mana.select_dealerbutton(players_number, name_data)
    End_Flag = True
    cip_data = np.zeros([1,com.cast_cip(players_number)], dtype=np.int32)
    fold_count = 0
    cip_index = 0
    while(End_Flag):

        #プリフロップ
        cip_data, cip_index, sb_player = add_mana.process_preflop(cip_data, cip_index, name_data, sb_value, players_number, dealer)

        fold_count = com.count_fold(cip_data, cip_index, players_number)
        if fold_count < players_number-1:
            #フロップ
            cip_data, cip_index = add_mana.process_flop(cip_data, cip_index, name_data, players_number, dealer, sb_player)

        fold_count = com.count_fold(cip_data, cip_index, players_number)
        if fold_count < players_number-1:
            #ターン
            cip_data, cip_index = add_mana.process_turn(cip_data, cip_index, name_data, players_number, dealer, sb_player)

        fold_count = com.count_fold(cip_data, cip_index, players_number)
        if fold_count < players_number-1:
            #リバー
            cip_data, cip_index = add_mana.process_river(cip_data, cip_index, name_data, players_number, dealer, sb_player)
            
        fold_count = com.count_fold(cip_data, cip_index, players_number)
        if fold_count < players_number-1:
            #ショウダウン
            cip_data, cip_index = add_mana.process_showdwon(cip_data, cip_index, name_data, players_number)
        else:
            #最後まで降りなかった人が勝つ処理
            cip_data, cip_index = add_mana.process_survive(cip_data, cip_index, name_data, players_number)
        
        print("Enter C to continue or Q to stop.")
        entered_char = com.check_data_qc()

        if entered_char == "q":
            End_Flag = False

        dealer = com.process_next_dealer(dealer, players_number)

    print("--------------------")
    print("GAME OVER")

    return cip_data


#戦績を精算
def calculate_result(cip_data, name_data):
    print(name_data)
    print(cip_data)
    pass

#結果を表示する
def display_result():
    pass

#結果をテキストファイルに出力する
def export_reult():
    pass