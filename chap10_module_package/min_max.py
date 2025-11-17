"""최솟값과 최댓값을 구하는 모듈"""

def min_max2(a: 'value', b: 'value') -> 'value':
    """a와b의 최소값과 최댓값을 구하여 리턴"""
    return min(a, b), max(a, b)

def min_max3(a: 'value', b: 'value', c: 'value') -> 'value':
    """a, b, c의 최솟값과 최댓값을 구하여 리턴"""
    return min(a, b, c), max(a, b, c)

if __name__ == '__main__':
    x = int(input('정수 x：'))
    y = int(input('정수 y：'))
    z = int(input('정수 z：'))

    print('x와 y의 최솟값은 {}이고, 최댓값은 {}입니다.'.format(*min_max2(x, y)))
    print('y와 z의 최솟값은 {}이고, 최댓값은 {}입니다.'.format(*min_max2(y, z)))
    print('x와 z의 최솟값은 {}이고, 최댓값은 {}입니다.'.format(*min_max2(x, z)))
    print('x, y, z의 최솟값은 {}이고, 최댓값은 {}입니다.'.format(*min_max3(x, y, z)))
