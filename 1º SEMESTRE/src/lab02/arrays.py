def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список не должен быть пустым")
    return (min(nums), max(nums))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))


def flatten(mat: list[list | tuple]) -> list:
    flat_list = []
    for element in mat:
        if isinstance(element, (list, tuple)):
            flat_list.extend(element)
        else:
            raise TypeError("Элемент должен быть списком или кортежем")
    return flat_list

if __name__ == "__main__":
    print(min_max([]))  # (1, 5)
    print(unique_sorted([3, 1, 2, 2, 3]))  # [1, 2, 3]
    print(flatten([[1, 2], (3, 4), [5]]))  # [1, 2, 3, 4, 5]cls
