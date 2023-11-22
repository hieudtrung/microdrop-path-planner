# OpenDrop Route Planner Plugin

[OpenDrop](https://www.gaudi.ch/OpenDrop/) is an open-source microfluidic-control platform that leverages the cutting-edge electro-wetting technology. The device is integrated in many lab-on-chip systems to automate various experiments of digital biology. Nevertheless, the current design is flexible enough that we can broaden more use cases to other fields such as art, music, games, or robotics.

This plugin provides a GUI-based controller for OpenDrop. Users only need to define each droplet's start & one or more destinations. Then, the routes are calculated by the [Windowed Hierachical Cooperative A* (WHCA)](https://www.davidsilver.uk/wp-content/uploads/2020/03/coop-path-AIIDE.pdf) algorithm. No more explicit, static definition in JSON.

## Getting Started

### Build standalone WHCA demo from source

1. Install Java Development Kit 8 (JDK 8) and Maven (version 3.4 or newer)

2. Clone this source code & navigate to the right folder

    ```bash
    git clone https://github.com/hieudtrung/opendrop-planner.git
    cd algorithms/WHCA
    ```

3. Modify your source code or build file `pom.xml` and start building or running

    ```bash
    # build byte code
    mvn package
    # run target
    mvn spring-boot:run
    ```

4. Run the demo

    ```bash
    java -jar target/coop-pathfinder.jar
    ```

### Run the standalone WHCA demo

1. If you only want to run the pre-compiled WHCA demo, just install Java runtime environment (JRE) instead of the whole JDK. Make sure it is in your `$PATH` environment variable.

2. Clone this source code & navigate to the right folder

    ```bash
    git clone https://github.com/hieudtrung/opendrop-planner.git
    cd algorithms/WHCA
    ```

3. Run with JRE

    ```bash
    java -jar target/coop-pathfinder.jar
    ```

### Run the plugin with OpenDrop

Coming soon

## References

A big thanks to the original Java implementation of WHCA by [igrek51](https://github.com/igrek51/coop-pathfinder/tree/master).
