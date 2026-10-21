def parse_record(line: str) -> dict:
    """
    Разбирает строку «город;температура;дата» в словарь.
    """
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Строка должна содержать ровно 3 поля, разделенных ';'")
    
    city, temp_str, date = parts
    
    # Город или дата не должны быть пустыми
    if not city or not date:
        raise ValueError("Город и дата не могут быть пустыми")
        
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Некорректное значение температуры: '{temp_str}'")
        
    return {
        "city": city,
        "temperature": temp,
        "date": date
    }


def read_valid(lines: list[str]) -> list[dict]:
    """
    Разбирает строки журнала, пропуская пустые и негодные.
    """
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            pass
    return valid_records


def average_by_city(records: list[dict]) -> dict:
    """
    Вычисляет среднюю температуру по каждому городу.
    """
    if not records:
        return {}
        
    city_totals = {}
    city_counts = {}
    
    for r in records:
        city = r["city"]
        temp = r["temperature"]
        city_totals[city] = city_totals.get(city, 0.0) + temp
        city_counts[city] = city_counts.get(city, 0) + 1
        
    averages = {}
    for city in city_totals:
        # Округляем до десятых, как просит условие
        averages[city] = round(city_totals[city] / city_counts[city], 1)
        
    return averages


def warmest_city(records: list[dict]) -> str:
    """
    Находит самый теплый город. При равенстве — первый по алфавиту.
    """
    averages = average_by_city(records)
    if not averages:
        return ""
        
    max_temp = max(averages.values())
    warmest_cities = [city for city, temp in averages.items() if temp == max_temp]
    warmest_cities.sort()
    return warmest_cities[0]
