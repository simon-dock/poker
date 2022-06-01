
def main():

    End_Flag = True

    print("start Tool of Poker")

    data = []

    while(End_Flag):

        entered_char = input()
        print("The character entered is ",entered_char)
        data.append(entered_char)
        

        if entered_char == "q":
            End_Flag = False

    print(data)

if __name__ == '__main__':
    main()