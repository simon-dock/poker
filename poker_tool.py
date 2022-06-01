
def main():

    End_Flag = True

    print("start Tool of Poker")

    # make_entrant_list() 参加者のデータリストを作成
    data = []

    # manage_poket()　ポーカーの管理をする

    while(End_Flag):

        entered_char = input()
        print("The character entered is ",entered_char)
        data.append(entered_char)
         
        # make        

        if entered_char == "q":
            End_Flag = False

    # calculate_result() 戦績を精算する

    # display_result() 結果を表示する

    # export_reult() 結果をテキストファイルに出力する

    print(data)

if __name__ == '__main__':
    main()