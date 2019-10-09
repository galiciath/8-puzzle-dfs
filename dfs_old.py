from random import shuffle

goal_state = "012345678"


def generate_initial_state():
    numbers = list(range(0,9))
    shuffle(numbers)
    return "".join(list(map(lambda number: str(number),numbers)))

def print_state(state):
    print(f'[{state[0]} {state[1]} {state[2]}]\n[{state[3]} {state[4]} {state[5]}]\n[{state[6]} {state[7]} {state[8]}]\n')

def get_index_of_char(state,char):
    return state.index(char)

def move_up(state):
    zero_index = get_index_of_char(state,'0')
    top_value = state[zero_index-3]
    state_chars = list(state)
    state_chars[zero_index] = top_value
    state_chars[zero_index-3] = '0'
    return "".join(state_chars)

def move_down(state):
    zero_index = get_index_of_char(state,'0')
    down_value = state[zero_index+3]
    state_chars = list(state)
    state_chars[zero_index] = down_value
    state_chars[zero_index+3] = '0'
    return "".join(state_chars)

def move_left(state):
    zero_index = get_index_of_char(state,'0')
    left_value = state[zero_index-1]
    state_chars = list(state)
    state_chars[zero_index] = left_value
    state_chars[zero_index-1] = '0'
    return "".join(state_chars)

def move_right(state):
    zero_index = get_index_of_char(state,'0')
    right_value = state[zero_index+1]
    state_chars = list(state)
    state_chars[zero_index] = right_value
    state_chars[zero_index+1] = '0'
    return "".join(state_chars)

def expand(state):
    zero_index = get_index_of_char(state, '0')
    children = []
    #move up
    if(zero_index > 2):
        children.append(move_up(state))
    #move down
    if(zero_index < 6):
        children.append(move_down(state))
    #move left
    if(not zero_index in list(range(0,7,3))):
        children.append(move_left(state))
    #move right
    if(not zero_index in list(range(2,9,3))):
        children.append(move_right(state))
    return children;

def main():
    stack = []
    solution = []
    visited = set({})
    current_state = generate_initial_state()
    stack.append(current_state)
    solution.append(current_state)
    visited.add(current_state)
    iterations = 0
    while len(stack) > 0:
        iterations +=1
        print_state(current_state)
        children = expand(current_state)
        
        #filter out visited children
        children = list(filter(lambda child: not child in visited, children))
        if(len(children) > 0):
            stack += children
        else:
            stack.pop()
            solution.pop()
        if(len(stack) > 0):
            current_state = stack[len(stack) - 1]
            visited.add(current_state)
            solution.append(current_state)
            if(current_state == goal_state):
                print_state(current_state)
                print(f'solution found')
                break
    print(f'iterations: {iterations}')

main()    