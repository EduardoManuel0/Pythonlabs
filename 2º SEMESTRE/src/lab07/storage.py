import json
from typing import List
from models import Athlete, Workout

def save_athletes(athletes: List[Athlete], filepath: str) -> None:
    data = [
        {'id': a.id, 'name': a.name, 'weight': a.weight, 'record': a.record}
        for a in athletes
    ]
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def load_athletes(filepath: str) -> List[Athlete]:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [Athlete(a['id'], a['name'], a['weight'], a['record']) for a in data]
    except FileNotFoundError:
        return []

def save_workouts(workouts: List[Workout], filepath: str) -> None:
    data = [
        {'id': w.id, 'athlete_id': w.athlete_id, 'duration': w.duration, 'intensity': w.intensity}
        for w in workouts
    ]
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def load_workouts(filepath: str) -> List[Workout]:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [Workout(w['id'], w['athlete_id'], w['duration'], w['intensity']) for w in data]
    except FileNotFoundError:
        return []
