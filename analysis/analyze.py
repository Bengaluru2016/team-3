import numpy as np
import matplotlib.pyplot as plt

# Reading the dataset
x = np.genfromtxt('data.csv', dtype=int, delimiter=',')

# bar graph variables
jun = x[:, 8]
jul = x[:, 9]
aug = x[:, 10]

bar_width = 0.3
bar_x = ("June", "July", "August")
bar_y = [sum(jun) / len(jun), sum(jul) / len(jul), sum(aug) / len(aug)]
y_pos = np.arange(len(bar_x))

# Plotting
plt.bar(y_pos, bar_y, align='center', alpha=0.5)

plt.xticks(y_pos, bar_x)
plt.ylabel('Attendance')
plt.title('Monthly View - Attendance')

plt.show()
