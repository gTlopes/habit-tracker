from src.weather import get_weather

def test_get_weather():
    temperature = get_weather()

    assert isinstance(temperature, (int, float))