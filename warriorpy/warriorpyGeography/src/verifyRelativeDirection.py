from .relativeDirections import RELATIVE_DIRECTIONS

# /**
#  * Checks if the given direction is a valid relative direction.
#  *
#  * @param {string} direction The direction.
#  *
#  * @throws Will throw if the direction is not valid.
#  */

def verifyRelativeDirection(direction):
        if direction not in RELATIVE_DIRECTIONS:
            raise Exception("Unknown direction %s. "
                            "Should be 'forward', 'backward', "
                            "'left' or 'right'")