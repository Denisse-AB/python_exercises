'''
Evaluate if there is a guard between the money and the thief.
casino floor example: xxxxxGxx$xxxxT
'''
floor = 'xxxGGxxxxGxxT$'

split_floor = [v for v in floor if v != 'x']

money = split_floor.index('$')

previous_value = split_floor[money-1]

def combinations(split_floor, previous_value):
  try:
    next_value = split_floor[money+1]

    if split_floor[0] == '$' and next_value[0] == 'G':
      return 'quiet'
    elif split_floor[0] == '$' and next_value[0] == 'T':
      return 'ALARM'
    elif split_floor[-1] == '$' and previous_value[-1] == 'T':
      return 'ALARM'
    elif split_floor[-1] == '$' and previous_value[-1] == 'G':
      return 'quiet'
    elif previous_value[-1] == 'G' and next_value[0] == 'G':
      return 'quiet'
    elif previous_value[-1] == 'T' and next_value[0] == 'G':
      return 'ALARM'
    elif previous_value[-1] == 'G' and next_value[0] == 'T':
      return 'ALARM'

  except IndexError:
    if split_floor[-1] == '$' and previous_value[-1] == 'T':
      return 'ALARM'
    else:
      return 'quiet'

print(combinations(split_floor, previous_value))
