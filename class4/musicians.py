
class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f"{self.name} ({self.get_instrument()})"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.instrument}')"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "Playing a solo!"


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar")

    def play_solo(self):
        return "Playing an awesome guitar solo!"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, "bass")

    def play_solo(self):
        return "Playing a groovy bass solo!"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "drums")

    def play_solo(self):
        return "Playing an epic drum solo!"


class Band:
    all_bands = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members or []
        Band.all_bands.append(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.members})"

    def add_musician(self, musician):
        if isinstance(musician, Musician):
            self.members.append(musician)

    def play_solos(self):
        solos = [member.play_solo() for member in self.members]
        return solos

    @classmethod
    def to_list(cls):
        return cls.all_bands
