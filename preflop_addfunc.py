import common_function as com

#ポジションを設定する
def set_position(cip_data, cip_index, name_data, sb_value, players_number, dealer):

    print("Dealer Button is ",name_data[dealer])

    sb_player, cip_data, cip_index = com.process_next_index(players_number, dealer, cip_data, cip_index)
    print("Small  Blind  is ",name_data[sb_player])
    cip_data[cip_index][com.cast_cip(sb_player)] = sb_value

    bb_player, cip_data, cip_index = com.process_next_index(players_number, sb_player, cip_data, cip_index)
    print("Big    Blind  is ",name_data[bb_player])
    print("")
    cip_data[cip_index][com.cast_cip(bb_player)] =  sb_value*2

    now_player, cip_data, cip_index = com.process_next_index(players_number, bb_player, cip_data, cip_index)

    return now_player, sb_player, bb_player, cip_data, cip_index 


#preflop独自の処理　誰もレイズせず、はじめてbbの番になった場合　レイズかチェックか選べる
def check_bb_raise(First_Flag, Redo_Flag, cip_data, cip_index, players_number, bb_player, now_player):

    if bb_player == now_player and Redo_Flag == False and First_Flag == True:
        First_Flag = False
        Redo_Flag = True
        Redo_Flag = check_survive(Redo_Flag, cip_data, cip_index, players_number, now_player)

    return First_Flag, Redo_Flag


def check_survive(Redo_Flag, cip_data, cip_index, players_number, now_player):
   
    fold_count = 0

    while(1):
        
        now_player -= 1
        if now_player == -1:
            now_player = players_number-1
            cip_index -= 1

        if cip_data[cip_index][com.cast_cip(now_player)] == -1:
            fold_count += 1
        else:
            break

        if fold_count == players_number-1:
            Redo_Flag = False
            break

    return Redo_Flag
