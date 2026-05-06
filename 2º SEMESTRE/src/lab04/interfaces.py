from abc import ABC, abstractmethod

class Printable(ABC):
    """Интерфейс для объектов, которые могут возвращать форматированную строку."""
    @abstractmethod
    def to_short_string(self) -> str:
        pass

class Rewardable(ABC):
    """Интерфейс для объектов, имеющих систему вознаграждений."""
    @abstractmethod
    def get_reward_info(self) -> str:
        pass
