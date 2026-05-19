import os
import re
from collections import Counter


def process_imdb_data():
    input_path = "./data5/ratings.list"

  
    if not os.path.exists(input_path):
        print(f"Ошибка: Файл {input_path} не найден!")
        return

  
    with open(input_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    movies = []
    ratings = []
    years = []

  
    pattern = re.compile(r"^\d+\.\s+(.+?)\s+\((\d{4})\)\s+(\d+\.\d+|\d+)")

   
    for line in lines:
        match = pattern.search(line.strip())
        if match:
            title, year, rating = match.groups()
            movies.append(title)
            ratings.append(float(rating))
            years.append(int(year))

       
        if len(movies) == 250:
            break

    
    if not movies:
        print("Ошибка: Не удалось извлечь данные о фильмах. Проверьте формат файла.")
        return

    
    with open("top250_movies.txt", "w", encoding="utf-8") as f_movies:
        for movie in movies:
            f_movies.write(f"{movie}\n")

    
    rating_counts = Counter(ratings)
    year_counts = Counter(years)

   
    with open("ratings.txt", "w", encoding="utf-8") as f_ratings:
        for rate in sorted(rating_counts.keys(), reverse=True):
            stars = "*" * rating_counts[rate]
            f_ratings.write(f"{rate}: {stars}\n")

   
    with open("years.txt", "w", encoding="utf-8") as f_years:
        for yr in sorted(year_counts.keys()):
            stars = "*" * year_counts[yr]
            f_years.write(f"{yr}: {stars}\n")

    print("Обработка завершена успешно! Созданы 3 файла.")


if __name__ == "__main__":
    process_imdb_data()
