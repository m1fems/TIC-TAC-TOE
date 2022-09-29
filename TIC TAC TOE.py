# function printing the game field
def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


player1 = input("Player 1's name: ")
player2 = input("Player 2's name: ")

# the playing field
test_row1 = [" ", " ", " "]
test_row2 = [" ", " ", " "]
test_row3 = [" ", " ", " "]
# instructions to the players
print("Please pick a position TL(Top Left);TM(Top Middle);TR(Top Right);ML(Middle Left);C(Centre);MR(Middle Right);"
      "BL(Bottom Left);BM(Bottom Middle);BR(Bottom Right)")
# player1's wins counter
player1_wins = 0
# player2's wins
player2_wins = 0
play_again = " "
while play_again.upper() != "N":
    display(test_row1, test_row2, test_row3)
    # tie counter
    cnt = 0
    # game logic
    while True:
        while True:
            # player1's turn
            position_player1 = input(f"{player1} : ")
            if position_player1.upper() == "TL":
                if test_row1[0] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row1[0] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row1[0] = "X"
                    display(test_row1, test_row2, test_row3)
                    break
            elif position_player1.upper() == "TM":
                if test_row1[1] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row1[1] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row1[1] = "X"
                    display(test_row1, test_row2, test_row3)
                    break
            elif position_player1.upper() == "TR":
                if test_row1[2] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row1[2] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row1[2] = "X"
                    display(test_row1, test_row2, test_row3)
                    break
            elif position_player1.upper() == "ML":
                if test_row2[0] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row2[0] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row2[0] = "X"
                    display(test_row1, test_row2, test_row3)
                    break
            elif position_player1.upper() == "C":
                if test_row2[1] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row2[1] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row2[1] = "X"
                    display(test_row1, test_row2, test_row3)
                    break
            elif position_player1.upper() == "MR":
                if test_row2[2] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row2[2] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row2[2] = "X"
                    display(test_row1, test_row2, test_row3)
                    break
            elif position_player1.upper() == "BL":
                if test_row3[0] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row3[0] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row3[0] = "X"
                    display(test_row1, test_row2, test_row3)
                    break
            elif position_player1.upper() == "BM":
                if test_row3[1] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row3[1] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row3[1] = "X"
                    display(test_row1, test_row2, test_row3)
                    break
            elif position_player1.upper() == "BR":
                if test_row3[2] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row3[2] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row3[2] = "X"
                    display(test_row1, test_row2, test_row3)
                    break
            else:
                print("Wrong input")
                pass
        if (test_row1[0] == "X" and test_row1[1] == "X" and test_row1[2] == "X") or (
                test_row2[0] == "X" and test_row2[1] == "X" and test_row2[2] == "X") or (
                test_row3[0] == "X" and test_row3[1] == "X" and test_row3[2] == "X") or (
                test_row1[0] == "X" and test_row2[1] == "X" and test_row3[2] == "X") or (
                test_row1[0] == "X" and test_row2[0] == "X" and test_row3[0] == "X") or (
                test_row1[1] == "X" and test_row2[1] == "X" and test_row3[1] == "X") or (
                test_row1[2] == "X" and test_row2[2] == "X" and test_row3[2] == "X") or (
                test_row1[2] == "X" and test_row2[1] == "X" and test_row3[0] == "X"):
            print(f"{player1} WON")
            player1_wins += 1
            break
        # tie checker
        for a in range(len(test_row1)):
            if test_row1[a] == "X" or test_row1[a] == "O":
                cnt += 1
            else:
                cnt += 0
        for b in range(len(test_row2)):
            if test_row2[b] == "X" or test_row2[b] == "O":
                cnt += 1
            else:
                cnt += 0
        for c in range(len(test_row3)):
            if test_row3[c] == "X" or test_row3[c] == "O":
                cnt += 1
            else:
                cnt += 0
        if cnt == 45:
            print("TIE")
            break
        elif cnt != 45:
            pass
        # player2's turn
        while True:
            position_player2 = input(f"{player2} : ")
            if position_player2.upper() == "TL":
                if test_row1[0] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row1[0] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row1[0] = "O"
                    display(test_row1, test_row2, test_row3)
                    break
            elif position_player2.upper() == "TM":
                if test_row1[1] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row1[1] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row1[1] = "O"
                    display(test_row1, test_row2, test_row3)
                    break
            elif position_player2.upper() == "TR":
                if test_row1[2] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row1[2] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row1[2] = "O"
                    display(test_row1, test_row2, test_row3)
                    break
            elif position_player2.upper() == "ML":
                if test_row2[0] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row2[0] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row2[0] = "O"
                    display(test_row1, test_row2, test_row3)
                    break
            elif position_player2.upper() == "C":
                if test_row2[1] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row2[1] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row2[1] = "O"
                    display(test_row1, test_row2, test_row3)
                    break
            elif position_player2.upper() == "MR":
                if test_row2[2] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row2[2] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row2[2] = "O"
                    display(test_row1, test_row2, test_row3)
                    break
            elif position_player2.upper() == "BL":
                if test_row3[0] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row3[0] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row3[0] = "O"
                    display(test_row1, test_row2, test_row3)
                    break
            elif position_player2.upper() == "BM":
                if test_row3[1] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row3[1] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row3[1] = "O"
                    display(test_row1, test_row2, test_row3)
                    break
            elif position_player2.upper() == "BR":
                if test_row3[2] == "X":
                    print("It's already X")
                    display(test_row1, test_row2, test_row3)
                    pass
                elif test_row3[2] == "O":
                    print("It's already O")
                    display(test_row1, test_row2, test_row3)
                    pass
                else:
                    test_row3[2] = "O"
                    display(test_row1, test_row2, test_row3)
                    break
            else:
                print("Wrong input")
                pass
        if (test_row1[0] == "O" and test_row1[1] == "O" and test_row1[2] == "O") or (
                test_row2[0] == "O" and test_row2[1] == "O" and test_row2[2] == "O") or (
                test_row3[0] == "O" and test_row3[1] == "O" and test_row3[2] == "O") or (
                test_row1[0] == "O" and test_row2[1] == "O" and test_row3[2] == "O") or (
                test_row1[0] == "O" and test_row2[0] == "O" and test_row3[0] == "O") or (
                test_row1[1] == "O" and test_row2[1] == "O" and test_row3[1] == "O") or (
                test_row1[2] == "O" and test_row2[2] == "O" and test_row3[2] == "O") or (
                test_row1[2] == "O" and test_row2[1] == "O" and test_row3[0] == "O"):
            print(f"{player2} WON")
            player2_wins += 1
            break
        # tie checker
        for a in range(len(test_row1)):
            if test_row1[a] == "X" or test_row1[a] == "O":
                cnt += 1
            else:
                cnt += 0
        for b in range(len(test_row2)):
            if test_row2[b] == "X" or test_row2[b] == "O":
                cnt += 1
            else:
                cnt += 0
        for c in range(len(test_row3)):
            if test_row3[c] == "X" or test_row3[c] == "O":
                cnt += 1
            else:
                cnt += 0
        if cnt == 45:
            print("TIE")
            break
        elif cnt != 45:
            pass
    print(f"{player1} won {player1_wins} times")
    print(" ")
    print(f"{player2} won {player2_wins} times")
    print(" ")
    while True:
        # play again?
        play_again = input("Do you want to play again (Y/N) ")
        if play_again.upper() == "Y":
            # clear the playing field
            test_row1.clear()
            test_row2.clear()
            test_row3.clear()
            # create new playing field
            for x in range(3):
                test_row1.append(" ")
            for y in range(3):
                test_row2.append(" ")
            for z in range(3):
                test_row3.append(" ")
            break
        elif play_again.upper() == "N":
            print("FINAL RESULT:")
            print(f"{player1} won {player1_wins} times")
            print(f"{player2} won {player2_wins} times")
            print(" ")
            # Who is the winner?
            if player1_wins > player2_wins:
                print(f"{player1} is the winner")
                break
            elif player2_wins > player1_wins:
                print(f"{player2} is the winner")
                break
            else:
                print("The points are equal there is no winner")
                break
        else:
            print("Wrong input try again")
            pass
