# The name of the game.
print('-- The Living Room Riddle --\n')

print("Welcome to 'The Living Room Riddle' by Lea-Sophie Böhm!\n") 

print("You are trapped in a magical living room! ")

print("There are clues hidden throughout different corners of the living room.\n")

print('Use "go" followed by a direction to move to different corners of the living room.')

print('Use "look around" to explore the area you are in.')

print('Use "read" followed by an object to receive clues.')

print('Use "answer" followed by the secret word to excape the living room you are trapped in.\n')

print('Now go explore!\n')

# +------------+------------+
# | Couch      | Bookshelf  |
# +------------+------------+
# | Desk       | Painting   |
# +------------+------------+

places = ['couch', 'bookshelf', 'desk', 'painting']

descriptions = ['You are looking at an old blue and white couch. There is '
                'something hidden beneath the cushions. It is a folded note. '
                'Interesting. You are wondering what it says.',

                'You are looking at an old raggedy bookshelf. There are '
                'a bunch of different styled books here, and a peculiar '
                'golden one.',

                'You are looking at a thick, brown oak desk that is falling '
                'apart with age. Once you look closer you notice a carving '
                'in the top of the desk. It looks like it was made with something sharp!',

                'You are looking at a painting of a beautiful woman with long brown hair. '
                'Did she just move? You catch yourself watching her as if to catch her next movement. '
                'In the bottom corner of the painting you notice some words in a bright red color.']

objects = ['note', 'book', 'carving', 'words']

solutions = ['You pick up the folded note. Written in what looks like an Old English font, it reads: '
             '"The one who makes it, sells it."',
       
             'You open up the peculiar looking book. The book is missing several pages. '
             'It looks like someone or something tore them out. On page 90 you spot a highlighted sentence, it says: '
             '"The one who buys it, never uses it."',

             'You remove a white cloth that is partly hidding the carving on the desk. '
             'You walk around the desk to get a better look at the carving, and it says: '
             '"The one who uses it, never knows that they are using it."',

             'The words written on the painting in a bright red color say: "What is it?"']

player_location = 0

print('You are in the living room next to the ' + places[0])

command = ''

while command != 'stop':

  # strip gets rid of the white space at the beginning and end of a string
  command = input('>> ').strip()

  if command == 'go north':
    if player_location - 2 >= 0:
      player_location = player_location - 2
      print('You are next to a ' + places[player_location])
    else:
      print('Too far!')

  elif command == 'go south':
    if player_location + 2 < 4:
      player_location = player_location + 2
      print('You are next to a ' + places[player_location])
    else:
      print('Too far!')

  elif command == 'go east':
    if player_location == 1 or player_location == 3:
      print('Too far!')
    else:
      player_location = player_location + 1 
      print('You are next to a ' + places[player_location])

  elif command == 'go west':
    if player_location == 0 or player_location == 2:
      print('Too far!')
    else:
      player_location = player_location - 1 
      print('You are next to a ' + places[player_location])

  elif command == 'look around':
    print(descriptions[player_location])

  elif command == 'read ' + objects[player_location]:
    print(solutions[player_location])

  elif command == 'answer coffin' or command == 'answer casket':
    print('Congratulations! You escaped the horror awaiting you within this magical living room.\n')
    break
  else:
      print('Try again. I do not understand.')  

print('Goodbye!')

