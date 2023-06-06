import numpy as np
import matplotlib.pyplot as plt

python = (85, 67, 23, 98)
java = (50, 67, 89, 14)
networking = (60, 20, 56, 22)
machine_learning = (88, 23, 40, 87)

people = ['Rhina', 'Bob', 'John', 'Anna']

# plt.style.use("classic")
index = np.arange(4)
plt.bar(index, python, width=0.2, label="Python")
plt.bar(index + 0.2, java, width=0.2, label="Java")
plt.bar(index + 0.4, networking, width=0.2, label="Networking")
plt.bar(index + 0.6, machine_learning, width=0.2, label="Machine Learning")

plt.title("Levels of skills in different areas of computing")
plt.xlabel("Persons")
plt.ylabel("Skill level")
plt.xticks(index + 0.2, people)
plt.ylim(0, 130)
# plt.grid(True)
plt.legend(loc="upper center")
plt.show()
