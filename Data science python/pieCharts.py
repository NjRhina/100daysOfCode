import numpy as np
import matplotlib.pyplot as plt

nationalities = ['Ugandan', 'Kenyan', 'Rwandan', 'Other']
students = [70, 55, 32, 20]

pairs = zip(students, nationalities)
pairs = sorted(list(pairs))
# print(sorted(list(pairs)))
students, nationalities = zip(*pairs)

explode = [0.2, 0, 0, 0.1]

plt.pie(students, labels=nationalities, autopct='%.2f%%', explode=explode,
        counterclock=False, startangle=60)  # you can add a shadow with shadow=True

plt.title('Students nationalities')
plt.show()
