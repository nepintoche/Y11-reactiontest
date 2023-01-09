"""
this program is an app which tests your reaction time

-Noha Epiney
"""
from guizero import *
import random
from timeit import default_timer as timer
import pickle
#First window and layout
textfont = "gameovercre"
titlefont = "gameplay"

resultlist = []
agelist = []


app = App(title="Noha reaction test",bg="turquoise")

greeting = Text(app,text="Noha Reaction",size = 50,font =titlefont)
greeting2 = Text(app,text="Tester",size = 50,font =titlefont)
leftbox = Box(app, align ="left", width = 70)
rightbox = Box(app, align ="right", width = 70)
rowbox = Box(app,width = "fill",height = "fill")
bottomrowbox= Box(app,width = "fill",height = "fill",align = "bottom")
alignmentbottomrowbox = Box(bottomrowbox,width = "fill",height=60)
lbottomrow = Box(alignmentbottomrowbox,width = "fill",height = 60,align="left")
rbottomrow = Box(alignmentbottomrowbox,width = "fill",height = 60,align = "right")
bottomrow = Box(alignmentbottomrowbox,width = 60,height = 60,)

lmiddlerow = Box(app,width = "fill",height = 50,align="left")
rmiddlerow = Box(app,width = "fill",height = 50,align = "right")
middlerow = Box(app,width = 100,height = 50)
buttonid = 0
clickcounter = 0
scorelist = []


comingfromrank = False
def rank():
    global rankwindow,comingfromrank,ageslider2,ageresultbox,rightrankbox,resultlist,agelist,submitbutton2
    comingfromrank = True
    rankwindow = Window(app,title = "Rankings",bg ="turquoise",width = 1000,height = 750)
    rankwindow.show(wait = True)
    app.hide()

    menubutton = PushButton(rankwindow,text = "Menu",command = returnfromtest)
    menubutton.font = textfont

    with open("test.pickle","rb") as infile:
        resultlist = pickle.load(infile)

    total = 0
    for m,i in enumerate(resultlist):
        total += resultlist[m][0]

    averagescore = int(total/len(resultlist))

    resultlist.sort()
    print(resultlist)
    leftrankbox = Box(rankwindow,align="left",height = 550,width = "fill")
    leftrankbox.font = textfont
    rightrankbox = Box(rankwindow,align="left",height = 550,width = "fill")
    rightrankbox.font = textfont


    allresulttitle = Text(leftrankbox,text = "All ages",font = titlefont, size = 30)
    agespecifictitle = Text(rightrankbox,text = "Select age",font = titlefont, size = 30)
    averageresult = Text(leftrankbox,size = 20, font=textfont,text = "average score: " + str(averagescore))

    resultbox = ListBox(leftrankbox,align= "bottom",scrollbar = True,height = 450,width = "fill",items = resultlist)
    ageresultbox = ListBox(rightrankbox,align= "bottom",scrollbar = True,height = 450,width = "fill",items = agelist)


    ageslider2 = Slider(rightrankbox,start = 12, end = 18)
    ageslider2.font= textfont

    rankboxforbutton = Box(rightrankbox,height = 50,width = 200)
    submitbutton2 = PushButton(rankboxforbutton,text = "Submit",command = applyage,align="left")
    submitbutton2.font = textfont

    resetbutton = PushButton(rankboxforbutton,align="left",command = resetlist,text = "Reset")

def resetlist():
    global ageresultbox,submitbutton2
    ageresultbox.clear()
    submitbutton2.enable()

def applyage():
    global ageslider2,resultlist,ageresultbox,agelist,submitbutton2
    ageselection = ageslider2.value
    submitbutton2.disable()

    for m,i in enumerate(resultlist):


        #print(resultlist[i][2])
        if resultlist[m][2] == ageselection:
            ageresultbox.append(resultlist[m])




def testprep():
    global nameinput, nameorder,submitname,testwindow,ageslider
    testwindow = Window(app,title = "Reaction test",bg = "turquoise",width = 1300,height= 800)
    testwindow.show(wait = True)
    app.hide()
    nameorder = Text(testwindow,text="Enter your name and age",size = 40,font = titlefont)
    nameinput = TextBox(testwindow)
    ageslider = Slider(testwindow,start = 12, end = 18)
    ageslider.font = textfont
    submitname = PushButton(testwindow,text = "submit",command = testpage)
    submitname.font = textfont

def testpage():
    global nameinput,nameorder,submitname,testwindow,topleft,topright,bottomleft,bottomright,startbutton,resultbox,row1,row2,row3,name,age
    global name,age
    name = nameinput.value
    age = ageslider.value
    print(name)

    nameinput.destroy()
    nameorder.destroy()
    submitname.destroy()
    ageslider.destroy()


    row1 = Box(testwindow,width = "fill",height = "fill")
    #row1.bg = "red"
    topleft = Picture(row1, align = "left",image = "venv/Images/blue.png")
    topright = Picture(row1, align = "right",image = "venv/Images/blue.png")
    Title = Text(row1, text = "The Test", size = 65,font= titlefont)
    Title2 = Text(row1, text = "  ", size = 65,font= titlefont)
    insturctions = Text(row1, text = "1. When ready press start", size = 27,font= textfont)
    insturctions2 = Text(row1, text = "2.One of the 4 squares in the corners", size = 27,font= textfont)
    insturctions22 = Text(row1, text = "will change colors, click it as fast as", size = 27,font= textfont)
    insturctions23 = Text(row1, text = "possible", size = 27,font= textfont)
    insturctions3 = Text(row1, text = "3.Do this 3 times", size = 27,font= textfont)

    row2 = Box(testwindow,width = "fill",height = "fill")
    #row2.bg = "yellow"
    topspacebox = Box(row2,align = "top",height = "fill")
    startbutton = PushButton(row2, text= "Start",command = ready)
    startbutton.font = textfont

    bottomspacebox = Box(row2,align = "bottom",height="fill")

    row3 = Box(testwindow,width = "fill",height = "fill")
    bottomleft = Picture(row3, align = "left",image = "venv/Images/blue.png")
    bottomright = Picture(row3, align = "right",image = "venv/Images/blue.png")
    resultext = Text(row3,text = "Result (ms):", size = 65,font= titlefont)
    resultbox = Box(row3,height = 75,width = 300)
    resultbox.bg = "turquoise"
    topresultspace = Box(resultbox,align = "top",height = "fill")

    bottomresultspace = Box(resultbox,align = "bottom",height = "fill")

def ready():
    global topleft,topright,bottomleft,bottomright,start,buttonid,startbutton
    buttonselect = random.randint(1,4)
    start = timer()
    startbutton.disable()

    if buttonselect == 1:
        topleft.image = "venv/Images/FFCC00.png.png"
        topleft.when_clicked = stop
        buttonid = 1
    if buttonselect == 2:
        topright.image = "venv/Images/FFCC00.png.png"
        topright.when_clicked = stop
        buttonid = 2
    if buttonselect == 3:
        bottomleft.image = "venv/Images/FFCC00.png.png"
        bottomleft.when_clicked = stop
        buttonid = 3
    if buttonselect == 4:
        bottomright.image = "venv/Images/FFCC00.png.png"
        bottomright.when_clicked = stop
        buttonid = 4


def stop():
    global start,buttonid,startbutton,resultext,clickcounter,result1,result2,result3,row1,row2,row3,averageresult,scorelist,result
    end = timer()
    result= (end-start)

    resultext = Text(resultbox,text = str(int((round(result,3))*1000)),size = 27,font=textfont)
    clickcounter += 1


    if buttonid == 1:
        topleft.image = "venv/Images/blue.png"
        topleft.when_clicked = nothing
    elif buttonid == 2:
        topright.image = "venv/Images/blue.png"
        topright.when_clicked = nothing
    elif buttonid == 3:
        bottomleft.image = "venv/Images/blue.png"
        bottomleft.when_clicked = nothing
    else:
        bottomright.image = "venv/Images/blue.png"
        bottomright.when_clicked = nothing

    if clickcounter == 3:
        startbutton.destroy()
        result3 = result
        averageresult = (result1 +result2 + result3)/3
        averageresult = round(averageresult,3)
        averageresult = int(averageresult*1000)
        print(averageresult)

        scorelist.append((name,age,averageresult))

        row1.destroy()
        row2.destroy()
        row3.destroy()

        averageresultext = Text(testwindow,text = "Final score average (ms):",size = 60,font=titlefont)
        averageresultdisplay = Text(testwindow,text = str(averageresult),size = 25,font=textfont)
        resultpagebox = Box(testwindow,width=250,height=50)
        returnhomebutton = PushButton(resultpagebox,text="Return to menu",command=returnfromtest,align= "left")
        returnhomebutton.font = textfont
        savebutton = PushButton(resultpagebox,text="Save",command=save,align="right")
        savebutton.font = textfont
    else:
        startbutton.enable()

    if clickcounter == 2:
        result2 = result
    if clickcounter == 1:
        result1 = result

def save():
    global resultlist,averageresult,name,age
    resultlist.append([averageresult,name,age])
    with open("test.pickle","rb") as infile:
        resultlist = pickle.load(infile)
    resultlist.append([averageresult,name,age])
    with open("test.pickle","wb") as outfile:
        pickle.dump(resultlist,outfile)

    saveconfirmation = Text(testwindow,text = "Results saved",size = 25,font=textfont)

def returnfromtest():
    global clickcounter,scorelist,comingfromrank
    if comingfromrank:
        rankwindow.destroy()
        comingfromrank = False
    else:
        testwindow.destroy()
    app.show()
    clickcounter = 0


def nothing():
    pass

def quit():
    app.destroy()

rankbutton = PushButton(lmiddlerow,align = "left",height = 49,text = "Leaderboard",command = rank)
rankbutton.font = textfont
rankicon = Picture(lbottomrow,image = "venv/icons/numbered-list.png",align="left",width = 60,height = 60)
testbutton = PushButton(middlerow,height = 49,text = "Play",command = testprep)
testbutton.font = textfont
testicon = Picture(bottomrow,image = "venv/icons/arrowhead-pointing-to-the-right.png",width = 60,height = 60)
quitbutton = PushButton(rmiddlerow,align = "right",height = 49,text = "Quit",command = quit)
quitbutton.font = textfont
quiticon = Picture(rbottomrow,image = "venv/icons/sign-out-option.png",align="right",width = 60,height = 60)


app.display()

