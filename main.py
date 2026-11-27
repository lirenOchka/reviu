def even(nums):
    res = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            res.append(nums[i])
    return res

def unique(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] not in result:
            result.append(nums[i])
    return result

def sum_list(numbers):
    """Возвращает сумму всех чисел. Пустой список → 0."""
    total = 0
    for n in numbers:
        total += n
    return total
