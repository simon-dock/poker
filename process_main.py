import common_function as com
import process_commons as com_process

def manage(raund_name, cip_data, cip_index, name_data, players_number, dealer, now_player):

    cip_data, cip_index = com.full_not_played(cip_data, cip_index, dealer)

    max_bet = 0
    now_bet = 0
    past_bet = 0
    counting = 0
    Redo_Flag = True
    Fold_Flag = com.check_fold(cip_data, cip_index, now_player)
    while(Redo_Flag):

        #前半の処理
        now_bet = com_process.first_half(Fold_Flag, name_data, cip_data, cip_index, now_player, max_bet, past_bet)

        #後半の処理
        Fold_Flag, Redo_Flag, cip_data, cip_index, now_player, max_bet, past_bet = com_process.second_half(raund_name, cip_data, cip_index, now_player, players_number, max_bet, now_bet, past_bet)

        #全員チェックするまでは回す
        if counting < players_number-1 and max_bet == 0:
            counting += 1
            Redo_Flag = True

    #ラウンド最後の処理
    cip_data, cip_index = com_process.mark_fold(cip_data, cip_index, players_number, now_player)

    return cip_data, cip_index