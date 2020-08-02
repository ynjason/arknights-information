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
        name = input("get operator information with name: ")
        if name == "stop":
            break
        print(operatorInformation[name.lower()])




if __name__ == "__main__":
    main()

