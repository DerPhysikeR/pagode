import argparse
from pathlib import Path


def start_share(directory):
    print(directory)


def main():
    parser = argparse.ArgumentParser(
        description="Share a directory for pair programming"
    )
    parser.add_argument(
        "dir", metavar="directory", type=str, help="the directory to share"
    )
    args = parser.parse_args()
    directory = Path(args.dir).resolve()
    if not directory.is_dir():
        raise ValueError(f"The given path is not a directory '{directory}'")
    start_share(directory)


if __name__ == "__main__":
    main()
