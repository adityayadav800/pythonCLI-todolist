import sys
import os
from datetime import date

def add(argument):
    todoStorage.seek(0,0)
    c=todoStorage.readlines()
    x=len(c)
    todoStorage.write("["+str(x+1)+"] "+argument+" ")
    todoStorage.write('\n')
    doneCounter.write("["+str(x+1)+"] "+argument)
    doneCounter.write('\n')
    print("Added todo:",argument)
def help():
    print('$ ./todo add "todo item" # Add a new todo')
    print('$ ./todo ls              # Show remaining todos')
    print('$ ./todo del NUMBER      # Delete a todo')
    print('$ ./todo done NUMBER     # Complete a todo')
    print('$ ./todo help            # Show Usage')
    print('$ ./todo report          # Statistics')
def ls():
    todoStorage.seek(0,0)
    alltask=todoStorage.readlines()
    for task in alltask:
        print(task[:len(task)-1])
def delete(number):
    todoStorage.seek(0,0)
    alltask=todoStorage.readlines()
    alltask.pop(int(number)-1)
    todoStorage.seek(0,0)
    todoStorage.truncate(0)
    doneCounter.seek(0,0)
    alltask1=doneCounter.readlines()
    alltask1.pop(int(number)-1)
    doneCounter.seek(0,0)
    doneCounter.truncate(0)
    for task in alltask:
        todoStorage.write(task)
    for task in alltask1:
        doneCounter.write(task)
def done(number):
    doneCounter.seek(0,0)
    alltask=doneCounter.readlines()
    taskM=alltask[int(number)-1]
    alltask[int(number)-1]=taskM[:len(taskM)-1]+" DONE\n"
    doneCounter.seek(0,0)
    doneCounter.truncate(0)
    for task in alltask:
        doneCounter.write(task)
    print("Marked todo #%s as done"%(number))
def report():
    done=0
    incomplete=0
    doneCounter.seek(0,0)
    alltask=doneCounter.readlines()
    for task in alltask:
        if("DONE" in task):
            done+=1
        else:
            incomplete+=1
    print(date.today(),"PENDING : %d COMPLETED : %d"%(incomplete,done))

commandDict={"add":add,"help":help,"ls":ls,"del":delete,"done":done,"report":report}
todoStorage=open("todo.txt","a+")
doneCounter=open("Done.txt","a+")
if(len(sys.argv)==1):
    help()

command=sys.argv[1]
func=commandDict[sys.argv[1]]
if(command=="add" or command=="del" or command=="done"):
    func(sys.argv[2])
else:
    func()

    
