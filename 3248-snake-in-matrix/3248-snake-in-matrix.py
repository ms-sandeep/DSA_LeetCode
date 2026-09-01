class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        i, j = 0, 0

        for command in commands:
            if command == "LEFT" :
                j -= 1
            elif command == "RIGHT":
                j += 1
            elif command == "UP":
                i -=1
            elif command == "DOWN":
                i += 1

        return (i * n) + j
        