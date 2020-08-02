import json


def main():
    command = input("give command (retrieve or input): ")
    if command == "input":
        inputOperator()
    elif command == "retrieve":
        retrieve()
    
    
def inputOperator():
    with open("information.json", 'r') as infile:
        currentInformation = json.load(infile)
    while True:
        name = input("give an operator name: ")
        if name == "stop":
            break
        operatorClass = input("give operator class: ")
        if operatorClass == "stop":
            break
        race = input("give operator race: ")
        if race == "stop":
            break
        koreanName = input("give korean name: ")
        if koreanName == "stop":
            break
        currentInformation[name] = {"operatorClass": operatorClass,
                                    "koreanName": koreanName,
                                    "race": race}

    with open("information.json", 'w') as outfile:
        json.dump(currentInformation, outfile)

def retrieve():
    with open("information.json", 'r') as infile:
        operatorInformation = json.load(infile)
    while True:
        commandType = input("how do you want to get operators? ")
        if commandType == "name":
            retrieveName(operatorInformation)
        elif commandType == "class":
            retrieveClass(operatorInformation)
        elif commandType == "race":
            retrieveRace(operatorInformation)
        else:
            print("invalid command")
            
        if commandType == "stop":
            break


def retrieveName(operatorInformation):
    while True:
        name = input("get operator information with name: ")
        if name == "stop":
            break
        try:
            info = operatorInformation[name.lower()]
            print(info)
        except:
            print("this operator does not exist")


def retrieveClass(operatorInformation):
    while True:
        operatorClass = input("get operator informations with class: ")
        if operatorClass == "stop":
            break
        groupedOperators = {}
        for name, info in operatorInformation.items():
            if info["operatorClass"] == operatorClass:
                groupedOperators[name] = info
        print(groupedOperators)
                
                

def retrieveRace(operatorInformation):
    while True:
        operatorRace = input("get operator information with race")
        if operatorRace == "stop":
            break
        groupedOperators = {}
        for name, info in operatorInformation.items():
            if info["operatorRace"] == operatorRace:
                groupedOperators[name] = info
        print(groupedOperators)
                


if __name__ == "__main__":
    main()

