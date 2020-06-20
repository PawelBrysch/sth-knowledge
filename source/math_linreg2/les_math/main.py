import numpy as np

# array1 = np.array([
#     [2, -2, 1],
#     [1, 2, 2],
#     [2, 1, -2]
# ])



array2 = np.array([
    [0.68567, 0.12975, -0.71626],
    [0.14807, 0.93855, 0.31176],
    [0.71269, -0.31982, 0.62433]
])
# array2 = np.array([
#     [0.68567, 0.12975],
#     [0.14807, 0.93855],
#     [0.71269, -0.31982]
# ])
array2_T = np.transpose(array2)

U__x__Ut = np.matmul(array2, array2_T)
Ut_x__U = np.matmul(array2_T, array2)

columns = []
for i in range(2):
    columns.append(array2[:, i].reshape(-1, 1))

funcs = []
for column in columns:
    func = np.matmul(
        column,
        np.transpose(column)
    )
    funcs.append(func)

sums = []
for func in funcs:
    sums.append(sum(sum(func)))



# print(array2)
# print(array2_T)
# print(np.round_(U__x__Ut, 2))
# print(np.round_(Ut_x__U, 2))