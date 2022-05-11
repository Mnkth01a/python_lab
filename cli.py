#!/usr/bin/env python3

# my first python code
""" Now, i'm stepping it up by working through the ITProTV hands on python course.
This is giving me the experience of writing python script and making it work."""

import argparse

import commands


# define the multiplication function
def multiply(_ns):
    """Multiplies all of the numbers contained in ns."""
    result = 1
    for _n in _ns:
        result *= _n
    return result


# main entry point
def main():
    """Main entrypoint of the cli."""

    # this creates an instance of argparse called parser with a ArgumentParser constructor.
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    # first command add the numbers input from cli
    add = subparsers.add_parser(commands.ADD)
    add.add_argument(
        "numbers",
        nargs="+",
        type=int,
    )

    # second command subtract the numbers input from cli
    sub = subparsers.add_parser(commands.SUBTRACT)
    sub.add_argument(
        "numbers",
        nargs="+",
        type=int,
    )

    # third command multiply the numbers input from cli
    mul = subparsers.add_parser(commands.MULTIPLY)
    mul.add_argument("numbers", nargs="+", type=int)

    # and fourth command divide the numbers input from cli
    div = subparsers.add_parser(commands.DIVIDE)
    div.add_argument(
        "numbers",
        nargs="+",
        type=int,
    )

    args = parser.parse_args()

    if args.command == commands.ADD:
        result = sum(args.numbers)
        operation = " + ".join(str(i) for i in args.numbers)
        print(f"The sum of {operation} is {result}.")

    elif args.command == commands.SUBTRACT:
        first, *rest = args.numbers
        result = first - sum(rest)
        operation = " - ".join(str(i) for i in args.numbers)
        print(f"The difference of {operation} is {result}.")

    elif args.command == commands.MULTIPLY:
        result = multiply(args.numbers)
        operation = " x ".join(str(i) for i in args.numbers)
        print(f"The result of {operation} is {result}.")

    elif args.command == commands.DIVIDE:
        first, *rest = args.numbers
        result = first / multiply(rest)
        operation = " / ".join(str(i) for i in args.numbers)
        print(f"The result of {operation} is {result}.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
