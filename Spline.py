import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# initial data
x = [random.randint(1,100)]
y = [random.randint(1,100)]

# creating the figure and axes object
fig, ax = plt.subplots()

# update function to update data and plot
def update(frame):
    # updating the data by adding one more point
    x.append(random.randint(1,100))
    y.append(random.randint(1,100))

    ax.clear()  # clearing the axes
    ax.scatter(x,y, s = y, c = 'b', alpha = 0.5)  # creating new scatter chart with updated data
    fig.canvas.draw()  # forcing the artist to redraw itself

anim = FuncAnimation(fig, update)
plt.show()