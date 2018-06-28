from absoluteDirections import ABSOLUTE_DIRECTIONS
from relativeDirections import RELATIVE_DIRECTIONS
from verifyAbsoluteDirection import verifyAbsoluteDirection
from verifyRelativeDirection import verifyRelativeDirection

# /**
#  * Returns the absolute direction for a given direction, with reference to
#  * another direction (reference direction).
#  *
#  * @param {string} direction The direction (relative).
#  * @param {string} referenceDirection The reference direction (absolute).
#  *
#  * @returns {string} The absolute direction.
#  */

def getAbsoluteDirection(direction, referenceDirection):
    verifyRelativeDirection(direction)
    verifyAbsoluteDirection(referenceDirection)

    index = (ABSOLUTE_DIRECTIONS.index(referenceDirection) + RELATIVE_DIRECTIONS.index(direction)) % 4

    return ABSOLUTE_DIRECTIONS[index]
