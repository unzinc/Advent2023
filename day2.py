games=[]
game_entries=[]

max_dice={"red":12, "green":13, "blue":14}
count=0
count_b=0
num_sub_games=0
with open ('day2_input.txt', 'r') as file:                                      
    for line in file:
        gamenum_plus_hands=line.strip().split(':')             #split games into dice shown 
        game_id=int(line.strip().split(':')[0].split()[1])
        game_hands=gamenum_plus_hands[1].strip().split(';')    #split dice shown into seperate handfulls shown
        possible_game=True
        partb_min_dice={"red":0, "green":0, "blue":0}
        #print(dice_shown[0].split(','))
        for hand in game_hands:          #cycle through each hand for a game
            num_sub_games+=1
            dice_temp={'red':0, 'blue':0, 'green':0}
            hand=hand.strip().split(',')        #Split the hand into 'num color'
            for dice_colors in hand:  
                dice_colors=dice_colors.split() #Split each hand into an array [num, color]
                dice_temp[dice_colors[1]]=int(dice_colors[0])  #Change the number to an int and add to temp dict
                if int(dice_colors[0]) > partb_min_dice[dice_colors[1]]:  #Check the max dice per color per game
                    partb_min_dice[dice_colors[1]]=int(dice_colors[0])
            if dice_temp["red"] > max_dice["red"] or dice_temp["blue"] > max_dice["blue"] or dice_temp["green"] > max_dice["green"]:
                   possible_game=False
                   #break
        if possible_game == True:
            count+=game_id
        #multiple and add to part B total.    
        count_b+=partb_min_dice['red']*partb_min_dice['green']*partb_min_dice['blue']
                    
print("Part A answer: ",count)
print("Part B answer: ",count_b)
