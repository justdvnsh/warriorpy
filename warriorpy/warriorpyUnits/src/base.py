import re

import warriorpyAbilities.src.attack.Attack as Attack
import warriorpyAbilities.src.bind.Bind as Bind
import warriorpyAbilities.src.detonate.Detonate as Detonate
import warriorpyAbilities.src.direction_of.DirectionOf as DirectionOf
import warriorpyAbilities.src.direction_of_stairs.DirectionOfStairs as DirectionOfStairs
import warriorpyAbilities.src.distance_of.DistanceOf as DistanceOf
import warriorpyAbilities.src.explode.Explode as Explode
import warriorpyAbilities.src.feel.Feel as Feel
import warriorpyAbilities.src.health.Health as Health
import warriorpyAbilities.src.listen.Listen as Listen
import warriorpyAbilities.src.look.Look as Look
import warriorpyAbilities.src.pivot.Pivot as Pivot
import warriorpyAbilities.src.rescue.Rescue as Rescue
import warriorpyAbilities.src.rest.Rest as Rest
import warriorpyAbilities.src.shoot.Shoot as Shoot
import warriorpyAbilities.src.walk.Walk as Walk
import warriorpyCore.src.turn.Turn as Turn
import warriorpyCli.src.ui.ui.UI as UI


class UnitBase(object):
    def __init__(self):
        self.position = None
        self._health = None
        self.abilities_attr = None
        self.bound = False
        self.max_health = 0

    @property
    def abilities(self):
        if not self.abilities_attr:
            self.abilities_attr = {}
        return self.abilities_attr

    def __repr__(self):
        return self.name()

    @property
    def attack_power(self):
        return 0

    def is_alive(self):
        return self.position is not None

    def earn_points(self, points):
        pass

    @property
    def health(self):
        if self._health is None:
            self._health = self.max_health
        return self._health

    @health.setter
    def health(self, value):
        self._health = value

    def take_damage(self, amount):
        if self.is_bound():
            self.unbind()
        if self.health:
            self._health -= amount
            self.say("takes %(amount)d damage, "
                     "%(health)d health power left" %
                     {'amount': amount, 'health': self.health})
            if self.health <= 0:
                self.position = None
                self.say("dies")

    def name(self):
        return self.__class__.__name__

    def prepare_turn(self):
        self.current_turn = self.next_turn()
        self.play_turn(self.current_turn)

    def next_turn(self):
        return Turn(self.abilities)

    def play_turn(self, turn):
        return None

    def is_bound(self):
        return self.bound

    def add_abilities(self, *new_abilities):
        for ability in new_abilities:
            class_name = re.sub("_", "", ability.title())
            self.abilities[ability] = eval("%s(self)" % class_name)

    def say(self, msg):
        UI.puts_with_delay("%(name)s %(msg)s" % {'name': self.name(),
                                                 'msg': msg})

    @property
    def character(self):
        return "?"

    def bind(self):
        self.bound = True

    def unbind(self):
        self.say("released from bonds")
        self.bound = False

    def perform_turn(self):
        if self.position:
            for ability in self.abilities.values():
                ability.pass_turn()
            if self.current_turn.action and not self.is_bound():
                name = self.current_turn.action[0]
                args = self.current_turn.action[1:]
                self.abilities[name].perform(*args)
