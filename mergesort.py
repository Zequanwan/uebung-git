from typing import List

def merge_sort(data: List[int]) -> List[int]:
    """
    Sorts a list of integers using the merge sort algorithm.

    Args:
        data: A list of integers to sort.

    Returns:
        A new list containing all elements from `data` in ascending order.
    """
    # 1) 基本情况：长度 ≤ 1 时直接返回拷贝
    if len(data) <= 1:
        return data.copy()

    # 2) 分割列表
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    # 3) 合并两个已排序子列表
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merges two sorted lists into one sorted list, preserving stability.

    Args:
        left: First sorted list.
        right: Second sorted list.

    Returns:
        A merged, sorted list containing all elements from `left` and `right`.
    """
    merged: List[int] = []      # 4) 有意义的变量名
    i = j = 0

    # 5) 使用 <= 保持稳定性：相等时优先选 left
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # 6) 追加剩余元素
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    # 7) 主入口示例，并保持原列表不被修改
    sample = [5, 2, 9, 1, 5, 6]
    print(f"Original: {sample}")
    sorted_list = merge_sort(sample)
    print(f"Sorted:   {sorted_list}")

