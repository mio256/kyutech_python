import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# rvsで正規分布に従う疑似乱数を生成
norm_rvs = stats.norm.rvs(loc=50, scale=20, size=1000, random_state=0) # 期待値=50, 標準偏差=20, 個数=1000

# 可視化（ヒストグラムに表現）
plt.hist(norm_rvs, bins=10, alpha=0.3, ec='blue')
plt.xlabel("class", fontsize=13)
plt.ylabel("freq", fontsize=13)

plt.show()
