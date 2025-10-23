import matplotlib.pyplot as plt
scores=[45,19,52,63,69,61,34,16,91,58,76,72,44,33]
plt.hist(scores,bins=5,color='purple',edgecolor='black')
plt.xlabel('Score Range')
plt.ylabel('Number of students')
plt.title("Score Distrubuttion")
plt.grid()
plt.show()