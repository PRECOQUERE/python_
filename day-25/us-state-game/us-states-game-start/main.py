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
screen.title("U.S. States Game")
image = "day-25/us-state-game/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
screen.setup(800,600)
turtle.shape(image)

# After 영상
data = pandas.read_csv("day-25/us-state-game/us-states-game-start/50_states.csv")
state_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50 :
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                prompt = "What's another state's name?").title()
    if answer_state == 'Exit' : 
        break

    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.ht()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        
state_learn = []
for state in state_list :
    if state in guessed_states :
        pass
    else :
        state_learn.append(state)
df = pandas.DataFrame(state_learn)
df.to_csv('day-25/us-state-game/us-states-game-start/states_to_learn.csv')


screen.exitonclick()


# 처음 영상없이 짠 소스
# answer_state = screen.textinput(title="Guess the State", prompt = "What's another state's name?")
# 맨 앞 알파벳 대문자로 바꿔줌
# answer_state = screen.textinput(title="Guess the State", 
#                                 prompt = "What's another state's name?").title()
# while len(guessed_states) > 50 :
#     answer_tf = state_50[state_50.state.str.lower() == answer_state.lower()]
#     if answer_state == 'exit' : 
#         break

#     if len(answer_tf):
#         guessed_states.append(answer_state)
#         state_x = int(answer_tf.x)
#         state_y = int(answer_tf.y)
#         ans.goto(state_x, state_y)
#         ans.write(answer_state)
#         # ans.write(state_data.state.item())

#         score += 1
#         answer_state = screen.textinput(title=f"{score}/50 Correct state", prompt = "What's another state's name?")
#     else :
#         answer_state = screen.textinput(title=f"{score}/50 Wrong answer", prompt = "What's another state's name?")

# # 영상 내 소스
# # state_50 = state_50.to_list()

# # if answer_state in state_50 :
# screen.exitonclick()
# # def get_mouse_click_coor(x, y):
# #     print(x, y)