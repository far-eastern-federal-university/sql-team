import random
import numpy as np
g = ["граф", "мультиграф", "псевдограф"]
kind = ["ориентированный", "взвешенный", "плоский", "связный", "полный"]
opp_kind = ["неориентированный", "невзвешенный", "планарный", "несвязный", "неполный"]
n = [10, 20, 100, 200, 500]
graph_list = [];
new_graph = [];

secure_random = random.SystemRandom()
for i in range(10):
    new_graph.append(secure_random.choice(g))
    coin = np.random.sample()
    if (coin > 0.5):
        new_graph.append(secure_random.choice(kind))
    else:
        new_graph.append(secure_random.choice(opp_kind))
    new_graph.append(secure_random.choice(n))
    graph_list.append(new_graph)
    new_graph = []
    
print(graph_list)

for i in range(len(graph_list) - 1):
    for j in range (i + 1, len(graph_list)):
        if (graph_list[i] == graph_list[j]):
            print(graph_list[i], graph_list[j], "ПОВТОРЕНИЕ!!!")
            del graph_list[j];
            
print(graph_list)
