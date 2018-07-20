# -*- coding: utf-8 -*-
from tkinter import *
import time, random
import subprocess

x = 0
checke = ""
xgagne = 0
xperdu = 0
xegalite = 0
iagagne = 0
iaperdu = 0
iaegalite = 0
fenetre = Tk()
fenetre.geometry("790x350+220+220") 
fenetre.title("Morpion avec L'intelligence artificielle")
fenetre.configure(bg = "#00A7EB") 
fenetre.resizable(width=False, height=False)


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
case_confirm1 = 0
case_confirm2 = 0
case_confirm3 = 0
case_confirm4 = 0
case_confirm5 = 0
case_confirm6 = 0
case_confirm7 = 0
case_confirm8 = 0
case_confirm9 = 0
check1 = 0
check2 = 0
check3 = 0
check4 = 0
check5 = 0
check6 = 0
check7 = 0
check8 = 0
check9 = 0
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
recomm = 0
t = 1

def temps():
    global t,p,check1, check2, check3, check4, check5, check6, check7,check8, check9,text11,text22,text33,text44,text55,text66,text77,text88,text99, messagewin, nbr1, nbr2, nbr3, nbr4, nbr5, nbr6, nbr7, nbr8, nbr9, enleve,text1 , x, case_confirm1,case_confirm2,case_confirm3,case_confirm4,case_confirm5,case_confirm6,case_confirm7,case_confirm8,case_confirm9, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
    if t == 1:
        check1 = 1
        check2 = 1
        check3 = 1
        check4 = 1
        check5 = 1
        check6 = 1
        check7 = 1
        check8 = 1
        check9 = 1
        ranf = random.randint(700,1500)
        fenetre.after(ranf, temps)
    elif recomm == 0:
        check1 = 0
        check2 = 0
        check3 = 0
        check4 = 0
        check5 = 0
        check6 = 0
        check7 = 0
        check8 = 0
        check9 = 0
        if x == 1 or x == 3 or x == 5 or x == 7 or x == 9 :
            ia()
    t = 2
    

def ia():
    global p,check1, check2, check3, check4, check5, check6, check7,check8, check9,text11,text22,text33,text44,text55,text66,text77,text88,text99, messagewin, nbr1, nbr2, nbr3, nbr4, nbr5, nbr6, nbr7, nbr8, nbr9, enleve,text1 , x, case_confirm1,case_confirm2,case_confirm3,case_confirm4,case_confirm5,case_confirm6,case_confirm7,case_confirm8,case_confirm9, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
    p = 0
    if case_confirm5 == 0 and p == 0:
        text55 = case5.create_text(70,50,text="O",font ="Impact 50",fill="black")
        case_confirm5 = 1
        x = x + 1
        p = 1
        check5 = 1
        joueur52 = "b"
        tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
        touro.delete(ALL)
        
        
    elif case_confirm5 == 1 and x == 1 and p == 0:
        aleat = random.randint(1,4)
        if aleat == 1 and case_confirm1 == 0:
            text11 = case1.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm1 = 1
            x = x + 1
            p = 1
            check1 = 1
            joueur12 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
        if aleat == 2 and case_confirm3 == 0 and p == 0:
            text33 = case3.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm3 = 1
            x = x + 1
            p = 1
            check3 = 1
            joueur32 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
        if aleat == 3 and case_confirm7 == 0 and p == 0:
            text77 = case7.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm7 = 1
            x = x + 1
            p = 1
            check7 = 1
            joueur72 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
        if aleat == 4 and case_confirm9 == 0 and p == 0:
            text99 = case9.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm9 = 1
            x = x + 1
            p = 1
            check9 = 1
            joueur92 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)



#------------------------------------------ debut forcage de la case du milieu -----------------------------------------------------------
#------------------------------------------ intelligence artificielle en dessous -----------------------------------------------------------


    if joueur42 == "b" and joueur52 == "b" and p == 0:
        if case_confirm6 == 0:
            text66 = case6.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm6 = 1
            x = x + 1
            p = 1
            check6 = 1
            joueur62 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur92 == "b" and joueur62 == "b" and p == 0:
        if case_confirm3 == 0:
            text33 = case3.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm3 = 1
            x = x + 1
            p = 1
            check3 = 1
            joueur32 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur32 == "b" and joueur62 == "b" and p == 0:
        if case_confirm9 == 0:
            text99 = case9.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm9 = 1
            x = x + 1
            p = 1
            check9 = 1
            joueur92 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur92 == "b" and joueur32 == "b" and p == 0:
        if case_confirm6 == 0:
            text66 = case6.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm6 = 1
            x = x + 1
            p = 1
            check6 = 1
            joueur62 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur42 == "b" and joueur62 == "b" and p == 0:
        if case_confirm5 == 0:
            text55 = case5.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm5 = 1
            x = x + 1
            p = 1
            check5 = 1
            joueur52 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur62 == "b" and joueur52 == "b" and p == 0:
        if case_confirm4 == 0:
            text44 = case4.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm4 = 1
            x = x + 1
            p = 1
            check4 = 1
            joueur42 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)


    if joueur72 == "b" and joueur82 == "b" and p == 0:
        if case_confirm9 == 0:
            text99 = case9.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm9 = 1
            x = x + 1
            p = 1
            check9 = 1
            joueur92 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur92 == "b" and joueur72 == "b" and p == 0:
        if case_confirm8 == 0:
            text88 = case8.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm8 = 1
            x = x + 1
            p = 1
            check8 = 1
            joueur82 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur92 == "b" and joueur82 == "b" and p == 0:
        if case_confirm7 == 0:
            text77 = case7.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm7 = 1
            x = x + 1
            p = 1
            check7 = 1
            joueur72 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
            
    if joueur12 == "b" and joueur32 == "b" and p == 0:
        if case_confirm2 == 0:
            text22 = case2.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm2 = 1
            x = x + 1
            p = 1
            check2 = 1
            joueur22 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur12 == "b" and joueur22 == "b" and p == 0:
        if case_confirm3 == 0:
            text33 = case3.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm3 = 1
            x = x + 1
            p = 1
            check3 = 1
            joueur32 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur22 == "b" and joueur32 == "b" and p == 0:
        if case_confirm1 == 0:
            text11 = case1.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm1 = 1
            x = x + 1
            p = 1
            check1 = 1
            joueur12 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur12 == "b" and joueur42 == "b" and p == 0:
        if case_confirm7 == 0:
            text77 = case7.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm7 = 1
            x = x + 1
            p = 1
            check7 = 1
            joueur72 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur12 == "b" and joueur72 == "b" and p == 0:
        if case_confirm4 == 0:
            text44 = case4.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm4 = 1
            x = x + 1
            p = 1
            check4 = 1
            joueur42 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur42 == "b" and joueur72 == "b" and p == 0:
        if case_confirm1 == 0:
            text11 = case1.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm1 = 1
            x = x + 1
            p = 1
            check1 = 1
            joueur12 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)

    if joueur22 == "b" and joueur52 == "b" and p == 0:
        if case_confirm8 == 0:
            text88 = case8.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm8 = 1
            x = x + 1
            p = 1
            check8 = 1
            joueur82 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur52 == "b" and joueur82 == "b" and p == 0:
        if case_confirm2 == 0:
            text22 = case2.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm2 = 1
            x = x + 1
            p = 1
            check2 = 1
            joueur22 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur12 == "b" and joueur52 == "b" and p == 0:
        if case_confirm9 == 0:
            text99 = case9.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm9 = 1
            x = x + 1
            p = 1
            check9 = 1
            joueur92 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur32 == "b" and joueur52 == "b" and p == 0:
        if case_confirm7 == 0:
            text77 = case7.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm7 = 1
            x = x + 1
            p = 1
            check7 = 1
            joueur72 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur72 == "b" and joueur52 == "b" and p == 0:
        if case_confirm3 == 0:
            text33 = case3.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm3 = 1
            x = x + 1
            p = 1
            check3 = 1
            joueur32 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur91 == "b" and joueur51 == "b" and p == 0:
        if case_confirm1 == 0:
            text11 = case1.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm1 = 1
            x = x + 1
            p = 1
            check1 = 1
            joueur12 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur31 == "b" and joueur51 == "b" and p == 0:
        if case_confirm7 == 0:
            text77 = case7.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm7 = 1
            x = x + 1
            p = 1
            check7 = 1
            joueur72 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur71 == "b" and joueur51 == "b" and p == 0:
        if case_confirm3 == 0:
            text33 = case3.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm3 = 1
            x = x + 1
            p = 1
            check3 = 1
            joueur32 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur92 == "b" and joueur52 == "b" and p == 0:
        if case_confirm1 == 0:
            text11 = case1.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm1 = 1
            x = x + 1
            p = 1
            check1 = 1
            joueur12 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur12 == "b" and joueur52 == "b" and p == 0:
        if case_confirm9 == 0:
            text99 = case9.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm9 = 1
            x = x + 1
            p = 1
            check9 = 1
            joueur92 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    
    






            
    if joueur11 == "a" and joueur71 == "a" and p == 0:
        if case_confirm4 == 0:
            text44 = case4.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm4 = 1
            x = x + 1
            p = 1
            check4 = 1
            joueur42 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur11 == "a" and joueur31 == "a" and p == 0:
        if case_confirm2 == 0:
            text22 = case2.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm2 = 1
            x = x + 1
            p = 1
            check2 = 1
            joueur22 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur31 == "a" and joueur91 == "a" and p == 0:
        if case_confirm6 == 0:
            text66 = case6.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm6 = 1
            x = x + 1
            p = 1
            check6 = 1
            joueur62 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur71 == "a" and joueur91 == "a" and p == 0:
        if case_confirm8 == 0:
            text88 = case8.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm8 = 1
            x = x + 1
            p = 1
            check8 = 1
            joueur82 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)


    if joueur21 == "a" and joueur51 == "a" and p == 0:
        if case_confirm8 == 0:
            text88 = case8.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm8 = 1
            x = x + 1
            p = 1
            check8 = 1
            joueur82 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur81 == "a" and joueur51 == "a" and p == 0:
        if case_confirm2 == 0:
            text22 = case2.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm2 = 1
            x = x + 1
            p = 1
            check2 = 1
            joueur22 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)


    if joueur11 == "a" and joueur51 == "a" and p == 0:
        if case_confirm9 == 0:
            text99 = case9.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm9 = 1
            x = x + 1
            p = 1
            check9 = 1
            joueur92 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
         
    if joueur11 == "a" and joueur41 == "a" and p == 0:
        if case_confirm7 == 0:
            text77 = case7.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm7 = 1
            x = x + 1
            p = 1
            check7 = 1
            joueur72 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
            
    if joueur71 == "a" and joueur41 == "a" and p == 0:
        if case_confirm1 == 0:
            text11 = case1.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm1 = 1
            x = x + 1
            p = 1
            check1 = 1
            joueur12 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur91 == "a" and joueur51 == "a" and p == 0:
        if case_confirm1 == 0:
            text11 = case1.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm1 = 1
            x = x + 1
            p = 1
            check1 = 1
            joueur12 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)

    if joueur71 == "a" and joueur81 == "a" and p == 0:
        if case_confirm9 == 0:
            text99 = case9.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm9 = 1
            x = x + 1
            p = 1
            check9 = 1
            joueur92 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur11 == "a" and joueur21 == "a" and p == 0:
        if case_confirm3 == 0:
            text33 = case3.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm3 = 1
            x = x + 1
            p = 1
            check3 = 1
            joueur32 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur31 == "a" and joueur21 == "a" and p == 0:
        if case_confirm1 == 0:
            text11 = case1.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm1 = 1
            x = x + 1
            p = 1
            check1 = 1
            joueur12 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur31 == "a" and joueur61 == "a" and p == 0:
        if case_confirm9 == 0:
            text99 = case9.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm9 = 1
            x = x + 1
            p = 1
            check9 = 1
            joueur92 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur91 == "a" and joueur81 == "a" and p == 0:
        if case_confirm7 == 0:
            text77 = case7.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm7 = 1
            x = x + 1
            p = 1
            check7 = 1
            joueur72 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur71 == "a" and joueur51 == "a" and p == 0:
        if case_confirm3 == 0:
            text33 = case3.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm3 = 1
            x = x + 1
            p = 1
            check3 = 1
            joueur32 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur91 == "a" and joueur61 == "a" and p == 0:
        if case_confirm3 == 0:
            text33 = case3.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm3 = 1
            x = x + 1
            p = 1
            check3 = 1
            joueur32 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur51 == "a" and joueur81 == "a" and case_confirm2 == 0 and p == 0:
        if case_confirm9 == 0:
            text22 = case2.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm2 = 1
            x = x + 1
            p = 1
            check2 = 1
            joueur22 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur11 == "a" and joueur71 == "a" and p == 0:
        if case_confirm4 == 0:
            text44 = case4.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm4 = 1
            x = x + 1
            p = 1
            check4 = 1
            joueur42 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur31 == "a" and joueur91 == "a" and p == 0:
        if case_confirm6 == 0:
            text66 = case6.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm6 = 1
            x = x + 1
            p = 1
            check6 = 1
            joueur62 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)



    if joueur41 == "a" and joueur51 == "a" and p == 0:
        if case_confirm6 == 0:
            text6 = case6.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm6 = 1
            x = x + 1
            p = 1
            check6 = 1
            joueur62 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur61 == "a" and joueur51 == "a" and p == 0:
        if case_confirm4 == 0:
            text44 = case4.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm4 = 1
            x = x + 1
            p = 1
            check4 = 1
            joueur42 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur21 == "a" and joueur51 == "a" and p == 0:
        if case_confirm8 == 0:
            text88 = case8.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm8 = 1
            x = x + 1
            p = 1
            check8 = 1
            joueur82 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    
    if joueur31 == "a" and joueur51 == "a" and p == 0:
        if case_confirm7 == 0:
            text77 = case7.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm7 = 1
            x = x + 1
            p = 1
            check7 = 1
            joueur72 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur71 == "a" and joueur51 == "a" and p == 0:
        if case_confirm3 == 0:
            text33 = case3.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm3 = 1
            x = x + 1
            p = 1
            check3 = 1
            joueur32 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur11 == "a" and joueur91 == "a" and joueur52 == "b" and p == 0:
        if case_confirm6 == 0:
            text66 = case6.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm6 = 1
            x = x + 1
            p = 1
            check6 = 1
            joueur62 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur71 == "a" and joueur31 == "a" and joueur52 == "b" and p == 0:
        if case_confirm6 == 0:
            text66 = case6.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm6 = 1
            x = x + 1
            p = 1
            check6 = 1
            joueur62 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    
    
    








            
    
        
            
            
    if joueur81 == "a" and joueur51 == "a" and p == 0:
        if case_confirm2 == 0:
            text22 = case2.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm2 = 1
            x = x + 1
            p = 1
            check2 = 1
            joueur22 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    if joueur31 != "a" and joueur71 != "a" and p == 0:
        if case_confirm7 == 0:
            text77 = case7.create_text(70,50,text="O",font ="Impact 50",fill="black")
            case_confirm7 = 1
            x = x + 1
            p = 1
            check7 = 1
            joueur72 = "b"
            tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
            touro.delete(ALL)
    else:
        if case_confirm1 != "a" and p == 0 or case_confirm1 != "b" and p == 0:
            if case_confirm1 == 0:
                text11 = case1.create_text(70,50,text="O",font ="Impact 50",fill="black")
                case_confirm1 = 1
                x = x + 1
                p = 1
                check1 = 1
                joueur12 = "b"
                tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
                touro.delete(ALL)
        if case_confirm2 != "a" and p == 0 or case_confirm2 != "b" and p == 0:
            if case_confirm1 == 0:
                text22 = case2.create_text(70,50,text="O",font ="Impact 50",fill="black")
                case_confirm2 = 1
                x = x + 1
                p = 1
                check2 = 1
                joueur22 = "b"
                tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
                touro.delete(ALL)
        if case_confirm3 != "a" and p == 0 or case_confirm3 != "b" and p == 0:
            if case_confirm3 == 0:
                text33 = case3.create_text(70,50,text="O",font ="Impact 50",fill="black")
                case_confirm3 = 1
                x = x + 1
                p = 1
                check3 = 1
                joueur32 = "b"
                tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
                touro.delete(ALL)
        if case_confirm4 != "a" and p == 0 or case_confirm4 != "b" and p == 0:
            if case_confirm4 == 0:
                text44 = case4.create_text(70,50,text="O",font ="Impact 50",fill="black")
                case_confirm4 = 1
                x = x + 1
                p = 1
                check4 = 1
                joueur42 = "b"
                tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
                touro.delete(ALL)
        if case_confirm6 != "a" and p == 0 or case_confirm6 != "b" and p == 0:
            if case_confirm6 == 0:
                text66 = case6.create_text(70,50,text="O",font ="Impact 50",fill="black")
                case_confirm6 = 1
                x = x + 1
                p = 1
                check6 = 1
                joueur62 = "b"
                tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
                touro.delete(ALL)
        if case_confirm7 != "a" and p == 0 or case_confirm7 != "b" and p == 0:
            if case_confirm7 == 0:
                text77 = case7.create_text(70,50,text="O",font ="Impact 50",fill="black")
                case_confirm7 = 1
                x = x + 1
                p = 1
                check7 = 1
                joueur72 = "b"
                tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
                touro.delete(ALL)
        if case_confirm8 != "a" and p == 0 or case_confirm8 != "b" and p == 0:
            if case_confirm8 == 0:
                text88 = case8.create_text(70,50,text="O",font ="Impact 50",fill="black")
                case_confirm8 = 1
                x = x + 1
                p = 1
                check8 = 1
                joueur82 = "b"
                tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
                touro.delete(ALL)
        if case_confirm9 != "a" and p == 0 or case_confirm9 != "b" and p == 0:
            if case_confirm9 == 0:
                text99 = case9.create_text(70,50,text="O",font ="Impact 50",fill="black")
                case_confirm9 = 1
                x = x + 1
                p = 1
                check9 = 1
                joueur92 = "b"
                tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
                touro.delete(ALL)
    
    gagner()
    
            
    
    



            

            
            

    
        
    




def principale():
    global recomm,messagewin, nbr1, nbr2, nbr3, nbr4, nbr5, nbr6, nbr7, nbr8, nbr9, enleve,text1 , x, case_confirm1, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
    tourxmsg = tourx.create_text(40,25,text="au tour du\n  joueur X",fill="white",font="Impact 13")
    def click1(event):
        global check1, t ,enleve ,text1 , x, case_confirm1, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case1")
        t = 1
        if check1 == 0:
            if x == 0:
                messagewin.delete(ALL)
            if case_confirm1 == 0 and recomm == 0:
                check1 = 1
                if x == 0 or x == 2 or x == 4 or x == 6 or x == 8 :
                    text1 = case1.create_text(70,50,text="X",font ="Impact 50",fill="black")
                    case_confirm1 = 1
                    x = x + 1
                    joueur11 = "a"
                    nbr1 = 1
                    tourx.delete(ALL)
                    touromsg = touro.create_text(40,25,text="   au tour de\n            l'IA",fill="white",font="Impact 13")
                    
                else:
                    pass
           
            else:
                pass
        
            gagner()
            temps()
#====================================================================================
    
    def click2(event):
        global check2, t, recomm,x, text2, text22, case_confirm2, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case2")
        t = 1
        if check2 == 0:
            if x == 0:
                messagewin.delete(ALL)
            if case_confirm2 == 0 and recomm == 0:
                check2=1
                if x == 0 or x == 2 or x == 4 or x == 6 or x == 8 :
                    text2 = case2.create_text(70,50,text="X",font ="Impact 50",fill="black")
                    case_confirm2 = 1
                    x = x + 1
                    joueur21 = "a"
                    nbr2 = 1
                    tourx.delete(ALL)
                    touromsg = touro.create_text(40,25,text="   au tour de\n            l'IA",fill="white",font="Impact 13")
                   
                else:
                    pass
           
            else :
                pass
            gagner()
            temps()
#====================================================================================
    
    def click3(event):
        global check3, t, recomm,x, text3, text33, case_confirm3, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case3")
        t = 1
        if check3 == 0:
            if x == 0:
                messagewin.delete(ALL)
            if case_confirm3 == 0 and recomm == 0:
                check3=1
                if x == 0 or x == 2 or x == 4 or x == 6 or x == 8 :
                    text3 = case3.create_text(70,50,text="X",font ="Impact 50",fill="black")
                    case_confirm3 = 1
                    x = x + 1
                    joueur31 = "a"
                    nbr3 = 1
                    tourx.delete(ALL)
                    touromsg = touro.create_text(40,25,text="   au tour de\n            l'IA",fill="white",font="Impact 13")
                   
                else:
                    pass
           
            else :
                pass
            gagner()
            temps()
#====================================================================================
    
    def click4(event):
        global check4,t, recomm,x, text4,text44 , case_confirm4, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case4")
        t = 1
        if check4 == 0:
            if x == 0:
                messagewin.delete(ALL)
            if case_confirm4 == 0 and recomm == 0:
                check4 =1
                if x == 0 or x == 2 or x == 4 or x == 6 or x == 8 :
                    text4 = case4.create_text(70,50,text="X",font ="Impact 50",fill="black")
                    case_confirm4 = 1
                    x = x + 1
                    joueur41 = "a"
                    nbr4 = 1
                    tourx.delete(ALL)
                    touromsg = touro.create_text(40,25,text="   au tour de\n            l'IA",fill="white",font="Impact 13")
                    
                else:
                    pass
            
            else :
                pass
            gagner()
            temps()
#====================================================================================
    
    def click5(event):
        global check5,t, recomm,x,text5, text55, case_confirm5, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case5")
        t = 1
        if check5 == 0:
            if x == 0:
                messagewin.delete(ALL)
            if case_confirm5 == 0 and recomm == 0:
                check5 =1
                if x == 0 or x == 2 or x == 4 or x == 6 or x == 8  :
                    text5 = case5.create_text(70,50,text="X",font ="Impact 50",fill="black")
                    case_confirm5 = 1
                    x = x + 1
                    joueur51 = "a"
                    nbr5 = 1

                    tourx.delete(ALL)
                    touromsg = touro.create_text(40,25,text="   au tour de\n            l'IA",fill="white",font="Impact 13")
                    
                else:
                    pass
            
            else :
                pass
            gagner()
            
            temps()
#====================================================================================
    
    def click6(event):
        global check6,t, recomm,x,text6, text66 , case_confirm6, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case6")
        t = 1
        if check6 == 0:
            if x == 0:
                messagewin.delete(ALL)
            if case_confirm6 == 0 and recomm == 0:
                check6=1
                if x == 0 or x == 2 or x == 4 or x == 6 or x == 8 :
                    text6 = case6.create_text(70,50,text="X",font ="Impact 50",fill="black")
                    case_confirm6 = 1
                    x = x + 1
                    joueur61 = "a"
                    nbr6 = 1
                    tourx.delete(ALL)
                    touromsg = touro.create_text(40,25,text="   au tour de\n            l'IA",fill="white",font="Impact 13")
                    
                else:
                    pass
           
            else :
                pass
            gagner()
            temps()
#====================================================================================
    
    def click7(event):
        global check7,t, recomm,x,text7,text77 , case_confirm7, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case7")
        t = 1
        if check7 == 0:
            if x == 0:
                messagewin.delete(ALL)
            if case_confirm7 == 0 and recomm == 0:
                check7=1
                if x == 0 or x == 2 or x == 4 or x == 6 or x == 8 :
                    text7 = case7.create_text(70,50,text="X",font ="Impact 50",fill="black")
                    case_confirm7 = 1
                    x = x + 1
                    joueur71 = "a"
                    nbr7 = 1
                    tourx.delete(ALL)
                    touromsg = touro.create_text(40,25,text="   au tour de\n            l'IA",fill="white",font="Impact 13")
                    
                else:
                    pass
            else :
                pass
            gagner()
            temps()

    
    def click8(event):
        global check8,t, recomm,x,text8, text88 , case_confirm8, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case8")
        t = 1
        if check8==0:
            if x == 0:
                messagewin.delete(ALL)
            if case_confirm8 == 0 and recomm == 0:
                check8=1
                if x == 0 or x == 2 or x == 4 or x == 6 or x == 8 :
                    text8 = case8.create_text(70,50,text="X",font ="Impact 50",fill="black")
                    case_confirm8 = 1
                    x = x + 1
                    joueur81 = "a"
                    nbr8 = 1
                    tourx.delete(ALL)
                    touromsg = touro.create_text(40,25,text="   au tour de\n            l'IA",fill="white",font="Impact 13")
                
                else:
                    pass
            else :
                pass
            gagner()
            
            temps()

    def click9(event):
        global check9,t, recomm,x,text9, text99, case_confirm9, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
        print ("case9")
        t = 1
        if check9==0:
            if x == 0:
                messagewin.delete(ALL)
            if case_confirm9 == 0 and recomm == 0:
                check9=1
                if x == 0 or x == 2 or x == 4 or x == 6 or x == 8 :
                    text9 = case9.create_text(70,50,text="X",font ="Impact 50",fill="black")
                    case_confirm9 = 1
                    x = x + 1
                    joueur91 = "a"
                    nbr9 = 1
                    tourx.delete(ALL)
                    touromsg = touro.create_text(40,25,text="   au tour de\n            l'IA",fill="white",font="Impact 13")
                    
                else:
                    pass
            else :
                pass
                
            gagner()
            temps()
            
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
    global check1, check2, check3, check4, check5, check6, check7,check8, check9, checke,xperdu, xgagne, xegalite, iaperdu, iagagne, iaegalite,recomm,tourx,touro,text11,text2, text22,text3,text33,text4,text44,text5,text55,text6,text66,text7,text77,text8,text88,text9,text99, nbr1,nbr2, nbr3, nbr4, nbr5, nbr6, nbr7, nbr8, nbr9 ,case_confirm1,case_confirm2,case_confirm3,case_confirm4,case_confirm5,case_confirm6,case_confirm7,case_confirm8,case_confirm9, x,click11 ,text1 , case_confirm3, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
    check1 = 1
    check2 = 1
    check3 = 1
    check4 = 1
    check5 = 1
    check6 = 1
    check7 = 1
    check8 = 1
    check9 = 1
    if recomm == 0:
        print ("joueur X a gagné")
        checke = checke + "oui"
        messagewin.delete(ALL)
        messagewin1 = messagewin.create_text(130,15,text="bravo, joueur X a gagné !",fill="white",font="Impact 18")
        x = 0
        recomm = 1
        if checke == "oui":
            iaperdu = iaperdu + 1
            xgagne = xgagne + 1
            stats.itemconfigure(joueuriaperdu, text="Parties perdues  : " + str(iaperdu))
            stats.itemconfigure(joueurxgagne, text="Parties gagnés  : " + str(xgagne))
    
    

def winO():
    global check1, check2, check3, check4, check5, check6, check7,check8, check9, checke,xperdu, xgagne, xegalite, iaperdu, iagagne, iaegalite,recomm,tourx,touro,text11,text2, text22,text3,text33,text4,text44,text5,text55,text6,text66,text7,text77,text8,text88,text9,text99, nbr1,nbr2, nbr3, nbr4, nbr5, nbr6, nbr7, nbr8, nbr9 ,case_confirm1,case_confirm2,case_confirm3,case_confirm4,case_confirm5,case_confirm6,case_confirm7,case_confirm8,case_confirm9, x,click11 ,text1 , case_confirm3, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
    check1 = 1
    check2 = 1
    check3 = 1
    check4 = 1
    check5 = 1
    check6 = 1
    check7 = 1
    check8 = 1
    check9 = 1
    if recomm == 0:
        print ("joueur IA a gagné")
        checke = checke + "oui"
        messagewin.delete(ALL)
        messagewin1 = messagewin.create_text(130,15,text="bravo, L'IA a gagné !",fill="white",font="Impact 18")
        x = 0
        recomm = 1
        if checke == "oui":
            iagagne = iagagne + 1
            xperdu = xperdu + 1
            stats.itemconfigure(joueuriagagne, text="Parties gagnés  : " + str(iagagne))
            stats.itemconfigure(joueurxperdu, text="Parties perdues  : " + str(xperdu))

   
def recommencer():
    global  check1, check2, check3, check4, check5, check6, check7,check8, check9,checke,recomm,text11,text2, text22,text3,text33,text4,text44,text5,text55,text6,text66,text7,text77,text8,text88,text9,text99, nbr1,nbr2, nbr3, nbr4, nbr5, nbr6, nbr7, nbr8, nbr9 ,case_confirm1,case_confirm2,case_confirm3,case_confirm4,case_confirm5,case_confirm6,case_confirm7,case_confirm8,case_confirm9, x,click11 ,text1 , case_confirm3, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
    enleve()
    messagewin.delete(ALL)
    x = 0
    recomm = 0
    checke = ""
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
    check1 = 0
    check2 = 0
    check3 = 0
    check4 = 0
    check5 = 0
    check6 = 0
    check7 = 0
    check8 = 0
    check9 = 0
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
def egalite():
    global  checke,xperdu, xgagne, xegalite, iaperdu, iagagne, iaegalite,recomm,tourx,touro,text11,text2, text22,text3,text33,text4,text44,text5,text55,text6,text66,text7,text77,text8,text88,text9,text99, nbr1,nbr2, nbr3, nbr4, nbr5, nbr6, nbr7, nbr8, nbr9 ,case_confirm1,case_confirm2,case_confirm3,case_confirm4,case_confirm5,case_confirm6,case_confirm7,case_confirm8,case_confirm9, x,click11 ,text1 , case_confirm3, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
    print ("égalité")
    checke = checke + "oui"
    messagewin.delete(ALL)
    messagewin1 = messagewin.create_text(130,15,text="Dommage, vous avez fait égalité !",fill="white",font="Impact 14")
    x = 0
    recomm = 1
    if checke == "oui":
        iaegalite = iaegalite + 1
        xegalite = xegalite + 1
        stats.itemconfigure(joueuriaegalite, text="Egalités  : " + str(iaegalite))
        stats.itemconfigure(joueurxegalite, text="Egalités  : " + str(xegalite))
        
        
def gagner():
    global  tourx,touro,text11,text2, text22,text3,text33,text4,text44,text5,text55,text6,text66,text7,text77,text8,text88,text9,text99, nbr1,nbr2, nbr3, nbr4, nbr5, nbr6, nbr7, nbr8, nbr9 ,case_confirm1,case_confirm2,case_confirm3,case_confirm4,case_confirm5,case_confirm6,case_confirm7,case_confirm8,case_confirm9, x,click11 ,text1 , case_confirm3, joueur11, joueur21, joueur31, joueur41, joueur51, joueur61, joueur71, joueur81, joueur91, joueur12, joueur22, joueur32, joueur42, joueur52, joueur62, joueur72, joueur82, joueur92, case1, case2 , case3, case4, case5, case6, case7, case8, case9
    if joueur11 == joueur21 == joueur31:
        winX()        
    if joueur12 == joueur22 == joueur32:
        winO()
    if joueur41 == joueur51 == joueur61:
        winX()
    if joueur42 == joueur52 == joueur62:
        winO()
    if joueur71 == joueur81 == joueur91:
        winX()
    if joueur72 == joueur82 == joueur92:
        winO()
    if joueur11 == joueur41 == joueur71:
        winX()
    if joueur12 == joueur42 == joueur72:
        winO()
    if joueur21 == joueur51 == joueur81:
        winX()
    if joueur22 == joueur52 == joueur82:
        winO()
    if joueur31 == joueur61 == joueur91:
       winX()
    if joueur32 == joueur62 == joueur92:
        winO()
    if joueur11 == joueur51 == joueur91:
        winX()
    if joueur12 == joueur52 == joueur92:
       winO()
    if joueur31 == joueur51 == joueur71:
        winX()
    if joueur32 == joueur52 == joueur72:
        winO()
    if case_confirm1 == 1 and case_confirm2 == 1 and case_confirm3 == 1 and case_confirm4 == 1 and case_confirm5 == 1 and case_confirm6 == 1 and case_confirm7 == 1 and case_confirm8 == 1 and case_confirm9 == 1:
        egalite()
    
def resetstat():
    global  checke,xperdu, xgagne, xegalite, iaperdu, iagagne, iaegalite
    xgagne = 0
    xperdu = 0
    xegalite = 0
    iagagne = 0
    iaperdu = 0
    iaegalite = 0
    stats.itemconfigure(joueuriagagne, text="Parties gagnés  : " + str(iagagne))
    stats.itemconfigure(joueurxperdu, text="Parties perdues  : " + str(xperdu))
    stats.itemconfigure(joueuriaegalite, text="Egalités  : " + str(iaegalite))
    stats.itemconfigure(joueurxegalite, text="Egalités  : " + str(xegalite))
    stats.itemconfigure(joueuriaperdu, text="Parties perdues  : " + str(iaperdu))
    stats.itemconfigure(joueurxgagne, text="Parties gagnés  : " + str(xgagne))
    
stats = Canvas(fenetre,width="150", height ="325", background="white")
stats.place(x="610",y="10")


recommencer = Button(fenetre,text="recommencer\n la partie",command = recommencer).place(x="515",y="289")
tect = stats.create_text(53,25,text="intelligence \nartificielle  :",fill="#EB002E",font="Impact 13")
tect1 = stats.create_text(40,190,text="JOUEUR X  :",fill="#EB002E",font="Impact 13")
joueurxgagne = stats.create_text(60,305,text="Parties gagnés  :",fill="#EB002E",font="Impact 11")
joueurxperdu = stats.create_text(65,265,text="Parties perdues  :",fill="#EB002E",font="Impact 11")
joueurxegalite = stats.create_text(40,225,text="Egalités  :",fill="#EB002E",font="Impact 11")

joueuriagagne = stats.create_text(60,145,text="Parties gagnés  :",fill="#EB002E",font="Impact 11")
joueuriaperdu = stats.create_text(65,105,text="Parties perdues  :",fill="#EB002E",font="Impact 11")
joueuriaegalite = stats.create_text(40,65,text="Egalités  :",fill="#EB002E",font="Impact 11")


resetstats = Button(fenetre, text="réinitialisation\n des scores", command = resetstat).place(x="515",y="240")

stats.itemconfigure(joueuriagagne, text="Parties gagnés  : " + str(iagagne))
stats.itemconfigure(joueurxperdu, text="Parties perdues  : " + str(xperdu))
stats.itemconfigure(joueuriaegalite, text="Egalités  : " + str(iaegalite))
stats.itemconfigure(joueurxegalite, text="Egalités  : " + str(xegalite))
stats.itemconfigure(joueuriaperdu, text="Parties perdues  : " + str(iaperdu))
stats.itemconfigure(joueurxgagne, text="Parties gagnés  : " + str(xgagne))

principale()
fenetre.mainloop()
