# from tkinter import *
# first_number=second_number=operator=None
# def get_digit(digit):
#     current = result_label['text']
#     new = current + str(digit)
#     result_label.config(text=new)

# def clear():
#     result_label.config(text='')

# def get_operator(op):
#     global first_number,operator
#     first_number = int(result_label['text'])
#     operator = op
#     result_label.config(text='')

# def get_result():
#     global first_number,second_number,operator

#     second_number = int(result_label['text'])

#     if operator == '+':
#         result_label.config(text=str(first_number+second_number))
#     elif operator == '-':
#         result_label.config(text=str(first_number - second_number))
#     elif operator == '*':
#         result_label.config(text=str(first_number * second_number))
#     else:
#         if second_number == 0:
#             result_label.config(text='Error')
#         else:
#             result_label.config(text=str(round(first_number / second_number,2)))

# root = Tk()
# root.title('Calculator')
# root.geometry('280x380')
# root.resizable(0,0)
# root.configure(background='black')

# result_label = Label(root,text='',bg='black',fg='white')
# result_label.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky='w')
# result_label.config(font=('verdana',30,'bold'))

# btn7 = Button(root,text='7',bg="#2f3331",fg='white',width=5,height=2,command=lambda :get_digit(7))
# btn7.grid(row=1,column=0)
# btn7.config(font=('verdana',14))

# btn8 = Button(root,text='8',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(8))
# btn8.grid(row=1,column=1)
# btn8.config(font=('verdana',14))

# btn9 = Button(root,text='9',bg="#88a600",fg='white',width=5,height=2,command=lambda :get_digit(9))
# btn9.grid(row=1,column=2)
# btn9.config(font=('verdana',14))

# btn_add = Button(root,text='+',bg="#dce6e1",fg='white',width=5,height=2,command=lambda :get_operator('+'))
# btn_add.grid(row=1,column=3)
# btn_add.config(font=('verdana',14))

# btn4 = Button(root,text='4',bg="#04351f",fg='white',width=5,height=2,command=lambda :get_digit(4))
# btn4.grid(row=2,column=0)
# btn4.config(font=('verdana',14))

# btn5 = Button(root,text='5',bg="#2d5f48",fg='white',width=5,height=2,command=lambda :get_digit(5))
# btn5.grid(row=2,column=1)
# btn5.config(font=('verdana',14))

# btn6 = Button(root,text='6',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(6))
# btn6.grid(row=2,column=2)
# btn6.config(font=('verdana',14))

# btn_sub = Button(root,text='-',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('-'))
# btn_sub.grid(row=2,column=3)
# btn_sub.config(font=('verdana',14))

# btn1 = Button(root,text='1',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(1))
# btn1.grid(row=3,column=0)
# btn1.config(font=('verdana',14))

# btn2 = Button(root,text='2',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(2))
# btn2.grid(row=3,column=1)
# btn2.config(font=('verdana',14))

# btn3 = Button(root,text='3',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(3))
# btn3.grid(row=3,column=2)
# btn3.config(font=('verdana',14))

# btn_mul = Button(root,text='*',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('*'))
# btn_mul.grid(row=3,column=3)
# btn_mul.config(font=('verdana',14))

# btn_clr = Button(root,text='C',bg='#00a65a',fg='white',width=5,height=2,command=lambda :clear())
# btn_clr.grid(row=4,column=0)
# btn_clr.config(font=('verdana',14))

# btn0 = Button(root,text='0',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(0))
# btn0.grid(row=4,column=1)
# btn0.config(font=('verdana',14))

# btn_equals = Button(root,text='=',bg='#00a65a',fg='white',width=5,height=2,command=get_result)
# btn_equals.grid(row=4,column=2)
# btn_equals.config(font=('verdana',14))

# btn_div = Button(root,text='/',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('/'))
# btn_div.grid(row=4,column=3)
# btn_div.config(font=('verdana',14))

# root.mainloop()



# Python program to create a simple GUI 
# calculator using Tkinter 
# import everything from tkinter module 
from tkinter import *
# globally declare the expression variable 
expression = "" 
# Function to update expression 
# in the text entry box 
def press(num): 
    # point out the global expression variable 
    global expression 
 
    # concatenation of string 
    expression = expression + str(num) 
 
    # update the expression by using set method 
    equation.set(expression) 
 
 
# Function to evaluate the final expression 
def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
 
    # Put that code inside the try block 
    # which may generate the error 
    try: 
 
        global expression 
 
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(expression)) 
 
        equation.set(total) 
 
        # initialize the expression variable 
        # by empty string 
        expression = "" 
 
    # if error is generate then handle 
    # by the except block 
    except: 
 
        equation.set(" error ") 
        expression = "" 
 
 
# Function to clear the contents 
# of text entry box 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
 
 
# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk() 
 
    # set the background colour of GUI window 
    gui.configure(background="light green") 
 
    # set the title of GUI window 
    gui.title("Simple Calculator") 
 
    # set the configuration of GUI window 
    gui.geometry("270x150") 
 
    # StringVar() is the variable class 
    # we create an instance of this class 
    equation = StringVar() 
 
    # create the text entry box for 
    # showing the expression . 
    expression_field = Entry(gui, textvariable=equation) 

    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    expression_field.grid(columnspan=4, ipadx=70)

    # create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed . 
    button1 = Button(gui, text=' 1 ', fg='black', bg='red', command=lambda: press(1), height=1, width=7) 
    button1.grid(row=2, column=0) 
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='red', command=lambda: press(2), height=1, width=7) 
    button2.grid(row=2, column=1) 
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='red', command=lambda: press(3), height=1, width=7) 
    button3.grid(row=2, column=2) 
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='red', command=lambda: press(4), height=1, width=7) 
    button4.grid(row=3, column=0) 
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='red', command=lambda: press(5), height=1, width=7) 
    button5.grid(row=3, column=1) 
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='red', command=lambda: press(6), height=1, width=7) 
    button6.grid(row=3, column=2) 
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='red', command=lambda: press(7), height=1, width=7) 
    button7.grid(row=4, column=0) 
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='red', command=lambda: press(8), height=1, width=7) 
    button8.grid(row=4, column=1) 
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='red', command=lambda: press(9), height=1, width=7) 
    button9.grid(row=4, column=2) 
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='red', command=lambda: press(0), height=1, width=7) 
    button0.grid(row=5, column=0) 
 
    plus = Button(gui, text=' + ', fg='black', bg='blue', command=lambda: press("+"), height=1, width=7) 
    plus.grid(row=2, column=3) 
 
    minus = Button(gui, text=' - ', fg='black', bg='red', command=lambda: press("-"), height=1, width=7) 
    minus.grid(row=3, column=3) 
 
    multiply = Button(gui, text=' * ', fg='black', bg='green', command=lambda: press("*"), height=1, width=7) 
    multiply.grid(row=4, column=3) 
 
    divide = Button(gui, text=' / ', fg='black', bg='red', command=lambda: press("/"), height=1, width=7) 
    divide.grid(row=5, column=3) 
 
    equal = Button(gui, text=' = ', fg='black', bg='red', command=equalpress, height=1, width=7) 
    equal.grid(row=5, column=2) 
 
    clear = Button(gui, text='Clear', fg='black', bg='red', command=clear, height=1, width=7) 
    clear.grid(row=5, column='1')
 
    Decimal= Button(gui, text='.', fg='black', bg='red', command=lambda: press('.'), height=1, width=7) 
    Decimal.grid(row=6, column=0) 
    # start the GUI 
    gui.mainloop() 