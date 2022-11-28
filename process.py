from multiprocessing import Process
from RandomWordGenerator import RandomWord
import multiprocessing
import random
from typing import List
import os 

def file_set():
    file_name = str(os.getpid()) + '.txt'
    random_file(file_name)
    file_red(file_name)

def random_file(file_name):
    random_word = RandomWord(constant_word_size = False)
    with open(file_name, 'w+') as file:
        random_range = random.randint(100000, 5000000)
        for i in range(random_range):
            file.write(random_word.generate() + '\n')

def file_red(file_name):
    with open(file_name, 'r') as file:
        a, b, c, d = analiz(file)
         
        result_analiz(file_name, a, b, c, d)

def strip(line):
    line.strip()
    return len(line)


def max_len(line):
    max_l = 0
    array = line.split('\n')
    for word in array:
        if (len(word) > max_l):
            max_l = len(word)
    return max_l

def min_len(line):
    min_l = 10
    array = line.split('\n')
    for word in array:
        if (len(word) < min_l):
            min_l = len(word)
    return min_l

def count(line):
    word_range = line.split('\n')
    return len(word_range)
    

def analiz(file):
    symwol = 0
    maximum = 0
    minimum = 10
    small = 0
    big = 1
    word_count = 0
    for line in file:
        symwol += strip(line)
        small = max_len(line)
        if small > maximum:
            maximum = small
            small = 0
        small = min_len(line)
        if small < minimum:
            minimum = big
            big = 1
        word_count += count(line)
    
    
    return symwol, maximum, minimum, word_count
            

if __name__ == '__main__':
    list_process :List[Process] = []
    cpu_count = multiprocessing.cpu_count() // 2
    for i in range(cpu_count):
        proc = Process(target= file_set)
        list_process.append(proc)
        list_process[i].start()

    for i in range(cpu_count):
        list_process[i].join()

def result_analiz(file_name, a, b, c, d):
    res = f"""
Анализ файла: {file_name}
Символов: {a}
Самое большое слово: {b}
Самое маленькое слово: {c}
Средний размер слова: {a // d}
"""
    print(res)