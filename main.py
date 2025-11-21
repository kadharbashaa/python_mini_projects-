

# a= 10
# print(a)


# a="five"
# print(a+" |" +a)

# this is variables ''


# operators :
# a=2
# a+=5
# print(a)

# ins=(input("enter your certidicate name :"))
# print("hai ",ins , "you are completed python coruse certificate visit our website and buy that")


# # this is a  input note that 

# b=2%3
# print(b)

# num= 2.5
# print(type(num))

# abc=123
# deff="456"
# deff=int(deff)
# print(abc+deff)



# hi="hai"                                                                                                                     
# ho="123"
# yo="456"
# yo=int(yo)
# ho=int(ho)

# print(str(ho+yo)+hi)


# num=1.45
# num=str(num)
# print(num)


# print(type(5))

# list=[1,2,3,"hai", 4.6]
# print(list[4])

# print(list)

# lang =["eng", "german","French", "polish"]

# print(lang)

# print(lang[0])

# lang[0]=12.0
# print(lang)

# tuples 

# lang=("1eng","2eng","3eng","4eng","5eng",)

# lang=("1eng","2eng","3eng","4eng","5eng",)
# print(lang)

# string 

# str="shekbabu"
# print(str[1])

# str='shekbabuh'
# print(str[0:-3])

# str="hello"
# print("str:",str[3:-1])


# str1="hai"
# hi="world"
# print(hi+str1)

# print(hi *3)

# sets

# sets={1,2,3,}
# print(sets)

# sets.add(4)
# print(sets)

# sets.update(["hai", 42,"hello", 20])
# # sets.remove(2)
# print(sets)


# a={0, 1, 2,3 }
# b={2,3,4,5}

# # print(a|b)   #union 
# print(a&b)   #intersection

# print(a-b)    # Set difference

# print(a^b)   # eedhu commom that remove panni show agum # intersection ku opposite 
#                #symettric difference


#   dictionary          # 
# dict ={}    empty dictionary 

# dict={1:"apple" , 2:"ball" }   - example of dictionary 

# person={"name":"babu", "age":25 , "location":"chennai"}

# person['age']=40
# print(person)

# add key value 

# person['salary']=20000
# print(person)

# deleting the key and value

# del person['location']
# print(person)

# delete total dictionary

# del person
# print(person)


# range learnig in python




# p=range(1,10)   # it it create letters for that 1 to 99 make numbers [] 
# print(list(p))  ## it it create letters for that 1 to 99 make numbers ()
# print(tuple(p))  ## it it create letters for that 1 to 99 make numbers {}
# print(dict.fromkeys(p,20))  ## it it create letters for that 1 to 99 make numbers {key:value} make that in  output 



# nu=range(1,6,1)
# print(nu)                     # 1,2,3,4,5
# print(list(nu))

# numm=range(1,6,2)
# print(numm)
# print(list(numm))   # 1,3, 5,

# nu=range(5,0,-1)
# print(nu)            # 5,4,3,2,1
# print(list(nu))


# if else 
# num =1000
# if num>100:
#     print("PN")
# else:
#     print("NN")
 

# elif
#  statement

# num=0
# if num==20:         # first idhu check panudhu correct aa nu pos wrong
#      #after go to elif section  yes its correct  output shows zero
#     print("+pos")
# elif num==0:
#  print("zero")
# else:
#  print("Neg -")


# while loop 
# n=100

# sum=0
# i=1
# while i <= n:
#   sum=sum+i
#   i=i+1

#   print(sum)


# for lopop 

# for i in range(1,6) :
#   print(i)

#    while loop 


  

# i = 2

# while i <= 10:
#     print(i)
#     i = i + 2



#  break statement

# for val in "string":
#     if val =="r":
#         continue
#     print(val) 
#     print("the end")


#function

# def printer():
#     print("hai")
#     print("hello")


# printer()

#  function arguments 

# def adding_no(a,b):
#     sum= a+b
#     print(sum)



# post=adding_no(4.5, 5.7)
# print (post)


# def adding_no(a, b):
#     sum = a + b
#     return sum     # ← This is what you were missing!

# post = adding_no(4.5, 5.7)
# print(post)        # Now it prints 10.2 (not None)

#  recursive function 
# it means   function inside a function any thing  we can use that 

# def fac(x):
#     if x==1:
#          return 1
#     else:
#         return(x * fac(x-1))
# num=6
# print("the factorial of ",num ,"is", fac(num))

 
 

#   task 01 
#  find the big numbers like 25 12 10

# a=10


# if(a>=50):
#    print("very good")
# elif(a>=40):
#     print("good") 
# elif(a>=30):
#     print(" level")
# elif(a==25):
#     print("bad")
# elif(a>=20):
#     print("worst")
# else:
#     print(" low mark need imporovement ")  


 
# # lAMBDA functions 

# square = lambda x:x** 2
# print(square(5))

# exception handling 
import sys

# randomlist = [1, 3, 0, 4, 'a', 32, 5, 2]

# for en in randomlist:
try:
        x=(input("The entry is: "))
        r = 100 /float(x)
        print("Reciprocal is:", r)
except Exception as r:
        print("Oops", r, "occurred")
finally:
        print("\n")


        








