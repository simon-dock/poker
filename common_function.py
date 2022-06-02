import imp


import numpy as np

#入力されたデータがint型かチェックする
def check_data_int():
    
    Correct_Flag = True

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box.isnumeric():
            value_int = int(tmp_box)
            Correct_Flag = False
        else:
            print("Please enter the number.")

    return value_int

#場の最大ベット額を更新する
def update_max_bet(max_bet, now_bet, past_bet):
    
    if now_bet + past_bet > max_bet:
        max_bet = now_bet + past_bet
    
    return max_bet

#次の添字にアクセスする
def process_next_index(players_number, now_index, cip_data, cip_index):

    next_index = now_index + 1
    if next_index == players_number:
        cip_index += 1
        new_array = np.zeros([1,cast_cip(players_number)], dtype=np.int32)
        cip_data = np.concatenate([cip_data, new_array])
        next_index = 0

    return next_index, cip_data, cip_index

#cip_dataの第二引数に入れるために変換する
def cast_cip(index):
    index += 1
    return index

#now_playerの現在のラウンドまでの掛け金を求める
def sum_round_bet(round_name, cip_data, cip_index, now_player):

    begin_index = cip_index   
    while(1):
        if cip_data[begin_index][0] == round_name:
            break
        begin_index -= 1

    sum = 0

    for i in range(begin_index, cip_index+1):
        sum +=cip_data[i][cast_cip(now_player)]

    return sum

#前のフェイズにフォールドしているかチェックする
def check_fold(cip_data, cip_index, now_player):
    
    Fold_Flag = False

    if cip_data[cip_index][0] == 0:
        if cip_data[cip_index-1][cast_cip(now_player)] == 0:
            Fold_Flag = True
    #elif cip_data[cip_index][0] != 1:

    
    
    return Fold_Flag
