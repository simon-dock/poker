from sympy import im
import common_function as com
import preflop_addfunc as add_pre
import process_commons as com_process
import process_main as main_process
import random
import numpy as np
PREFLOP = 1
FLOP = 2
TURN = 3
RIVER = 4

#ディーラーボタンをランダムで決定する
def select_dealerbutton(players_number, name_data):

    dealer = random.randrange(players_number)

    return dealer


#プリフロップの処理を行う
def process_preflop(cip_data, cip_index, name_data, sb_value, players_number, dealer):

    print("--------------------")
    print("Now it's Preflop.")
    print("")

    cip_data[cip_index][0] = PREFLOP

    cip_data, cip_index = com.full_not_played(cip_data, cip_index, dealer)

    now_player, sb_player, bb_player, cip_data, cip_index = add_pre.set_position(cip_data, cip_index, name_data, sb_value, players_number, dealer)
    
    #preflop固有の処理
    max_bet = sb_value*2
    First_Flag = True

    #共通の処理
    past_bet = 0
    Redo_Flag = True
    Fold_Flag = False
    while(Redo_Flag):
        #前半の処理
        now_bet = com_process.first_half(Fold_Flag, name_data, cip_data, cip_index, now_player, max_bet, past_bet)

        #後半の処理
        Fold_Flag, Redo_Flag, cip_data, cip_index, now_player, max_bet, past_bet = com_process.second_half(PREFLOP, cip_data, cip_index, now_player, players_number, max_bet, now_bet, past_bet)

        #preflop独自の処理
        First_Flag, Redo_Flag = add_pre.check_bb_raise(First_Flag, Redo_Flag, bb_player, now_player)

    #ラウンド最後の処理
    cip_data, cip_index = com_process.mark_fold(cip_data, cip_index, players_number, now_player)
    

    print(cip_data)

    return cip_data, cip_index, sb_player


#フロップの処理を行う
def process_flop(cip_data, cip_index, name_data, players_number, dealer, now_player):

    print("--------------------")
    print("Now it's Flop.")
    print("")

    cip_data[cip_index][0] = FLOP

    return main_process.manage(FLOP, cip_data, cip_index, name_data, players_number, dealer, now_player)
    


def process_turn(cip_data, cip_index, name_data, players_number, dealer, now_player):
    print("--------------------")
    print("Now it's Turn.")
    print("")

    cip_data[cip_index][0] = TURN

    return main_process.manage(TURN, cip_data, cip_index, name_data, players_number, dealer, now_player)
