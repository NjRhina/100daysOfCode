import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# style.use('ggplot')
# style.use('fivethirtyeight')
# style.use('fast')
# style.use('dark_background')
# style.use('bmh')
# style.use('classic')
# style.use('seaborn-v0_8')
# style.use('seaborn-v0_8-bright')
# style.use('seaborn-v0_8-dark')
# style.use('seaborn-v0_8-dark-palette')
# style.use('seaborn-v0_8-darkgrid')
# style.use('seaborn-v0_8-deep') # seaborn-v0_8-muted
# style.use('seaborn-v0_8-notebook') #seaborn-v0_8-paper
# style.use('seaborn-v0_8-pastel')
# style.use('seaborn-v0_8-poster')
# style.use('seaborn-v0_8-ticks')
style.use('seaborn-v0_8-white')

x = np.arange(0, 30, 0.2)
y1 = np.sin(x)
y2 = np.cos(x)

plt.title("Sine function")
plt.suptitle("Trig functions")  # this bigger and on top of title
plt.xlabel("Students")
plt.ylabel("Height")
plt.grid(True)

plt.plot(x, y1, label="sine")
plt.plot(x, y2, label="cosine")
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()
