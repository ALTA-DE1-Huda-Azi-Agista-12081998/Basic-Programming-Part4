def play_with_asterisk(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '* ' * i
        print(spaces + stars)

if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """
