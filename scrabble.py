letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {letters:points for letters, points in zip(letters, points)}

letters_to_points[" "] = 0

# Scoring the word
def score_word(word):
  total = 0
  word = word.upper()
  for letter in word:
    total += letters_to_points.get(letter, 0)
  return total
  
# Score a Game
players_to_points = {}

num_players = int(input("Enter the number of players: "))

for i in range(num_players):
  name = input(f"\nEnter name of the player {i+1}: ")
  players_to_points[name] = 0

  print(f"{name}, enter your words one by one.")
  print("Type STOP when finished.\n")

  while True:
    word = input("Enter Word: ")

    if word.upper() == "STOP":
      break
  
    score = score_word(word)
    players_to_points[name] += score
    print(f"'{word}' score {score} points!")
    print(f"{name}'s total = {players_to_points[name]}\n")

print('\n 🏆 FINAL SCORES')
for player, pts in players_to_points.items():
  print(player, ":", pts)

winner = max(players_to_points, key=players_to_points.get)
print(f"\n Winner is {winner} with {players_to_points[winner]} points!")