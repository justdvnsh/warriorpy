import warriorpyCore.src.position.Position as Position
import warriorpyGeography.src.getAbsoluteOffset.getAbsoluteOffset as getAbsoluteOffset
import warriorpyGeography.src.verifyAbsoluteDirection.verifyAbsoluteDirection as verifyAbsoluteDirection

class AbilityBase(object):
    def __init__(self, unit):
        self._unit = unit

    def offset(self, direction, forward=1, right=0):
        getAbsoluteOffset(forward, right, direction)

    def verify_direction(self, direction):
        verifyAbsoluteDirection(direction)

    def space(self, direction, forward=1, right=0):
        offset = self.offset(direction, forward, right)
        return self._unit.position.relative_space(*offset)

    def unit(self, direction, forward=1, right=0):
        return self.space(direction, forward, right).unit

    def damage(self, receiver, amount):
        receiver.take_damage(amount)
        if not receiver.is_alive():
            self._unit.earn_points(receiver.max_health)

    def description(self):
        return None

    def pass_turn(self):
        return None

    
