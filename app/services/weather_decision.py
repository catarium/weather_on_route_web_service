def is_weather_bad(temperature: int, wind: int, precipitation: bool) -> bool:
    score = 0
    perfect_temperature = 25
    perfect_wind = 3
    
    score += abs(temperature - perfect_temperature)
    score += abs(wind - perfect_wind)
    score += int(precipitation) * 20

    if score > 50:
        return True
    return False
