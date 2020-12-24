from typing import Optional
from abc import ABC, abstractmethod


class Model(ABC):
    url: Optional[str]

    @classmethod
    @abstractmethod
    def get(cls) -> str:
        raise NotImplementedError
