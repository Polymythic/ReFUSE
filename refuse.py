import random

# each terminal will have a list of moves "attached" to it: these are the wires
# id, description, 
move_list = (
            "connect battery + to bus",
            "connect battery - to bus",
            "connect battery to personal +",
            "connect battery to personal -",
            "connect personal + to left", 
            "connect personal - to left",
            "connect personal + to right",
            "connect personal - to right",
            "connect left_right +",
            "connect left_right -",
            "set value - digit 1",
            "set value - digit 2",
            "set value - digit 3",
            "switch + digit 1",
            "switch + digit 2",
            "switch + digit 3",
            "switch - digit 1",
            "switch - digit 2",
            "switch - digit 3"
            )

node_list = (
    "+ battery terminal",
    "- battery terminal",
    "+ digit 1",
    "- digit 1",
    "+ digit 2",
    "- digit 2",
    "+ digit 3",
    "- digit 3",
    "+ bus",
    "- bus")

class node():
    pass
    #id
    #wire[] wires
    #all of the places to attach wires
    #stack of wires attached to this node

class wire():
    pass
    #id, prev_node, next_node, energized?


class player():
    player_terminal_list = {"+":[], "-":[]}
    player_move_list = []


def resolve_nodes_and_wires():
    resolve_negative_battery()
    resolve_positive_battery()
    resolve_digit_1_positive()
    resolve_digit_1_negative()
    resolve_digit_2_positive()
    resolve_digit_2_negative()
    resolve_digit_3_positive()
    resolve_digit_3_negative()


def resolve_negative_battery():
    #for each wire attached in the stack, energize the wire, and go to next node
    pass

def resolve_positive_battery():
    pass

def resolve_digit_1_positive():
    pass

def resolve_digit_1_negative():
    pass

def resolve_digit_2_positive():
    pass

def resolve_digit_2_negative():
    pass

def resolve_digit_3_positive():
    pass

def resolve_digit_4_negative():
    pass



if __name__ == "__main__":

    player1 = player()
    player2 = player()
    player3 = player()
    player4 = player()
    player_list = (player1, player2, player3, player4)


    for turn in range(1,20):
            player_num = int((turn % 4))
            move = random.randint(0, len(move_list)-1)
 
            # Get a new number until we have one we have not done yet
            while move_list[move] in player_list[player_num].player_move_list:
                move = random.randint(0, len(move_list)-1)

            print(f"Player {player_num}: Move: {move_list[move]}")
            
            if player_num == len(player_list)-1:
                next_player_num = 0
                prev_player_num = player_num-1
            elif player_num == 0:
                next_player_num = player_num+1
                prev_player_num = len(player_list)-1
            else:
                prev_player_num = player_num-1
                next_player_num = player_num+1

            # Add this move to the player's list
            player_list[player_num].player_move_list.append(move)

            if move == 4:
                #"connect personal + to left",
                player_list[prev_player_num].player_terminal_list["+"].append((player_num, move))
            elif move == 5:
                #"connect personal - to left",
                player_list[prev_player_num].player_terminal_list["-"].append((player_num, move))
            elif move == 6:
                #"connect personal + to right",
                player_list[next_player_num].player_terminal_list["+"].append((player_num, move))
            elif move == 7:
                #"connect personal - to right",
                player_list[next_player_num].player_terminal_list["-"].append((player_num, move))
            elif move == 8:
                #"connect left_right +",
                player_list[next_player_num].player_terminal_list["+"].append((player_num, move))
                player_list[prev_player_num].player_terminal_list["+"].append((player_num, move))
            elif move == 9:
                #"connect left_right -",
                player_list[next_player_num].player_terminal_list["-"].append((player_num, move))
                player_list[prev_player_num].player_terminal_list["-"].append((player_num, move))


    for count, player in enumerate(player_list):
        print(f"Player {count}")

        print("\tMoves Made")
        for move in player.player_move_list:
            print(f"\t\t{move}")

        print("\t+Terminal")
        for connections in player.player_terminal_list["+"]:
            print(f"\t\t{connections}")


    # Best play seems to be to connect left and right together (2 players) - takes out both opponents



    ## Aggressive
    #   Keep one bus
    #   Connect leads to self
    #   Connect to left
    #   Connect to right

    #Calculating
    #   If most other numbers are the same, wire them up
    #   Keep detonator on those numbers


    #Defensive
    #   Test
    #   Cut bus wires

    #Spiteful (4 Moves)
    #   Connect Self + to Left
    #   Connect Self + to Right
    #   Connect Self - to Left
    #   Connect Self - to Right

    #Self Destructive(2 Moves)
    #   Connect + to Bus
    #   Connect = to Bus
