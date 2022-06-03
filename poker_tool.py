import functions as funcs

def main():

    #プログラムの起動メッセージ
    funcs.display_massege_start() 

    #参加者のデータリストを作成
    name_data = funcs.make_players_data()

    #ゲームの設定を行う
    sb_value = funcs.make_game_setting()

    #ポーカーの管理をする
    cip_data = funcs.manage_poker(name_data, sb_value)

    #戦績を精算
    funcs.calculate_result(cip_data, name_data)

    #結果を表示する
    # display_result()

    #結果をテキストファイルに出力する
    # export_result()

if __name__ == '__main__':
    main()