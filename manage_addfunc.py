import common_function as com
import random

PREFLOP = 1

#ディーラーボタンをランダムで決定する
def select_dealerbutton(players_number, name_data):

    dealer = random.randrange(players_number)

    return dealer

#プリフロップの処理を行う

def process_preflop(cip_index, cip_data, name_data, sb_value, player_number, dealer):

    print("--------------------")
    print("Now it's Preflop.")
    print("")

    now_player, cip_index, cip_data = set_position(cip_index, cip_data, name_data, sb_value, player_number, dealer)
    print(name_data)
    print(cip_data)
    while(True):
        print("Now    Player is ",name_data[now_player])
        now_bet = com.sum_round_bet(PREFLOP, cip_data, cip_index, now_player)
        print("Betting $",now_bet)
        number_cip = com.check_data_int()
        cip_data[cip_index][com.cast_cip(now_player)] = number_cip
        now_player, cip_index = com.process_next_index(player_number, now_player, cip_index)
        if cip_index == 4:
            break

    print(cip_data)

#ポジションを設定する
def set_position(cip_index, cip_data, name_data, sb_value, player_number, dealer):

    print("Dealer Button is ",name_data[dealer])

    small_blind, cip_index = com.process_next_index(player_number, dealer, cip_index)
    print("Small  Blind  is ",name_data[small_blind])
    cip_data[cip_index][0] = PREFLOP
    cip_data[cip_index][com.cast_cip(small_blind)] = sb_value

    big_blind, cip_index = com.process_next_index(player_number, small_blind, cip_index)
    print("Big    Blind  is ",name_data[big_blind])
    print("")
    cip_data[cip_index][com.cast_cip(big_blind)] =  sb_value*2

    now_player, cip_index = com.process_next_index(player_number, big_blind, cip_index)

    return now_player, cip_index, cip_data 

