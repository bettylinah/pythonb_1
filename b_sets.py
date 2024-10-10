# we use {} in sets
# don't care about order
# uses of values
# 1) if value is part of the set
# 2)to remove duplicate values
# 3)determine what values they share with other variables
#ex

fruits ={"mango","apple","pineapple"}
print("mango" in fruits)
fruits1 ={"mango","apple","pineapple","apple"}
print(fruits1)
subjects ={"maths","english","bcom","science"}
subject ={"kiswahili","history","maths","bcom"}
print(subject.difference(subjects))
print(subject.intersection(subjects))
print(subject.union(subjects))

#N/B
#empty lists
empty_list=[]
empty_list =list()

#empty_tuples
empty_tuple =()
empty_tuple =tuple()

#empty_set
empty_set =set()
