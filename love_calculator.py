import time
import os

print("""
  ,ad8PPPP88b,     ,d88PPPP8ba,
 d8P"      "Y8b, ,d8P"      "Y8b
dP'           "8a8"           `Yd
8(              "              )8
I8                             8I
 Yb,                         ,dP
  "8a,                     ,a8"
    "8a,                 ,a8"
      "Yba             adP"
        `Y8a         a8P'
          `88,     ,88'
            "8b   d8"  LOVE
             "8b d8"   CALCULATOR!
              `888'
""")
first_name = input('Enter name of first lover: ')
second_name = input('Enter name of second lover: ')
together = first_name.lower() + 'loves' + second_name.lower()
counts = {}


def sumallnumbers(numbers_array):
    percentage = []
    if len(numbers_array) == 2:
        return numbers_array
    else:
        left = 0
        right = len(numbers_array) - 1
        result = []
        while left < right:
            result.append(numbers_array[left] + numbers_array[right])
            left += 1
            right -= 1
        if left == right:
            result.append(numbers_array[left])

    numbers_array = result
    result = sumallnumbers(numbers_array)

    for _ in result:
        percentage.append(str(_))
    percentage = ''.join(percentage)
    if len(percentage) > 2:
        percentage = percentage[:2]

    return percentage

for i in together:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

only_numbers = [i for i in counts.values()]
print(f'\n{first_name.capitalize()} loves {second_name.capitalize()}')
print('Checking LOVE...')
print('█▒▒▒▒▒▒▒▒▒ 5%')
time.sleep(2)
os.system('cls')
print('Checking LOVE...')
print('██▒▒▒▒▒▒▒▒ 21%')
time.sleep(2)
os.system('cls')
print('Checking LOVE...')
print('████▒▒▒▒▒▒ 44%')
time.sleep(1)
os.system('cls')
print('Opening vine...')
print('█████▒▒▒▒▒ 50%')
time.sleep(.1)
os.system('cls')
print('Checking LOVE...')
print('███████▒▒▒ 69%')
time.sleep(2)
os.system('cls')
print('Lighting candles...')
print('███████▒▒▒ 77%')
time.sleep(.5)
os.system('cls')
print('Almost there...')
print('█████████▒ 89%')
time.sleep(1)
os.system('cls')
print('You are still here?...')
print('██████████ 91%')
time.sleep(1)
os.system('cls')
print('Checking LOVE...')
print('██████████ 99%')
time.sleep(1.5)
os.system('cls')
print('Final check...')
print('██████████ 99.999%')
time.sleep(4)
os.system('cls')
print(f'DONE. Your love score is {sumallnumbers(only_numbers)}%')
time.sleep(10)
