import common_function as com


#参加者の人数を入力する
def input_players_number():

    players_number = com.check_data_int()

    print("The number entered is ",players_number)
    print("")

    return players_number

#参加者の名前を入力する　左隣の人の名前を入力していく
def input_players_name(players_number):

    name_data = []

    for i in range(players_number):
        if i == 0:
            print("Enter the name of the first person.")
        else:
            print("Eenter the name of the person to your left.")

        name = input()
        name_data.append(name)

    return name_data

#参加者の確認
def confirm_players(name_data):

    print("Please confirm the name you entered.")

    for i in range(len(name_data)):
        print(name_data[i])
    
    print("Is this correct? y/n")

    Correct_Flag = True
    Yes_Flag = True

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box == 'y':
            Correct_Flag = False
            Yes_Flag = False
        elif tmp_box == 'n':
            Correct_Flag = False
        else:
            print("Please enter y/n.")

    return Yes_Flag

