# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:44:26 2024

@author: web1
"""


# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.

#Load in all lines of input and set each line as an entry to an array
input_text_array=[]
with open ('day3_input.txt', 'r') as file: 
    for line in file:
        input_text_array.append(list(line.strip()))      #Create a matrix of each character - list() does this - strip() removes \n
        
soln_matrix=[]

#Create a Solutions Matrix to copy numbers adjacent to a symbol to
for row in range(len(input_text_array)):
    rowadd=[]
    for col in range(len(input_text_array[row])):
        rowadd.append('.')
    soln_matrix.append(rowadd)
        
    
#set up some known value arrays, assume anything else is a trigger symbol        
nums=['1','2','3','4','5','6','7','8','9','0']
deci=['.']
numsanddeci=nums+deci

#Function to check the linear adjacent cells
def cross_check(xcoord, ycoord):
    for n in [-1, 1]:
        if input_text_array[ycoord+n][xcoord] in nums:
            soln_matrix[ycoord+n][xcoord]=input_text_array[ycoord+n][xcoord]
            input_text_array[ycoord+n][xcoord]='.'
        if input_text_array[ycoord][xcoord+n] in nums:
            soln_matrix[ycoord][xcoord+n]=input_text_array[ycoord][xcoord+n]
            input_text_array[ycoord][xcoord+n]='.'

def diag_check(xcoord, ycoord):
    for diag in [[-1,-1],[-1,1],[1,-1],[1,1]]:
        while True:
            if input_text_array[ycoord+diag[0]][xcoord+diag[1]] in nums:   ### Adjust here
                
                
            else:
                break
y=0

for row in input_text_array:
    x=0
    for char in row:
        if char not in numsanddeci:
            cross_check(x, y)
        x+=1
    y+=1

# linecount=0
# charcount=0
# for line in input_text_array:
#     for char in line:
#         if char in nums:
            
            
            
          
    #         charcount+=1
    # linecount+=1

# val=0
# line_char_count=0
# while val < len(text) :
#     if text[val] not in deci:
#         print(text[val])
#     val+=1    
