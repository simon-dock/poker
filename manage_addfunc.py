import common_function as com
import preflop_addfunc as add_pre
import process_commons as com_process
import random
import numpy as np
PREFLOP = 1

#ディーラーボタンをランダムで決定する
def select_dealerbutton(players_number, name_data):

    dealer = random.randrange(players_number)

    return dealer


#プリフロップの処理を行う
def process_preflop(cip_data, cip_index, name_data, sb_value, players_number, dealer):

    print("--------------------")
    print("Now it's Preflop.")
    print("")

    now_player, bb_player, cip_data, cip_index = add_pre.set_position(cip_data, cip_index, name_data, sb_value, players_number, dealer)
    
    #preflop固有の処理
    max_bet = sb_value*2
    First_Flag = True

    #共通の処理
    past_bet = 0
    Redo_Flag = True
    Fold_Flag = False
    while(Redo_Flag):
        #前半の処理
        #フォールドしていなければ
        #・データの表示
        #・入力受付、格納
        now_bet = com_process.first_half(Fold_Flag, name_data, cip_data, cip_index, now_player, max_bet, past_bet)

        #後半の処理
        #・場の最大ベット額の更新
        #・次のプレイヤーの添字を取得
        #・そのプレイヤーが前ラウンドフォールドしているかチェック
        #・そのプレイヤーの現在までのベット額を取得
        #・上の値が場の最大ベット額と同額であれば終了
        #・プリフロップのbbだけが持つ特殊な処理
        max_bet = com.update_max_bet(max_bet, now_bet, past_bet)
        now_player, cip_data, cip_index = com.process_next_index(players_number, now_player, cip_data, cip_index)
        Fold_Flag = com.check_fold(cip_data, cip_index, now_player)
        past_bet = com.sum_round_bet(PREFLOP, cip_data, cip_index, now_player)
        if past_bet == max_bet:
            Redo_Flag = False

        if bb_player == now_player and Redo_Flag == False and First_Flag == True:
            First_Flag = False
            Redo_Flag = True

    if com.cast_cip(now_player) != 1:
        cip_index += 1
        new_array = np.zeros([1,com.cast_cip(players_number)], dtype=np.int32)
        cip_data = np.concatenate([cip_data, new_array])
    
    cip_data[cip_index][0] = -1

    for i in range(players_number):
        preflop_bet = com.sum_round_bet(PREFLOP, cip_data, cip_index, i)
        if preflop_bet != max_bet:
            cip_data[cip_index][com.cast_cip(i)] = -1

