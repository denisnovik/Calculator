from tkinter import *
from tkinter import messagebox
import math

root = Tk()
root.title("Calculator")

calc_entry = Entry(root, width = 33)
calc_entry.grid(row=0, column=0, columnspan=5)

bttn_list = [
"7", "8", "9", "+", "=",
"4", "5", "6", "-", "/",
"1", "2", "3",  "*", "xⁿ",
"0", ".", "±",  "C", "π", "sin", "cos",
"(", ")","√2", "exp", "log2", "Exit"]

r = 1
c = 0
for i in bttn_list:
    cmd=lambda x=i: calc(x)
    Button(root, text=i, command = cmd,  width = 10).grid(row=r, column = c)
    if c > 4:
        c = 0
        r += 1
    else:
        c += 1

def encode(encode):

    """
    A function that processes the received string for duplicate characters and combines them into one.
    Args:
        encode: Data type: string. Variable holding the raw string

    Returns: Data type: string. The function returns a new variable with the symbols replaced
    """

    stroka = ''
    for i in range(len(encode) - 1):
        if encode[i] == encode[i + 1]:
            pass
        else:
            stroka += encode[i]
        if i == (len(encode) - 2):
            stroka += encode[i + 1]
    return stroka
help(encode)

def sin_value(value, i):

    """
    A function that gets the value of any sine by finding a number from "(" to ")"
    and using the internal library calculates the value of the trigonometric function
    Args:
        value: Data type: string. Variable containing the string entered by the user
        i: Data type: integer. Variable containing the index of the first occurrence of "sin" in the string entered by the user

    Returns: Data type: string. The function returns the value of the trigonometric function that was first mentioned in the string entered by the user
    """

    sinus = ''
    while str(value[i + 4]) != ")":
        sinus = sinus + value[i + 4]
        i = i + 1
    number = str(math.sin(int(sinus)))
    return number
help(sin_value)

def sin_mask(value, i, number):

    """
    The function finds the first occurrence of the value "sin" and replaces "sin(...)" with "ж".
    After the character "ж" is replaced by the number obtained from the sin_value() function.
    Args:
        value: Data type: string. Variable containing the string entered by the user
        i: Data type: integer. Variable containing the index of the first occurrence of "sin" in the string entered by the user
        number: Data type: string. Variable containing a string with the value of the trigonometric function

    Returns: Data type: string. The function returns a string in which the "sin(...)" value has been replaced by "number"
    """
    spisok = list(value)
    while str(spisok[i]) != ")":
        spisok[i] = "ж"
        i = i + 1
    spisok[i] = "ж"
    value = ''.join(spisok)
    value = encode(value)
    value = value.replace("ж", number, 1)
    return value
help(sin_mask)

def sin(value):

    """
    A function that finds all occurrences of "sin" and replaces them with the function's trigonometric value.
    Until all "sin"s have been replaced, the function will not complete.
    Args:
        value: Data type: string. Variable containing the string entered by the user

    Returns: Data type: string. The function returns a string with "sin(...)" replaced with its trigonometric function value
    """

    while value.find("sin") != -1:
        i = value.find('sin')
        number = sin_value(value, i)
        example = sin_mask(value, i, number)
        value = example
    return value
help(sin)

def cos_value(value, i):

    """
    A function that gets the value of any cosine by finding a number from "(" to ")"
    and using the internal library calculates the value of the trigonometric function
    Args:
        value: Data type: string. Variable containing the string entered by the user
        i: Data type: integer. Variable containing the index of the first occurrence of "cos" in the string entered by the user

    Returns: Data type: string. The function returns the value of the trigonometric function that was first mentioned in the string entered by the user
    """

    cosinus = ''
    while str(value[i + 4]) != ")":
        cosinus = cosinus + value[i + 4]
        i = i + 1
    number = str(math.cos(int(cosinus)))
    return number
help(cos_value)

def cos_mask(value, i, number):

    """
    The function finds the first occurrence of the value "cos" and replaces "cos(...)" with "ж".
    After the character "ж" is replaced by the number obtained from the cos_value() function.
    Args:
        value: Data type: string. Variable containing the string entered by the user
        i: Data type: integer. Variable containing the index of the first occurrence of "cos" in the string entered by the user
        number: Data type: string. Variable containing a string with the value of the trigonometric function

    Returns: Data type: string. The function returns a string in which the "cos(...)" value has been replaced by "number"
    """

    spisok = list(value)
    while str(spisok[i]) != ")":
        spisok[i] = "ж"
        i = i + 1
    spisok[i] = "ж"
    value = ''.join(spisok)
    value = encode(value)
    value = value.replace("ж", number, 1)
    return value
help(cos_mask)

def cos(value):

    """
    A function that finds all occurrences of "cos" and replaces them with the function's trigonometric value.
    Until all "cos"s have been replaced, the function will not complete.
    Args:
        value: Data type: string. Variable containing the string entered by the user

    Returns: Data type: string. The function returns a string with "cos(...)" replaced with its trigonometric function value
    """

    while value.find("cos") != -1:
        i = value.find('cos')
        number = cos_value(value, i)
        example = cos_mask(value, i, number)
        value = example
    return value
help(cos)

def plusminus(value):

    """
    A function that finds all possible locations next to the "+" and "-" signs.
    They are combined into one "-" or "+" depending on the arrangement.
    Args:
        value: Data type: string. Variable containing the string entered by the user

    Returns: Data type: string. Function, returns a string with characters replaced by new ones
    """

    while value.find("--") != -1 or value.find("-+") != -1 or value.find("+-") != -1 or value.find("++") != -1:
        if value.find("--") != -1:
            i = value.find("--")
            value = value.replace("--", "+")
        elif value.find("-+") != -1:
            i = value.find("-+")
            value = value.replace("-+", "-")
        elif value.find("+-") != -1:
            i = value.find("+-")
            value = value.replace("+-", "-")
        elif value.find("++") != -1:
            i = value.find("++")
            value = value.replace("++", "+")
    return value
help(plusminus)

def e_value(value, i):

    """
    A function that takes the value of any exponent by finding the power from "^" to the
    last number and using the internal library calculates
    Args:
        value: Data type: string. Variable containing the string entered by the user
        i: Data type: integer. Variable containing the index of the first occurrence of "e" in the string entered by the user

    Returns: Data type: string. The function returns the value of the exponent that was first mentioned in the string entered by the user
    """

    e = ''
    symb = "-+.*/)( "
    while str(value[i + 2]) not in symb and (i + 2) <= (len(value) - 1):
        if (i + 2) == (len(value) - 1):
            e = e + value[i + 2]
            break
        else:
            e = e + value[i + 2]
            i = i + 1
    number = str(math.exp(int(e)))
    return number
help(e_value)

def e_mask(value, i, number):

    """
    The function finds the first occurrence of the value "e" and replaces "e^..." with "ж".
    After the character "ж" is replaced by the number obtained from the e_value() function.
    Args:
        value: Data type: string. Variable containing the string entered by the user
        i: Data type: integer. Variable containing the index of the first occurrence of "e" in the string entered by the user
        number: Data type: string. Variable containing a string with the computed exponent value

    Returns: Data type: string. The function returns a string in which the "e^..." value has been replaced by "number"
    """

    spisok = list(value)
    symb = "-+.*/)( "
    while str(value[i]) not in symb and i <= (len(value) - 1):
        if i == (len(value)-1):
            spisok[i] = "ж"
            break
        else:
            spisok[i] = "ж"
            i = i + 1
    value = ''.join(spisok)
    value = encode(value)
    value = value.replace("ж", number, 1)
    return value
help(e_mask)

def exponenta(value):

    """
    A function that finds all occurrences of "e" and replaces them with computed exponent values.
    Until all "e"s have been replaced, the function will not complete.
    Args:
        value: Data type: string. Variable containing the string entered by the user

    Returns: Data type: string. The function returns a string with "e^..." replaced with computed exponent values
    """

    symb = "-+.*/)( "
    while value.find("e") != -1:
        i = value.find('e')
        number = e_value(value, i)
        example = e_mask(value, i, number)
        value = example
    return value
help(exponenta)

def log_value(value, i):

    """
    A function that takes the value of any logarithm in base 2, finding the argument
    from "(" to ")" and using the internal library is calculated
    Args:
        value: Data type: string. Variable containing the string entered by the user
        i: Data type: integer. Variable containing the index of the first occurrence of "log2" in the string entered by the user

    Returns: Data type: string. The function returns the base 2 logarithm value that is first mentioned in the string entered by the user.
    """

    log = ''
    while str(value[i + 5]) != ")":
        log = log + value[i + 5]
        i = i + 1
    number = str(math.log2(int(log)))
    return number
help(log_value)

def log_mask(value, i, number):

    """
    The function finds the first occurrence of the value "log2" and replaces "log2(...)" with "ж".
    After the character "ж" is replaced by the number obtained from the log_value() function.
    Args:
        value: Data type: string. Variable containing the string entered by the user
        i: Data type: integer. Variable containing the index of the first occurrence of "log2" in the string entered by the user
        number: Data type: string. Variable containing a string with the computed exponent value

    Returns: Data type: string. The function returns a string in which the "log2(...)" value has been replaced by "number"
    """

    spisok = list(value)
    while str(spisok[i]) != ")":
        spisok[i] = "ж"
        i = i + 1
    spisok[i] = "ж"
    value = ''.join(spisok)
    value = encode(value)
    value = value.replace("ж", number, 1)
    return value
help(log_mask)

def logarifm(value):

    """
    A function that finds all occurrences of "log2" and replaces them with the computed logarithm values.
    Until all "log2"s have been replaced, the function will not complete.
    Args:
        value: Data type: string. Variable containing the string entered by the user

    Returns: Data type: string. The function returns a string with "log2(...)" replaced by the computed logarithm values.
    """

    while value.find("log2") != -1:
        i = value.find('log2')
        number = log_value(value, i)
        example = log_mask(value, i, number)
        value = example
    return value
help(logarifm)

def sqrt_value(value, i):

    """
   A function that takes the value of any root and finds a number
   from "(" to ")" and using the internal library is calculated
   Args:
       value: Data type: string. Variable containing the string entered by the user
       i: Data type: integer. Variable containing the index of the first occurrence of "sqrt" in the string entered by the user

   Returns: Data type: string. The function returns the root value that appears first in the string entered by the user.
   """

    sqrt = ''
    while str(value[i + 5]) != ")":
        sqrt = sqrt + value[i + 5]
        i = i + 1
    number = str(math.sqrt(int(sqrt)))
    return number
help(sqrt_value)

def sqrt_mask(value, i, number):

    """
    The function finds the first occurrence of the value "sqrt" and replaces "sqrt(...)" with "ж".
    After the character "ж" is replaced by the number obtained from the sqrt_value() function.
    Args:
        value: Data type: string. Variable containing the string entered by the user
        i: Data type: integer. Variable containing the index of the first occurrence of "sqrt" in the string entered by the user
        number: Data type: string. Variable containing a string with the computed exponent value

    Returns: Data type: string. The function returns a string in which the "sqrt(...)" value has been replaced by "number"
    """

    spisok = list(value)
    while str(spisok[i]) != ")":
        spisok[i] = "ж"
        i = i + 1
    spisok[i] = "ж"
    value = ''.join(spisok)
    value = encode(value)
    value = value.replace("ж", number, 1)
    return value
help(sqrt_mask)

def koren(value):

    """
    A function that finds all occurrences of "sqrt" and replaces them with the computed root values.
    Until all "sqrt"s have been replaced, the function will not complete.
    Args:
        value: Data type: string. Variable containing the string entered by the user

    Returns: Data type: string. The function returns a string with "sqrt(...)" replaced by the computed values of the root.
    """

    while value.find("sqrt") != -1:
        i = value.find('sqrt')
        number = sqrt_value(value, i)
        example = sqrt_mask(value, i, number)
        value = example
    return value
help(koren)

def calc(key):

    """
    A function that is called when any button is clicked and, depending on the event, one of the conditions is met
    Args:
        key: Data type: string. Variable containing the string one of the pressed buttons

    Returns: The function executes one of the conditions depending on the pressed button
    """

    if key == "=":
        try:
            check1 = logarifm(calc_entry.get())
            check2 = exponenta(check1)
            check3 = cos(check2)
            check4 = sin(check3)
            check5 = plusminus(check4)
            check6 = koren(check5)
            calc_entry.delete(0, END)
            calc_entry.insert(END, eval(check6))
        except Exception:
            messagebox.showerror("Error!", "Check the correctness of data")
            calc_entry.delete(0, END)
    elif key == "exp":
        calc_entry.insert(END, "e^")
    elif key == "log2":
        calc_entry.insert(END, "log2")
    elif key == "xⁿ":
        calc_entry.insert(END, "**")
    elif key == "sin":
        calc_entry.insert(END, "sin")
    elif key == "cos":
        calc_entry.insert(END, "cos")
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")
    elif key == "√2":
        calc_entry.insert(END, 'sqrt')
    elif key == "π":
        calc_entry.insert(END, math.pi)
    elif key == "Exit":
        root.after(1, root.destroy)
    elif key == "C":
        calc_entry.delete(0, END)
    elif key == "±":
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except Exception:
            pass
help(calc)

root.mainloop()
