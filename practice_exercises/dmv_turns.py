'''
Determine how long it will take to get to your turn,
5 people show up at the same time, turns in alphabetical order,
waiting period of 20 minutes.
'''

me = 'Eric'
employees = int('2')
people = 'Bob Jym Becky Pat '+ me

order = sorted(people.split(' '))

dmv_turns = []

if employees == 1:
  print(order.index(me)*20+20)
else:
  dmv_turns.append(order[:employees])
  dmv_turns.append(order[employees:-1])
  dmv_turns.append(order[-1])

  value = ["{} {}".format(index1,index2) for index1,value1 in enumerate(dmv_turns) for index2,value2 in enumerate(value1) if value2==me]


  def turns(value):
    if value[0][0] == '0':
      return 20
    elif value[0][0] == '1':
      return 40
    elif value[0][0] == '2':
      return 60
    elif value[0][0] == '3':
      return 80
    else:
      return 100

  print(turns(value))
