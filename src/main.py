import copy

inp = raw_input().split()
N = int(inp[0]) # Number of Rows is Grid
M = int(inp[1]) # Number of Columns in Grid
grid = [[long(0) for j in range(M)] for i in range(N)] # The mini world rewards
for i in range(N):
    inp = raw_input().split()
    for j in range(M):
        grid[i][j] = float(inp[j])
inp = raw_input().split()
E = int(inp[0]) # Number of End States
W = int(inp[1]) # Number of Walls
end_states = [] # List containing coordinates of terminal states
walls = []      # List containing coordinates of walls
for i in range(E):
    inp = raw_input().split()
    a = []
    a.append(int(inp[0]))
    a.append(int(inp[1]))
    end_states.append(a)
for i in range(W):
    inp = raw_input().split()
    a = []
    a.append(int(inp[0]))
    a.append(int(inp[1]))
    walls.append(a)
    grid[a[0]][a[1]] = '-'
start = raw_input().split()
start[0] = int(start[0])
start[1] = int(start[1])
step_reward = float(raw_input())
gamma = 1.0
################## End of input ################################
################## Some Helper Functions #######################
def isWall(r, c):
    for i in range(W):
        if walls[i][0] == r and walls[i][1] == c:
            return True
    return False

def isGoal(r, c):
    for i in range(E):
        if end_states[i][0] == r and end_states[i][1] == c:
            return True
    return False

def terminate(a, b):
    for i in range(N):
        for j in range(M):
            if isWall(i, j):
                continue
            if isGoal(i, j):
                continue
            if (a[i][j] - b[i][j]) > (b[i][j] / 100):
                #Some cell has increased by more than 1% of previous value. Therefore, don't terminate
                return False
    return True

def format_print_utility(A, iteration):
    print "Iteration: ", iteration
    for i in range(N):
        for j in range(M):
            print A[i][j], "   \t   ",
        print
    print
    print

def print_policy(A):
    policy = [['-' for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            U = []
            if isGoal(i, j):
                continue
            if isWall(i, j):
                continue
            # Try North
            if (i - 1) >= 0 and isWall(i - 1, j) == False:
                U.append(A[i - 1][j])
            else:
                U.append(A[i][j])
            # Try South
            if (i + 1) < N and isWall(i+1,j) == False:
                U.append(A[i + 1][j])
            else:
                U.append(A[i][j])
            # Try East
            if (j + 1) < M and isWall(i,j+1) == False:
                U.append(A[i][j + 1])
            else:
                U.append(A[i][j])
            # Try West
            if (j - 1) >= 0 and isWall(i,j-1) == False:
                U.append(A[i][j - 1])
            else:
                U.append(A[i][j])
            MAX = max(U)
            if U[0] == MAX:
                policy[i][j] = 'N'
            elif U[1] == MAX:
                policy[i][j] = 'S'
            elif U[2] == MAX:
                policy[i][j] = 'E'
            else:
                policy[i][j] = 'W'
    print "POLICY : "
    for i in range(N):
        for j in range(M):
            print policy[i][j], " ",
        print
    print

#################################################################
utility = copy.deepcopy(grid)
iteration = 0
while True:
    utility_dash = copy.deepcopy(utility)
    iteration += 1
    for i in range(N):
        for j in range(M):
            rewards = []
            if isWall(i, j) == True:
                continue
            if isGoal(i, j) == True:
                continue
            # Try moving north from the given cell
            score = 0.0
            if (i - 1) >= 0 and isWall(i - 1, j) == False:
                # North
                score = (0.8 * (utility_dash[i - 1][j]))
            else:
                # Stay in i,j
                score = (0.8 * (utility_dash[i][j]))
            if (j - 1) >= 0 and isWall(i, j - 1) == False:
                # West
                score += (0.1 * (utility_dash[i][j - 1]))
            else:
                # Stay in i,j
                score += (0.1 * (utility_dash[i][j]))
            if (j + 1) < M and isWall(i, j + 1) == False:
                # East
                score += (0.1 * (utility_dash[i][j + 1]))
            else:
                # Stay in i,j
                score += (0.1 * (utility_dash[i][j]))
            rewards.append(gamma * score)
            ###################################################################
            
            
            # Try moving east from the given cell
            score = 0.0
            if (j + 1) < M and isWall(i, j + 1) == False:
                # East
                score = (0.8 * (utility_dash[i][j + 1]))
            else:
                # Stay in i,j
                score = (0.8 * (utility_dash[i][j]))
            if (i - 1) >= 0 and isWall(i - 1, j) == False:
                # North
                score += (0.1 * (utility_dash[i - 1][j]))
            else:
                # Stay in i,j
                score += (0.1 * (utility_dash[i][j]))
            if (i + 1) < N and isWall(i + 1, j) == False:
                # South
                score += (0.1 * (utility_dash[i + 1][j]))
            else:
                # Stay in i,j
                score += (0.1 * (utility_dash[i][j]))
            rewards.append(gamma * score)
            ###################################################################
            
            
            # Try moving south from the given cell
            score = 0.0
            if (i + 1) < N and isWall(i + 1, j) == False:
                # South
                score = (0.8 * (utility_dash[i + 1][j]))
            else:
                # Stay in i,j
                score = (0.8 * (utility_dash[i][j]))
            if (j + 1) < M and isWall(i, j + 1) == False:
                # East
                score += (0.1 * (utility_dash[i][j + 1]))
            else:
                # Stay in i,j
                score += (0.1 * (utility_dash[i][j]))
            if (j - 1) >= 0 and isWall(i, j - 1) == False:
                # West
                score += (0.1 * (utility_dash[i][j - 1]))
            else:
                # Stay in i,j
                score += (0.1 * (utility_dash[i][j]))
            rewards.append(gamma * score)
            ###################################################################
            
            
            # Try moving west from the given cell
            score = 0.0
            if (j - 1) >= 0 and isWall(i, j - 1) == False:
                # West
                score = (0.8 * (utility_dash[i][j - 1]))
            else:
                # Stay in i,j
                score = (0.8 * (utility_dash[i][j]))
            if (i - 1) >= 0 and isWall(i - 1, j) == False:
                # North
                score += (0.1 * (utility_dash[i - 1][j]))
            else:
                # Stay in i,j
                score += (0.1 * (utility_dash[i][j]))
            if (i + 1) < N and isWall(i + 1, j) == False:
                # South
                score += (0.1 * (utility_dash[i + 1][j]))
            else:
                # Stay in i,j
                score += (0.1 * (utility_dash[i][j]))
            rewards.append(gamma * score)
            ###################################################################
            
            utility[i][j] = max(rewards) # Take the action which gives maximum expected utility
            utility[i][j] += step_reward
            utility[i][j] = round(utility[i][j], 3)
    format_print_utility(utility, iteration)
    ############# Check for termination ###############
    if terminate(utility, utility_dash) == True:
        break
print_policy(utility)
