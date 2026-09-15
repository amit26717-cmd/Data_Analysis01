import matplotlib.pyplot as plt
# import random
# d=[random.randint(1,30) for _ in range (400)]
# print(d)



# plt.hist(d, bins=15, color='g', edgecolor='black', linewidth=2, alpha=0.7)
# plt.title("Random value histogram")
# plt.show()


cate = ['Fation ', 'Electronics','Travel','manufacturing']
sale=[200,450,600,1000]
plt.pie(sale,labels = cate , autopct = '%1.1f%%',startangle=0)
plt.title("sector wise sale")
plt.show()



