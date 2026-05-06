import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.lab03.models import AtletaPro, AtletaAmador
from src.lab04.interfaces import Printable, Rewardable

class ProfessionalAthlete(AtletaPro, Printable, Rewardable):
    """Профессионал, реализующий два интерфейса."""
    
    def to_short_string(self) -> str:
        return f"[ПРО] {self.nome} (Рейтинг: {self.ranking})"

    def get_reward_info(self) -> str:
        return f"Денежный бонус: ${self.calcular_bonus()}"

class AmateurAthlete(AtletaAmador, Printable, Rewardable):
    """Любитель, реализующий те же интерфейсы, но с другой логикой."""
    
    def to_short_string(self) -> str:
        return f"[ЛЮБ] {self.nome} ({self.esporte})"

    def get_reward_info(self) -> str:
        return "Награда: Почетная грамота и медаль участника"
