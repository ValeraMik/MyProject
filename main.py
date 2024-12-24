import threading
import time

def calculate_square(numbers):
    """
    Потік 1: Обчислення квадратів чисел.
    """
    for n in numbers:
        print(f"Thread 1 (Square): {n}^2 = {n ** 2}")
        time.sleep(1)

def calculate_cube(numbers):
    """
    Потік 2: Обчислення кубів чисел.
    """
    for n in numbers:
        print(f"Thread 2 (Cube): {n}^3 = {n ** 3}")
        time.sleep(1)

if __name__ == "__main__":
    # Список чисел для обчислення
    numbers = [1, 2, 3, 4, 5]

    # Створення потоків
    thread1 = threading.Thread(target=calculate_square, args=(numbers,))
    thread2 = threading.Thread(target=calculate_cube, args=(numbers,))

    # Запуск потоків
    thread1.start()
    thread2.start()

    # Очікування завершення потоків
    thread1.join()
    thread2.join()

    print("Both threads have finished their calculations!")
