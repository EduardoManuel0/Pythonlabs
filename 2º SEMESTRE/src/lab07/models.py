class Athlete:
    def __init__(self, athlete_id, name, weight, record):
        self.athlete_id = athlete_id
        self.name = name
        self.weight = weight
        self.record = record

    def __str__(self):
        return f"ID: {self.athlete_id} | Nome: {self.name} | Peso: {self.weight}kg | Recorde: {self.record}"

class Workout:
    def __init__(self, workout_id, athlete_id, date, duration, intensity):
        self.workout_id = workout_id
        self.athlete_id = athlete_id
        self.date = date
        self.duration = duration  # em minutos
        self.intensity = intensity  # 1 a 5

    def __str__(self):
        return f"Treino {self.workout_id} (Atleta {self.athlete_id}) - {self.date}: {self.duration}min (Intensidade: {self.intensity})"
