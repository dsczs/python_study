from sklearn.datasets import load_iris

li = load_iris()

print("获取特征值")
print(li.data)
print("目标值")
print(li.target)

# print(li.DESCR)