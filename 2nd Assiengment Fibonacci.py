


 n = int(input("Enter the number : "))
def fibonacci(n):   
  n=1
     
  if n < 0:   
    
   print(" Print incorrect input ")
   #First Fibonacci number is 0

  if (n == 1):       
            print (0) 
   #Second Fibonacci number is 1

  elif (n == 2):        
          print (1) 
  else:        
        return (n-1) + (n+2)

       #Driver program

  print ( "Fibonacci is 9")
