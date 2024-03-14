import math


def sep(exp):
    # getting separate terms
    separate = []  # list that separates the equation based on + and -
    nstr = ""
    ind = []
    for i in range(len(exp)):
        if exp[i] == "+" or exp[i] == "-" or exp[i] == "=":
            ind.append(i)
    for i in range(len(ind)):
        if i == 0:
            separate.append(exp[:ind[i]])
        if i == len(ind) - 1:
            separate.append(exp[ind[i]::])
        else:
            separate.append(exp[ind[i]:ind[i + 1]])
    return separate


def check_quad(exp):
    separate = sep(exp)
    var = variable(exp)
    # checking if its a linear equation or quadratic equation
    if len(var) == 1:
        for el in separate:
            if "**2" in el:
                return 2
            elif "**" not in el or "**1" in el:
                x = 1
            else:
                x = 0
        return x


def variable(exp):
    separate = sep(exp)
    var = []
    for let in exp:
        if let.isalpha() and let not in var:
            var.append(let)
    return var


def linearsoln(eqn):
    var = variable(eqn)
    expression = eqn.replace("=", "-(") + ")"  # bringing everything to right side
    grouped = eval(expression.replace(var[0], '1j'))  # as python can evaluate j we replace x with j
    print(var[0], "=", -grouped.real / grouped.imag)  # -b/a is the answer


def simplify(eqn):
    expr = eqn.replace("**", "^")
    nexpr = ""
    for a in range(len(expr) - 1):
        if expr[a].isalpha() and not expr[a + 1] == "^":
            nexpr += expr[a] + "^1"
        else:
            nexpr += expr[a]
    nexpr += expr[-1]
    if nexpr[-1].isalpha():
        nexpr += "^1"
    expr = nexpr
    separate = sep(expr)
    var = variable(expr)
    nexpr = ""
    for k in range(len(var)):
        for i in range(len(separate)):
            """li = separate[i].split("*")
            print(separate[i])
            if li[0].lstrip("+").isdigit() or li[0].lstrip("-").isdigit():
                z = li[0]
                separate[i]=separate[i][len(li)[0]:]
            print(separate[i])"""
            if "*" in separate[i]:
                x = separate[i].index("*")
                if var[k] in separate[i][:x] and var[k] in separate[i][x + 1:]:
                    num1, num2 = "", ""
                    ind1 = separate[i][:x].index("^")
                    ind2 = separate[i][x + 1:].index("^") + x + 1
                    for j in range(ind1 + 1, x):
                        num1 += separate[i][j]
                    for j in range(ind2 + 1, len(separate[i])):
                        num2 += separate[i][j]
                    num3 = int(num1) + int(num2)
                    nexpr += separate[i][0] + var[k] + "^" + str(num3)
                    break
            nexpr += separate[i]
    separate = sep(adding_1(nexpr))
    bli = []
    for el in separate:
        li = el.split("*")
        if len(li[0]) > 1:
            if not li[0][1].isdigit():
                li.insert(0, '1')
        else:
            if not li[0].isdigit():
                li.insert(0, '1')
        bli.append(li)
    nbli = []
    for i in range(len(bli)):
        for el in bli[i][1:]:
            nli = list(bli[i][1:])
            x = int(bli[i][0])
            for k in bli[i + 1:]:
                if el not in k:
                    break
                else:
                    x += int(k[0])
            nli.insert(0, str(x))
        for a in nbli:
            if nli[1] in a:
                break
        else:
            nbli.append(nli)
    nexpr = ""
    for elem in nbli:
        nexpr += "+"
        nexpr += "*".join(elem)
    print(nexpr)


def quadsolve(eqn):
    var = variable(eqn)
    i = eqn.index("=")
    temp = int(eqn[i + 1:])
    expr = eqn[:i].replace("**", "^")
    separate = sep(expr)
    bli = []
    for el in separate:
        li = el.split("*")
        if len(li[0]) > 1:
            if not li[0][1].isdigit():
                li.insert(0, '1')
        else:
            if not li[0].isdigit():
                li.insert(0, '1')
        bli.append(li)
    di = {"a": 0, "b": 0, "c": 0}
    for el in bli:
        if len(el) == 1:
            di["c"] = di["c"] + int(el[0])
        elif var[0] + "^2" in el:
            di["a"] = di["a"] + int(el[0])
        elif var[0] in el:
            di["b"] = di["b"] + int(el[0])
    root1 = (-di["b"] + ((di["b"] ** 2 - (4 * di["a"] * di["c"])) ** (1 / 2))) / (2 * di["a"])
    root2 = (-di["b"] - (di["b"] ** 2 - (4 * di["a"] * di["c"])) ** (1 / 2)) / (2 * di["a"])
    print("Root 1: ", root1)
    print("Root 2: ", root2)

def quadsolve2(exp):
    i = eqn.index("=")
    temp = int(eqn[i + 1:])
    if len(temp)>0:
        simplify(temp)



def adding_1(exp):
    nexp = ""
    for i in range(len(exp)):
        if (exp[i] == "+" or exp[i] == "-") and exp[i + 1].isalpha():
            nexp += exp[i] + "1*"
        else:
            nexp += exp[i]
    return nexp


def integrate(eqn, llim, ulim):
    var = variable(eqn)
    # ulim=llim+ nh where n is even
    """if "e" in eqn:
        eqn=eqn.replace("e","math.exp")
    for el in ["sin","cos","tan"]:
        if el in eqn:
            eqn=eqn.replace(el,"math."+el)"""
    h = (float(ulim) - float(llim)) / 4
    temp = float(llim)
    fx, li = 0, []
    for i in range(4 + 1):
        y = eqn.replace(var[0], str(temp))
        li.append(float(eval(y)))
        temp += h
    x = (h / 3) * (li[0] + li[4] + 4 * (li[1] + li[3]) + 2 * li[2])
    print(x)


# main
print("Select option")
print("1. Solve Linear equation")
print("2. Solve quadratic equation")
print("3. Simplify an equation")
print("4. Integration")
opt = int(input("Enter option: "))
exp = input("Enter expression: ")
separate = sep(exp)
if opt == 3:
    simplify(exp)
elif opt == 1:
    linearsoln(exp)
elif opt == 2:
    quadsolve(exp)
elif opt == 4:
    limit1 = input("Enter lower limit: ")
    limit2 = input("Enter upper limit: ")
    integrate(exp, limit1, limit2)
