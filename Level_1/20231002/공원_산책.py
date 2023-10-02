def Mysolution(park, routes):
    array = [[i for i in j] for j in park]
    route = [i.split() for i in routes]
    
    for idx1, i in enumerate(array) :
        for idx2, j in enumerate(i) :
            if array[idx1][idx2] == 'S' :
                point = [idx1, idx2]
    
    for i in route :
        try :
            if i[0] == 'E' :
                for e in range(1, int(i[1])+ 1) :
                    if array[point[0]][point[1] + e] == 'X' : raise IndexError
                    if point[1] + int(i[1]) >= len(array[0]) : raise IndexError
                
                array[point[0]][point[1] + int(i[1])] = 'S'
                array[point[0]][point[1]] = 'O'
                point[1] += int(i[1])
                
            if i[0] == 'W' :
                for w in range(1, int(i[1]) + 1) :
                    if array[point[0]][point[1] - w] == 'X' : raise IndexError
                    if point[1] - int(i[1]) < 0 : raise IndexError
                
                array[point[0]][point[1] - int(i[1])] = 'S'
                array[point[0]][point[1]] = 'O'
                point[1] -= int(i[1])
                
            if i[0] == 'S' :
                for s in range(1, int(i[1]) + 1) :
                    if array[point[0] + s][point[1]] == 'X' : raise IndexError
                    if point[0] + int(i[1]) >= len(array[0]) : raise IndexError
                
                array[point[0] + int(i[1])][point[1]] = 'S'
                array[point[0]][point[1]] = 'O'
                point[0] += int(i[1])
                
            if i[0] == 'N' :
                for n in range(1, int(i[1]) + 1) :
                    if array[point[0] - n][point[1]] == 'X' : raise IndexError
                    if point[0] - int(i[1]) < 0 : raise IndexError
                        
                array[point[0] - int(i[1])][point[1]] = 'S'
                array[point[0]][point[1]] = 'O'
                point[0] -= int(i[1])
                
        except IndexError : continue
    
    return point

# 아래의 코드는 직접 푼 것이 아닌 다른 사람의 풀이를 그대로 가져온 것
# 클래스에 익숙하지 않아서 가져와 봤습니다

class Dog:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = {"N": (-1, 0), "W": (0, -1), "E": (0, 1), "S": (1, 0)}

    def move(self, park, direction, distance):
        i, j = self.g[direction]
        x, y = self.x + (i * distance), self.y + (j * distance)
        if x < 0 or y < 0 or x >= len(park) or y >= len(park[0]):
            return park
        elif "X" in park[x][min(self.y, y) : max(self.y, y) + 1] or "X" in [
            row[y] for row in park[min(self.x, x) : max(self.x, x)]
        ]:
            return park
        park[self.x][self.y] = "O"
        park[x][y] = "S"
        self.x = x
        self.y = y
        return park

    @classmethod
    def detect_start_dogs_location(self, park):
        for i, row in enumerate(park):
            for j, item in enumerate(row):
                if item == "S":
                    return i, j


def solution(park, routes):
    park = [list(row) for row in park]
    x, y = Dog.detect_start_dogs_location(park)

    dog = Dog(x, y)

    for route in routes:
        direction, distance = route.split()
        park = dog.move(park, direction, int(distance))

    return [dog.x, dog.y]