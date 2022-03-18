import random
from tkinter import *
from tkinter.ttk import Separator,Progressbar
from tkinter.messagebox import showinfo
from time import time,strftime
root=Tk()
root.geometry("700x500")
root.resizable(0,0)
root.title('Quiz App designed by : Aman shukla')
#img=('wm','iconphoto',root.w,PhotoImage(file='exam.png'))
#root.tk.call(img)# add image as icon of exam
root.config(bg='black')
i=0
timeleft={'min':5, 'sec':30}# 3 total time +30 waiting time for intro
intro='''\t\t : : Instruction::
1. total time is :05 minutes
2. total question :05
3. Total score  : 05 x 100=500
4. Please select the approprite option at once an you have only one chance to select.
\t   Good Luck !


'''
print (intro)
def timeshow():
    global i, timeleft
    if timeleft['min']==5 and timeleft['sec']>0:
        note.config(text=" you start quiz after {} seconds".format(timeleft['sec']))
        timeleft['sec']-=1
    elif timeleft['sec']>0:
        submit.config(state=NORMAL)
        instruction.config(text='' )
        timeleft['sec']-=1
        note.config(text="time left  {} seconds".format(timeleft['sec']))
    elif timeleft['min']!=0 and timeleft['sec']==0:
        timeleft['min']-=1
        timeleft['sec']=59
        note.config(text="time left  {} seconds".format(timeleft['sec']))
    elif timeleft['min']==0 and timeleft['sec']==0 :
        print('Time up')
    showtime.config(text=strftime('%H:%M:%S'))
    showtime.after(1000,timeshow)

# make student Attendance
def getdetails():
    global name,roll,mainWindow,Name,Roll
    Name=name.get()
    Roll=roll.get()
    root.deiconify()
    timeshow()
    mainWindow.destroy()
def attendance():
    global roll,name,mainWindow
    mainWindow=Toplevel(root)
    mainWindow.geometry('700x500')
    mainWindow.resizable(0,0)
    mainWindow.title('Quiz App designed by Aman shukla [make attendance]')
 #   mainWindow.tk.call(img)
    mainWindow.config(bg='black')
    # app name same as icon of exam
    appName=Label(mainWindow,text=title,font=20 ,fg='red',justify=CENTER)
    appName.pack(side=TOP,fill=BOTH)
    # show current time
    showtime1=Label(mainWindow,text='', font=20,fg='red')
    showtime1.place(x=600,y=50)
    # label showinfo of attendance
    info=Label(mainWindow,text="Enter your name and roll number",bg='black',font=15)
    info.place(x=210,y=200)
    name=Entry(mainWindow,width=30)
    name.place(x=250,y=235)
    roll = Entry(mainWindow, width=30)
    roll.place(x=250, y=260)
    name.insert(END,'Name')
    roll.insert(END,'roll')
    submit=Button(mainWindow,text='confirm and start',width=20,fg='green',command=getdetails)
    submit.place(x=265,y=300)
    mainWindow.mainloop()


def quit_function():
    answer=showinfo(title='Good Luck',message='Good luck for your future...\n')
    print(answer)
    if answer=='ok':
        sys.exit(root.destroy())
def desableAllButton():
    option1.config(state=DISABLED)
    option2.config(state=DISABLED)
    option3.config(state=DISABLED)
    option4.config(state=DISABLED)


def enableAllButton():
    option1.config(state=NORMAL)
    option2.config(state=NORMAL)
    option3.config(state=NORMAL)
    option4.config(state=NORMAL)

def result():
    global score,Name,Roll
    root.withdraw()
    top=Toplevel(root)
    #top.tk.call('wm','iconphoto',top.w,PhotoImage(file='exam.png'))
    top.resizable(0,0)
    top.geometry('200x300')
    top.title('Quiz result')
    top.config(bg='blue')
    top.protocol('WM_DELETE_WINDOW',quit_function)
    filename=Name+'_'+Roll+'.txt'
    data='\nStudent'+Name+'\n roll'+Roll+'\n score:'+str(score)+'\n Completed quiz at :'+strftime('%d /%m/%y --%H: %M:%S')
    with open(filename,"a") as file:
        file.write(data)
    label=Label(top,text="Quiz over ... \n score;"+str(score),font=30,fg='white',bg='blue').place(x=50,y=25)
    exitBtn=Button(top,text='EXIT',width=10,bg='black',fg='red',command=quit_function).place(x=50,y=70)
    top.mainloop()
# question
question={'who is the founder of python':'Guido van rossum',
          'what is the output  of 13/3  ?':'4.0',
''' i=0
while= i<3:
print(i)
i+=1
print(i+1)   //  what is output  ?''':'0213324',
          ''' what is output of following code ?
          print ("welcome to aman shukla) [::-1]''':'aman ot emocleW',
          'what is the output of 0.1+0.2==0.3 ?':'False'}
# separate question and answers from question variable
que=[]
ans=[]
for key,value in question.items():
    que.append(key)
    ans.append(value)

# corresponding answer with answer including at random
options=[
    ['van neuman',ans[0],'jemes gosling','Gudo van rosom'],
    [ans[1],'4','4.5','Error'],
    ['012345','03345',ans[2],'56743'],
    ['aman to welcome','welcome  to aman',ans[3],'error'],
    ['True','0.6','syntaxError',ans[4]]

]
currentQ=''
queNo=None
currenA=''
score=0
qn=1 # for printing no of question finished
var =StringVar()
def _next():
    global currentQ,currenA,queNo,score,bar,i,qn
    i=0
    # till last question is left
    if len(que)>0:
        currentQ=random.choice(que)
        print(currentQ)
        q=Label(root,text='Que.'+str(qn),font='arial 10').place(x=20,y=80)
        qn+=1

        queNo=que.index(currentQ)
        print(options[queNo])
        currenA=question[currentQ]
        # firstly change caption of button
        submit.config(text='Next')
        # print option for question on questionlabel
        queLabel.config(text=currentQ,fg='green',height=6)
        # print option for question on quelabel
        enableAllButton()
        option1.config(text=options[queNo] [0],bg='sky blue', value=options[queNo][0],bd=1,command=answer)
        option2.config(text=options[queNo][1], bg='sky blue', value=options[queNo] [1], bd=1, command=answer)
        option3.config(text=options[queNo][2], bg='sky blue', value=options[queNo] [2], bd=1, command=answer)
        option4.config(text=options[queNo][3], bg='sky blue', value=options[queNo] [3], bd=1, command=answer)
        # remove question from list which are asked
        que.remove(currentQ)
        ans.remove(currenA)
        options.remove(options[queNo])
    elif len(que)==0:
        result()

def answer():
    global  currentQ,currenA,queNo,score
    a=var.get()
    if currenA==str(a):
        score+=100
        desableAllButton()
    else:
        desableAllButton()

title=''' Enterance exam for admission in Mca 2022-2025 vinobha bhave university hazaribagh'''
appName=Label(root,text=title ,font=' 20,italic',justify=CENTER,bg='goldenrod2',fg='white')
appName.pack(side=TOP,fill=BOTH)
# label is show current question
queLabel=Label(root,text='', justify=LEFT,font=25)
queLabel.pack(side=TOP,fill=BOTH)
s=Separator(root).place(x=0,y=195)
# option labels
option1=Radiobutton(root,text='',bg='black',font=20,width=20,relief=FLAT,indicator=0,value=1,variable=var,bd=0)
option1.place(x=150,y=250)
option2=Radiobutton(root,text='',bg='black',font=20,width=20,relief=FLAT,indicator=0,value=2,variable=var,bd=0)
option2.place(x=400,y=250)
option3=Radiobutton(root,text='',bg='black',font=20,width=20,relief=FLAT,indicator=0,value=3,variable=var,bd=0)
option3.place(x=150,y=300)
option4=Radiobutton(root,text='',bg='black',font=20,width=20,relief=FLAT,indicator=0,value=4,variable=var,bd=0)
option4.place(x=400,y=300)
# instruction of quiz
instruction=Label(root,text=intro,bg='black',fg='white',font='calibri 15',justify=LEFT)
instruction.place(x=150,y=200)
# note to quiz
note=Label(root,text='')
note.pack(side=BOTTOM)
# submit button
submit=Button(root,text="start quiz ",width=15,state=DISABLED,command=_next)


submit.pack(side=BOTTOM)
# show current item
showtime=Label(root,text='')
showtime.place(x=620,y=50)
# progress  bar  foe time left for each question
copyri8=Label(root,text='DEVELOPED by aman shukla',justify=LEFT,width=25)

if __name__=="__main__":
    root.withdraw()
    attendance()
    root.mainloop()




