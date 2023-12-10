from algorithms import PathFinder


def main():
    # Generate a map with GUI

    # Generate droplets
    droplets = []
    # Init a path finder instance
    finder = PathFinder()
    paths = finder.find(droplets)

    print(paths)


if __name__ == "__main__":
    main()
