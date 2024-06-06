"""
Created on Thu Jun  6 14:34:42 2024

@author: KDM
"""

#Create some blank arrays
nums=[]
nums_cut=[]

#open file and filter out the letters
with open('input.txt', 'r') as file:
    for line in file:
        nums.append(''.join(filter(str.isdigit, line)))
        #print(''.join(filter(str.isdigit, line)))
        
#Check number length and add first and last number to nums_cut array
for num in nums:
    if len(num) == 2:
        nums_cut.append(int(num))
    if len(num) == 1:
        repeat_num=num*2
        nums_cut.append(int(repeat_num))
    if len(num) > 2:
        mod_num=num[0]+num[len(num)-1]
        nums_cut.append(int(mod_num))

#sum up all the numbers
print(sum(nums_cut))
        
