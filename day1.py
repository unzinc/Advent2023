"""
Created on Thu Jun  6 14:34:42 2024

@author: KDM
"""
import re
#Create some blank arrays
nums=[]
nums_cut=[]

#num dict set up this way for any instances of joined number words eg: eightwo, twone
num_dict={'one':'o1ne',
          'two':'t2wo',
          'three':'t3ree',
          'four':'f4our',
          'five':'f5ive',
          'six':'s6ix',
          'seven':'s7even',
          'eight':'e8ight',
          'nine':'n9ine'}

#Function to replace string numbers to digits
def replace_text_numbers(text, mapping):
    for ent in mapping:
        text=text.replace(ent, mapping[ent])
    return text

#open file and filter out the letters
with open('input.txt', 'r') as file:
    for line in file:
        mod_text=replace_text_numbers(line, num_dict)
        nums.append(''.join(filter(str.isdigit, mod_text)))
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
        
