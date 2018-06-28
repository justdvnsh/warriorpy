from verifyRelativeDirection import verifyRelativeDirection
from relativeDirections import BACKWARD, FORWARD, RIGHT

# /**
#  * Rotates the given relative offset in the given direction.
#  *
#  * @param {number[]} offset The relative offset as [forward, right].
#  * @param {string} direction The direction (relative direction).
#  *
#  * @returns {number[]} The rotated offset as [forward, right].
#  */

def rotateRelativeOffset(forward, right, direction):
  verifyRelativeDirection(direction);

  if (direction == FORWARD):
    return [forward, right]
  elif (direction == RIGHT):
    return [-right, forward]
  elif (direction == BACKWARD):
    return [-forward, -right]

  return [right, -forward];