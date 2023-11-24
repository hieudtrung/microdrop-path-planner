from abc import ABC, abstractmethod


class RouteFinder(ABC):
    @abstractmethod
    def find(self):
        ...
