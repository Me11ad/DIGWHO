import random

num = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку!")
print("Введите имя!")
name = (input())


def is_valid(a):
    return a.isdigit() and 1 <= int(a) <= 100

def checker():
    while True:
        numb = input()
        if is_valid(numb):
            return int(numb)
        else:
            print("A может быть все-таки введем целое число от 1 до 100?")

def compare_nums():
    print(f"Приветствую {name}! Введите число от 1 до 100!")
    while True:
        a = checker()
        if a < num:
            print(f"{name}, ваше число меньше загаданного, попробуйте еще разок!")
        elif a > num:
            print(f"{name}, ваше число больше загаданного, попробуйте еще разок!")
        else:
            print(f"Вы угадали, поздравляем {name}!")
            
            print("Вы хотите начать заново?(Д/Н)")
            accept = (input())
            while True:
                if accept == 'Д':
                    compare_nums()
                elif accept == 'Н':
                    print("Пока-пока")
                    break
                break
            break
            

compare_nums()



