import argparse
from importlib import import_module


def challenge(day, stage):
    print(f"Running challenge for day {day:0=2} stage {stage}")
    module = import_module(f".{day:0=2}_{stage}.challenge", package="aoc24")
    return module.challenge


def run():
    parser = argparse.ArgumentParser("aoc24")
    parser.add_argument("day", help="The challenge day to be run.", type=int)
    parser.add_argument("stage", help="The challenge stage to be run.", type=int)
    args = parser.parse_args()

    result = challenge(args.day, args.stage)()

    print(f"Output for day {args.day} stage {args.stage} is: {result}")


if __name__ == "__main__":
    print("Hello, World from main!")
