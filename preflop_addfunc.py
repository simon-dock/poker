import common_function as com
PREFLOP = 1

#ポジションを設定する
def set_position(cip_data, cip_index, name_data, sb_value, players_number, dealer):

    print("Dealer Button is ",name_data[dealer])

    sb_player, cip_data, cip_index = com.process_next_index(players_number, dealer, cip_data, cip_index)
    print("Small  Blind  is ",name_data[sb_player])
    cip_data[cip_index][0] = PREFLOP
    cip_data[cip_index][com.cast_cip(sb_player)] = sb_value

    bb_player, cip_data, cip_index = com.process_next_index(players_number, sb_player, cip_data, cip_index)
    print("Big    Blind  is ",name_data[bb_player])
    print("")
    cip_data[cip_index][com.cast_cip(bb_player)] =  sb_value*2

    now_player, cip_data, cip_index = com.process_next_index(players_number, bb_player, cip_data, cip_index)

    return now_player, bb_player, cip_data, cip_index 