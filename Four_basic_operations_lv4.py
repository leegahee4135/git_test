def apply_operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b

def solution(arr):
    ## 내가 처음 푼 풀이 ##
    ## 문제점 1: dp방법을 쓰지 않음. 즉 점화식이 없고 이전 결과를 활용하지 않는 방법임 -> 매우 비효율적으로 효율성 0이고, 심지어 재귀 써서 연산량 더 많아질 수 있음
    ## 문제점 2: 최대값만을 계산하고 있기 때문에 - 연산이 언제 되는지에 따라 달라지는 결과값을 고려하지 못함

    answer = -1

    if len(arr) == 1:
        return int(arr[0])

    N = len(arr)//2

    tmp = []
    for i in range(N):
        arr1 = arr[: 2*i +1]
        arr2 = arr[2*i +2 :]

        tmp.append(apply_operation(solution(arr1), solution(arr2), arr[2*i+1]))

    answer = max(tmp)
    return answer

arr = ["5", "-", "3", "+", "1", "+", "2", "-", "4"]
result = solution(arr)
print(result)


#---------------------------- GPT 쓴 풀이
def apply_operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b


# 최댓값과 최솟값을 구하는 함수
def solution(arr):
    N = len(arr)

    # 메모이제이션 테이블
    max_dp = [[None] * N for _ in range(N)]
    min_dp = [[None] * N for _ in range(N)]

    # 초기값 설정
    for i in range(0, N, 2):
        max_dp[i][i] = int(arr[i])
        min_dp[i][i] = int(arr[i])

    # 길이 2 이상인 구간을 처리
    for length in range(3, N + 1, 2):  # 연산자는 2씩 증가
        for i in range(0, N - length + 1, 2):
            j = i + length - 1
            max_dp[i][j] = float('-inf')
            min_dp[i][j] = float('inf')

            # 구간을 나눠서 최댓값과 최솟값 계산
            for k in range(i + 1, j, 2):
                operator = arr[k]
                left_max = max_dp[i][k - 1]
                left_min = min_dp[i][k - 1]
                right_max = max_dp[k + 1][j]
                right_min = min_dp[k + 1][j]

                max_dp[i][j] = max(max_dp[i][j],
                                   apply_operation(left_max, right_max, operator),
                                   apply_operation(left_max, right_min, operator),
                                   apply_operation(left_min, right_max, operator),
                                   apply_operation(left_min, right_min, operator))

                min_dp[i][j] = min(min_dp[i][j],
                                   apply_operation(left_max, right_max, operator),
                                   apply_operation(left_max, right_min, operator),
                                   apply_operation(left_min, right_max, operator),
                                   apply_operation(left_min, right_min, operator))

    return max_dp[0][N - 1]