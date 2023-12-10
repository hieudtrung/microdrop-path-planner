import streamlit as st
import pandas as pd
import numpy as np
from algorithms.AStar import astar


def simple_web_ui():
    """A simple Streamlit app to demo path finding algorithms"""
    ...


def main():
    n_rows, n_cols = 4, 10
    nmaze = np.zeros((n_rows, n_cols))
    maze = nmaze.tolist()

    startA = (0, 0)
    endA = (3, 4)

    startB = (1, 9)
    endB = (1, 3)

    # Todo! Boundary checking: raise exception if either start/end is out of range

    # Todo2! if endA == endB: allow blending

    pathA = astar(maze, startA, endA)
    print(pathA)
    pathB = astar(maze, startB, endB)
    print(pathB)


if __name__ == "__main__":
    # main()
    print("Hello")
