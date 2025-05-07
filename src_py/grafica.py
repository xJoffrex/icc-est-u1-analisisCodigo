import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5,]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, label = "Linea", color = "blue")

plt.title("Primer grafico")
plt.xlabel("Eje x")
plt.ylabel("Eje y")

plt.legend()

plt.show()