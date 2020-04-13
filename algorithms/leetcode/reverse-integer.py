'''
Given an integer, reverse it and return the new reversed value.
'''

class reverseSolution:
    def reverse(self, x: int) -> int:
        strX = str(x)

        if x < 0:
            reversedString = ""
            stringToReverse = strX[1:len(strX)]
            for index in range(len(stringToReverse) - 1, -1, -1):
                reversedString = reversedString + stringToReverse[index]

            return int("-" + reversedString)

        else:
            reversedString = ""
            for index in range(len(strX) - 1, -1, -1):
                reversedString = reversedString + strX[index]

            return int(reversedString)



newSolution = reverseSolution()

# print(newSolution.reverse(123))
# print(newSolution.reverse(-123))
print(newSolution.reverse(1534236469))

