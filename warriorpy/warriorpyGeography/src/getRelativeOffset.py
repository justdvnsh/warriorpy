from .verifyAbsoluteDirection import verifyAbsoluteDirection
from .absoluteDirections import EAST, NORTH, SOUTH

# /**
#  * Returns the relative offset for a given location, with reference to another
#  * location (reference location) and direction (reference direction).
#  *
#  * @param {number[]} location The location.
#  * @param {number[]} referenceLocation The reference location.
#  * @param {string} referenceDirection The reference direction (absolute).
#  *
#  * @returns {number[]} The relative offset as [forward, right].
#  */

def getRelativeOffset(x1, y1, x2, y2, referenceDirection):
    verifyAbsoluteDirection(referenceDirection)

    [deltaX, deltaY] = [x1 - x2, y1 - y2]

    if ( referenceDirection == NORTH ):
        return [ -deltaY, deltaX ]
    elif ( referenceDirection == EAST ):
        return [ deltaX, deltaY ]
    elif ( referenceDirection == SOUTH ):
        return [ deltaY, -deltaX ]

    return [-deltaX, -deltaY]