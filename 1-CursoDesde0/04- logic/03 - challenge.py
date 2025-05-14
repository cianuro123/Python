import os
os.system("cls")

"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y 
devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""
nums = [4, 4, 6, 2]
goal = 8


# def sumar(nums, goal):
#     if len(nums) == 0:
#         return None
#     for i in range(len(nums)):
#         for j in range(len(nums)+1):
#             if nums[i] + nums[j] == goal:
#                 return i, j

nums = [4, 5, 6, 2]
goal = 8


def find_numbers(nums, goal):
    seen = {}
    if len(nums) == 0:
        return None
    for index, value in enumerate(nums):
        missing = goal - value
        if missing in seen:
            return index, value
        else:
            seen += seen[index]
            


print(find_numbers(nums, goal))
# resultado = sumar(nums, goal)
# print(resultado)
