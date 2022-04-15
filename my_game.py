"""my game"""

import doctest

class Location:
    """
    Location of Minister of Defense of Ukraine
    """
    def __init__(self, name, description) -> None:
        """init"""
        self.name = name
        self.description = description
        self.link = {}
        self.character = None


class Country:
    """
    country class
    """
    def __init__(self, name, info) -> None:
        self.name = name
        self.info = info
        self.influence = []
        self.weakness = None
        self.enemy = None

    def add_influence(self, influence):
        """
        function add influences
        """
        self.influence.append(influence)

    def add_weakness(self, weakness: str):
        """
        function add weakness
        """
        self.weakness = weakness

    def check_weakness(self, weakness):
        """
        function check weakness
        """
        if weakness == self.weakness:
            print(f"Браво! Тобі вдалось вмовити {self.name}.")
            print("Україна отримуєш таку допомогу")
            for i in self.influence:
                print(f"* {i}")
            return self.influence
        return f"тобі не вдалось домовитись з {self.name}"

class Friend(Country):
    """
    friend class
    """
    def __init__(self, name, info) -> None:
        super().__init__(name, info)
        self.enemy = False

class Enemy(Country):
    """
    enemy class
    """
    def __init__(self, name, info) -> None:
        super().__init__(name, info)
        self.enemy = True


class Superenemy(Enemy):
    """
    class for superenemy(росія)
    """
    def __init__(self, name, info) -> None:
        super().__init__(name, info)
        self.enemy = True
        self.hit_points = 100
        self.num_of_weakness = 0

    def add_weakness(self, weakness: dict):
        """
        function add weakness
        """
        self.weakness = weakness
        for i in weakness.keys():
            self.num_of_weakness += weakness[i]

    def hit_enemy(self, weapon: str):
        """
        hits enemy
        """
        self.weakness[weapon] -= 1
        # self.hit_points

    def check_weapon(self, weapon: str):
        """
        check if the weapon is a weakness
        """
        if weapon in self.weakness:
            return True
        return False

    def get_hp(self):
        """
        returns hp
        """
        return self.hit_points



class Ukraine(Friend):
    """
    what Ukrain has to deal with Enemies
    """
    def __init__(self, name, info) -> None:
        super().__init__(name, info)
        self.influence = {}
        self.enemy = False

    def add_influence(self, influence):
        """
        function add influences
        """
        if influence not in self.influence:
            self.influence[influence] = 1
        else:
            self.influence[influence] += 1

    def check_influence(self, influence):
        """
        function check influences
        """
        if influence in self.influence:
            return True
        return False

    def return_all(self):
        """
        returns all
        """
        print("Ви маєте таку зброю:")
        for i in self.influence:
            print(i, " - ", self.influence[i], " к-сть")
