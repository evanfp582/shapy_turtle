"""
shapy_turtle.py
Author: Evan Fisher-Perez
Description: Asks the user for a string and then draws shapes according to the input
Language: Python 3
"""
import turtle



def chunk(counter,text):
    """
    Takes a string and starting index and finds a non number and the numbers that follow it
    if there are no numbers after the non number there is an error
    :param counter:The current index
    :param text: A user inputted text
    :return:
        nextNonNum: The index of the next character that isn't a number
        finalNumber: The number that was after the non number
    """
    generalList = []
    finalNumber = None
    counter = int(counter) + 1

    nextNonNum = indexNonNum(text, counter)

    if nextNonNum - counter <= 0:
        return "error"
    else:
        for i in range(counter, nextNonNum):
            newNumber = text[i]
            generalList.append(newNumber)
            finalNumber = (''.join(generalList))
    return nextNonNum,finalNumber

def promptUser():
    """
    asks the user for an input
    :return: a string that the user wants
    """
    answer=str(input("What string would you like to input"))
    answer=answer+" "
    return answer

def leftTurn(counter,text):
    """
    Take the text that begins with '<' and find the numbers (if any) afterwards
    Then tell the turtle to move left that amount
    :param counter:The starting index point
    :param text: the originally inputted string
    :return:nextNonNum: The index of the next non number
    """


    result=chunk(counter,text)
    if result == "error":
        # KILL PROGRAM with error statement
        print("ERROR:'<' is missing an angle number after")
        exit()
    nextNonNum=result[0]
    finalNumber=float(result[1])
    #The actual command goes here
    turtle.left(finalNumber)
    return nextNonNum

def rightTurn(counter,text):
    """
        Take the text that begins with '>' and find the numbers (if any) afterwards
        Then tell the turtle to move right that amount
        :param counter:The starting index point
        :param text: the originally inputted string
        :return:nextNonNum: The index of the next non number t
        """
    result = chunk(counter, text)
    if result == "error":
        # KILL PROGRAM with error statement
        print("ERROR:'>' is missing an angle number after")
        exit()
    nextNonNum = result[0]
    finalNumber = float(result[1])
    # The actual command goes here
    turtle.right(finalNumber)
    return nextNonNum

def square(counter,text):
    """
    Makes a square with a size depending on the input
    :param counter: The starting index point
    :param text: The originally inputted string
    :return:nextNonNum: The index of the next non number
    """
    result = chunk(counter, text)
    if result == "error":
        # KILL PROGRAM with error statement
        print("ERROR:'S' is missing an angle number after")
        exit()
    nextNonNum = result[0]
    finalNumber = float(result[1])
    #The actual shape goes here
    turtle.left(90)
    turtle.forward(finalNumber)
    turtle.left(90)
    turtle.forward(finalNumber)
    turtle.left(90)
    turtle.forward(finalNumber)
    turtle.left(90)
    turtle.forward(finalNumber)

    return nextNonNum

def triangle(counter,text):
    """
    Makes a Triangle with a size depending on the input
    :param counter: The starting index point
    :param text: The originally inputted string
    :return:nextNonNum: The index of the next non number
    """
    result = chunk(counter, text)
    if result == "error":
        # KILL PROGRAM with error statement
        print("ERROR:'T' is missing an angle number after")
        exit()
    nextNonNum = result[0]
    finalNumber = float(result[1])
    #The shape drawling here
    turtle.left(120)
    turtle.forward(finalNumber)
    turtle.left(120)
    turtle.forward(finalNumber)
    turtle.left(120)
    turtle.forward(finalNumber)
    return nextNonNum

def circle(counter,text):
    """
    Makes a circle with a radius depending on the input
    :param counter: The starting index point
    :param text: The originally inputted string
    :return:nextNonNum: The index of the next non number
    """
    result = chunk(counter, text)
    if result == "error":
        # KILL PROGRAM with error statement
        print("ERROR:'C' is missing a radius length after")
        exit()
    nextNonNum = result[0]
    finalNumber = float(result[1])
    #Shape drawling here
    turtle.circle(finalNumber)
    return nextNonNum

def forward(counter,text):
    """
    Makes a circle with a radius depending on the input
    :param counter: The starting index point
    :param text: The originally inputted string
    :return:nextNonNum: The index of the next non number
    """
    result = chunk(counter, text)
    if result == "error":
        # KILL PROGRAM with error statement
        print("ERROR:'F' is missing a length after")
        exit()
    nextNonNum = result[0]
    finalNumber = float(result[1])
    #Drawling here
    turtle.forward(finalNumber)
    return nextNonNum

def backward(counter,text):
    """
    Makes a circle with a radius depending on the input
    :param counter: The starting index point
    :param text: The originally inputted string
    :return:nextNonNum: The index of the next non number
    """
    result = chunk(counter, text)
    if result == "error":
        # KILL PROGRAM with error statement
        print("ERROR:'B' is missing a length after")
        exit()
    nextNonNum = result[0]
    finalNumber = float(result[1])
    #Drawling here
    turtle.backward(finalNumber)
    return nextNonNum

def penUp(counter,text):
    """
    Picks pen up
    :param counter: The starting index point
    :param text: The originally inputted string
    :return:nextNonNum: The index of the next non number
    """

    nextNonNum=counter+1
    if text[nextNonNum].isdigit():
        print("ERROR:Not expecting a number after 'U'")
        exit()
    turtle.penup()
    return nextNonNum

def penDown(counter,text):
    """
    Picks pen up
    :param counter: The starting index point
    :param text: The originally inputted string
    :return:nextNonNum: The index of the next non number
    """

    nextNonNum=counter+1
    if text[nextNonNum].isdigit():
        print("ERROR:Not expecting a number after 'U'")
        exit()
    turtle.pendown()
    return nextNonNum

def rectangle(counter,text):
    """
    Draws a rectangle with the parameters given
    :param counter: The starting index point
    :param text: The originally inputted string
    :return:nextNonNum: The index of the next non number
    """
    height = chunk(counter, text)
    if height == "error":
        # KILL PROGRAM with error statement
        print("ERROR:'Height' is missing after 'R'")
        exit()
    nextNonNum = height[0]
    height = float(height[1])

    if text[nextNonNum]!=",":
        print("ERROR. Expecting 2 values separated by a comma")
        exit()

    counter=nextNonNum
    width = chunk(counter, text)
    if width == "error":
        # KILL PROGRAM with error statement
        print("ERROR:'width' is missing after 'R'")
        exit()
    nextNonNum = width[0]
    width = float(width[1])

    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)

    return nextNonNum

def polygon(counter,text):
    """
    Draws a polygon with the parameters given
    :param counter: The starting index point
    :param text: The originally inputted string
    :return:nextNonNum: The index of the next non number
    """
    sideNumber = chunk(counter, text)
    if sideNumber == "error":
        # KILL PROGRAM with error statement
        print("ERROR:'Side number' is missing after 'P'")
        exit()
    nextNonNum = sideNumber[0]
    sideNumber = float(sideNumber[1])

    if text[nextNonNum] != ",":
        print("ERROR. Expecting 2 values separated by a comma")
        exit()

    counter = nextNonNum
    length = chunk(counter, text)
    if length == "error":
        # KILL PROGRAM with error statement
        print("ERROR:'length' is missing after 'P'")
        exit()
    nextNonNum = length[0]
    length = float(length[1])

    angleNumber=360/sideNumber

    for num in range(int(sideNumber)):
        turtle.left(angleNumber)
        turtle.forward(length)


    return nextNonNum

def goTo(counter,text):
    """
    Goes to a specific x and y
    :param counter: The starting index point
    :param text: The originally inputted string
    :return:nextNonNum: The index of the next non number
    """
    xCord = chunk(counter, text)
    if xCord == "error":
        # KILL PROGRAM with error statement
        print("ERROR:'x' is missing after 'G'")
        exit()
    nextNonNum = xCord[0]
    xCord = float(xCord[1])

    if text[nextNonNum] != ",":
        print("ERROR. Expecting 2 values separated by a comma")
        exit()

    counter = nextNonNum
    yCord = chunk(counter, text)
    if yCord == "error":
        # KILL PROGRAM with error statement
        print("ERROR:'y' is missing after 'G'")
        exit()
    nextNonNum = yCord[0]
    yCord = float(yCord[1])
    #Directions go here
    turtle.penup()
    turtle.goto(xCord,yCord)
    turtle.pendown()
    return nextNonNum
def color(counter,text):
    """
    Makes the turtle a color
    :param counter: The starting index point
    :param text: The originally inputted string
    :return:nextNonNum: The index of the next non number
    """
    counter=counter+1
    afterZ=int(text[counter])
    if afterZ==0:
        turtle.pencolor("red")
    elif afterZ==1:
        turtle.pencolor("blue")
    elif afterZ==2:
        turtle.pencolor("green")
    elif afterZ==3:
        turtle.pencolor("yellow")
    elif afterZ==4:
        turtle.pencolor("brown")
    elif afterZ>4:
        turtle.pencolor("black")

    nextNonNum=counter+1
    if text[nextNonNum].isdigit():
        print("Not 2 numbers after 'Z'")
        exit()
    turtle.pendown()
    return nextNonNum

def interpreter(text):
    """
    Takes a short string and translates the shorthand
    :param text: The user inputted string
    :return:
    """
    counter=0
    while counter< len(text):
        if text[counter]=="<":
            counter=leftTurn(counter,text)
        if text[counter]==">":
            counter=rightTurn(counter,text)
        if text[counter]=="S":
            counter=square(counter,text)
        if text[counter]=="T":
            counter=triangle(counter,text)
        if text[counter]=="C":
            counter=circle(counter,text)
        if text[counter]=="F":
            counter=forward(counter,text)
        if text[counter]=="B":
            counter=backward(counter,text)
        if text[counter]=="U":
            counter=penUp(counter,text)
        if text[counter]=="D":
            counter=penDown(counter,text)
        if text[counter]=="R":
            counter=rectangle(counter,text)
        if text[counter]=="P":
            counter=polygon(counter,text)
        if text[counter]=="G":
            counter=goTo(counter,text)
        if text[counter]=="Z":
            counter=color(counter,text)




def indexNonNum(text,counter):
    """
    Takes the text and checks if there are any non-numeric character and then returns the index of the first one
    :param counter:
    :param text: The text that the user imputed
    :return: Returns the index of where the first non-numeric is
    or returns none if there is only numeric characters
    """
    for i in range(counter, len(text)):
        if not text[i].isdigit() and text[i]!="-":
            return int(i)
    return counter


def main():
    """
    Body of the function
    """

    text=promptUser()
    interpreter(text)


    turtle.done()
if __name__ == '__main__':
    main()



