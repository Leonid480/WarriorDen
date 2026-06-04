import time
import os
import datetime

def run_timer():
    # 1. Принимаем данные от пользователя
    first_name = input("Введите ваше Имя: ")
    last_name = input("Введите вашу Фамилию: ")
    
    print("\nНастройка таймера:")
    try:
        hours = int(input("Часы: "))
        minutes = int(input("Минуты: "))
        seconds = int(input("Секунды: "))
    except ValueError:
        print("Ошибка ввода. Пожалуйста, вводите только целые числа.")
        return

    # 2. Логирование запуска программы
    log_filename = "program_log.txt"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Открываем файл для добавления записи
    with open(log_filename, "a", encoding="utf-8") as log_file:
        log_file.write(f"Пользователь: {first_name} {last_name} | Запуск: {current_time}\n")
    
    # 3. Переводим все введенные значения в секунды
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    if total_seconds <= 0:
        print("Указано нулевое время.")
        return

    print("\nТаймер запущен!")
    
    # 4. Обратный отсчет
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        hrs, mins = divmod(mins, 60)
        
        # Вывод времени в формате ЧЧ:ММ:СС
        timer_display = f'{hrs:02d}:{mins:02d}:{secs:02d}'
        print(timer_display, end='\r')  # \r позволяет обновлять строку в той же линии
        
        time.sleep(1)
        total_seconds -= 1
        
    print("Время вышло!                 ")

if __name__ == "__main__":
    run_timer()
