from collections import deque
def bfs(numbers, target):
    answer = 0

    queue = deque()
    queue.append((numbers[0], 0))
    queue.append((-numbers[0], 0))

    while (queue):
        sum, lev = queue.popleft()
        # print(sum, lev)

        if sum == target and lev == len(numbers) - 1:
            answer += 1
            continue
        elif sum != target and lev == len(numbers) - 1:
            continue

        newnum = numbers[lev + 1]
        queue.append((sum + newnum, lev + 1))
        queue.append((sum - newnum, lev + 1))

    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print("The number of solutions getting target number with numbers list is ", bfs(numbers, target))