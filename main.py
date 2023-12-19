# from algorithms import PathFinder
from flask import Flask

app = Flask(__name__)


@app.post("/astar")
def main():
    return {"nextX": 5, "nextY": 10}


if __name__ == "__main__":
    main()
