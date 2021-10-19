from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui

menu_img = ""
menuname = ""
cart = []
# cart = [['Milk Tea', 20, 2, 5], ['Apple Soda', 22, 1, 7]]
member = False
point_use = False
member_name = 'Wan Chanmuang'
point = 0

point_get = 0
final_total = 0


def addproduct(pro):
    check = True
    if len(cart) == 0:
        cart.append([pro[0], pro[1], pro[2], 1])
    else:
        for i in range(len(cart)):
            if cart[i][0] == pro[0]:
                #print("already added")
                check = False
                cart[i][3] = cart[i][3] + 1
                break
        if check == True:
            cart.append([pro[0], pro[1], pro[2], 1])



def pricecalculate():
    total = 0
    for i in cart:
        total = total + int(i[1]) * i[3]

    return total


def point_sum():
    total = 0
    for i in cart:
        total = total + int(i[2]) * i[3]

    return  total


def recipe_view(message):
    font = QtGui.QFont()
    font.setPointSize(16)
    msg = QMessageBox()
    msg.setWindowTitle("Recipe")
    msg.setFont(font)
    msg.setText(message)

    x = msg.exec_()

def show_popuperror(message):
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText(message)
    msg.setIcon(QMessageBox.Critical)
    x = msg.exec_()


def show_popupsuccess(message):
    msg = QMessageBox()
    msg.setWindowTitle("success")
    msg.setText(message)
    x = msg.exec_()

def show_member(name,point):
    font = QtGui.QFont()
    font.setPointSize(16)
    msg = QMessageBox()
    msg.setWindowTitle("Member")
    msg.setFont(font)
    msg.setText("Name : {}\nPoint : {}".format(name,point))
    x = msg.exec_()

def show_member2():
    msg = QMessageBox()
    msg.setWindowTitle("Member")
    msg.setText("ไม่เจอ Member")
    x = msg.exec_()