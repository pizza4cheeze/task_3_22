def find_longest_couple(arr):
    arr = [sorted(row) for row in arr]
    # print(arr)
    arr = sorted(arr)
    # print(arr)
    lengths = []
    for row in range(len(arr)):
        for subrow in range(row + 1, len(arr)):
            if arr[row][1] < arr[subrow][0]:
                lengths.append(arr[row][1] - arr[row][0] + (arr[subrow][1] - arr[subrow][0]))
            else:
                lengths.append(max(arr[subrow][1], arr[row][1]) - arr[row][0])
    # print(lengths)
    return max(lengths)


def read_file_to_array(input_file):
    array = []
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            row = line.split(', ')
            row = [int(value) for value in row]
            array.append(row)
    return array


filename = 'input3.txt'
output_arr = read_file_to_array(filename)
res = find_longest_couple(output_arr)
print(res, output_arr)


# input_arr = [
#     [5, 8],
#     [3, 7],
#     [1, 6],
#     [2, 10],
#     [4, 9],
#     [6, 5],
#     [8, 3],
#     [7, 4],
#     [10, 2],
#     [9, 1],
#     [11, 14],
#     [12, 12],
#     [13, 11],
#     [15, 13],
#     [14, 15],
#     [16, 18],
#     [17, 16],
#     [18, 17],
#     [20, 19],
#     [19, 20],
#     [21, 22],
#     [23, 21],
#     [22, 23],
#     [24, 25],
#     [25, 24],
#     [30, 40]
# ]
# print(find_longest_couple(input_arr))