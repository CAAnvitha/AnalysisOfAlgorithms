import matplotlib.pyplot as plt
l = [12976,13052,13092,13092,13152,13104,13328,13324,13644,13648,13684,14336,14308,23628,23908,34312,55692,74344]
m = [12912,13040,13064,13076,13072,13060,13080,13128,13080,13148,13132,13084,13080,13160,13176,13092,13236,13384]
a = [0.001617,0.002829,0.003078,0.004752,0.004547,0.004472,0.004675,0.008178,0.013614,0.014275,0.014349,0.024719,0.024091,0.160895,0.159996,0.318861,0.634125,0.725854]
b = [0.002573,0.005185,0.006082,0.009545,0.009089,0.006198,0.016516,0.016823,0.028272,0.028842,0.029546,0.052317,0.051663,0.345283,0.341556,0.668205,1.366221,1.652804]
x = [76,96,128,128,128,128,192,192,256,256,320,384,384,1024,1280,1536,2048,2064]
plt.xlabel("Problem Size")
plt.ylabel("CPU Time")
plt.title("Graph: Problem Size vs CPU Time in Seconds")
#plt.legend()
plt.plot(b, x, linewidth=2, color='green', marker='o', markersize=5, label = 'Basic')
plt.plot(a, x, linewidth=2, color='blue', marker='o',  markersize=5, label = 'Memory')
leg = plt.legend()
plt.show()

'''
plt.ylabel("Problem Size")
plt.xlabel("Memory Usage")
plt.title("Graph: Problem Size vs Memory Usage in KB")
#plt.legend()

plt.plot(l, x, linewidth=2, color='red', marker='o', markersize=5, label = "Basic")
plt.plot(m, x, linewidth=2, color='pink', marker='o',markersize=5, label = "Memory")
leg = plt.legend()
plt.show()
'''