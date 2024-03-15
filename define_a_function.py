import numpy as np


def __sum():
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    sum = a + b
    print(sum)


def __matrix():
    M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    v = np.array([1, 2, 3])
    rank_M = np.linalg.matrix_rank(M)
    shape_M = M.shape
    shape_v = v.shape
    print("Giới hạn của ma trận M:", rank_M)
    print("Dạng của ma trận M:", shape_M)
    print("Dạng của vector V:", shape_v)


def new_matrix():
    M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    new_matrix = M + 3
    print("Ma trận M:")
    print(M)
    print("\nMa trận mới sau khi cộng thêm 3:")
    print(new_matrix)


def transpose_matrix():
    M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    v = np.array([1, 2, 3])
    M_transpose = np.transpose(M)
    v_transpose = np.transpose(v)
    print("Ma trận M:")
    print(M)
    print("\nBiến đổi ma trận M:")
    print(M_transpose)
    print("\nVector v:")
    print(v)
    print("\nBiến đổi vector v:")
    print(v_transpose)


if __name__ == '__main__':
    __sum()
    __matrix()
    new_matrix()
    transpose_matrix()