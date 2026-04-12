from src.habits import HabitTracker
import pytest

def test_add_habit():
    tracker = HabitTracker()
    tracker.add_habit("Beber água")
    assert "Beber água" in tracker.habits

def test_add_invalid_habit():
    tracker = HabitTracker()
    with pytest.raises(ValueError):
        tracker.add_habit("")

def test_complete_habit():
    tracker = HabitTracker()
    tracker.add_habit("Estudar")
    tracker.complete_habit("Estudar")
    assert tracker.habits["Estudar"] is True