games=[]
game_entries=[]

max_dice={"red":12, "green":13, "blue":14}
count=0
with open ('day2_input.txt', 'r') as file:                                      
    for line in file:
        gamenum_plus_hands=line.strip().split(':')             #split games into dice shown 
        game_id=int(line.strip().split(':')[0].split()[1])     #Get the Game Number 
        game_hands=gamenum_plus_hands[1].strip().split(';')    #split dice shown into seperate handfulls shown
        possible_game=True
        #print(dice_shown[0].split(','))
        for hand in game_hands:          #cycle through each hand for a game
            dice_temp={'red':0, 'blue':0, 'green':0}
            hand=hand.strip().split(',')        #Split the hand into 'num color'
            for dice_colors in hand:  
                dice_colors=dice_colors.split() #Split each hand into an array [num, color]
                dice_temp[dice_colors[1]]=int(dice_colors[0])  #Change the number to an int anD add to temp dict
            if dice_temp["red"] > max_dice["red"] or dice_temp["blue"] > max_dice["blue"] or dice_temp["green"] > max_dice["green"]:
                   possible_game=False
                   break
        if possible_game == True:
            count+=game_id

                    
print(count)
