from ninetyninebottles.i18n import gettext


def main() -> None:
    """Prints the lyrics to 99 Bottles of Beer."""
    for bottles in range(99, 1, -1):
        print(gettext("{} bottles of beer on the wall,").format(bottles))
        print(gettext("{} bottles of beer.").format(bottles))
        print(gettext("Take one down, pass it around,"))
        print(gettext("{} bottles of beer on the wall.").format(bottles - 1))

    print(gettext("1 bottle of beer on the wall,"))
    print(gettext("1 bottle of beer."))
    print(gettext("Take one down, pass it around,"))
    print(gettext("no more bottles of beer on the wall."))


if __name__ == "__main__":
    main()
