def input_particpants_number():#参加者の人数を入力する
    Correct_Flag = True

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box.isnumeric():
            participants_number = int(tmp_box)
            Correct_Flag = False
        else:
            print("Please enter the number.")

    print("The number entered is ",participants_number)
