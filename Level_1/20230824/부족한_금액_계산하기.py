def solution(price, money, count):
    count = (count + 1) * (count / 2)
    price *= count
    
    return price - money if price > money else 0