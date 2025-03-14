import numpy as np

# 1. Define two custom numpy arrays, say A and B. 
# Generate two new numpy arrays by stacking A and B vertically and horizontally.
#NOTE: I don't understand the question here, so I interpreted it as well as I could
#This is what I think you meant
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

A = iris_2d[:5] 
B = iris_2d[5:10]
Vert = np.vstack((A,B))
Horiz = np.hstack((A,B))
# print("A", A)
# print("B", B)
print("Vertically \n", Vert)
print("Horizonatlly: \n", Horiz)


# 2. Find common elements between A and B. 
# [Hint : Intersection of two sets]
overlap = []
elem = 0

for item1 in A:
    for num1 in item1:
        for item2 in B:
            for num2 in item2:
                if num2 == num1:
                    overlap.append(num1)

print(overlap)


# 3. Extract all numbers from A which are within a specific range. 
# eg between 5 and 10. [Hint: np.where() might be useful or boolean masks]
indices = np.where((A >= 5) & (A <= 10))
filtered_values = A[indices]

print(filtered_values)

# 4. Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and 
# sepallength (1st column) < 5.0
iris_2d = np.vstack((A, B))  # Stack A and B vertically

condition = (iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)

filtered_rows = iris_2d[np.where(condition)]

print(filtered_rows)