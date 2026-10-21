Python 3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Enter "help" below or click "Help" above for more information.
def parse_record(line: str) -> dict:
    """
    Разбирает строку «город;температура;дата» в словарь.
    Возбуждает ValueError, если строка некорректна.
    """
    # Разделяем строку по точке с запятой
    parts = line.split(";")
    
    # Полей должно быть ровно три
    if len(parts) != 3:
        raise ValueError("Строка должна содержать ровно 3 поля, разделенных ';'")
    
    city, temp_str, date = parts
    
    # Город или дата не должны быть пустыми
    if not city or not date:
        raise ValueError("Город и дата не могут быть пустыми")
        
    # Преобразуем температуру в число с плавающей точкой
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
    Разбирает строки журнала, пропуская пустые и некорректные.
    Возвращает список валидных словарей-записей.
    """
    valid_records = []
    for line in lines:
        # Пропускаем пустые строки молча (они не считаются ошибками)
        if not line.strip():
            continue
            
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            # Некорректные строки просто пропускаем (подсчет идет в main.py)
            pass
            
    return valid_records


def average_by_city(records: list[dict]) -> dict:
    """
    Вычисляет среднюю температуру по каждому городу.
...     """
...     if not records:
...         return {}
...         
...     city_totals = {}
...     city_counts = {}
...     
...     for r in records:
...         city = r["city"]
...         temp = r["temperature"]
...         city_totals[city] = city_totals.get(city, 0.0) + temp
...         city_counts[city] = city_counts.get(city, 0) + 1
...         
...     averages = {}
...     for city in city_totals:
...         averages[city] = city_totals[city] / city_counts[city]
...         
...     return averages
... 
... 
... def warmest_city(records: list[dict]) -> str:
...     """
...     Находит город с наибольшей средней температурой.
...     При равенстве возвращает первый по алфавиту.
...     """
...     averages = average_by_city(records)
...     if not averages:
...         return ""
...         
...     # Находим максимальную среднюю температуру
...     max_temp = max(averages.values())
...     
...     # Отбираем все города, у которых температура равна максимальной
...     warmest_cities = [city for city, temp in averages.items() if temp == max_temp]
...     
...     # Сортируем по алфавиту и берем первый
...     warmest_cities.sort()
...     return warmest_cities[0]
