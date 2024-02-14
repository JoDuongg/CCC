# Poblano	1500
# Mirasol	6000
# Serrano	15500
# Cayenne	40000
# Thai	75000
# Habanero	125000

def main():
    
    numChili = int(input())
    chiliList = []
    totalSpice = 0
    
    for i in range(numChili):
        chiliList.append(str(input()))
    
    for i in range(numChili):
        if(chiliList[i] == "Poblano"):
            totalSpice += 1500
        elif(chiliList[i] == "Mirasol"):
            totalSpice += 6000
        elif(chiliList[i] == "Serrano"):
            totalSpice += 15500
        elif(chiliList[i] == "Cayenne"):
            totalSpice += 40000
        elif(chiliList[i] == "Thai"):
            totalSpice += 75000
        elif(chiliList[i] == "Habanero"):
            totalSpice += 125000
        else:
            totalSpice += 0
    
    return totalSpice
    
print(main())
