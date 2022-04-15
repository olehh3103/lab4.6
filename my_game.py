"""my game"""

import doctest
import copy

class Country:
    """
    country class
    >>> me = Country("fghjk", "ooo")
    >>> me.info
    'ooo'
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
            print("Україна отримує таку допомогу")
            for i in self.influence:
                print(f"* {i}")
            part = copy.deepcopy(self.influence)
            self.influence = []
            return part
        return None

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
        self.hit_points = 110

    def hit_enemy(self):
        """
        hits enemy
        """
        self.hit_points -= 10
        if self.hit_points == 0:
            print('Ти переміг кляту росію')
            print('you won\ngane over!!!')
            return True
        print("Ти завдав шкоди клятій росії на 10 балів, але треба ще!!!")
        print(f"Залишилось ще {self.hit_points}")
        return False
        # self.hit_points


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
        if isinstance(influence, str):
            self.influence[influence] = 1
        else:
            for i in influence:
                if i not in self.influence:
                    self.influence[i] = 1
                else:
                    self.influence[i] += 1

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
        if not bool(self.influence):
            return "Україна ще не має дипломатичної зброї"
        res = "Ви маєте таку дипломатичну зброю:\n"
        for i in self.influence:
            res += f"{i} - {self.influence[i]} к-сть\n"
        return res

    def delete(self, command):
        """
        delete function
        """
        if self.influence[command] == 1:
            del self.influence[command]
        else:
            self.influence[command] -= 1

if __name__ == "__main__":
    print(doctest.testmod())
