import json


def sortlists(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        data = json.loads(file.read())

    list1 = data['list1']
    list2 = data['list2']

    result = []

    max_length = max(len(list1), len(list2))

    for i in range(max_length):
        # Добавление элемента из первого списка на нечетные позиции
        if i % 2 == 0 and i < len(list1):
            result.append(list1[i])
        # Добавление элемента из второго списка на четные позиции
        elif i % 2 == 1 and i < len(list2):
            result.append(list2[i])
        # Добавление элемента из более длинного списка на недостающие позиции
        elif len(list1) > len(list2):
            result.append(list1[i])
        else:
            result.append(list2[i])

    with open(output_filename, 'w') as file:
        file.write(str(result))

    print("Лист 1:", list1, "\nЛист 2:", list2, "\nРезультат:", str(result))


input_file = "input.txt"
output_file = "result.txt"

sortlists(input_file, output_file)
