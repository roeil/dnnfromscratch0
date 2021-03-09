nr = np.random.normal(0,10,500)
nr1 = np.random.uniform(0.7,1.3,500)
nr2 = np.random.uniform(-0.7,1.3,500)

xs = np.sin(nr)
ys = np.cos(nr)

plt.scatter((xs*nr1),(ys*nr1))
plt.scatter(0.5*xs*nr2,0.5*ys*nr2)