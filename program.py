import random


print("Добро пожаловать в числовую угадайку!")
print("Введите имя!")
name = input()
rng = int(input("Введите максимальное число"))
num = random.randint(1, rng)



def is_valid(a):
    return a.isdigit() and 1 <= int(a) <= rng

def checker():
    while True:
        numb = input()
        if is_valid(numb):
            return int(numb)
        else:
            print(f"A может быть все-таки введем целое число от 1 до {rng}?")

def compare_nums():
    print(f"Приветствую {name}! Введите число от 1 до {rng}!")
    count = 0
    while True:
        a = checker()
        count += 1
        if a < num:
            print(f"{name}, ваше число меньше загаданного, попробуйте еще разок!")
        elif a > num:
            print(f"{name}, ваше число больше загаданного, попробуйте еще разок!")
        else:
            print(f"Вы угадали за {count} попыток, поздравляем {name}!")
            
            print("Вы хотите начать заново?(д/н)")
            accept = input()
            while True:
                if accept == 'д':
                    compare_nums()
                elif accept == 'н':
                    print("Пока-пока")
                    break
                break
            break
            

compare_nums()



