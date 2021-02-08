# parsing the file will give us a staggered 2d array in the general form
# x
# xx
# xxx
# ....
grid = []

f = open("triangle.txt")

#reading each line in .txt
for line in f:
    arr = line.split() #creating an array - each element is the string representation of the integer
    for i in range(len(arr)):
        arr[i] = int(arr[i]) #casting it to an int so its more workable

    grid.append(arr) #adding it to the grid array

f.close()

#starting from the second to last row in the grid (and working our way up)
#we want to loop through each element in the row, and add to it the larger adjacent element,
#that is, the element right below it and the element NEXT to the element right below it.
for i in range(len(grid) - 2, -1, -1):
    for j in range(len(grid[i])):
        left = grid[i + 1][j]
        right = grid[i + 1][j + 1]
        grid[i][j] += max(left, right)

#this bottom up approach leads us to have the answer in the 1st cell in the 2d array - return it
print(grid[0][0])