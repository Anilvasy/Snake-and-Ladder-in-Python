import random
RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
Blue = "\033[94m"
Magenta = "\033[95m"
Cyan = "\033[96m"
def daies_display(val):
      ''' print(" -------- ")
       print("|        |")
       print("|        |")
       print("|        |")
       print(" -------- ")'''
      line1 = " -------- "
      line2= "|        |"
      print( )
      match val:
          case 1:
           print(line1)
           print(line2)
           print("|   *    |")
           print(line2)
           print(line1)
          case 2:
             print(line1)
             print(line2)
             print("| *    * |")
             print(line2)
             print(line1)
          case 3:
               print(line1)
               print(line2)
               print("|   *    |")
               print("| *    * |")
               print(line1)
          case 4:
            print(line1)
            print("|   *    |")
            print("| *    * |")
            print("|   *    |")
            print(line1)
          case 5:
                print(line1)
                print("| *    * |")
                print("|   *    |")
                print("| *    * |")
                print(line1)
          case 6:
               print(line1)
               print("| *    * |")
               print("| *    * |")
               print("| *    * |")
               print(line1)
def game_board(l):
    k=35
    print("----Snake and Ladder-----")
    for i in range(6):
        print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
        for j in range(6):
            cell = l[k]
            if cell.strip() == 'S':  # strip to match ' O' safely
                print("|", f"{RED}{cell}{RESET}", end=" ")
            elif cell.strip()=='L':
                print("|", f"{GREEN}{cell}{RESET}", end=" ")
            elif cell=="^^":
                print("|", f"{YELLOW}{cell}{RESET}", end=" ")

            else:
                 print("|",cell,end=" ")
            k=k-1
        print("|")
    print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
def roll_daies(key):
    while True:
        if key == 'D' or key == 'd':
            dai = random.randint(1, 6)
            daies_display(dai)
            return dai
        else:
            key = input("enter 'd' or 'D' to roll the daies:")
def start_game(l, p1, p2,p3):
    original_board = l.copy()  # Save original board for resetting
    snakes = {12: 5, 19: 7, 33: 20}  # Snake: from -> to
    ladders = {8: 15, 23: 28}  # Ladder: from -> to
    pos1, pos2 = 0, 0  # Initialize positions outside loop
    prev1, prev2 = -1, -1
    i = 1

    print(f"player1 indication will be: {p1}")
    print(f"player2 indication will be: {p2}")
    print(f"if both player at same position{p3}")
    print("snakes will be indicate by",f"{RED}{'S'}{RESET}")
    print("Ladders will be indicate by", f"{GREEN}{'L'}{RESET}")
    game_board(l)
    while True:
        if i % 2 != 0:
            i += 1
            print(f"{Blue}Hey player1 this you turn..{RESET}")
            player1 = input("enter 'd' or 'D' to roll the daies:")
            val = roll_daies(player1)
            if prev1 != -1:
                l[prev1] = original_board[prev1]  # Restore original value
            pos1 += val
            #print(f"position1: {pos1}")
            if pos1 == 36:
                l[pos1-1] = p1
                game_board(l)
                print(f"{Blue}-----Player 1 you are the Winner----{RESET}")
                break
            elif pos1 > 36:
                print(f"{YELLOW}You can't move, you need{RESET}",f"{36-(pos1-val)}",f"{YELLOW}WIN{RESET}")
                pos1 -= val
                prev1=pos1-1
                if prev1 == prev2:
                    l[pos1-1]=p3
                    game_board(l)
                else:
                    l[pos1-1] = p1
                    game_board(l)
                continue
            elif pos1 < 36:
                if pos1 in snakes:
                    print(f"{RED}snake ate you, moving to {snakes[pos1]}{RESET}")
                    pos1 = snakes[pos1]
                    prev1 = pos1 - 1
                    if prev1 == prev2:
                        l[pos1 - 1] = p3
                        game_board(l)
                    else:
                        l[pos1 - 1] = p1
                        game_board(l)
                elif pos1 in ladders:
                    print(f"{GREEN}you on ladder goto {ladders[pos1]}{RESET}")
                    pos1 = ladders[pos1]
                    prev1 = pos1 - 1
                    if prev1 == prev2:
                        l[pos1 - 1] = p3
                        game_board(l)
                    else:
                        l[pos1 - 1] = p1
                        game_board(l)
                else:
                    print(f"you goto {pos1}")
                    prev1 = pos1 - 1
                    if prev1 == prev2:
                        l[pos1 - 1] = p3
                        game_board(l)
                    else:
                        l[pos1 - 1] = p1
                        game_board(l)

        else:
            i += 1
            print(f"{Magenta}Hey player2 this you turn..{RESET}")
            player2 = input("enter 'd' or 'D' to roll the daies:")
            val = roll_daies(player2)
            if prev2 != -1:
                l[prev2] = original_board[prev2]  # Restore original value
            pos2 += val
            #print(f"position2: {pos2}")
            if pos2 == 36:
                l[pos2-1] = p2
                game_board(l)
                print(f"{Magenta}-----Player 2 you are the Winner----{RESET}")
                break
            elif pos2 > 36:
                print(f"{YELLOW}You can't move, you need{RESET}", f"{36-(pos2-val)}",f"{YELLOW}WIN{RESET}")
                pos2 -= val
                prev2=pos2-1
                if prev1 == prev2:
                    l[pos2 - 1] = p3
                    game_board(l)
                else:
                    l[pos2-1] = p2
                    game_board(l)
                continue
            elif pos2 < 36:
                if pos2 in snakes:
                    print(f"{RED}snake ate you, moving to {snakes[pos2]}{RESET}")
                    pos2 = snakes[pos2]
                    prev2 = pos2 - 1
                    if prev1 == prev2:
                        l[pos2 - 1] = p3
                        game_board(l)
                    else:
                        l[pos2 - 1] = p2
                        game_board(l)
                elif pos2 in ladders:
                    print(f"{GREEN}you on ladder goto {ladders[pos2]}{RESET}")
                    pos2 = ladders[pos2]
                    prev2 = pos2 - 1
                    if prev1 == prev2:
                        l[pos2 - 1] = p3
                        game_board(l)
                    else:
                        l[pos2 - 1] = p2
                        game_board(l)
                else:
                    print(f"you goto {pos2}")
                    prev2 = pos2 - 1
                    if prev1 == prev2:
                        l[pos2 - 1] = p3
                        game_board(l)
                    else:
                        l[pos2 - 1] = p2
                        game_board(l)
def main():
    while True:
        l = ['01', '02', '03', '04', '05', '06', '07', ' L', '09', '10',
             '11', ' S', '13', '14', '15', '16', '17', '18', ' S', '20',
             '21', '20', ' L', '24', '25', '26', '27', '28', '29', '30',
             '31', '32', ' S', '34', '35', '^^']
        p1 = f"{Blue}{'P1'}{RESET}"
        p2 = f"{Magenta}{'P2'}{RESET}"
        p3 = f"{Cyan}{'P3'}{RESET}"
        print("Snake and Ladder")
        print("enter '1' to start the game")
        print("if your enter any other value game will exit")
        s = int(input("enter:"))
        if s == 1:
            start_game(l, p1, p2, p3)
            break
        else:
            print("game exited")
            break
if __name__=="__main__":
    main()