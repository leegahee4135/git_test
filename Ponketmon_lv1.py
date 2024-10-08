def solution(nums):
    answer = 0

    dict = {}
    max_num = len(nums)/2

    for num in nums:
        if num not in dict:
            dict[str(num)] = 1
        elif num in dict:
            dict[str(num)] += 1

    total_num_of_ponketmon = len(dict.keys())

    if total_num_of_ponketmon >= max_num:
        return max_num
    else:
        return total_num_of_ponketmon

    return answer