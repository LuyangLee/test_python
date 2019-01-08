import matplotlib.pyplot as plt
import numpy as np

# 定义等高线高度函数
def f(x, y):
    return ( x ** 2 + y ** 2)

#l表示半径长，格式为list
def draw(l, max_r):
    # 数据数目
    n = 256
    # 定义x, y
    x = np.linspace(-max_r, max_r, n)
    y = np.linspace(-max_r, max_r, n)
    # for r in l:
    #     zl.append(f(r,r))
    # 生成网格数据
    X, Y = np.meshgrid(x, y)
    # 填充等高线的颜色, tc为了使最小的圆内部也有颜色
    tc = l
    tc.insert(0,0)
    plt.contourf(X, Y, f(X, Y), tc , alpha = 1.0, cmap = plt.cm.hot)
    # 绘制等高线
    C = plt.contour(X, Y, f(X, Y),tc , colors = 'black', linewidth = 2.0)
    
    # 绘制等高线数据
    plt.clabel(C, inline = True, fontsize = 10)

    # 去除坐标轴
    plt.xticks(())
    plt.yticks(())
    plt.show()

draw([1,2,3,4],2)
