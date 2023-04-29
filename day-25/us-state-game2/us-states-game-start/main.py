# TODO
# 1 Convert the guess to Title case
# 2 Check if the guess is among the 50 states
# 3 Write correct guesses onto the map
# 4 Use a loop to allow the user to keep guessing
# 5 Record the correct guesses in a list
# 6 Keep track of the score
# -----------------------------------------------
import turtle
import pandas

screen = turtle.Screen()
screen.title = "U.S. State Game"
image = 'day-25/us-state-game2/us-states-game-start/blank_states_img.gif'
screen.addshape(image)
screen.setup(800,600)
turtle.shape(image)

data = pandas.read_csv('day-25/us-state-game2/us-states-game-start/50_states.csv')
state_list = data.state.to_list()
guess_state = []

while len(guess_state) < 50 :
    ans_state = screen.textinput(title=f"{len(guess_state)}/50 Correct",
                            prompt="What's another state's name?").title()
    
    if ans_state == 'Exit' :
        miss_state = [state for state in state_list if state not in guess_state]
        data = pandas.DataFrame(miss_state)
        data.to_csv('day-25/us-state-game2/us-states-game-start/states_to_learn.csv')
        # for state in state_list :
        #     if state in guess_state :
        #         pass
        #     else :
        #         miss_state.append(state)        
        break
    
    if ans_state in state_list :
        guess_state.append(ans_state)
        x = int(data[data.state == ans_state].x)
        y = int(data[data.state == ans_state].y)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x, y)
        t.write(ans_state)

screen.exitonclick()
    
