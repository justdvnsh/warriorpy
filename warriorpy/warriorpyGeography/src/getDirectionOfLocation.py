from absoluteDirections import EAST, WEST, SOUTH, NORTH

# /**
#  * Returns the direction of a location from another location (reference
#  * location).
#  *
#  * @param {number[]} location The location as [x, y].
#  * @param {number[]} referenceLocation The reference location as [x, y].
#  *
#  * @returns {string} The direction.
#  */

def getDirectionOfLocation(x1, y1, x2, y2):
    if ( abs(x2 - x1) > abs(y2 - y1) ):
        if x1 > x2:
            return EAST
        
        return WEST

    if y1 > y2:
        return SOUTH

    return NORTH