import numpy as np


def __sum():
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    result = a + b
    print(result)


def __matrix():
    m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    v = np.array([1, 2, 3])
    rank_m = np.linalg.matrix_rank(m)
    shape_m = m.shape
    shape_v = v.shape
    print("Giới hạn của ma trận M:", rank_m)
    print("Dạng của ma trận M:", shape_m)
    print("Dạng của vector V:", shape_v)


def new_matrix():
    m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix = m + 3
    print("Ma trận M:")
    print(m)
    print("\nMa trận mới sau khi cộng thêm 3:")
    print(matrix)


def transpose_matrix():
    m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    v = np.array([1, 2, 3])
    m_transpose = np.transpose(m)
    v_transpose = np.transpose(v)
    print("Ma trận M:")
    print(m)
    print("\nBiến đổi ma trận M:")
    print(m_transpose)
    print("\nVector v:")
    print(v)
    print("\nBiến đổi vector v:")
    print(v_transpose)


if __name__ == '__main__':
    __sum()
    __matrix()
    new_matrix()
    transpose_matrix()
