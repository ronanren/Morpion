#!/usr/bin/env python
# coding: utf-8
from tkinter import *

x = 0
fenetre = Tk()
fenetre.geometry("590x350+400+300")
fenetre.title("Morpion")
fenetre.configure(bg = "#00A7EB") 
fenetre.resizable(width=False, height=False)
zbeub = 0
case1 = Canvas(fenetre,width="140", height ="100", background="white")
case1.place(x="80",y="20")
case2 = Canvas(fenetre,width="140", height ="100", background="white")
case2.place(x="80",y="120")
case3 = Canvas(fenetre,width="140", height ="100", background="white")
case3.place(x="80",y="220")
case4 = Canvas(fenetre,width="140", height ="100", background="white")
case4.place(x="220",y="20")
case5 = Canvas(fenetre,width="140", height ="100", background="white")
case5.place(x="220",y="120")
case6 = Canvas(fenetre,width="140", height ="100", background="white")
case6.place(x="220",y="220")
case7 = Canvas(fenetre,width="140", height ="100", background="white")
case7.place(x="360",y="20")
case8 = Canvas(fenetre,width="140", height ="100", background="white")
case8.place(x="360",y="120")
case9 = Canvas(fenetre,width="140", height ="100", background="white")
case9.place(x="360",y="220")
messagewin = Canvas(fenetre,width = "260",height="30", background="#EB002E")
messagewin.place(x="155",y="0")
tourx = Canvas(fenetre,width="80",height="50", background="#74F0AC")
tourx.place(x="-3",y="100")
touro = Canvas(fenetre,width="90",height="50", background="#74F0AC")
touro.place(x="502",y="100")
developer = Canvas(fenetre,width="200",height="24", background="#6DFDFD")
developer.place(x="0",y="322")
prenom = developer.create_text(101,11,text="developpé par Ronan",fill="#00A7EB",font="Impact 11")
case_confirm1 = 0
case_confirm2 = 0
case_confirm3 = 0
case_confirm4 = 0
case_confirm5 = 0
case_confirm6 = 0
case_confirm7 = 0
case_confirm8 = 0
case_confirm9 = 0
joueur11 = "c"
joueur21 = "d"
joueur31 = "e"
joueur41 = "f"
joueur51 = "g"
joueur61 = "l"
joueur71 = "m"
joueur81 = "n"
joueur91 = "o"
joueur12 = "p"
joueur22 = "q"
joueur32 = "r"
joueur42 = "s"
joueur52 = "t"
joueur62 = "u"
joueur72 = "v"
joueur82 = "w"
joueur92 = "x"
nbr1 = 0
nbr2 = 0
nbr3 = 0
nbr4 = 0
nbr5 = 0
nbr6 = 0
nbr7 = 0
nbr8 = 0
nbr9 = 0
text11 = 1
text22 = 1
text33 = 1
text44 = 1
text55 = 1
text66 = 1
text77 = 1
text88 = 1
text99 = 1
def principale():
    global zbeub, messagewin, nbr1, nbr2, nbr3, nbr4, nbr5, nbr6, nbr7, nbr8, nbr9, enleve,text1 , x, case_confirm1, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
    tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
    def click1(event):
        global zbeub, enleve,text1 , x, case_confirm1, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case1")
        if x == 0:
            messagewin.delete(ALL)
        if case_confirm1 == 0 and zbeub == 0 :
            if x == 0 or x == 2 or x == 4 or x == 6 or x == 8 :
                text1 = case1.create_text(70,50,text="X",font ="Impact 50",fill="black")
                case_confirm1 = 1
                x = x + 1
                joueur11 = "a"
                nbr1 = 1
                tourx.delete(ALL)
                touromsg = touro.create_text(40,25,text="au tour du\n  joueur O",fill="white",font="Impact 13")
            else:
                text11 = case1.create_text(70,50,text="O",font ="Impact 50",fill="black")
                case_confirm1 = 1
                x = x + 1
                joueur12 = "b"
                touro.delete(ALL)
                tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
       
        else:
            pass
        
        gagner()
#====================================================================================
    
    def click2(event):
        global x, text2, text22, case_confirm2, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case2")
        if x == 0:
            messagewin.delete(ALL)
        if case_confirm2 == 0 and zbeub == 0:
            if x == 0 or x == 2 or x == 4 or x == 6 or x == 8 :
                text2 = case2.create_text(70,50,text="X",font ="Impact 50",fill="black")
                case_confirm2 = 1
                x = x + 1
                joueur21 = "a"
                nbr2 = 1
                tourx.delete(ALL)
                touromsg = touro.create_text(40,25,text="au tour du\n  joueur O",fill="white",font="Impact 13")
            else:
                text22 = case2.create_text(70,50,text="O",font ="Impact 50",fill="black")
                case_confirm2 = 1
                x = x + 1
                joueur22 = "b"
                touro.delete(ALL)
                tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
       
        else :
            pass
        gagner()
#====================================================================================
    
    def click3(event):
        global x, text3, text33, case_confirm3, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case3")
        if x == 0:
            messagewin.delete(ALL)
        if case_confirm3 == 0 and zbeub == 0:
            if x == 0 or x == 2 or x == 4 or x == 6 or x == 8 :
                text3 = case3.create_text(70,50,text="X",font ="Impact 50",fill="black")
                case_confirm3 = 1
                x = x + 1
                joueur31 = "a"
                nbr3 = 1
                tourx.delete(ALL)
                touromsg = touro.create_text(40,25,text="au tour du\n  joueur O",fill="white",font="Impact 13")
            else:
                text33 = case3.create_text(70,50,text="O",font ="Impact 50",fill="black")
                case_confirm3 = 1
                x = x + 1
                joueur32 = "b"
                touro.delete(ALL)
                tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
       
        else :
            pass
        gagner()
     
#====================================================================================
    
    def click4(event):
        global x, text4,text44 , case_confirm4, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case4")
        if x == 0:
            messagewin.delete(ALL)
        if case_confirm4 == 0 and zbeub == 0:
            if x == 0 or x == 2 or x == 4 or x == 6 or x == 8 :
                text4 = case4.create_text(70,50,text="X",font ="Impact 50",fill="black")
                case_confirm4 = 1
                x = x + 1
                joueur41 = "a"
                nbr4 = 1
                tourx.delete(ALL)
                touromsg = touro.create_text(40,25,text="au tour du\n  joueur O",fill="white",font="Impact 13")
            else:
                text44 = case4.create_text(70,50,text="O",font ="Impact 50",fill="black")
                case_confirm4 = 1
                x = x + 1
                joueur42 = "b"
                touro.delete(ALL)
                tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
        
        else :
            pass
        gagner()
#====================================================================================
    
    def click5(event):
        global x,text5, text55, case_confirm5, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case5")
        if x == 0:
            messagewin.delete(ALL)
        if case_confirm5 == 0 and zbeub == 0:
            if x == 0 or x == 2 or x == 4 or x == 6 or x == 8 :
                text5 = case5.create_text(70,50,text="X",font ="Impact 50",fill="black")
                case_confirm5 = 1
                x = x + 1
                joueur51 = "a"
                nbr5 = 1
                tourx.delete(ALL)
                touromsg = touro.create_text(40,25,text="au tour du\n  joueur O",fill="white",font="Impact 13")
            else:
                text55 = case5.create_text(70,50,text="O",font ="Impact 50",fill="black")
                case_confirm5 = 1
                x = x + 1
                joueur52 = "b"
                touro.delete(ALL)
                tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
        
        else :
            pass
        gagner()
#====================================================================================
    
    def click6(event):
        global x,text6, text66 , case_confirm6, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case6")
        if x == 0:
            messagewin.delete(ALL)
        if case_confirm6 == 0 and zbeub == 0:
            if x == 0 or x == 2 or x == 4 or x == 6 or x == 8 :
                text6 = case6.create_text(70,50,text="X",font ="Impact 50",fill="black")
                case_confirm6 = 1
                x = x + 1
                joueur61 = "a"
                nbr6 = 1
                tourx.delete(ALL)
                touromsg = touro.create_text(40,25,text="au tour du\n  joueur O",fill="white",font="Impact 13")
            else:
                text66 = case6.create_text(70,50,text="O",font ="Impact 50",fill="black")
                case_confirm6 = 1
                x = x + 1
                joueur62 = "b"
                touro.delete(ALL)
                tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
       
        else :
            pass
        gagner()
#====================================================================================
    
    def click7(event):
        global x,text7,text77 , case_confirm7, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case7")
        if x == 0:
            messagewin.delete(ALL)
        if case_confirm7 == 0 and zbeub == 0:
            if x == 0 or x == 2 or x == 4 or x == 6 or x == 8 :
                text7 = case7.create_text(70,50,text="X",font ="Impact 50",fill="black")
                case_confirm7 = 1
                x = x + 1
                joueur71 = "a"
                nbr7 = 1
                tourx.delete(ALL)
                touromsg = touro.create_text(40,25,text="au tour du\n  joueur O",fill="white",font="Impact 13")
            else:
                text77 = case7.create_text(70,50,text="O",font ="Impact 50",fill="black")
                case_confirm7 = 1
                x = x + 1
                joueur72 = "b"
                touro.delete(ALL)
                tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
        else :
            pass
        gagner()

    
    def click8(event):
        global x,text8, text88 , case_confirm8, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case8")
        if x == 0:
            messagewin.delete(ALL)
        if case_confirm8 == 0 and zbeub == 0:
            if x == 0 or x == 2 or x == 4 or x == 6 or x == 8 :
                text8 = case8.create_text(70,50,text="X",font ="Impact 50",fill="black")
                case_confirm8 = 1
                x = x + 1
                joueur81 = "a"
                nbr8 = 1
                tourx.delete(ALL)
                touromsg = touro.create_text(40,25,text="au tour du\n  joueur O",fill="white",font="Impact 13")
            else:
                text88 = case8.create_text(70,50,text="O",font ="Impact 50",fill="black")
                case_confirm8 = 1
                x = x + 1
                joueur82 = "b"
                touro.delete(ALL)
                tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
        else :
            pass
        gagner()

    def click9(event):
        global x,text9, text99, case_confirm9, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case9")
        if x == 0:
            messagewin.delete(ALL)
        if case_confirm9 == 0 and zbeub == 0:
            if x == 0 or x == 2 or x == 4 or x == 6 or x == 8 :
                text9 = case9.create_text(70,50,text="X",font ="Impact 50",fill="black")
                case_confirm9 = 1
                x = x + 1
                joueur91 = "a"
                nbr9 = 1
                tourx.delete(ALL)
                touromsg = touro.create_text(40,25,text="au tour du\n  joueur O",fill="white",font="Impact 13")
            else:
                text99 = case9.create_text(70,50,text="O",font ="Impact 50",fill="black")
                case_confirm9 = 1
                x = x + 1
                joueur92 = "b"
                touro.delete(ALL)
                tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
        else :
            pass
        gagner()
    case1.bind('<Button-1>', click1)
    case2.bind('<Button-1>', click2)
    case3.bind('<Button-1>', click3)
    case4.bind('<Button-1>', click4)
    case5.bind('<Button-1>', click5)
    case6.bind('<Button-1>', click6)
    case7.bind('<Button-1>', click7)
    case8.bind('<Button-1>', click8)
    case9.bind('<Button-1>', click9)
def enleve():
    global  messagewin, text11,text2, text22,text3,text33,text4,text44,text5,text55,text6,text66,text7,text77,text8,text88,text9,text99, nbr1,nbr2, nbr3, nbr4, nbr5, nbr6, nbr7, nbr8, nbr9 ,case_confirm1,case_confirm2,case_confirm3,case_confirm4,case_confirm5,case_confirm6,case_confirm7,case_confirm8,case_confirm9, x,click11 ,text1 , case_confirm3, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
    if nbr1 == 1:
        case1.move(text1, 100, 100)
    else:
        case1.move(text11,100, 100) 
    if nbr2 == 1:
        case2.move(text2, 100, 100)
    else:
        case2.move(text22,100, 100)  
    if nbr3 == 1:
        case3.move(text3, 100, 100)
    else:
        case3.move(text33,100, 100)
    if nbr4 == 1:
        case4.move(text4, 100, 100)
    else:
        case4.move(text44,100, 100)
    if  nbr6 == 1:
        case6.move(text6, 100, 100)
    else:
        case6.move(text66,100, 100)
    if nbr7 == 1:
        case7.move(text7, 100, 100)
    else:
        case7.move(text77,100, 100)
    if nbr8 == 1:
        case8.move(text8, 100, 100)
    else:
        case8.move(text88,100, 100)
    if nbr9 == 1:
        case9.move(text9, 100, 100)
    else:
        case9.move(text99,100, 100)
    if (nbr5 == 1):
        case5.move(text5, 100, 100)
    else:
        case5.move(text55,100, 100)
def winX():
    global  tourx,touro,text11,text2, text22,text3,text33,text4,text44,text5,text55,text6,text66,text7,text77,text8,text88,text9,text99, nbr1,nbr2, nbr3, nbr4, nbr5, nbr6, nbr7, nbr8, nbr9 ,case_confirm1,case_confirm2,case_confirm3,case_confirm4,case_confirm5,case_confirm6,case_confirm7,case_confirm8,case_confirm9, x,click11 ,text1 , case_confirm3, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
    print ("joueur X a gagne")
    messagewin.delete(ALL)
    messagewin1 = messagewin.create_text(130,15,text="bravo, joueur X a gagne !",fill="white",font="Impact 18")
    
    

def winO():
    global  tourx,touro,text11,text2, text22,text3,text33,text4,text44,text5,text55,text6,text66,text7,text77,text8,text88,text9,text99, nbr1,nbr2, nbr3, nbr4, nbr5, nbr6, nbr7, nbr8, nbr9 ,case_confirm1,case_confirm2,case_confirm3,case_confirm4,case_confirm5,case_confirm6,case_confirm7,case_confirm8,case_confirm9, x,click11 ,text1 , case_confirm3, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
    print ("joueur O a gagne")
    messagewin.delete(ALL)
    messagewin1 = messagewin.create_text(130,15,text="bravo, joueur O a gagne !",fill="white",font="Impact 18")

        
def recommencer():
    global  zbeub, text11,text2, text22,text3,text33,text4,text44,text5,text55,text6,text66,text7,text77,text8,text88,text9,text99, nbr1,nbr2, nbr3, nbr4, nbr5, nbr6, nbr7, nbr8, nbr9 ,case_confirm1,case_confirm2,case_confirm3,case_confirm4,case_confirm5,case_confirm6,case_confirm7,case_confirm8,case_confirm9, x,click11 ,text1 , case_confirm3, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
    enleve()
    messagewin.delete(ALL)
    x = 0
    zbeub = 0
    tourx.delete(ALL)
    touro.delete(ALL)
    case1.delete(ALL)
    case2.delete(ALL)
    case3.delete(ALL)
    case4.delete(ALL)
    case5.delete(ALL)
    case6.delete(ALL)
    case7.delete(ALL)
    case8.delete(ALL)
    case9.delete(ALL)
    case_confirm1 = 0
    case_confirm2 = 0
    case_confirm3 = 0
    case_confirm4 = 0
    case_confirm5 = 0
    case_confirm6 = 0
    case_confirm7 = 0
    case_confirm8 = 0
    case_confirm9 = 0
    joueur11 = "c"
    joueur21 = "d"
    joueur31 = "e"
    joueur41 = "f"
    joueur51 = "g"
    joueur61 = "l"
    joueur71 = "m"
    joueur81 = "n"
    joueur91 = "o"
    joueur12 = "p"
    joueur22 = "q"
    joueur32 = "r"
    joueur42 = "s"
    joueur52 = "t"
    joueur62 = "u"
    joueur72 = "v"
    joueur82 = "w"
    joueur92 = "x"
    principale()
    
def gagner():
    global  zbeub, tourx,touro,text11,text2, text22,text3,text33,text4,text44,text5,text55,text6,text66,text7,text77,text8,text88,text9,text99, nbr1,nbr2, nbr3, nbr4, nbr5, nbr6, nbr7, nbr8, nbr9 ,case_confirm1,case_confirm2,case_confirm3,case_confirm4,case_confirm5,case_confirm6,case_confirm7,case_confirm8,case_confirm9, x,click11 ,text1 , case_confirm3, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
    if joueur11 == joueur21 == joueur31:
        zbeub = 1
        winX()
    if joueur12 == joueur22 == joueur32:
        winO()
        zbeub = 1
    if joueur41 == joueur51 == joueur61:
        winX()
        zbeub = 1
    if joueur42 == joueur52 == joueur62:
        winO()
        zbeub = 1
    if joueur71 == joueur81 == joueur91:
        winX()
        zbeub = 1
    if joueur72 == joueur82 == joueur92:
        winO()
        zbeub = 1
    if joueur11 == joueur41 == joueur71:
        winX()
        zbeub = 1
    if joueur12 == joueur42 == joueur72:
        winO()
        zbeub = 1
    if joueur21 == joueur51 == joueur81:
        winX()
        zbeub = 1
    if joueur22 == joueur52 == joueur82:
        winO()
        zbeub = 1
    if joueur31 == joueur61 == joueur91:
       winX()
       zbeub = 1
    if joueur32 == joueur62 == joueur92:
        winO()
        zbeub = 1
    if joueur11 == joueur51 == joueur91:
        winX()
        zbeub = 1
    if joueur12 == joueur52 == joueur92:
       winO()
       zbeub = 1
    if joueur31 == joueur51 == joueur71:
        winX()
        zbeub = 1
    if joueur32 == joueur52 == joueur72:
        winO()
        zbeub = 1
recommencer = Button(fenetre,text="recommencer",command = recommencer).place(x="505",y="323")
principale()
fenetre.mainloop()
