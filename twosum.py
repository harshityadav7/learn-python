nums=list(map(int,input("enter array elements").split()))
print(nums)
print("enter target")
target=int(input())
for i in range(len(nums)):
     for j in range(i+1,len(nums)):
         if nums[i]+nums[j]==target:
            print(i,j)


