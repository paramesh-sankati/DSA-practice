'''
Description:
Write a Program to print if sum of column elements is prime then print elements if it is not then print stars(*). 


Constraints:
Input            : First Line of The Input Consists of One Integer Value Which Represents No of Rows

                       Second Line of the Input Consists of One Integer Value Which Represents No of Columns 

                       And Next Line Consists of Elements for 2D Array 

Output         : Print the Columns whose sum is Prime And if it is not print the  remaining columns as stars( * ).

Constraints  : Row and Column Sizes Must be Greater Than zero or else Print "Invalid Input".


Example:
Input 1 :            3

                           3

                           3 5 8

                           7 8 9

                          12 15 12

Outupt 1 :        

                            * * 8

                            * * 9

                            * * 12

 

Input 2 :            3

                           4

                           1 12 12 4

                           22 14 18 3

                            9 15 1 1

 Outupt 2 :         

                          * 12 12 *

                          * 14 18 *

                          * 15 1 *


Explanation:
Input 1 :            3

                           3

                           3 5 8

                           7 8 9

                          12 15 12

Outupt 1 :        

                            * * 8

                            * * 9

                            * * 12

Explanation :    1st column consists of  3 , 7 , 12 and its sum is 3 + 7 + 12 = 22 and 22 is not a Prime Number, So print 1st column with Stars ( * )

                           2nd column consists of 5 , 8 , 15 and its sum is 5 + 8 + 15 = 28 and 28 is not a Prime Number, So print 2nd column with Stars ( * )

                           3nd column consists of 8 , 9 , 12 and its sum is 8 + 9 + 12 = 29 and 29 is a Prime Number, So print 3rd column elements

                           

 

 

 

Input 2 :            3

                           4

                           1 12 12 4

                           22 14 18 3

                            9 15 1 1

 Outupt 2 :         

                          * 12 12 *

                          * 14 18 *

                          * 15 1 *

Explanation :    1st column consists of 1 , 22 , 9 and its sum is 1 + 22 + 9 = 32 and 32 is not a Prime Number, So print 1st column with Stars ( * )

                           2nd column consists of 12 , 14 , 15 and its sum is 12 + 14 + 15 = 41 and 41 is a Prime Number, So print 2nd column elements

                           3rd column consists of 12 , 18 , 1 and its sum is 12 + 18 + 1 = 31 and 31 is a Prime Number, So print 3rd column elements

                           4th column consists of 4 , 3 , 1 and its sum is 4 + 3 + 1 = 8 and 8 is Not a Prime Number, So print 4th column with Stars ( * )

'''
def isPrime(num):
    if num==2:
        return True
    else:
        for i in range(2,num):
            if num%i==0:
                return False
        else:
            return True
        
def matrix_col(r,c,lst):
    for i in range(r):
        for j in range(c):
            s=0
            for k in range(r):
                s=s+lst[k][j]
            
            if isPrime(s):
                print(lst[i][j],end=' ')
            else:
                print('*',end=' ')
        print()
    return lst

r,c=3,3
lst=[[3,5,8],
     [7,8,9],
     [12,15,12]]

matrix_col(r,c,lst)
