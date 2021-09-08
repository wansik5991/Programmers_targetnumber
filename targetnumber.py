import os
os.system('cls')


def solution(numbers, target):
    answer = 0
    
    def back(result, point) :
        if point == len(numbers) :
            if result == target :
                nonlocal answer 
                answer += 1
            return 
        
        back(result + numbers[point], point + 1)
        back(result - numbers[point], point + 1)
    back(0, 0)

    return answer

print(solution([1,1], -2))
print(solution([2,3,5,7,9], 2))