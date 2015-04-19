def enum(**enums):
    return type('Enum', (), enums)

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)


SITES = enum(CURRENT=0, NORTH=1, EAST=2, SOUTH=3, WEST=4)
SITES_LENGTH = 5
OBSTACLES = enum(EMPTY=0, CAN=1, WALL=2)
OBSTACLES_LENGTH = 3
ACTIONS = enum(MOVE_NORTH=0, MOVE_EAST=1, MOVE_SOUTH=2, MOVE_WEST=3, MOVE_RANDOM=4, STAY_PUT=5, PICK_UP_CAN=6)
ACTIONS_LENGTH = 7

#how to use:
#-----------
#print(OBSTACLES.EMPTY)
#print(OBSTACLES.reverse_mapping[0])
