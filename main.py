import Snitch
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


goldenSnitch = Snitch.Snitch(0, 0, 0)
quidditchMatch = Snitch.Field(goldenSnitch, 500, 500, 500)

TIMESRAN: int = 10

i = 0

for i in range(TIMESRAN):
    quidditchMatch.fly()

with open('positionData.csv', 'w', newline='') as f:
    fieldnames = ["x_position",
                  "y_position",
                  "z_position"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(quidditchMatch.xArr.__len__()):
        writer.writerow({
            "x_position": quidditchMatch.xArr[i],
            "y_position": quidditchMatch.yArr[i],
            "z_position": quidditchMatch.zArr[i]
        })


"""

"""

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set(xlim=(0, 500), ylim=(0,500), zlim=(0,500))

data = pd.read_csv('positionData.csv')
x = data['x_position']
y = data['y_position']
z = data['z_position']

def animate_frame(i):
    ax.clear()

    ax.plot3D(x[:i], y[:i], z[:i])
    ax.set(xlim=(0, 500), ylim=(0, 500), zlim=(0, 500))

animate = FuncAnimation(plt.gcf(), animate_frame,
                    interval=1,
                    frames=len(quidditchMatch.xArr),
                    repeat=True)

plt.show()