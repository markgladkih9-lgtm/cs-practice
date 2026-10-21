Python 3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Enter "help" below or click "Help" above for more information.
import sys
from stats import average_by_city, read_valid, warmest_city, parse_record
... 
... def main():
...     # Читаем все строки из стандартного ввода
...     lines = sys.stdin.read().splitlines()
...     
...     valid_count = 0
...     error_count = 0
...     valid_records = []
...     
...     for line in lines:
...         # Пустые строки пропускаются молча, они не считаются ни ошибкой, ни успехом
...         if not line.strip():
...             continue
...             
...         try:
...             record = parse_record(line)
...             valid_records.append(record)
...             valid_count += 1
...         except ValueError:
...             error_count += 1
...             
...     # Вычисляем средние температуры и находим самый теплый город
...     averages = average_by_city(valid_records)
...     warmest = warmest_city(valid_records)
...     
...     # Получаем среднюю температуру самого теплого города
...     if warmest:
...         warmest_avg = averages[warmest]
...     else:
...         warmest_avg = 0.0
... 
...     # Печатаем строго три строки отчета
...     print(valid_count)
...     print(error_count)
...     print(f"{warmest_avg:.1f}")
... 
... if __name__ == "__main__":
...     main()
