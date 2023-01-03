from ninetyninebottles.i18n import gettext


def print_bottles_stanza(bottle_num: int) -> None:
    """Prints the stanza for the given number of bottles."""
    print(gettext("{0} bottles of beer on the wall, {0} bottles of beer.").format(bottle_num))
    print(gettext("Take one down, pass it around, {} bottles of beer on the wall.").format(bottle_num - 1))
    if bottle_num == 2:
        print(gettext("1 bottle of beer on the wall, 1 bottle of beer."))
        print(gettext("Take one down, pass it around, no more bottles of beer on the wall."))


def main() -> None:
    """Prints the lyrics to 99 Bottles of Beer."""
    for bottle_num in range(99, 1, -1):
        print_bottles_stanza(bottle_num)


if __name__ == "__main__":
    main()
