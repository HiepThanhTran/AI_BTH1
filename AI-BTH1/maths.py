import math
import numpy as np
import matplotlib.pyplot as plt


def compute_norm(vector):
    norm = math.sqrt(sum([x ** 2 for x in vector]))
    return norm


def normalize_vector(vector):
    norm = compute_norm(vector)
    normalized_vector = [x / norm for x in vector]
    return normalized_vector


def cau_5():
    x = [3, 7]
    norm_x = compute_norm(x)
    print("Norm of x:", norm_x)
    normalized_x = normalize_vector(x)
    print("Normalized vector x:", normalized_x)


def vector_addition(a, b):
    return [x + y for x, y in zip(a, b)]


def vector_subtraction(a, b):
    return [x - y for x, y in zip(a, b)]


def cau_6():
    a = [10, 15]
    b = [8, 2]
    c = [1, 2, 3]
    sum_ab = vector_addition(a, b)
    print("a + b:", sum_ab)
    diff_ab = vector_subtraction(a, b)
    print("a - b:", diff_ab)
    diff_ac = vector_subtraction(a, c)
    print("a - c:", diff_ac)


def cau_7():
    a = [10, 15]
    b = [8, 2]
    dot_product = np.dot(a, b)
    print("Tích vô hướng của a và b:", dot_product)


def cau_8():
    a = np.array([[2, 4, 9], [3, 6, 7]])
    print(a)
    rank_a = np.linalg.matrix_rank(a)
    shape_a = a.shape
    print("Hạng của A:", rank_a)
    print("Dạng của A:", shape_a)
    value_7 = a[1, 2]
    print("Giá trị 7 trong A:", value_7)
    second_column = a[:, 1]
    print("Cột thứ 2 trong A:", second_column)


def cau_9():
    matrix = np.random.randint(-10, 10, (3, 3))
    print("Ma trận:")
    print(matrix)


def cau_10():
    identity_matrix = np.eye(3)
    print("Ma trận:")
    print(identity_matrix)


def cau_11():
    matrix = np.random.randint(1, 10, (3, 3))
    print("Ma trận:")
    print(matrix)
    trace_a = np.trace(matrix)
    print("Tổng đường chéo chính (A):", trace_a)
    trace_b = 0
    for i in range(3):
        trace_b += matrix[i][i]
    print("Tổng đường chéo chính (B):", trace_b)


def cau_12():
    diagonal_matrix = np.diag([1, 2, 3])
    print("Ma trận đường chéo:")
    print(diagonal_matrix)


def cau_13():
    a = np.array([[1, 1, 2], [2, 4, -3], [3, 6, -5]])
    print(a)
    determinant_a = np.linalg.det(a)
    print("Định thức của A:", determinant_a)


def cau_14():
    a1 = [1, -2, -5]
    a2 = [2, 5, 6]

    M = np.column_stack((a1, a2))
    print(M)


def cau_15():
    y = np.arange(-5, 6)

    y_squared = y ** 2

    plt.plot(y, y_squared)
    plt.xlabel('y')
    plt.ylabel('y^2')
    plt.title('Plot of y^2')
    plt.grid(True)
    plt.show()


def cau_16():
    values = np.linspace(0, 32, 5)

    print(values)


def cau_17():
    x = np.linspace(-5, 5, 50)

    y = x ** 2

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of y = x^2')
    plt.grid(True)
    plt.show()


def cau_18():
    x = np.linspace(0, 5, 100)

    y = np.exp(x)

    plt.plot(x, y, label='y = exp(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of y = exp(x)')
    plt.legend()
    plt.grid(True)
    plt.show()


def cau_19():
    x = np.linspace(0.1, 5, 100)

    y = np.log(x)

    plt.plot(x, y, label='y = log(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of y = log(x)')
    plt.legend()
    plt.grid(True)
    plt.show()


def cau_20():
    # Define the x-axis range for a smoother curve
    x = np.linspace(0, 5, 100)

    # Calculate functions
    y1 = np.exp(x)
    y2 = np.exp(2 * x)
    y3 = np.log(x)  # Avoid log(0) error with starting point > 0
    y4 = np.log(2 * x)

    # Create the subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))  # Adjust figsize for dual plots

    # Plot exponential functions on the first subplot
    ax1.plot(x, y1, label='y = exp(x)')
    ax1.plot(x, y2, label='y = exp(2x)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Exponential Functions')
    ax1.legend()
    ax1.grid(True)

    # Plot logarithmic functions on the second subplot
    ax2.plot(x[1:], y3[1:], label='y = log(x)')  # Skip x=0 for log(x)
    ax2.plot(x, y4, label='y = log(2x)')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_title('Logarithmic Functions')
    ax2.legend()
    ax2.grid(True)

    # Tighten spacing between plots (optional)
    plt.tight_layout()

    plt.show()


if __name__ == '__main__':
    cau_5()
    cau_6()
    cau_7()
    cau_8()
    cau_9()
    cau_10()
    cau_11()
    cau_12()
    cau_13()
    cau_14()
    cau_15()
    cau_16()
    cau_17()
    cau_18()
    cau_19()
    cau_20()
