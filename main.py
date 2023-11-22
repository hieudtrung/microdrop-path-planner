from algorithms import RouteFinder


def main():
    # Generate a map with GUI

    # Generate droplets
    droplets = []
    # Init a path finder instance
    finder = RouteFinder()
    routes = finder.find(droplets)

    print(routes)


if __name__ == "__main__":
    main()