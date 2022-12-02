#A - Rock - 1 - X
#B - Paper - 2 - Y
#C - Scissor - 3  - Z
# B > A, C > B, A > C
# Win: 6 Draw: 3 Lose: 0

# read Input
my_file = open('input.txt', 'r')
data = my_file.read()
data_game = data.split('\n')

# Part 1
me = {'X':1,'Y':2,'Z':3}
strategy_guide = {'A':{'X':3,'Y':6,'Z':0},'B':{'X':0,'Y':3,'Z':6},'C':{'X':6,'Y':0,'Z':3}}
game = [x.split(' ') for x in data_game]
game = game[:-1]
score = sum([strategy_guide[round[0]][round[1]] + me[round[1]] for round in game])
print('Part 1: '+ str(score))

# Part 2
# X - Lose, Y - Draw, Z - Win
new_strategy = {'A': {'X':'Z','Y':'X','Z':'Y'},'B':{'X':'X','Y':'Y','Z':'Z'},'C':{'X':'Y','Y':'Z','Z':'X'}}
game = [[round[0],new_strategy[round[0]][round[1]]] for round in game]
score = sum([strategy_guide[round[0]][round[1]] + me[round[1]] for round in game])
print('Part 2: ' + str(score))