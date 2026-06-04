import datetime
import os
import time
from playsound import playsound


def get_user_input():
    print("--- Настройка Pomodoro ---")
    name = input("Ваше имя (по-умолчанию Гость): ") or "Гость"
    surname = input("Ваша фамилия: ") or "Без фамилии"
    task = input("Название задачи: ") or "Общая задача"

    # Обработка времени фокусировки
    focus_input = (
        input("Время для фокусировки в минутах (по-умолчанию 25): ") or "25"
    )
    focus_min = int(focus_input)

    # Обработка длины перерыва
    break_input = (
        input("Длина перерыва в минутах (по-умолчанию 5): ") or "5"
    )
    break_min = int(break_input)

    # Обработка количества циклов
    cycles_input = (
        input("Количество циклов (по-умолчанию 4): ") or "4"
    )
    cycles = int(cycles_input)

    return name, surname, focus_min, break_min, cycles, task


def log_event(filename, event_text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {event_text}\n")


def timer_countdown(minutes, label):
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"{label}: {timer}", end="\r")
        time.sleep(1)
        total_seconds -= 1
    print(f"{label}: 00:00" + " " * 10)


def play_notification():
    # Звуковой сигнал (убедитесь, что файл alarm.mp3 находится в папке со скриптом)
    # Если файла нет, можно закомментировать эту строку или использовать стандартный звук ОС
    try:
        playsound("alarm.mp3")
    except Exception:
        print("\a")  # Системный звуковой сигнал, если файл не найден


def main():
    name, surname, focus_min, break_min, cycles, task = get_user_input()
    log_file_name = f"pomodoro_log_{name}_{surname}.txt"

    log_event(
        log_file_name,
        f"Пользователь: {name} {surname} начал задачу: '{task}'. Параметры: фокус {focus_min} мин., перерыв {break_min} мин., циклы: {cycles}.",
    )

    print(
        f"\nЗапуск задачи '{task}'. Всего циклов: {cycles}. Приятной работы!\n"
    )

    for i in range(1, cycles + 1):
        print(f"=== Цикл {i} из {cycles} ===")
        log_event(log_file_name, f"Цикл {i}: начало фокусировки.")

        # Таймер фокусировки
        timer_countdown(focus_min, "Оставшееся время фокуса")
        play_notification()
        log_event(
            log_file_name, f"Цикл {i}: фокусировка завершена. Начало перерыва."
        )

        if i < cycles:
            print("\nВремя для отдыха!")
            # Таймер перерыва
            timer_countdown(break_min, "Оставшееся время перерыва")
            play_notification()
            log_event(
                log_file_name,
                f"Цикл {i}: перерыв завершен. Начало нового цикла фокуса.",
            )
            print("\n")
        else:
            log_event(log_file_name, f"Задача '{task}' полностью завершена.")

    print("\n🎉 Поздравляем! Все циклы задачи успешно завершены.")


if __name__ == "__main__":
    main()
