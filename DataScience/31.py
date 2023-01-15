import matplotlib.pyplot as plt

games = ['PUBG', "Minecraft", "GTA-V", "Call Of Duty", "FIFA 22", "FreeFire"]
rating = [4.5, 4.9, 4, 4.2, 2.1, 3.5]
colors = ['black', 'red', 'green', 'blue', 'yellow', 'turquoise']

plt.bar(games, height=rating, color=colors)

plt.title("Best and the worst games 2022 (By rating)")
plt.xlabel('Games')
plt.ylabel('Rating')
plt.show()
