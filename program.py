import random

num = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку")

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
    while True:
        a = checker()
        if a < num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif a > num:
            print("Ваше число больше загаданного, попробуйте еще разок")
        else:
            print("Вы угадали, поздравляем!")
            break

compare_nums()




