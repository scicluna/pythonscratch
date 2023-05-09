import random


class Hat:

    houses = ["Griff", "Huff", "Raven", "Slith"]  # "class" variable

    @classmethod
    def sort(cls, name):
        # could use "self" still instead of cls, but we will never have more than one Hat class inted
        house = random.choice(cls.houses)
        print(f"{name} is in {house}")


def main():
    Hat.sort("Harry")


if __name__ == "__main__":
    main()
