def solution(order):
    return len([i for i in str(order) if int(i) % 3 == 0])

print(solution(15))