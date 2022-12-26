class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level can't be less than 1")

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    # This is also doing the same thing as above methods. But it is using a decorator here rather than an object.
    # both of the statements below are same as score = property(_get_setter, _set_score). The only difference is that, we are using a 
    # decorator this time.
    @property
    def score(self): # This is one of the ways in which we can define getter. 
        return self._score

    @score.setter # This is a new setter. 
    def score(self, score):
        self._score = score
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score {0._score}".format(self)

