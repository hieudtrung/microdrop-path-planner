# MicroDrop Path Planner Plugin

## Introduction

[DropBot](https://github.com/wheeler-microfluidics/dropbot/wiki) is an open-source instrument for digital micro-fluidic sensing (or microfluidics). DropBot features two key functionalities: (1) real-time monitoring of instantaneous drop velocity, and (2) application of constant electrostatic driving forces through compensation for amplifier-loading and device capacitance.

[MicroDrop](https://github.com/sci-bots/microdrop) (written in Python 2.7) is an open-sourced graphical user interface (GUI) for DropBot. It facilitates user experience when collecting data from DropBot. However, moving the droplets around still requires an explicit instruction define in JSON, which is tedious and unscalable.

In this project, I create a plugin for MicroDrop named "Path Planner". This plugin extends the GUI controller with an automatic path finding agent. Users only need to define each droplet's start & one or more destinations. Then, the paths are calculated by the [A* algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm). No more explicit, static definition in JSON.

> **Important**: please don't be confused by other names such as [OpenDrop](https://www.gaudi.ch/OpenDrop/), even though they share the same technology and use case.

## Getting Started

### Build standalone WHCA demo from source

1. Install Java Development Kit 8 (JDK 8) and Maven (version 3.4 or newer)

2. Clone this source code & navigate to the right folder

    ```bash
    git clone https://github.com/hieudtrung/MicroDrop-planner.git
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
    git clone https://github.com/hieudtrung/MicroDrop-planner.git
    cd algorithms/WHCA
    ```

3. Run with JRE

    ```bash
    java -jar target/coop-pathfinder.jar
    ```

### Run the plugin with MicroDrop

Coming soon

## Developer Guide

This section introduces how to develop your own path finding algorithm and plug it into the MicroDrop application as one of its plugin.

 1. Install dependencies listed in `requirements.host` section of
    [`.conda-recipe/meta.yaml`](/.conda-recipe/meta.yaml).
 2. Run the following command from the repository root:

    ```bash
    python -m mpm.bin.build -p path-planner --properties-only -s . -t .
    ```

 3. Select or create directory as root to hold development plugins, e.g.,

    ```bash
    mkdir %USERPROFILE%\microdrop-dev-plugins
    ```

 4. Create link to repo directory in development root with import-friendly **_plugin_** name, e.g.:

    ```bash
    mklink /J %USERPROFILE%\microdrop-dev-plugins\path-planner-plugin %REPO_DIR%
    ```

 5. Add this directory (or where you store all the plugins) to semi-colon-separated list of paths in `MICRODROP_PLUGINS_PATH` environment variable.

## TODO

- [ ] Implement WHCA
- [ ] Migrate the source code to C++
- [ ] Synchronize with the real hardware status, i.e., ensure that droplets are correctly placed

## References

[1] A big thanks to the original Java implementation of WHCA by [igrek51](https://github.com/igrek51/coop-pathfinder/tree/master).

[2] [Windowed Hierachical Cooperative A* (WHCA)](https://www.davidsilver.uk/wp-content/uploads/2020/03/coop-path-AIIDE.pdf)

[3] [Official guide](https://github.com/sci-bots/microdrop/wiki/Developer-Guide) from MicroDrop and their [Youtube channel](https://youtu.be/btmT3jUZpjs?feature=shared)
