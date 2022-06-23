from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ell1 = Ellipse(xy = (0.0, 0.0), width = 4, height = 8, angle = 90.0, facecolor= 'yellow', alpha=0.3)
ax.add_patch(ell1)
x, y = 0, 0
ax.plot(x, y, 'ro')
plt.show()
