def enter_data_int():
    
    Correct_Flag = True

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box.isnumeric():
            value_int = int(tmp_box)
            Correct_Flag = False
        else:
            print("Please enter the number.")

    return value_int

def process_next_index(player_number, now_index, cip_index):
    next_index = now_index + 1
    if next_index == player_number:
        cip_index += 1
        next_index = 0

    return next_index, cip_index