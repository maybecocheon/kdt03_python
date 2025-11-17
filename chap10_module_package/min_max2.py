"""두 값의 최솟값과 최댓값 구하기"""

def min_max2(a, b):
    """a와 b의 최솟값과 최댓값을 구하여 리턴"""
    return (a, b) if a < b else (b, a)

if __name__ == '__main__':
    n1 = int(input('정수 n1：'))
    n2 = int(input('정수 n2：'))

    minimum, maximum = min_max2(n1, n2)
    print('최솟값은', minimum, '이고 최댓값은', maximum, '입니다.')

