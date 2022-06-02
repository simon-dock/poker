import common_function as com

#前半の処理
#フォールドしていなければ
#・データの表示
#・入力受付、格納
def first_half(Fold_Flag, name_data, cip_data, cip_index, now_player, max_bet, past_bet):

    if Fold_Flag == False:
            print("Now    Player is ",name_data[now_player])
            print("You are betting $",past_bet)
            print("Max bet is $",max_bet)

            now_bet = com.check_data_int()
            cip_data[cip_index][com.cast_cip(now_player)] = now_bet

    return now_bet