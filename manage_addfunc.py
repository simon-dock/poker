from ast import Raise
from unicodedata import name
import common_function as com
import random

PREFLOP = 1

#ディーラーボタンをランダムで決定する
def select_dealerbutton(players_number, name_data):

    dealer = random.randrange(players_number)

    return dealer

#プリフロップの処理を行う

def process_preflop(cip_data, cip_index, name_data, sb_value, player_number, dealer):

    print("--------------------")
    print("Now it's Preflop.")
    print("")

    now_player, bb_player, cip_data, cip_index = set_position(cip_data, cip_index, name_data, sb_value, player_number, dealer)
    max_bet = sb_value*2
    past_bet = 0
    Redo_Flag = True
    First_Flag = True
    Fold_Flag = False
    while(Redo_Flag):
        #前半の処理
        #フォールドしていなければ
        #・データの表示
        #・入力受付、格納
        if Fold_Flag == False:
            print("Now    Player is ",name_data[now_player])
            print("You are betting $",past_bet)
            print("Max bet is $",max_bet)

            now_bet = com.check_data_int()
            cip_data[cip_index][com.cast_cip(now_player)] = now_bet

        #後半の処理
        #・場の最大ベット額の更新
        #・次のプレイヤーの添字を取得
        #・そのプレイヤーが前ラウンドフォールドしているかチェック
        #・そのプレイヤーの現在までのベット額を取得
        #・上の値が場の最大ベット額と同額であれば終了
        #・プリフロップのbbだけが持つ特殊な処理
        max_bet = com.update_max_bet(max_bet, now_bet, past_bet)
        now_player, cip_index = com.process_next_index(player_number, now_player, cip_index)
        Fold_Flag = com.check_fold(cip_data, cip_index, now_player)
        past_bet = com.sum_round_bet(PREFLOP, cip_data, cip_index, now_player)
        if past_bet == max_bet:
            Redo_Flag = False
        if bb_player == now_player and Redo_Flag == False and First_Flag == True:
            First_Flag = False
            Redo_Flag = True
    print(name_data)

    for i in range(cip_index+1):
        print(cip_data[i])

#ポジションを設定する
def set_position(cip_data, cip_index, name_data, sb_value, player_number, dealer):

    print("Dealer Button is ",name_data[dealer])

    sb_player, cip_index = com.process_next_index(player_number, dealer, cip_index)
    print("Small  Blind  is ",name_data[sb_player])
    cip_data[cip_index][0] = PREFLOP
    cip_data[cip_index][com.cast_cip(sb_player)] = sb_value

    bb_player, cip_index = com.process_next_index(player_number, sb_player, cip_index)
    print("Big    Blind  is ",name_data[bb_player])
    print("")
    cip_data[cip_index][com.cast_cip(bb_player)] =  sb_value*2

    now_player, cip_index = com.process_next_index(player_number, bb_player, cip_index)

    return now_player, bb_player, cip_data, cip_index 

