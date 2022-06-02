import common_function as com
import random

#ディーラーボタンをランダムで決定する
def select_dealerbutton(players_number, name_data):

    dealer = random.randrange(players_number)

    return dealer

#プリフロップの処理を行う

def process_preflop(access_data, cip_data, name_data, sb_value, player_number, dealer):

    print("--------------------")
    print("Now it's Preflop.")
    print("")

    now_player, cip_data = set_position(access_data, cip_data, name_data, sb_value, player_number, dealer)
    print(name_data)
    print(cip_data)
    while(True):
        print("Now    Player is ",name_data[now_player])
        entered_char = com.enter_data_int()

        if entered_char == "q":
            End_Flag = False
    


#ポジションを設定する
def set_position(cip_index, cip_data, name_data, sb_value, player_number, dealer):

    print("Dealer Button is ",name_data[dealer])

    small_blind, cip_index = com.process_next_index(player_number, dealer, cip_index)
    print("Small  Blind  is ",name_data[small_blind])
    cip_data[cip_index][small_blind+1] = sb_value

    big_blind, cip_index = com.process_next_index(player_number, small_blind, cip_index)
    print("Big    Blind  is ",name_data[big_blind])
    print("")
    cip_data[cip_index][big_blind+1] =  sb_value*2

    now_player, cip_index = com.process_next_index(player_number, big_blind, cip_index)

    return now_player, cip_data
