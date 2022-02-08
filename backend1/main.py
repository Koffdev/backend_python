MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'
                   }


def task1(english_text):
    morse_text = ''
    for letter in english_text.upper():
        if letter != ' ':
            morse_text += MORSE_CODE_DICT[letter] + ' '
        else:
            morse_text += ' '
    return morse_text


def task2():
    a = b = 1
    print(a, b, end=' ')
    for i in range(2, 100):
        a, b = b, a + b
        print(b, end=' ')


def task3(first_list, second_list):
    new_list = []
    length = len(first_list)
    for i in range(length):
        new_list.append(first_list[i])
        new_list.append(second_list[i])
    return new_list


def task4(my_list1):
    return my_list1[1::2]


def task5(my_list2):
    new_list = []
    for item in my_list2[::-1]:
        new_list.append(item[::-1])
    return new_list


def task6(my_list3):
    return my_list3[::-1]


message = input("Enter english text")

print('Task1', task1(message))

print('Task2', end=' ')
task2()

list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3, 4]

print('Task3', task3(list1, list2))

my_first_list = ['one', 'two', 'three', 'four', 'five']
my_second_list = [1, '23', 2, 5, 'car', 'plane', 'apple', 9]

print('Task4', task4(my_second_list))

print('Task5', task5(my_first_list))

print('Task6', task6(my_first_list))
