from .verifyAbsoluteDirection import verifyAbsoluteDirection
from .absoluteDirections import ABSOLUTE_DIRECTIONS
from .relativeDirections import RELATIVE_DIRECTIONS

# /**
#  * Returns the relative direction for a given direction, with reference to a
#  * another direction (reference direction).
#  *
#  * @param {string} direction The direction (absolute).
#  * @param {string} referenceDirection The reference direction (absolute).
#  *
#  * @returns {string} The relative direction.
#  */

def getRelativeDirection(direction, referenceDirection):
  verifyAbsoluteDirection(direction)
  verifyAbsoluteDirection(referenceDirection)

  index = ( ABSOLUTE_DIRECTIONS.index(direction) - ABSOLUTE_DIRECTIONS.index(referenceDirection) +
      len(RELATIVE_DIRECTIONS)) % len(RELATIVE_DIRECTIONS)

  return RELATIVE_DIRECTIONS[index];