from abc import ABC, abstractmethod


class View(ABC):
    command: str

    @abstractmethod
    def get(self) -> str:
        raise NotImplementedError
