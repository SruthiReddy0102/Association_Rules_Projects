install.packages("arules")
library("arules") # Used for building association rules i.e. apriori algorithm

# Importing the dataset
Groceries <- read.excel(file.choose()) # Data set is imported from Text(base),so the data will convert to factors
View(Groceries)

# Checking NA Values
sum(is.na(Groceries))


summary(Groceries)

# making rules using apriori algorithm 
# Keep changing support and confidence values to obtain different rules

# Building rules using apriori algorithm
arules <- apriori(Groceries, parameter = list(support = 0.002, confidence = 0.75, minlen = 2))
arules

# Viewing rules based on lift value
inspect(head(sort(arules, by = "lift"))) # to view we use inspect 

# Overal quality 
head(quality(arules))

# install.packages("arueslViz")
library("arulesViz") # for visualizing rules

# Different Ways of Visualizing Rules
plot(arules)

plot(arules,method="two-key plot") # Two-key Plot
plotly_arules(arules)
plot(arules, method = "grouped")

windows()
plot(arules[1:90], method = "graph") # for good visualization try plotting only few rules

write(arules, file = "Groceries_Output.csv", sep = ",")

getwd()

