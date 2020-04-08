# Get priority in equation
def Priority(equation):
    equation = equation.replace(" ", "")

    left = 0
    right = 0

    max_priority = 0
    priority = ""

    for char in range(0, len(equation)):
        if equation[char] == "(":
            left += 1
        elif equation[char] == ")":
            right += 1

        if left == right and left != 0 and right != 0:
            rank = left
            if rank > max_priority:
                max_priority = rank
            left = 0
            right = 0

    left = 0
    right = 0
    char = 0

    while char < len(equation):
        if equation[char] == "(":
            left += 1
        elif equation[char] == ")":
            right += 1

        if left == right and left != 0 and right != 0 and left != max_priority:
            left = 0
            right = 0

        if left == max_priority and right == 0:
            if equation[char] != "(":
                while equation[char] != ")":
                    try:
                        priority += equation[char]
                        char += 1
                    except:
                        break

                return priority

        char += 1

    print("Priority: {0}\nLevel: [{1}]\n".format(priority, str(max_priority)))

    if max_priority == 0:
        return ""
    else:
        return priority

def RemoveBrackets(equation):
    equation = equation.replace(" ", "")
    priority = Priority(equation)

    while "(" + priority + ")" in equation:
        try:
            print("{0} --> {1}".format(equation, equation.replace("(" + priority + ")", Calculate(priority))))
            equation = equation.replace("(" + priority + ")", Calculate(priority))
        except:
            print("")

    return equation

def GetItemLeft(equation, operator):
    operators = ["+", "-", "*", "/", "^"]
    equation = equation.replace(" ", "")
    equation = equation.split(operator)[0]

    index = len(equation)-1
    item = ""

    if equation[len(equation)-1] == ")":
        while equation[index] != "(":
            if equation[index] != "(" and equation[index] != ")":
                item += equation[index]
            index -= 1

    else:
        while equation[index] not in operators and equation[index] != "(" and index >= 0:
            if equation[index] != "(" and equation[index] != ")":
                item += equation[index]
            index -= 1


    # Rotate string
    char = len(item)-1
    result = ""
    for a in range(char, -1, -1):
        result += item[a]

    item = result
    if "e+" in item:
        right = GetItemRight(item, "e+")
        left = GetItemLeft(item, "e+")
        item = item.replace("e+" + index, str(float(left) * 10 ** float(right)))

    if "e-" in item:
        right = GetItemRight(item, "e-")
        left = GetItemLeft(item, "e-")
        item = item.replace("e-" + index, str(float(left) * 10 ** (-1 * float(right))))
    return item

def GetItemRight(equation, operator):
    operators = ["+", "-", "*", "/", "^"]
    equation = equation.replace(" ", "")
    equation = equation.split(operator)[1]
    add = False

    index = 0
    item = ""

    if equation[0] == "(":
        while equation[index] != ")":
            if equation[index] != "(" and equation[index] != ")":
                item += equation[index]
            index += 1

    else:
        add = True
        while equation[index] not in operators and equation[index] != ")" and index != len(equation)-1:
            if equation[index] != "(" and equation[index] != ")":
                item += equation[index]
            index += 1

    if add == True:
        item += equation[index]

    if "e+" in item:
        right = GetItemRight(item, "e+")
        left = GetItemLeft(item, "e+")
        item = item.replace("e+" + index, str(float(left) * 10 ** float(right)))

    if "e-" in item:
        right = GetItemRight(item, "e-")
        left = GetItemLeft(item, "e-")
        item = item.replace("e-" + index, str(float(left) * 10 ** (-1 * float(right))))

    for operator in operators:
        item = item.replace(operator, "")
    return item

def Calculate(equation):
    operators = ["+", "-", "*", "/", "^"]
    equation = equation.replace(" ", "")

    ops = False
    for operator in operators:
        if operator in equation:
            ops = True

    if ops == False:
        return equation

    while "(" in equation:
        equation = RemoveBrackets(equation)
    
    while "^" in equation:
        to_replace = GetItemLeft(equation, "^") + "^" + GetItemRight(equation, "^")
        #try:
        replace = float(GetItemLeft(equation, "^")) ** float(GetItemRight(equation, "^"))
        #except:
        #    return equation

        print("Replacing {0} with {1}".format(to_replace, str(replace)))
        print("{0} --> {1}".format(equation, equation.replace(to_replace, str(replace))))

        equation = equation.replace(to_replace, str(replace))

    while "*" in equation:
        to_replace = GetItemLeft(equation, "*") + "*" + GetItemRight(equation, "*")
        #try:
        replace = float(GetItemLeft(equation, "*")) * float(GetItemRight(equation, "*"))
        #except:
        #    return equation

        print("Replacing {0} with {1}".format(to_replace, str(replace)))
        print("{0} --> {1}".format(equation, equation.replace(to_replace, str(replace))))
        equation = equation.replace(to_replace, str(replace))

    while "/" in equation:
        to_replace = GetItemLeft(equation, "/") + "/" + GetItemRight(equation, "/")
        #try:
        replace = float(GetItemLeft(equation, "/")) / float(GetItemRight(equation, "/"))
        #except:
        #    return equation

        print("Replacing {0} with {1}".format(to_replace, str(replace)))
        print("{0} --> {1}".format(equation, equation.replace(to_replace, str(replace))))

        equation = equation.replace(to_replace, str(replace))

    while "+" in equation:
        to_replace = GetItemLeft(equation, "+") + "+" + GetItemRight(equation, "+")
        #try:
        replace = float(GetItemLeft(equation, "+")) + float(GetItemRight(equation, "+"))
        #except:
        #    return equation

        print("Replacing {0} with {1}".format(to_replace, str(replace)))
        print("{0} --> {1}".format(equation, equation.replace(to_replace, str(replace))))

        equation = equation.replace(to_replace, str(replace))

    while "-" in equation:
        to_replace = GetItemLeft(equation, "-") + "-" + GetItemRight(equation, "-")
        #try:
        replace = float(GetItemLeft(equation, "-")) - float(GetItemRight(equation, "-"))
        #except:
        #    return equation

        print("Replacing {0} with {1}".format(to_replace, str(replace)))
        print("{0} --> {1}".format(equation, equation.replace(to_replace, str(replace))))

        equation = equation.replace(to_replace, str(replace))

    return equation
