def next_state(cur_state):
    cur_state = '0' + cur_state + '0'
    new_state = ''
    for before,after in zip(cur_state[:-2],cur_state[2:]):
        if before == after:
            new_state += '_'
        else:
            new_state += '1'
    return new_state

def print_states(state):
    for _ in range(25):
        print state
        state = next_state(state)

if __name__ == '__main__':
    print_states('00000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000')
