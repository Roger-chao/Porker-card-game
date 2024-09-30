import random
import time
import tkinter

root = tkinter.Tk()
root.title("撲克牌比大小")
canvas = tkinter.Canvas(root, width=1360, height=765)
canvas.pack()


def poker():
    card1 = ["梅花 A.png", "梅花 2.png", "梅花 3.png", "梅花 4.png", "梅花 5.png", "梅花 6.png",
             "梅花 7.png", "梅花 8.png", "梅花 9.png", "梅花 10.png", "梅花 J.png", "梅花 Q.png", "梅花 K.png"]
    card2 = ["方塊 A.png", "方塊 2.png", "方塊 3.png", "方塊 4.png", "方塊 5.png", "方塊 6.png",
             "方塊 7.png", "方塊 8.png", "方塊 9.png", "方塊 10.png", "方塊 J.png", "方塊 Q.png", "方塊 K.png"]
    card3 = ["紅心 A.png", "紅心 2.png", "紅心 3.png", "紅心 4.png", "紅心 5.png", "紅心 6.png",
             "紅心 7.png", "紅心 8.png", "紅心 9.png", "紅心 10.png", "紅心 J.png", "紅心 Q.png", "紅心 K.png"]
    card4 = ["黑桃 A.png", "黑桃 2.png", "黑桃 3.png", "黑桃 4.png", "黑桃 5.png", "黑桃 6.png",
             "黑桃 7.png", "黑桃 8.png", "黑桃 9.png", "黑桃 10.png", "黑桃 J.png", "黑桃 Q.png", "黑桃 K.png"]
    card5 = card1+card2+card3+card4
    numberA = ["梅花 A.png", "方塊 A.png", "紅心 A.png", "黑桃 A.png"]
    number2 = ["梅花 2.png", "方塊 2.png", "紅心 2.png", "黑桃 2.png"]
    number3 = ["梅花 3.png", "方塊 3.png", "紅心 3.png", "黑桃 3.png"]
    number4 = ["梅花 4.png", "方塊 4.png", "紅心 4.png", "黑桃 4.png"]
    number5 = ["梅花 5.png", "方塊 5.png", "紅心 5.png", "黑桃 5.png"]
    number6 = ["梅花 6.png", "方塊 6.png", "紅心 6.png", "黑桃 6.png"]
    number7 = ["梅花 7.png", "方塊 7.png", "紅心 7.png", "黑桃 7.png"]
    number8 = ["梅花 8.png", "方塊 8.png", "紅心 8.png", "黑桃 8.png"]
    number9 = ["梅花 9.png", "方塊 9.png", "紅心 9.png", "黑桃 9.png"]
    number10 = ["梅花 10.png", "方塊 10.png", "紅心 10.png", "黑桃 10.png"]
    numberJ = ["梅花 J.png", "方塊 J.png", "紅心 J.png", "黑桃 J.png"]
    numberQ = ["梅花 Q.png", "方塊 Q.png", "紅心 Q.png", "黑桃 Q.png"]
    numberK = ["梅花 K.png", "方塊 K.png", "紅心 K.png", "黑桃 K.png"]

    img1 = [" "]*5
    img2 = [" "]*5
    x = [" "]*5
    y = [" "]*5
    p1suit = [0]*5
    p1number = [0]*5
    p2suit = [0]*5
    p2number = [0]*5
    tmp = 0
    temp = 0
    score1 = 0
    score2 = 0
    c1 = 0
    c2 = 0
    d1 = 0
    d2 = 0
    h1 = 0
    h2 = 0
    s1 = 0
    s2 = 0
    canvas.create_text(600, 35, text='Player1 → ', font=('Arial', 25))
    canvas.create_text(600, 380, text='Player2 → ', font=('Arial', 25))
    for i in range(5):
        x[i] = random.choice(card5)
        img1[i] = tkinter.PhotoImage(file=x[i])
        canvas.create_image(180+i*200, 75, anchor="nw", image=img1[i])
        card5.remove(x[i])
        time.sleep(0.5)
        canvas.update()
    for i in range(5):
        for j in range(13):
            if x[i] == card1[j]:
                p1suit[i] = 1
                c1 = c1+1
            elif x[i] == card2[j]:
                p1suit[i] = 2
                d1 = d1+1
            elif x[i] == card3[j]:
                p1suit[i] = 3
                h1 = h1+1
            elif x[i] == card4[j]:
                p1suit[i] = 4
                s1 = s1+1
        for j in range(4):
            if x[i] == numberA[j]:
                p1number[i] = 13
            elif x[i] == number2[j]:
                p1number[i] = 1
            elif x[i] == number3[j]:
                p1number[i] = 2
            elif x[i] == number4[j]:
                p1number[i] = 3
            elif x[i] == number5[j]:
                p1number[i] = 4
            elif x[i] == number6[j]:
                p1number[i] = 5
            elif x[i] == number7[j]:
                p1number[i] = 6
            elif x[i] == number8[j]:
                p1number[i] = 7
            elif x[i] == number9[j]:
                p1number[i] = 8
            elif x[i] == number10[j]:
                p1number[i] = 9
            elif x[i] == numberJ[j]:
                p1number[i] = 10
            elif x[i] == numberQ[j]:
                p1number[i] = 11
            elif x[i] == numberK[j]:
                p1number[i] = 12
    for i in range(5):
        for j in range(4-i):
            if p1number[j] < p1number[j+1]:
                tmp = p1number[j]
                p1number[j] = p1number[j+1]
                p1number[j+1] = tmp
                temp = p1suit[j]
                p1suit[j] = p1suit[j+1]
                p1suit[j+1] = temp
    if c1 == 5 or d1 == 5 or h1 == 5 or s1 == 5:
        if p1number[0] == 13 and p1number[1] == 12 and p1number[2] == 11 and p1number[3] == 10 and p1number[4] == 9:
            score1 = 10
            canvas.create_text(800, 35, text='Royal Flush', font=('Arial', 25))
        elif p1number[0] == p1number[1]-1 and p1number[1] == p1number[2]-1 and p1number[2] == p1number[3]-1 and p1number[3] == p1number[4]-1:
            score1 = 9
            canvas.create_text(
                800, 35, text='Straight Flush', font=('Arial', 25))
        else:
            score1 = 6
            canvas.create_text(800, 35, text='Flush', font=('Arial', 25))
    elif (p1number[0] == p1number[1] and p1number[1] == p1number[2] and p1number[2] == p1number[3]) or (p1number[1] == p1number[2] and p1number[2] == p1number[3] and p1number[3] == p1number[4]):
        score1 = 8
        canvas.create_text(800, 35, text='Full Of a Kind', font=('Arial', 25))
    elif (p1number[0] == p1number[1] and p1number[1] == p1number[2] and p1number[3] == p1number[4]) or (p1number[0] == p1number[1] and p1number[2] == p1number[3] and p1number[3] == p1number[4]):
        score1 = 7
        canvas.create_text(800, 35, text='Full House', font=('Arial', 25))
    elif (p1number[0] == p1number[1] and p1number[1] == p1number[2]) or (p1number[2] == p1number[3] and p1number[3] == p1number[4]):
        score1 = 4
        canvas.create_text(800, 35, text='Three of a Kind', font=('Arial', 25))
    elif p1number[0] == p1number[1]-1 and p1number[1] == p1number[2]-1 and p1number[2] == p1number[3]-1 and p1number[3] == p1number[4]-1:
        score1 = 5
        canvas.create_text(800, 35, text='Straight', font=('Arial', 25))
    elif (p1number[0] == p1number[1] and p1number[2] == p1number[3]) or (p1number[0] == p1number[1] and p1number[3] == p1number[4]) or (p1number[1] == p1number[2] and p1number[3] == p1number[4]):
        score1 = 3
        canvas.create_text(800, 35, text='Two Pair', font=('Arial', 25))
    elif p1number[0] == p1number[1] or p1number[1] == p1number[2] or p1number[3] == p1number[2] or p1number[3] == p1number[4]:
        score1 = 2
        canvas.create_text(800, 35, text='Pair', font=('Arial', 25))
    else:
        score1 = 1
        canvas.create_text(800, 35, text='High Card', font=('Arial', 25))
    for i in range(5):
        y[i] = random.choice(card5)
        img2[i] = tkinter.PhotoImage(file=y[i])
        canvas.create_image(180+i*200, 425, anchor="nw", image=img2[i])
        card5.remove(y[i])
        time.sleep(0.5)
        canvas.update()
    for i in range(5):
        for j in range(13):
            if y[i] == card1[j]:
                p2suit[i] = 1
                c2 = c2+1
            elif y[i] == card2[j]:
                p2suit[i] = 2
                d2 = d2+1
            elif y[i] == card3[j]:
                p2suit[i] = 3
                h2 = h2+1
            elif y[i] == card4[j]:
                p2suit[i] = 4
                s2 = s2+1
        for j in range(4):
            if y[i] == numberA[j]:
                p2number[i] = 13
            elif y[i] == number2[j]:
                p2number[i] = 1
            elif y[i] == number3[j]:
                p2number[i] = 2
            elif y[i] == number4[j]:
                p2number[i] = 3
            elif y[i] == number5[j]:
                p2number[i] = 4
            elif y[i] == number6[j]:
                p2number[i] = 5
            elif y[i] == number7[j]:
                p2number[i] = 6
            elif y[i] == number8[j]:
                p2number[i] = 7
            elif y[i] == number9[j]:
                p2number[i] = 8
            elif y[i] == number10[j]:
                p2number[i] = 9
            elif y[i] == numberJ[j]:
                p2number[i] = 10
            elif y[i] == numberQ[j]:
                p2number[i] = 11
            elif y[i] == numberK[j]:
                p2number[i] = 12
    for i in range(5):
        for j in range(4-i):
            if p2number[j] < p2number[j+1]:
                tmp = p2number[j]
                p2number[j] = p2number[j+1]
                p2number[j+1] = tmp
                temp = p2suit[j]
                p2suit[j] = p2suit[j+1]
                p2suit[j+1] = temp
    if c2 == 5 or d2 == 5 or h2 == 5 or s2 == 5:
        if p2number[0] == 13 and p2number[1] == 12 and p2number[2] == 11 and p2number[3] == 10 and p2number[4] == 9:
            score2 = 10
            canvas.create_text(800, 380, text='Royal Flush',
                               font=('Arial', 25))
        elif p2number[0] == p2number[1]-1 and p2number[1] == p2number[2]-1 and p2number[2] == p2number[3]-1 and p2number[3] == p2number[4]-1:
            score2 = 9
            canvas.create_text(
                800, 380, text='Straight Flush', font=('Arial', 25))
        else:
            score2 = 6
            canvas.create_text(800, 380, text='Flush', font=('Arial', 25))
    elif (p2number[0] == p2number[1] and p2number[1] == p2number[2] and p2number[2] == p2number[3]) or (p2number[1] == p2number[2] and p2number[2] == p2number[3] and p2number[3] == p2number[4]):
        score2 = 8
        canvas.create_text(800, 380, text='Full Of a Kind', font=('Arial', 25))
    elif (p2number[0] == p2number[1] and p2number[1] == p2number[2] and p2number[3] == p2number[4]) or (p2number[0] == p2number[1] and p2number[2] == p2number[3] and p2number[3] == p2number[4]):
        score2 = 7
        canvas.create_text(800, 380, text='Full House', font=('Arial', 25))
    elif (p2number[0] == p2number[1] and p2number[1] == p2number[2]) or (p2number[2] == p2number[3] and p2number[3] == p2number[4]):
        score2 = 4
        canvas.create_text(800, 380, text='Three of a Kind',
                           font=('Arial', 25))
    elif p2number[0] == p2number[1]-1 and p2number[1] == p2number[2]-1 and p2number[2] == p2number[3]-1 and p2number[3] == p2number[4]-1:
        score2 = 5
        canvas.create_text(800, 380, text='Straight', font=('Arial', 25))
    elif (p2number[0] == p2number[1] and p2number[2] == p2number[3]) or (p2number[0] == p2number[1] and p2number[3] == p2number[4]) or (p2number[1] == p2number[2] and p2number[3] == p2number[4]):
        score2 = 3
        canvas.create_text(800, 380, text='Two Pair', font=('Arial', 25))
    elif p2number[0] == p2number[1] or p2number[1] == p2number[2] or p2number[3] == p2number[2] or p2number[3] == p2number[4]:
        score2 = 2
        canvas.create_text(800, 380, text='Pair', font=('Arial', 25))
    else:
        score2 = 1
        canvas.create_text(800, 380, text='High Card', font=('Arial', 25))
    if score1 > score2:
        canvas.create_text(680, 700, text='Player1 Win!', font=('Arial', 25))
    elif score2 > score1:
        canvas.create_text(680, 700, text='Player2 Win!', font=('Arial', 25))
    else:
        for i in range(5):
            if (p1number[i] > p2number[i]):
                canvas.create_text(
                    680, 700, text='Player1 Win!', font=('Arial', 25))
                break
            elif (p1number[i] < p2number[i]):
                canvas.create_text(
                    680, 700, text='Player2 Win!', font=('Arial', 25))
                break
            elif (p1number[i] == p2number[i] and p1suit[i] > p2suit[i]):
                canvas.create_text(
                    680, 700, text='Player1 Win!', font=('Arial', 25))
                break
            elif (p1number[i] == p2number[i] and p2suit[i] < p2suit[i]):
                canvas.create_text(
                    680, 700, text='Player2 Win!', font=('Arial', 25))
                break
    root.mainloop()


def reset():
    canvas.delete("all")
    poker()


resetbtn = tkinter.Button(
    canvas, text="Reset", command=reset, width=11, height=4).place(x=800, y=650)
poker()
