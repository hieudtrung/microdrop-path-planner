from abc import ABC, abstractmethod


class PathFinder(ABC):
    @abstractmethod
    def find(self):
        ...
