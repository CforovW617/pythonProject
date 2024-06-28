import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
# 给出的数据
data = [15, 10, 4, 9, 8, 13, 17, 51, 61, 97, 86, 84, 97, 61, 84, 66, 64, 35, 37, 36, 21, 28, 13, 8, 3, 15]
# 绘制直方图
plt.subplot(1, 2, 1)
plt.hist(data, bins=10)
plt.title('Histogram')
# 绘制QQ图
plt.subplot(1, 2, 2)
stats.probplot(data, dist="norm", plot=plt)
plt.title('Normal Q-Q Plot')
# 展示图表
plt.show()
# 正态性检验
stat, p = stats.shapiro(data)
print('Shapiro-Wilk检验:')
print('统计值 =', stat, 'p值 =', p)
alpha = 0.05
if p > alpha:
    print('样本数据符合正态分布')
else:
    print('样本数据不符合正态分布')