import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from scipy.interpolate import make_interp_spline

# 平均値
mu = 1

# ポアソン分布の確率質量関数から確率を計算
x = np.arange(poisson.ppf(0.01, mu), poisson.ppf(0.99, mu))
y = poisson.pmf(x, mu)

# スプライン補間を用いてなめらかな曲線を作る
spline = make_interp_spline(x, y)
x_smooth = np.linspace(x.min(), x.max(), 500)
y_smooth = spline(x_smooth)

plt.figure(figsize=(10,6))
plt.plot(x_smooth, y_smooth, ms=8)
plt.grid(True)
plt.show()
