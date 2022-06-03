import common_function as com
import numpy as np

#前半の処理
def first_half(Fold_Flag, name_data, cip_data, cip_index, now_player, max_bet, past_bet):

    #フォールドしていなければ
    now_bet = -1
    if Fold_Flag == False:

        #データの表示
        print("Now    Player is ",name_data[now_player])
        print("You are betting $",past_bet)
        print("Max bet is $",max_bet)
        
        #入力受付、格納
        now_bet = com.check_data_what()

    print(now_bet)
    cip_data[cip_index][com.cast_cip(now_player)] = now_bet
    
    return now_bet

#後半の処理
def second_half(round_name, cip_data, cip_index, now_player, players_number, max_bet, now_bet, past_bet):

    #場の最大ベット額の更新
    max_bet = com.update_max_bet(max_bet, now_bet, past_bet)

    #次のプレイヤーの添字を取得
    now_player, cip_data, cip_index = com.process_next_index(players_number, now_player, cip_data, cip_index)

    #そのプレイヤーが前ラウンドフォールドしているかチェック
    Fold_Flag = com.check_fold(cip_data, cip_index, now_player)

    #そのプレイヤーの現在までのベット額を取得
    past_bet = com.sum_round_bet(round_name, cip_data, cip_index, now_player)
    
    #上の値が場の最大ベット額と同額であれば終了
    if past_bet == max_bet:
        Redo_Flag = False
    else:
        Redo_Flag = True

    return Fold_Flag, Redo_Flag, cip_data, cip_index, now_player, max_bet, past_bet


def mark_fold(cip_data, cip_index, players_number, now_player):

    if now_player != 0: 
        for i in range(now_player, players_number):
            if cip_data[cip_index-1][com.cast_cip(i)] == -1:
                cip_data[cip_index][com.cast_cip(i)] = -1
            else:
                cip_data[cip_index][com.cast_cip(i)] = 0

        cip_data, cip_index = com.add_cip_data(cip_data, cip_index, players_number)

    return cip_data, cip_index