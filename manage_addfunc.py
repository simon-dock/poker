from cgitb import small
import random

#ディーラーボタンをランダムで決定する
def select_dealerbutton(players_number, name_data):

    dealer = random.randrange(players_number)

    return dealer

#プリフロップの処理を行う

def process_preflop(cip_data, name_data, player_number, dealer):

    print("--------------------")
    print("Now it's Preflop.")

    print("The Dealer Button is ",name_data[dealer])

    small_blind = dealer + 1
    if small_blind == player_number:
        small_blind = 0
    print("The Small  Blind  is ",name_data[small_blind])
    big_blind = small_blind + 1
    if big_blind == player_number:
        big_blind = 0
    print("The Big    Blind  is ",name_data[big_blind])