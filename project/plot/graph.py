import matplotlib.pyplot as plt

print(f"style - {plt.style.available}")

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

x_values = list(range(1, 1000))
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
ax.scatter(x_values, y_values, s=5)

# Назначение заголовка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Назначение размера шрифта делений на осях.
ax.tick_params(axis='both', labelsize=14)

# Назначение диапазона для каждой оси.
ax.axis([0, 1100, 0, 1100000])

# Scatter color
# ax.scatter(x_values, y_values, c='red', s=10)

# Scatter color map gradient
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Save plt
plt.savefig('img/plot .png', bbox_inches='tight')

# Show graph
plt.show()