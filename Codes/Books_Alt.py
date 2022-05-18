import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

#book=[]
#with open("C:\\Users\\Hello\\Desktop\\Data science\\data science\\assignments\\Association rules\\datasets\\book.csv") as f:book = f.read()

books = pd.read_csv("C:\\Users\\Hello\\Desktop\\Data science\\data science\\assignments\\Association rules\\datasets\\book.csv")

frequent_items = apriori(books, min_support = 0.005,max_len = 3, use_colnames = True)

## Most frequent items set based on support  
frequent_items.sort_values('support',ascending= False, inplace = True)

##Building the rules
rules = association_rules(frequent_items,metric="lift",min_threshold = 1)

##The above code gives us the rules with threshold greater than 1
rules.sort_values('lift', ascending = False, inplace = True)

######################Eliminating the reducdencies in the rules#######################3

## To eliminate the reducdancy in rules
def to_list(i):
    return sorted(i)

ma_x = rules.antecedents.apply(to_list)+rules.consequents.apply(to_list)

ma_x = ma_x.apply(sorted)

return_rules = list(ma_x)
unique_rules = [list(m) for m in set(tuple(i) for i in return_rules)]

index_rules = []
for i in unique_rules:
    index_rules.append(return_rules.index(i))

##Getting the rules without any reducdancies
rules_without_reducdancies = rules.iloc[index_rules, : ]

##Sorting them with respect to lift 
rules_without_reducdancies.sort_values('lift', ascending = False, inplace = True)

### to see only top 10
rules.head(10)

## 3D plot
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns

support = rules_without_reducdancies["support"]
confidence = rules_without_reducdancies["confidence"]
lift = rules_without_reducdancies["lift"]

fig = plt.figure()
ax= fig.add_subplot(111, projection = '3d')
ax.scatter(support,confidence,lift)
ax.set_xlabel("Support")
ax.set_ylabel("Confidence")
ax.set_zlabel("lift")

## Scatter plot
import scipy as sp
plt.scatter(x=support, y=confidence, c=lift , cmap = 'gray')
plt.colorbar()
plt.xlabel("support")
plt.ylabel("confidence")

### #######################Total number of rules are 212, wuth minimum support = 0.005 and maximum length = 4 , which are without any reducdancies


############### Changing the support value to 0.007
frequent_items1 = apriori(books,min_support = 0.007,max_len = 4 , use_colnames = True)

#Most frequent items based on the support, decending order
frequent_items1.sort_values('support', ascending = False, inplace = True)


##Building rules
rules2 = association_rules(frequent_items1 , metric = 'lift' , min_threshold = 1)

##Rules2 are the rules which are generated with the minimum threshold as 1
rules2.sort_values('lift',ascending = False , inplace = True)

###Elimiinating the reducdancies

def to_list1(i):
    return(sorted(i))

ma_x1 = rules2.antecedents.apply(to_list1)+ rules2.consequents.apply(to_list1)

ma_x1 = ma_x1.apply(sorted)

return_rules1 = list(ma_x1)
unique_rules1 = [list(m) for m in set(tuple(i) for i  in return_rules1 )]

index_rules1 = []
for i in unique_rules1:
    index_rules1.append(return_rules1.index(i))

### eliminate rules with reducdancies 
rules_without_reduc = rules2.iloc[index_rules1,:]

##Sorting the rules
rules_without_reduc.sort_values('lift', ascending = False, inplace = True)
### A Total of 459 rules

## 3D plots
support2 = rules_without_reduc["support"]
confidence2 =  rules_without_reduc["confidence"]
lift2 = rules_without_reduc["lift"]


fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection = '3d')
ax1.scatter(support2,confidence2,lift2)
ax1.set_xlabel("support")
ax1.set_ylabel("confidence")
ax1.set_zlabel("lift")

## Scatter plot
plt.scatter(support2,confidence2, c =lift2, cmap = 'gray')
plt.colorbar()
plt.xlabel("support");plt.ylabel("confidence")

############# Changing the minimum support value to 0.6 and maximum length = 3

frequent_items2 = apriori(books, min_support = 0.1 , max_len = 3,use_colnames = True)

## Sorting the rules is decending order
frequent_items2.sort_values('support', ascending = False, inplace = True)


## Building the rules 
rules3 = association_rules(frequent_items2, metric = 'lift', min_threshold = 1 )

rules3.sort_values('lift', ascending = False, inplace = True )

### To remove the reducdancies
def to_list3(i):
    return(sorted(i))
    
max_x2 = rules3.antecedents.apply(to_list3)+rules3.consequents.apply(to_list3)

max_x2 = max_x2.apply(sorted)

### to find unique rules

return_rules3 = list(max_x2)
unique_rules3 = [list(m) for m in set(tuple(i) for i in return_rules3)]

index_rules3=[]
for i in unique_rules3:
    index_rules3.append(return_rules3.index(i))
    
## removing reducdancies
rules_without_reduc1 = rules3.iloc[index_rules3,:]    

## Sorting these rules
rules_without_reduc1.sort_values('lift', ascending = False, inplace = True)
## A total of 30 rules are formed.

# 3D plots
support3 = rules_without_reduc1["support"]
confidence3 = rules_without_reduc1["confidence"]
lift3 = rules_without_reduc1["lift"]

fig3 = plt.figure()
ax3 = fig3.add_subplot(111, projection = '3d')
ax3.scatter(support3,confidence3,lift3)
ax3.set_xlabel("support")
ax3.set_ylabel("confidence")
ax3.set_zlabel("lift")

## Scatter plot
plt.scatter(support3, confidence3, c=lift3 , cmap='gray')
plt.colorbar()
plt.xlabel("Support");plt.ylabel("Confidence")