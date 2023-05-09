
def meow(n: int) -> str:
    return "meow\n" * n


number: int = 5
meows: str = meow(number)
print(meows, end="")
