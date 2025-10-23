import matplotlib.pyplot as plt
Product=['A','B','C','D']
Sales=[1000,1500,800,1200]

plt.barh(Product,Sales,color='orange',label='Sales 2025')
plt.title("Product Sales Comparision")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.legend()
plt.show()