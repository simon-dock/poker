import functions as funcs

def main():

    #プログラムの起動メッセージ
    funcs.display_massege_start() 

    #参加者のデータリストを作成
    name_data = funcs.make_players_data()

    #ゲームの設定を行う
    funcs.make_game_setting()

    #ポーカーの管理をする
    funcs.manage_poker(name_data)

    #戦績を精算
    # calculate_result()

    #結果を表示する
    # display_result()

    #結果をテキストファイルに出力する
    # export_result()

if __name__ == '__main__':
    main()