from random import randint
import random
from time import sleep

array = []
for c in range(11): array.append(randint(0, 100))

def titleTop(): print(), print('-' * 40)
def titleDown(): print('-' * 40, '\n\n')


from bubble import bubble_sort

titleTop()
print('Method in Bubble'.center(40))
titleDown()
random.shuffle(array)
print('Sem modificação:', array)
print('Modificado:', bubble_sort(array))
sleep(1)

from insertion import insertion_sort
titleTop()
print('Method in Insertion'.center(40))
titleDown()
random.shuffle(array)
print('Sem modificação:', array)
print('Modificado:', insertion_sort(array))
sleep(1)

from select_ import selection_sort
titleTop()
print('Method in Select'.center(40))
titleDown()
random.shuffle(array)
print('Sem modificação:', array)
print('Modificado:', selection_sort(array))
sleep(1)

from merge import merge_sort
titleTop()
print('Method in Merge'.center(40))
titleDown()
random.shuffle(array)
print('Sem modificação:', array)
print('Modificado:', merge_sort(array))
sleep(1)

from quick import quick_sort
titleTop()
print('Method in Quick'.center(40))
titleDown()
random.shuffle(array)
print('Sem modificação:', array)
print('Modificado:', quick_sort(array))
sleep(1)

from shell import shell_sort
titleTop()
print('Method in Shell'.center(40))
titleDown()
random.shuffle(array)
print('Sem modificação:', array)
print('Modificado:', shell_sort(array))