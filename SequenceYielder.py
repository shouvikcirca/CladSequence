import random

def yieldPermutation(choices):
    choiceList = [i for i in choices]
    originalChoiceList = [i for i in choices]
    
    combination = ''
    for i in range(5):
        c = random.choice(choiceList)
        choiceList.remove(c)
        combination+=c
        
    
    if combination in sequenceList:
        return yieldPermutation(originalChoiceList)
    if len(sequenceList)>0 and combination[0] == sequenceList[-1][-1]:
        return yieldPermutation(originalChoiceList)    
    
    sequenceList.append(combination)
    return combination
    
choices = ['O','V','G','C','B']
sequenceList = []
 
myChoices = [yieldPermutation(choices) for i in range(4)]
print(myChoices)
