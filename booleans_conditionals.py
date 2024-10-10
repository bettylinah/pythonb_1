#CONDITIONALS = IF,ELSE,ELIF
#BOOLEANS = TRUE AND FALSE
#if True:
    #print("The conditional was true")
#name =input()
#if name == "james" :
    # print("welcome james")
#else:
    #@!FW@print("user not found")
#ELIF
#user ="email"
#if user == "james" :
 #   print("welcome james")
#elif user == "gmail":
 #   print("gmail confirmed")
#else:
 #   print("wrong credentials")

#AND =used to ensure both commands are true
#OR  =means it can run as long as one of the commands are true
#NOT =uses to change false to true or viceversa
#EX

user1 ="linah"
logged_in =False
if user1 =="linah" and logged_in ==True:
    print("welcome to home page")
else:
    print("your not logged in plz create an account")

user2 ="max"
logged_in1 =True
if not logged_in1:
    print("plz log in")
else:
    print("your welcome")

#DIFFERENCE BTWN EQUAL(==) AND OBJECTIVE IDENTITY (IS){used to check if they are of the same id}
a =[1,2,3]
b =[1,2,3]
print(a==b)#the result will be true
print(a is b)#the result will be false cause they dont have the same id
#this can be tested by running the id of the two variables separetly
print(id(a)) #the id numbers dont much
print(id(b))

#N/B
#FALSE VALUES:
#false
#none
#zero of any numeric type(0)
#any empty sequence,for ex,'',(),[].
#any empty mapping,ex;{}.

condition =False
if condition :
    print("Evaluated to true")
else:
    print("Evaluated to false")
 #use the above n/b to understand the concept more better