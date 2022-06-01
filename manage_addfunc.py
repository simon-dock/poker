import common_function as com
import random

#ディーラーボタンをランダムで決定する
def select_dealerbutton(players_number, name_data):

    dealer = random.randrange(players_number)

    return dealer

#プリフロップの処理を行う

def process_preflop(cip_data, name_data, player_number, dealer):

    print("--------------------")
    print("Now it's Preflop.")
    print("")

    now_player = display_position(name_data, player_number, dealer)

    while(True):
        print("Now    Player is ",name_data[now_player])
        entered_char = com.enter_data_int()

        if entered_char == "q":
            End_Flag = False
    


#ポジションを表示する
def display_position(name_data, player_number, dealer):

    print("Dealer Button is ",name_data[dealer])

    small_blind = dealer + 1
    if small_blind == player_number:
        small_blind = 0
    print("Small  Blind  is ",name_data[small_blind])
    big_blind = small_blind + 1
    if big_blind == player_number:
        big_blind = 0
    print("Big    Blind  is ",name_data[big_blind])
    print("")

    now_player = big_blind + 1
    if now_player == player_number:
        now_player = 0

    return now_player
