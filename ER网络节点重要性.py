import networkx as nx # networkx是一个用于创建、操作和研究复杂网络的Python库
import matplotlib
matplotlib.use('TkAgg')  # 或 'Agg', 'Qt5Agg' 等 用来指定 Matplotlib 使用的图形后端（backend）。它告诉 Matplotlib 使用 TkAgg 后端来渲染图形并显示窗口
import matplotlib.pyplot as plt

# 设置节点数量和连接概率
N = 50  # 节点数量 (10^4)
P = 0.001  # 边的连接概率

# 生成ER网络
G = nx.erdos_renyi_graph(N, P)

# 计算度、接近度和介数
degree = dict(G.degree())
closeness = nx.closeness_centrality(G)
betweenness = nx.betweenness_centrality(G)

# 可视化度、接近度、介数分布
plt.figure(figsize=(18, 6))  # 创建一个新的图形窗口，并设置其大小

# 度分布
plt.subplot(1, 3, 1)  # 是 Matplotlib 用于创建和定位子图的一个函数。它用于在一个图形窗口（Figure）中，按照指定的布局，创建多个子图（subplot）
plt.hist(list(degree.values()), bins=50, color='blue', alpha=0.7)
plt.title('Degree Distribution')
plt.xlabel('Degree')
plt.ylabel('Frequency')

# 接近度分布
plt.subplot(1, 3, 2)
plt.hist(list(closeness.values()), bins=50, color='green', alpha=0.7)
plt.title('Closeness Centrality Distribution')
plt.xlabel('Closeness')
plt.ylabel('Frequency')

# 介数分布
plt.subplot(1, 3, 3)
plt.hist(list(betweenness.values()), bins=50, color='red', alpha=0.7)
plt.title('Betweenness Centrality Distribution')
plt.xlabel('Betweenness')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


