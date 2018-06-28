from absoluteDirections import ABSOLUTE_DIRECTIONS, NORTH, SOUTH, EAST, WEST

# /**
#  * Checks if the given direction is a valid absolute direction.
#  *
#  * @param {string} direction The direction.
#  *
#  * @throws Will throw if the direction is not valid.
#  */

def verifyAbsoluteDirection(direction):
    if ( direction not in ABSOLUTE_DIRECTIONS ):
        print('Unknown Direction "{0}". Should be one of "{1}" , "{2}", "{3}", "{4}"'.format(direction, NORTH, SOUTH, EAST, WEST))

# verifyAbsoluteDirection('suth')
