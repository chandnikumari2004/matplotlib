import matplotlib.pyplot as plt
hours_studied=[1,2,3,4,5,6,7,8]
exam_score=[50,60,68,74,79,85,90,96]
plt.scatter(hours_studied,exam_score,color='green',marker='o',label='Student Data')
plt.xlabel("Hours studied")
plt.ylabel("Exam Score")
plt.title("Relationship between Study time and score")
plt.legend()
plt.grid(True)
plt.show()