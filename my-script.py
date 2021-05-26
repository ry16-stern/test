


import asyncio
import random
import easygui
# Calculate Winner function: Returns ("Its a Tie", "You won!", "You lost!")
async def calc_winner(pick,rand):
    print("Computer chose: ",rand)
    if rand=="Rock":
        winner="Paper"

    if rand=="Paper":
        winner="Scissors"

    if rand=="Scissors":
        winner="Rock"

    if pick==rand:
        return "Its a Tie"
    else:
        if (winner==pick):
            return "You won!"
        else:
            return "You lost!"


async def main_code():
    play_again= True
    while play_again==True:
        gui=easygui.ynbox('Welcome to Rock, Paper, Scissors game, which interface do you prefer?', 'Title', ('GUI', 'Terminal'))
        options=["Rock","Paper","Scissors"]
        if gui==True: 
            #user selected GUI
            user_choice=easygui.buttonbox('Select Rock, Paper or Scissors', 'Pick', ('Rock', 'Paper', 'Scissors'))
            rand=random.choice(options)
            result=await calc_winner(user_choice,rand)
            play_again=easygui.ynbox('Computer picked '+rand + ' '+result, 'Title', ('Play again', 'Quit'))

        else: 
            #user selected terminal
            print("Rock, Paper, Scissors, Shoot!")
            rand=random.choice(options)
            user_choice=input("What do you pick?")
            #loop until user enters proper value
            while user_choice not in options:
                print("Wrong entry! Try again")
                user_choice=input(" What do you pick? (Rock, Paper, Scissors)?  ")
                break
            result=await calc_winner(user_choice,rand)
            print(result)
            again=input("Play again? Y/N ")
            if (again=="N"):
                print("Session terminated")
                play_again=False
            

asyncio.run(main_code())


    

        
            
            

     
        
#easygui.msgbox('This is a basic message fe
# box.', 'Welcome to Rock, Paper, Scissors game')


#