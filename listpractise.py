# l=[1,2,3,4,5]
# a=0
# for i in l:
#     a=a+i 
# print(a)


# a=int(input("enter the first number: "))
# b=int(input("enter the last number: "))
# # c=0
# # for i in range(a,b+1):
# #     c=c+i
# # print(c)

# c=[]
# for i in range(a,b+1):
#     c=sum(c+i)
#     c.append(i)
# print(c)

# def two_num():
#     first_num=int(input("enter the first number: "))
#     sec_num=int(input("Enter the last number: "))
#     empty_lst=[]

#     for i in range(first_num,sec_num+1):
#         a=empty_lst+i
#         empty_lst.append(a)
#     return empty_lst
# print(two_num())

# def store_sums_in_list():
#     first_num = int(input("Enter the first number: "))
#     last_num = int(input("Enter the last number: "))
#     sums_list = []

#     for i in range(first_num, last_num + 1):
#         num_sum = first_num + i
#         sums_list.append(num_sum)

#     return sums_list

# # Calling the function and printing the resulting list
# result_list = store_sums_in_list()
# print("List of sums:", result_list)

# def append_sum_to_list():
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     sum_result = []
#     for i in range(num1,num2+1):
#         sum_result=num1[i]+num2[i]

#     # Create an empty list
    
    
#     # Append the sum of the two numbers to the list
#     sum_result.append(sum_result)

#     return sum_result

# # Calling the function and storing the resulting list
# result_list = append_sum_to_list()
# print("List with sum of two numbers:", result_list)



# a=int(input("Enter the first number: "))
# b=int(input("Enter the last number: "))
# c=[]
# for i in range(a,b+1):
#     c.append(i)
# print(c)

# sum=0
# for i in c:
#     sum=sum+i
# print(sum)

# var_1=int(input("enter the first number: "))
# var_2=int(input("Enter the last number: "))
# lst=[]
# even_num=[]
# odd_num=[]

# for i in range(var_1,var_2+1):
#     lst.append(i)
# print(lst)

# for i in range(var_1,var_2+1):
#     if i%2==0:
#         even_num.append(i)
# print(even_num)

# for i in range(var_1,var_2+1):  
#     if i%2!=0:
#         odd_num.append(i)
# print(odd_num)

# for i in lst:
#     if i%2==0:
#         even_num.append(i)
#     else:
#         odd_num.append(i)

# print(even_num)
# print(odd_num)

# var_1=int(input("enter the first number: "))
# var_2=int(input("Enter the last number: "))
# lst=[]
# for i in range(var_1,var_2+1):
#     lst.append(i)
# print(lst)

# num=int(input("Enter the number: "))
# for i in lst:
#     if i==num:
#         lst.remove(num)
# print(lst)

# n1=int(input("Enter the starting number for list1: "))
# n2=int(input("Enter the ending number for list1: "))
# lst1=[]
# for i in range(n1,n2+1):
#     lst1.append(i)
# print(lst1)

# n3=int(input("Enter the starting number for lst2: "))
# n4=int(input("Enter the ending number for lst2: "))
# lst2=[]
# c=[]
# for i in range(n3,n4+1):
#     lst2.append(i)
# print(lst2)

# for i in lst1:
#     if i in lst2:
#         c.append(i)

# print(c)


# lst=[95,56,76,7667,454,86,454,8,6]

# print(lst)

# c=int(input("Enter the numb the element which you want some: "))

# sum=0

# for i in range(c):
#     sum = sum + lst[i]
# print(sum)

a=int(input("Enter the number: "))
marks=[]
for i in range(a):
    subject=int(input(f"Enter the marks{i+1}"))
    marks.append(subject)
print(marks)




