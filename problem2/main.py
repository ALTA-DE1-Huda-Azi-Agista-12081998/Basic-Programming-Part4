def draw_xyz(N):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            position = (i + j - 1) % 3
            if position == 1:
                print('Y', end=' ')
            elif position == 2:
                print('Z', end=' ')
            else:
                print('X', end=' ')
        print()

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """