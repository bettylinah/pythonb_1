#keyword
#break and continue statement
#loops = for and while loops
#for loop:iterates over a sequence(ex a list,tuple string or range)
# while loop:repeats as long as a condition is true
#FOR LOOP
#we use (FOR VARIABLE IN SEQUENCE)
#EX
animals =["dog","cat","lion"] #also intergers can be used
for animal in animals:
    print(animal)

#BREAK AND CONTINUE can be used in both loops either for or while
#used to break a loop while continue is used to continue a loop after you have found what you were looking for
animals_1 = ["dog", "cat", "lion"]  # also intergers can be used
for animal_1 in animals_1:
    if animal_1 =="cat":
        break  #instead of break use continue to see the difference
    print(animal_1)

#LOOP INSIDE LOOP(nested)
#users =["linah","james","tasha",]
#for user in users:
    #for age in "123":
     #print(user,age)

#RANGE
for i in range(10):  # if you want to start at a specific value you will have to indicate it(1,10)
    print(i)

#WHILE LOOP
#t = 5
#while t<15:
    #print(t)
    #t=t+1 #(this is what we call iteration)
#QUIZ
#print power of 2 from 2 to 128 in separate lines
#n = 128
#i =2
#while n>i:
    #print(i)
    #i=i*2

#creating infinity loop
#you must use true
#ex
#x =0
#while True:#this make the loop to continue adding one without stoping you can stop the loop by using break or pressing ctrl c
    #if x ==204:
       # break
    #print(x)
    #x=x+1