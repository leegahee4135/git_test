import heapq

def solution(jobs):
    answer = 0

    current_time, total_time = 0, 0
    start = -1
    heap = []
    for _ in range(len(jobs)):

        # start ~ current_time 안에 요청된 작업들을 힙에 넣기
        for job in jobs:
            if start < job[0] <= current_time:
                heapq.heappush([job[1], job[0]]) # 작업 소요시간, 요청시간 순으로 넣기

        if heap:
            duration, request_time = heapq.heappop(heap)
            start = current_time # 작업을 시작하는 시간으로, 현재 작업 하나 수행하려고 하니까 이걸로 업데이트 해줘야 함
            current_time += duration # 작업이 끝난 시간으로, 소요시간을 더해준다
            total_time += current_time - request

        else:
            current_time += 1

    return answer