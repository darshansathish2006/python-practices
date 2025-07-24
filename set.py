s={"stone","paper","scissor"}

player_choice=str(input("\nEnter your choice (stone/paper/scissor) : " ))
for x in s:
    if player_choice=="stone" and x=="paper":
        print(f"\nYou : {player_choice} vs Computer : {x}. You Lose!")
        break
    elif player_choice=="stone" and x=="scissor":
        print(f"\nYou : {player_choice} vs Computer : {x}. You Won!")
        break

    elif player_choice=="paper" and x=="stone":
        print(f"\nYou : {player_choice} vs Computer : {x}. You Won!")
        break

    elif player_choice=="paper" and x=="scissor":
        print(f"\nYou : {player_choice} vs Computer : {x}. You Lose!")
        break
            
    elif player_choice=="scissor" and x=="stone":
        print(f"\nYou : {player_choice} vs Computer : {x}. You Lose!")
        break

    elif player_choice=="scissor" and x=="paper":
        print(f"\nYou : {player_choice} vs Computer : {x}. You Won!")
        break           
  
            