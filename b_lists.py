#variables

print ("hello everyone")
var1 = "lenah"
print(var1)
var2 = 25
print(var2)
my_list="hi,everyone"
print(my_list[2:7])
print(29)
var4 = 29
print(var4)

#list and tuples
#the main difference is tha that list uses square bracket[] and tuples using()
#another diff is that you can replace a number in tuples like how we replaced 26 with 6 in lists
#list

list_one = ["linah",4,"pig",26,"pin"]
print(list_one )
print(list_one[2])
print(list_one[0:4])
list_one.insert(4,"pinned")

list_one[3]=7
print(list_one[3])
list_one.append(6)#to add a interger or string into the list
print(list_one)

fruit_one =["banana","kiwi","apple","pineapple"] #the same method is used also for strings
fruit_one.append("orange")#append is used to add at the end
print(fruit_one)
list_two=[3,5,7,9]
list_two.insert(3,10) #insert 10 at index 3 note when you insert nothing is deleted
print(list_two)
print(list_two[0:3])
list_two.extend([10,11,12])
print(list_two)
list_two.remove(7)#you remove the number you want i have removed 7
print(list_two)
list_two.pop()# pop removes the last index in the list
list_two.reverse()

del list_two[3]#the diff btwn remove and del is that del deletes according to index
#and remove deletes according to value
print(list_two)

list_two[0]=1# this one is to update a number so the number from 3 to one (is just replacind a num)
print(list_two)
#THIS ARE FOR THE NEGATIVE NUMBERS
list_three =[1,2,3,4,5]
print(list_three[-2:]) #n/b it starts counting from the end of the list.and there is no negative zero so we count from -1 hence the ans is [4,5]
#So, -1 represents the last element which is 5, -2 represents the second-to-last element which is 4, and so on.

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
my_list.sort()  # Sort the list in ascending order
print(my_list)  # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]

my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print("The number of elements in the list:", length)  # Output: The number of elements

