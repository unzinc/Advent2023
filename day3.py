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
input_check=[]
with open ('day3_input.txt', 'r') as file: 
    for line in file:
        input_text_array.append(list(line.strip()))      #Create a matrix of each character - list() does this - strip() removes \n
        input_check.append(list(line.strip()))
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
        while True:    
            if input_text_array[ycoord][xcoord+n] in nums:
                soln_matrix[ycoord][xcoord+n]=input_text_array[ycoord][xcoord+n]
                input_text_array[ycoord][xcoord+n]='.'
                n+=n
            else:
                break

def diag_check(xcoord, ycoord):
    for diag in [[-1,-1],[-1,1],[1,-1],[1,1]]:
        y_skid=diag[0]
        x_skid=diag[1]
        while True:
            ycoordskid=ycoord+y_skid 
            xcoordskid=xcoord+x_skid

            if ycoordskid < 0 or ycoordskid > len(input_text_array)-1 or xcoordskid < 0 or xcoordskid > len(input_text_array[0])-1:
                # print(ycoordskid,xcoordskid)
                break
            elif input_text_array[ycoord+y_skid][xcoord+x_skid] in nums:
                soln_matrix[ycoord+y_skid][xcoord+x_skid]=input_text_array[ycoord+y_skid][xcoord+x_skid]
                input_text_array[ycoord+y_skid][xcoord+x_skid]='.'
                x_skid+=diag[1]
            else:
                break
y=0

for row in input_text_array:
    x=0
    for char in row:
        if char not in numsanddeci:
            cross_check(x, y)
            diag_check(x, y)
        x+=1
    y+=1

soln_nums=[]
ans=0
delim=','
for row in soln_matrix:
    # soln_nums.append(''.join(row).split('.'))
    soln_nums+=''.join(row).split('.')
for element in soln_nums:
    if element.isdigit():
        ans+=int(element)    
