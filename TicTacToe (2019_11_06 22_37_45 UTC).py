#    |   | O

#  X | X | X

#    |   |

#============================
# Spielbrett definieren
#============================

class Board:

#============================
# Spielbrett in neun Felder teilen
#============================

    def __init__(self):
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0,]

#============================
# Auffordern zum Setzen eines Symobols
#============================

    def make_turn(self, cell, player):
        if self.is_valid_turn(cell):
            self.state[cell] = player.symbol
            return True
        return False

#============================
# Spielzug verweigern, wenn Spielzug ungültig gesetzt
#============================

    def is_valid_turn(self, cell):
        if self.state[cell] == 0:
            return True
        else:
            return False
            
#============================
# Spielregeln prüfen --> Wer hat gewonnen?
#============================

    def check_win(self, player):
        s = player.symbol
        if self.state[0] == s and self.state[1] == s and self.state[2] == s:
            return True
        elif self.state[3] == s and self.state[4] == s and self.state[5] == s:
            return True
        elif self.state[6] == s and self.state[7] == s and self.state[8] == s:
            return True

        elif self.state[0] == s and self.state[3] == s and self.state[6] == s:
            return True
        elif self.state[1] == s and self.state[4] == s and self.state[7] == s:
            return True
        elif self.state[2] == s and self.state[5] == s and self.state[8] == s:
            return True

        elif self.state[0] == s and self.state[4] == s and self.state[8] == s:
            return True
        elif self.state[2] == s and self.state[4] == s and self.state[6] == s:
            return True

    def is_full(self):
        for i in self.state:
            if i == 0:
                return False
        return True   

    def sign_to_printable(self, sign):
        if sign == 0:
            return " "
        elif sign == 1:
            return "X"
        else:
            return "0"

    def print_board(self):
        print(" " + self.sign_to_printable(self.state[0]) + " | " + self.sign_to_printable(self.state[1]) + " | " + self.sign_to_printable(self.state[2]) + " \n" + 
              " " + self.sign_to_printable(self.state[3]) + " | " + self.sign_to_printable(self.state[4]) + " | " + self.sign_to_printable(self.state[5]) + " \n" +
              " " + self.sign_to_printable(self.state[6]) + " | " + self.sign_to_printable(self.state[7]) + " | " + self.sign_to_printable(self.state[8]) + " \n")

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

if __name__ == "__main__":
    player_a = Player(1)
    player_b = Player(-1)
    board = Board()
    active_player = player_a

#============================
# Spielbrett definieren
#============================

    while not board.is_full():
        board.print_board()
        try:
            cell = int(input("Wo willst du hinsetzen? [1-9]"))
        except ValueError:
            continue
        cell = cell - 1
        if cell < 0 or cell > 8:
            print("Gib eine Zahl zwischen 1 und 9 ein!")
            continue

#============================
# Wenn kein ungültiger Zug gesetzt wurde --> weiterfahren
#============================

        if not board.make_turn(cell, active_player):
            print("Ungültiger Zug!")
            continue

        if board.check_win(active_player):
            print("Du hast gewonnen!")
            break

        if active_player == player_a:
            active_player = player_b
        else:
            active_player = player_a
            