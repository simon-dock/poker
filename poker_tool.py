import functions as func

def main():

    #プログラムの起動メッセージ
    func.display_massege_start() 

    #参加者のデータリストを作成
    func.make_players_data()

    #ポーカーの管理をする
    func.manage_poker()

    #戦績を精算
    # calculate_result()

    #結果を表示する
    # display_result()

    #結果をテキストファイルに出力する
    # export_reult()

if __name__ == '__main__':
    main()