import matplotlib.pyplot as plt 
value=[60,80,30,90,100]
sub=['ML','Math','Cloud','Big data','Data science']
fig,ax=plt.subplots()
ax.axis('equal')
ax.set_title('Favourite topics of the_psychoder')
sub_in_pie,texts,val=ax.pie(value,labels=sub,autopct='%0.0f%%',radius=.5,explode=[0,0,0,0,.05])
ax.legend(sub_in_pie,sub,title='Priorities',bbox_to_anchor=(1,0.7))
plt.setp(texts,weight='bold')
plt.show()
