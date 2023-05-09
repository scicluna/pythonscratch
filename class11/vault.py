class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} g, {self.sickles} s, {self.knuts} k"

    def __add__(self, other):
        return f"{self.galleons + other.galleons} g, {self.sickles + other.sickles} s, {self.knuts + other.knuts} k"


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

print(potter + weasley)
