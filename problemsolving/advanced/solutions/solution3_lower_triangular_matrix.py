# Python3 program to print Lower
# triangular and Upper triangular
# matrix of an array

# Function to form lower triangular
# matrix
def lower(matrix, row, col):
    for i in range(0, row):

        for j in range(0, col):

            if (i < j):

                print("0", end=" ");

            else:
                print(matrix[i][j],
                      end=" ");

        print(" ");


# Function to form upper triangular matrix
def upper(matrix, row, col):
    for i in range(0, row):

        for j in range(0, col):

            if (i > j):
                print("0", end=" ");

            else:
                print(matrix[i][j],
                      end=" ");

        print(" ");


# Driver Code
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]];
row = 3;
col = 3;

print("Lower triangular matrix: ");
lower(matrix, row, col);

print("Upper triangular matrix: ");
upper(matrix, row, col);