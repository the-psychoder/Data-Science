import matplotlib.pyplot as plt
priority_value=[90,5,3,2]
priority_labels=['Coding','study','books','food']
fig,ax=plt.subplots()
#plt.title('New Year Donut')
ax.axis('equal')
agenda,texts,autotexts=ax.pie(priority_value,labels=priority_labels,radius=1.3,autopct='%0.0f%%',shadow=True,explode=[0,0,0,0],startangle=20,wedgeprops=dict(width=.35,edgecolor='w'))
ax.set_title('New Year Donut')
ax.legend(agenda,priority_labels,title='daily agenda',bbox_to_anchor=(1,0.4))
plt.setp(texts,weight='bold')
plt.show()
