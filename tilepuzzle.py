import copy

def tilepuzzle(start, goal):
    oldPath = reverse(statesearch([start], goal, [], 0))
    return cleanUp(oldPath)

def statesearch(unexplored, goal, path, recLimit):
    recLimit += 1

    if recLimit > 90:
        return []
    if unexplored == []:
        return []
    elif goal == head(unexplored):
        return cons(goal, path)
    else:
        result = statesearch(generateNewStates(
            head(unexplored)), goal, cons(head(unexplored), path), recLimit)

        if result != []:
            return result
        else:
            return statesearch(tail(unexplored), goal, path, recLimit)

def generateNewStates(currState):
    return (moveUp(currState) + moveDown(currState) + moveLeft(currState) + moveRight(currState))

def generateNew(currState, newState):
    result = []
    if checkIfExists(newState, result) == False:
        result.append(newState)

    return result

# move functions
def moveUp(currState):
    posOfSpace = findPosOfSpace(currState)
    newState = []
    newState = copy.deepcopy(currState)
    i = posOfSpace[0]
    j = posOfSpace[1]
    if i != 0:
        temp = newState[i - 1][j]
        newState[i-1][j] = 0
        newState[i][j] = temp
    return generateNew(currState, newState)


def moveDown(currState):
    posOfSpace = findPosOfSpace(currState)
    newState = []
    newState = copy.deepcopy(currState)
    i = posOfSpace[0]
    j = posOfSpace[1]
    if i != len(currState) - 1:
        temp = newState[i + 1][j]
        newState[i+1][j] = 0
        newState[i][j] = temp
    return generateNew(currState, newState)


def moveLeft(currState):
    posOfSpace = findPosOfSpace(currState)
    newState = []
    newState = copy.deepcopy(currState)
    i = posOfSpace[0]
    j = posOfSpace[1]
    if j != 0:
        temp = newState[i][j-1]
        newState[i][j-1] = 0
        newState[i][j] = temp
    return generateNew(currState, newState)


def moveRight(currState):
    posOfSpace = findPosOfSpace(currState)
    newState = []
    newState = copy.deepcopy(currState)
    i = posOfSpace[0]
    j = posOfSpace[1]
    if j != len(currState) - 1:
        temp = newState[i][j+1]
        newState[i][j+1] = 0
        newState[i][j] = temp
    return generateNew(currState, newState)


# Helper Methods
# reverse list
def reverse(lst):
    return lst[::-1]
# get first element of list


def head(lst):
    return lst[0]
# get last element of list


def tail(lst):
    return lst[1:]

# add item to beginning of list


def cons(item, lst):
    return [item] + lst


def findPosOfSpace(lst):
    temp = []
    for i, x in enumerate(lst):
        if 0 in x:
            temp.append(i)
            temp.append(x.index(0))
            return temp


def checkIfExists(state, result):
    for i in result:
        if i == state:
            return True
    return False


def cleanUp(path):
    newPath = []

    for i in path:
        if i not in newPath:
            newPath.append(i)

    return newPath

