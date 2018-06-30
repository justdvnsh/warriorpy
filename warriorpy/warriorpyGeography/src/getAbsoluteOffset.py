from .verifyAbsoluteDirection import verifyAbsoluteDirection
from .absoluteDirections import EAST, NORTH, SOUTH

# /**
#  * Returns the absolute offset for a given relative offset with reference
#  * to a given direction (reference direction).
#  *
#  * @param {number[]} offset The relative offset as [forward, right].
#  * @param {string} referenceDirection The reference direction (absolute).
#  *
#  * @returns {number[]} The absolute offset as [deltaX, deltaY].
#  */

def getAbsoluteOffset(forward, right, referenceDirection):
  verifyAbsoluteDirection(referenceDirection)

  if (referenceDirection == NORTH):
    return [right, -forward]
  elif (referenceDirection == EAST):
    return [forward, right] 
  elif (referenceDirection == SOUTH):
    return [-right, forward]

  return [-forward, -right];