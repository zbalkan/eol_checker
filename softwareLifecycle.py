from dataclasses import dataclass
from typing import Any


@dataclass
class SoftwareLifecycle:
    name: str
    cycle: str
    cycleShortHand: str
    support: str
    eol: str
    releaseDate: str

    def __init__(self, name: str = '') -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name + ": " + str(self.cycle)

    @staticmethod
    def from_dict(obj: Any) -> 'SoftwareLifecycle':
        temp: SoftwareLifecycle = SoftwareLifecycle('')
        temp.cycle = str(obj.get("cycle"))
        temp.cycleShortHand = str(obj.get("cycleShortHand"))
        temp.support = str(obj.get("support"))
        temp.eol = str(obj.get("eol"))
        temp.releaseDate = str(obj.get("releaseDate"))
        return temp
