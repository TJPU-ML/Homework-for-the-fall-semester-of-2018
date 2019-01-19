# 因为数据格式很整齐, 所以用 vim 手动清理数据
# 去除了 50 个 virginica 数据,
# 只使用 4 个属性中的前 2 个
# Iris-setosa 类标记为 1, Iris-versicolor 标记为 0
iris_data = [
    5.1, 3.5, 1,
    4.9, 3.0, 1,
    4.7, 3.2, 1,
    4.6, 3.1, 1,
    5.0, 3.6, 1,
    5.4, 3.9, 1,
    4.6, 3.4, 1,
    5.0, 3.4, 1,
    4.4, 2.9, 1,
    4.9, 3.1, 1,
    5.4, 3.7, 1,
    4.8, 3.4, 1,
    4.8, 3.0, 1,
    4.3, 3.0, 1,
    5.8, 4.0, 1,
    5.7, 4.4, 1,
    5.4, 3.9, 1,
    5.1, 3.5, 1,
    5.7, 3.8, 1,
    5.1, 3.8, 1,
    5.4, 3.4, 1,
    5.1, 3.7, 1,
    4.6, 3.6, 1,
    5.1, 3.3, 1,
    4.8, 3.4, 1,
    5.0, 3.0, 1,
    5.0, 3.4, 1,
    5.2, 3.5, 1,
    5.2, 3.4, 1,
    4.7, 3.2, 1,
    4.8, 3.1, 1,
    5.4, 3.4, 1,
    5.2, 4.1, 1,
    5.5, 4.2, 1,
    4.9, 3.1, 1,
    5.0, 3.2, 1,
    5.5, 3.5, 1,
    4.9, 3.1, 1,
    4.4, 3.0, 1,
    5.1, 3.4, 1,
    5.0, 3.5, 1,
    4.5, 2.3, 1,
    4.4, 3.2, 1,
    5.0, 3.5, 1,
    5.1, 3.8, 1,
    4.8, 3.0, 1,
    5.1, 3.8, 1,
    4.6, 3.2, 1,
    5.3, 3.7, 1,
    5.0, 3.3, 1,
    7.0, 3.2, 0,
    6.4, 3.2, 0,
    6.9, 3.1, 0,
    5.5, 2.3, 0,
    6.5, 2.8, 0,
    5.7, 2.8, 0,
    6.3, 3.3, 0,
    4.9, 2.4, 0,
    6.6, 2.9, 0,
    5.2, 2.7, 0,
    5.0, 2.0, 0,
    5.9, 3.0, 0,
    6.0, 2.2, 0,
    6.1, 2.9, 0,
    5.6, 2.9, 0,
    6.7, 3.1, 0,
    5.6, 3.0, 0,
    5.8, 2.7, 0,
    6.2, 2.2, 0,
    5.6, 2.5, 0,
    5.9, 3.2, 0,
    6.1, 2.8, 0,
    6.3, 2.5, 0,
    6.1, 2.8, 0,
    6.4, 2.9, 0,
    6.6, 3.0, 0,
    6.8, 2.8, 0,
    6.7, 3.0, 0,
    6.0, 2.9, 0,
    5.7, 2.6, 0,
    5.5, 2.4, 0,
    5.5, 2.4, 0,
    5.8, 2.7, 0,
    6.0, 2.7, 0,
    5.4, 3.0, 0,
    6.0, 3.4, 0,
    6.7, 3.1, 0,
    6.3, 2.3, 0,
    5.6, 3.0, 0,
    5.5, 2.5, 0,
    5.5, 2.6, 0,
    6.1, 3.0, 0,
    5.8, 2.6, 0,
    5.0, 2.3, 0,
    5.6, 2.7, 0,
    5.7, 3.0, 0,
    5.7, 2.9, 0,
    6.2, 2.9, 0,
    5.1, 2.5, 0,
    5.7, 2.8, 0,
]
