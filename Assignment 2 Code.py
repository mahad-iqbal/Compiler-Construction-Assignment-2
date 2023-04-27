lr1_table = {0: {'id': 's4'}, 1: {'$': 'acc'}, 2: {'-': 'r2', '$': 'r2'}, 3: {'-': 's3', '$': 'r4'}, 4: {'id': 's4'}, 5: {'': 's2', '-': 'r1', '$': 'r1'}, 6: {'': 'r3', '-': 'r3', '$': 'r3'}}
productions = {1: ['E', 'T', '-', 'E'], 2: ['E', 'T'], 3: ['T', 'F', '*', 'T'], 4: ['T', 'F'], 5: ['F', 'id']}

def parse(input_string):
    stack, input_list, i = [0], input_string.split(), 0
    while True:
        state, lookahead = stack[-1], input_list[i]
        action = lr1_table[state].get(lookahead)
        if not action:
            print("error")
            break
        elif action == 'acc':
            print("accept")
            break
        elif action[0] == 's':
            stack.append(int(action[1:]))
            i += 1
        elif action[0] == 'r':
            prod_num, rhs_len = int(action[1:]), len(productions[int(action[1:])]) - 1
            stack[-rhs_len:] = [int(lr1_table[stack[-rhs_len - 1]][productions[prod_num][0]])]
        else:
            print("error")
            break
