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
#次の添字にアクセスする
def process_next_index(player_number, now_index, cip_index):
    next_index = now_index + 1
    if next_index == player_number:
        cip_index += 1
        next_index = 0

    return next_index, cip_index

#cip_dataの第二引数に入れるために変換する
def cast_cip(index):
    index += 1
    return index

#現在のラウンドの掛け金を求める
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