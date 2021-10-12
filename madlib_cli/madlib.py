import re

template = "./assets/ExampleTemplate.txt"


def read_template(path):
    """
    Read a file and return its content as a single doc string.
    """
    try:
        file = open(path)
        lines = file.readlines()
        file.close()
        finalString = f"{lines[0]}{lines[2]}{lines[4]}"
        return finalString

    except FileNotFoundError as err:
        print("oops, file not found :(")
        print(f"original error: {err}")
    
def parse_template(templateString):
    """
    Remove words inside of brackets and replace them with incremented numbers, returns a string.
    """
    regex = '\{.*?\}'
    strippedString = re.sub(regex,"{}",templateString)
    return strippedString


def merge_template(parsedTemplate, userAnswers):
    _string = f"{str(parsedTemplate)}"
    formatedString = _string.format(*userAnswers)
    #return _string.format('1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1')
    return formatedString

print(parse_template(read_template(template)))
def start_game(_template):
    gameTemplate =  read_template(_template)
    print(f"""
    Hello, User!

    Lets play a game, its called madlib, you have to fill in 20 words in order to complete the story, here is the example:
    {gameTemplate}

    now, go ahead and start guessing!
    your result will be viewed at the end :D
    """)
    listOfAnswers = []
    for i in range(21):
        listOfAnswers.append(input(f"Enter Word {i}:"))
        
    print("your full response:")
    result = merge_template(parse_template(gameTemplate),listOfAnswers)
    print(result)

    print("saving your response.......")
    newSave = open("./assets/playerSave.txt",'w')
    newSave.write(result)
    newSave.close()
    print("Done!")

start_game(template)
