from models import Athlete, Workout

class FitnessApp:
    def __init__(self):
        self.athletes = {}
        self.workouts = {}

    def add_athlete(self, athlete):
        if athlete.athlete_id in self.athletes:
            raise DuplicateItemError(f"Atleta com ID {athlete.athlete_id} já existe.")
        self.athletes[athlete.athlete_id] = athlete

    def add_workout(self, workout):
        if workout.workout_id in self.workouts:
            raise DuplicateItemError(f"Treino com ID {workout.workout_id} já existe.")
        self.workouts[workout.workout_id] = workout

    def get_all_athletes(self):
        return list(self.athletes.values())

    def find_athlete(self, athlete_id):
        if athlete_id not in self.athletes:
            raise ItemNotFoundError(f"Atleta com ID {athlete_id} não encontrado.")
        return self.athletes[athlete_id]

    def delete_athlete(self, athlete_id):
        if athlete_id not in self.athletes:
            raise ItemNotFoundError(f"Atleta com ID {athlete_id} não encontrado.")
        del self.athletes[athlete_id]

    def filter_athletes_by_record(self, record_threshold):
        return [a for a in self.athletes.values() if a.record >= record_threshold]

    def sort_athletes(self, criterion):
        if criterion == 'name':
            return sorted(self.athletes.values(), key=lambda x: x.name)
        elif criterion == 'weight':
            return sorted(self.athletes.values(), key=lambda x: x.weight)
        elif criterion == 'record':
            return sorted(self.athletes.values(), key=lambda x: x.record, reverse=True)
        return []

