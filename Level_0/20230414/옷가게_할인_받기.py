# 조건에 맞게 수를 나눈 값을 반환

def solution(price):
    return int(price * 0.95) if price >= 100000 and price < 300000 else int(price * 0.9) if price >= 300000 and price < 500000else int(price * 0.8) if price >= 500000 and price <= 1000000 else int(price)