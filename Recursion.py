3.RECURSION
3-1 head recursion 
count=0
def function():
  global count
  if count==4:
    return
  print("sahasrika")
  count+=1
  function()
function()

  3-2 Tail recursion
count=0
def func():
  global count 
  if count==4:
    return
  count+=1
  func()
  print("sahasrika")
func()
3.3 RECURSION USING PARAMETERS
n=10
def func(n):
  if n==0:
    return 
  print(n)
  func(n-1)
func(10)

 —-PRINT (N TO 1) USING HEAD RESURSION
def func(i,n):                                                                      
  if n==1:
    return
  print(n)
  func(i+1, n-1)
func(1 , 10)

—--
def func(n):
  if n==1:
    return
  print(n)
  func( n-1)
func(10)

—----- PARAMETRIZED AND FUNCTIONAL RECURSION

def func(sum,i,n):
  if i>n:
    print(sum)
    return
  func(sum+i,i+1,n)
func(0,0,4)

—--------------FACTORIAL USING RESURSION

def func(n,i,fact):
  if n==1:
    print(fact)
    return
  func(n-1,i+1,fact*n)   #function
func(5,1,1)    #parameters






—--------------REVERSING AN ARRAY USING RECURSION 
nums=[5,7,3,2,6,1,5,9]
n=len(nums)
def func(arr,left,right):
  if left>=right:
    print(nums)
    return 
  arr[left],arr[right]=arr[right],arr[left]
  func(arr,left+1,right-1)
func(nums,0,n-1)

—------------------------FIBANOCCI SERIES
def func(n):
  if n<=1:
    return n
  return func(n-1) + func(n-2)

print(func(5))

