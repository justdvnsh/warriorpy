# /**
#  * Returns the Manhattan distance of a location from another location (reference
#  * location).
#  *
#  * @param {number[]} location The location as [x, y].
#  * @param {number[]} referenceLocation The reference location as [x, y].
#  *
#  * @returns {number} The distance between the locations.
#  */

def getDistanceOfLocation(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)