# /**
#  * Translates the given location by a given offset.
#  *
#  * @param {number[]} location The location as [x, y].
#  * @param {number[]} offset The offset as [deltaX, deltaY].
#  *
#  * @returns {number[]} The translated location.
#  */

def translateLocation(x, y, deltaX, deltaY):
  return [x + deltaX, y + deltaY]