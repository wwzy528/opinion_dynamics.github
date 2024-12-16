import networkx as nx
import matplotlib
matplotlib.use('TkAgg')  # 或 'Agg', 'Qt5Agg' 等
import matplotlib.pyplot as plt

# 设置节点数量
N = 10000  # 节点数量 (10^4)

# 生成无标度网络（scale-free network）
G = nx.barabasi_albert_graph(N, 5)  # 参数3表示每个新节点连接到已有网络的5个节点

# 计算度、接近度和介数
degree = dict(G.degree())
closeness = nx.closeness_centrality(G)
betweenness = nx.betweenness_centrality(G)

# 可视化度、接近度和介数分布
plt.figure(figsize=(18, 6))

# 度分布
plt.subplot(1, 3, 1)
plt.hist(list(degree.values()), bins=50, color='blue', alpha=0.7)
plt.title('Degree Distribution')
plt.xlabel('Degree')
plt.ylabel('Frequency')

# 接近度分布
plt.subplot(1, 3, 2)
plt.hist(list(closeness.values()), bins=50, color='green', alpha=0.7)
plt.title('Closeness Centrality Distribution')
plt.xlabel('Closeness Centrality')
plt.ylabel('Frequency')

# 介数分布
plt.subplot(1, 3, 3)
plt.hist(list(betweenness.values()), bins=50, color='red', alpha=0.7)
plt.title('Betweenness Centrality Distribution')
plt.xlabel('Betweenness Centrality')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
