import random

#ディーラーボタンをランダムで決定する
def select_dealerbutton(players_number, name_data):

    dealer = random.randrange(players_number)

    print("The first dealer button is ",name_data[dealer])

    return dealer

#プリフロップの処理を行う

def process_preflop(cip_data, name_data, dealer):

    print(cip_data)

    pass