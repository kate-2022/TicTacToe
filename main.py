
field = ["",
         "1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]
run = True
player_active = "X"

def print_field():
    print(field[1] + "|" + field[2] + "|" + field[3])
    print(field[4] + "|" + field[5] + "|" + field[6])
    print(field[7] + "|" + field[8] + "|" + field[9])

def next_move():
   global run
   while True:
         players_move = input("Bitte ein Feld wählen: ")
         if players_move == "q":
            run = False
            return None
         players_move = int(players_move)
         if players_move >=1 and players_move<=9:
             if field[players_move] == "X" or field[players_move] == "0":
                print("Das Feld ist bereits belegt! Bitte wiederholen..")
             else:
                  return players_move
         else:
            print("Die eingegebene Zahl muss zwischen 1 und 9 liegen")

def change_player():
   global player_active
   if player_active == "X":
      player_active = "O"
   else:
      player_active = "X"

while run:
   print_field()
   players_move = next_move()
   field[players_move] = player_active
   change_player()
