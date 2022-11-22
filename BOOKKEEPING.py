from tabulate import tabulate 
from easygui import *
import webbrowser
import sys
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost", user="root", passwd="1#!IDmysql05s", database="okari")
cursor=mycon.cursor()

    
'''LOAD'''

def okari():
    choices = ["EXPENDITURE", "EARNINGS", "SAVINGS", "HELP", "INFORMATION", "EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)
    if reply=="EXPENDITURE":
        optionsforexpen1()
    elif reply=="EARNINGS":
        optionsforexpen1i()
    elif reply=="SAVINGS":
        optionsforexpen1ii()
    elif reply=="HELP":
        helpokari()
    elif reply=="INFORMATION":
        information()
    elif reply=="EXIT":
        exitokari()
        
    

def helpokari():
    message="To navigate between options use mouse cursor or use keyboard arrow keys or press the first alphabet of the option  \n To select a option use mouse right double click or use keyboard enter key or use touch if system is compatible  \n To exit the program click exit button or choose exit option or press Alt+F4 \n For more quires contact shon.parale@gmail.com"
    title ="HELP"
    output = msgbox(message, title)
    okari()
def information():
    webbrowser.open('shon1.in/hiki', new=2)
    okari()
def exitokari():
    sys.exit()


'''START'''
def optionsforexpen1() :
    choices = ["ENTER DATA", "UPDATE DATA", "DELETE DATA", "FIND DATA", "SHOW DATA", "GO BACK", "EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)
    if reply=="ENTER DATA":
        enterdata()
    elif reply=="UPDATE DATA":
        updatedata()
    elif reply=="DELETE DATA":
        deletedata()
    elif reply=="FIND DATA":
        finddata()
    elif reply=="SHOW DATA":
        showdata()
    elif reply=="GO BACK":
        okari()
    elif reply=="EXIT":
        exitokari() 



'''ENTERDATA'''
def enterdata():
    
    text = "ENTER THE NAME OF THE ENTRY"
    title="EXPENDITURE"
    a=enterbox(text, title)
    
    text = "ENTER THE AMOUNT OF THE ENTRY"
    title="EXPENDITURE"
    b=enterbox(text, title)
    
    text = "ENTER THE REASON OF THE ENTRY"
    title="EXPENDITURE"
    c=enterbox(text, title)
    
    text = "ENTER THE DATE OF THE ENTRY"
    title="EXPENDITURE"
    d=enterbox(text, title)
    
    sql = "INSERT INTO expenditure(name, amount, reason, date) VALUES (%s, %s, %s,%s)"
    val= [a, b, c, d]
    cursor.execute(sql,val)
    mycon.commit ()
    optionsforexpen1()


'''UPDATE DATA'''
def updatedata():
    choices = ["NAME", "AMOUNT", "REASON", "DATE", "GO BACK", "EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)
    if reply=="NAME":
        name()
    elif reply=="AMOUNT":
        amount()
    elif reply=="REASON":
        reason()
    elif reply=="DATE":
        date()
    elif reply=="GO BACK":
        optionsforexpen1()
    elif reply=="EXIT":
        exitokari()
        
def name():
    text = "ENTER THE NAME TO BE UPDATED"
    title="EXPENDITURE"
    a=enterbox(text, title)
    
    text = "ENTER THE AMOUNT OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EXPENDITURE"
    b=enterbox(text, title)
    
    text = "ENTER THE REASON OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EXPENDITURE"
    c=enterbox(text, title)
    
    text = "ENTER THE DATE OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EXPENDITURE"
    d=enterbox(text, title)
    sql = "UPDATE expenditure SET name =%s WHERE amount=%s AND reason =%s AND date=%s"
    cursor.execute(sql, (a, b,c,d)) 
    mycon.commit()
    updatedata()

def amount():
   text = "ENTER THE AMOUNT TO BE UPDATED"
   title="EXPENDITURE"
   a=enterbox(text, title)
   
   text = "ENTER THE NAME OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
   title="EXPENDITURE"
   b=enterbox(text, title)
   
   text = "ENTER THE REASON OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
   title="EXPENDITURE"
   c=enterbox(text, title)
   
   text = "ENTER THE DATE OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
   title="EXPENDITURE"
   d=enterbox(text, title)
   sql = "UPDATE expenditure SET amount =%s WHERE name=%s AND reason =%s AND date=%s"
   cursor.execute(sql, (a, b,c,d)) 
   mycon.commit()
   updatedata()

def reason():
    text = "ENTER THE REASON TO BE UPDATED"
    title="EXPENDITURE"
    a=enterbox(text, title)
    
    text = "ENTER THE NAME OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EXPENDITURE"
    b=enterbox(text, title)
    
    text = "ENTER THE AMOUNT OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EXPENDITURE"
    c=enterbox(text, title)
    
    text = "ENTER THE DATE OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EXPENDITURE"
    d=enterbox(text, title)

    sql = "UPDATE expenditure SET reason =%s WHERE name=%s AND amount =%s AND date=%s"
    cursor.execute(sql, (a, b,c,d)) 
    mycon.commit()
    updatedata()
    
def date():
    text = "ENTER THE DATE TO BE UPDATED"
    title="EXPENDITURE"
    a=enterbox(text, title)
    
    text = "ENTER THE NAME OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EXPENDITURE"
    b=enterbox(text, title)
    
    text = "ENTER THE AMOUNT OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EXPENDITURE"
    c=enterbox(text, title)
    
    text = "ENTER THE REASON OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EXPENDITURE"
    d=enterbox(text, title)
    sql = "UPDATE expenditure SET date =%s WHERE name=%s AND amount =%s AND reason=%s"
    cursor.execute(sql, (a, b,c,d)) 
    mycon.commit()
    updatedata()

'''DELETE DATA'''
def deletedata():
    choices = ["DELETE A ENTRY", "DELETE ENTRIES WITH SPECIFIC NAME", "DELETE ENTRIES WITH SPECIFIC AMOUNT", "DELETE ENTRIES WITH SPECIFIC REASON", "DELETE ENTRIES WITH SPECIFIC DATE", "DELETE ALL ENTRIES","GO BACK","EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)

    if reply=="DELETE A ENTRY":
        aaone()
    elif reply=="DELETE ENTRIES WITH SPECIFIC NAME":
        aatwo()
    elif reply=="DELETE ENTRIES WITH SPECIFIC AMOUNT":
        aathree()
    elif reply=="DELETE ENTRIES WITH SPECIFIC REASON":
        aafour()
    elif reply=="DELETE ENTRIES WITH SPECIFIC DATE":
        aafive()
    elif reply=="DELETE ALL ENTRIES":
        aasix()
    elif reply=="GO BACK":
        optionsforexpen1()
    elif reply=="EXIT":
        exitokari()
def aaone():
    text = "ENTER THE NAME OF THE ENTRY"
    title="EXPENDITURE"
    a=enterbox(text, title)
    text = "ENTER THE AMOUNT OF THE ENTRY"
    title="EXPENDITURE"
    b=enterbox(text, title)
    text = "ENTER THE REASON OF THE ENTRY"
    title="EXPENDITURE"
    c=enterbox(text, title)
    text = "ENTER THE DATE OF THE ENTRY"
    title="EXPENDITURE"
    d=enterbox(text, title)
    sql = "DELETE FROM expenditure WHERE name =%s AND amount=%s AND reason =%s AND date=%s "
    cursor.execute(sql, [a, b,c,d])
    mycon.commit()
    deletedata()

def aatwo():
    text = "ENTER THE NAMEs OF THE ENTRIES TO BE DELETEDY"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql = "DELETE FROM expenditure WHERE name=%s"
    cursor.execute(sql,[a])
    mycon.commit()
    deletedata()

def aathree():
    text = "ENTER THE AMOUNT OF THE ENTRIES TO BE DELETED"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql = "DELETE FROM expenditure WHERE amount=%s"
    cursor.execute(sql,[a])
    mycon.commit()
    deletedata()

def aafour():
    text = "ENTER THE REASON OF THE ENTRIES TO BE DELETED"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql = "DELETE FROM expenditure WHERE reason=%s"
    cursor.execute(sql,[a])
    mycon.commit()
    deletedata()

def aafive():
    text = "ENTER THE DATE OF THE ENTRIES TO BE DELETED"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql = "DELETE FROM expenditure WHERE date=%s"
    cursor.execute(sql,[a])
    mycon.commit()
    deletedata()
    
def aasix():
    sql = "DELETE FROM expenditure"
    cursor.execute(sql)
    mycon.commit()
    deletedata()
'''FIND DATA'''

def finddata():
    choices = ["FIND A ENTRIES REALTED TO NAME", "FIND ENTRIES RELATED TO AMOUNT", "FIND ENTRIES RELATED TO A REASON", "FIND ENTRIES RELATED TO A DATE", "GO BACK", "EXIT"]
    msg="SELECT"
    reply=choicebox(msg,choices=choices)
    if reply=="FIND A ENTRIES REALTED TO NAME":
        finddataname()
    elif reply=="FIND ENTRIES RELATED TO AMOUNT":
        finddataamount()
    elif reply=="FIND ENTRIES RELATED TO A REASON":
        finddatareason()
    elif "FIND ENTRIES RELATED TO A DATE":
        reply==finddatadate()
    elif reply=="GO BACK":
        optionsforexpen1()
    elif reply=="EXIT":
        exitokari()

def finddataname():
    choices = ["FIND MAXIMUM EXPENDITURE BY A PERSON", "FIND MINIMUM AMOUNT BY A PERSON", "FIND TOTAL EXPENDITURE BY A PERSON", "FIND ALL ENTRIES BY A PERSON", "FIND ALL ENTRIES BY A PERSON IN INCREASING ORDER", "FIND ALL ENTRIES BY A PERSON IN DECREASING ORDER", "FIND NUMBER OF EXPENDITURES BY A PERSON", "FIND NAMES OF ALL PEOPLE", "GO BACK", "EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)
    if reply=="FIND MAXIMUM EXPENDITURE BY A PERSON":
        maxamountbyperson()
    elif reply=="FIND MINIMUM EXPENDITURE BY A PERSON":
        minamountbyperson()
    elif reply=="FIND TOTAL EXPENDITURE BY A PERSON":
        sumamountbyperson()
    elif reply=="FIND ALL ENTRIES BY A PERSON":
        allentriesbyaperson()
    elif reply=="FIND ALL ENTRIES BY A PERSON IN INCREASING ORDER":
        allentriesbyapersoninincreasingorderofamount()
    elif reply=="FIND ALL ENTRIES BY A PERSON IN DECREASING ORDER":
        allentriesbyapersonindecreasingorderofamount()
    elif reply=="FIND NUMBER OF EXPENDITURES BY A PERSON":
        numberofentriesbyaperson()
    elif reply=="FIND NAMES OF ALL PEOPLE":
        namesofallpersons()
    elif reply=="GO BACK":
        finddata()
    elif reply=="EXIT":
        exitokari()
        
def finddataamount():
    choices = ["FIND MAXIMUM AMOUNT", "FIND MINIMUM AMOUNT", "FIND ENTRY WITH MAXIMUM AMOUNT", "FIND ENTRY WITH MINIMUM AMOUNT", "FIND ENTRIES WITH AMOUNT IN INCREASING ORDER", "FIND ENTRIES WITH AMOUNT IN DECREASING ORDER", "FIND ENTRIES WITH AMOUNT GREATER THAN A SPECIFIC AMOUNT", "FIND ENTRIES WITH AMOUNT LESSER THAN A SPECIFIC AMOUNT", "FIND ENTRIES WITH AMOUNT GREATER THAN EQUAL TO A SPECIFIC AMOUNT", "FIND ENTRIES WITH AMOUNT LESSER THAN EQUAL TO A SPECIFIC AMOUNT", "FIND ENTIES WITH AMOUNT GREATER THAN AND LESSER THAN A SPECIFIC AMOUNT", "FIND ENTIES WITH AMOUNT GREATER THAN EQUAL TO AND LESSER THAN EQUAL TO A SPECIFIC AMOUNT", "FIND ENTRIES WITH SPECIFIC AMOUNT", "FIND NUMBER OF ENTRIES WITH SPECIFIC AMOUNT","GO BACK", "EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)

    if reply=="FIND MAXIMUM AMOUNT":
        maxamount()
    elif reply=="FIND MINIMUM AMOUNT":
        minamount()
    elif reply=="FIND ENTRY WITH MAXIMUM AMOUNT":
        entrymaxamount()
    elif reply=="FIND ENTRY WITH MINIMUM AMOUNT":
        entryminamount()
    elif reply=="FIND ENTRIES WITH AMOUNT IN INCREASING ORDER":
        entriesamountinincreasingorder()
    elif reply=="FIND ENTRIES WITH AMOUNT IN DECREASING ORDER":
        entriesamountindecreasingorder()
    elif reply=="FIND ENTRIES WITH AMOUNT GREATER THAN A SPECIFIC AMOUNT":
        entriesamountgreater()
    elif reply=="FIND ENTRIES WITH AMOUNT LESSER THAN A SPECIFIC AMOUNT":
        entriesamountlesser()
    elif reply=="FIND ENTRIES WITH AMOUNT GREATER THAN EQUAL TO A SPECIFIC AMOUNT":
        entiresamountgreaterthanequalto()
    elif reply=="FIND ENTRIES WITH AMOUNT LESSER THAN EQUAL TO A SPECIFIC AMOUNT":
        entriesamountlesserthanequalto()
    elif reply=="FIND ENTIES WITH AMOUNT GREATER THAN AND LESSER THAN A SPECIFIC AMOUNT":
        entriesamountgreaterthanlesserthan()
    elif reply=="FIND ENTIES WITH AMOUNT GREATER THAN EQUAL TO AND LESSER THAN EQUAL TO A SPECIFIC AMOUNT":
        entriesamountgreaterthaneqaltolesserthanequalto()
    elif reply=="FIND ENTRIES WITH SPECIFIC AMOUNT":
        entrieswithamount()
    elif reply=="FIND NUMBER OF ENTRIES WITH SPECIFIC AMOUNT":
        numberofentrieswithamount()
    elif reply=="GO BACK":
        finddata()
    elif reply=="EXIT":
        exitokari()
    
def finddatareason():
    choices = ["FIND ENTRIES WITH SPECIFIC REASON", "FIND NUMBER OF ENTRIES WIHT SPECIFIC REASON", "FIND DIFFERENT TYPES OF REASONS", "FIND NUMBER OF DIFFERENT TYPES OF REASONS", "GO BACK", "EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)
    if reply=="FIND ENTRIES WITH SPECIFIC REASON":
        entrieswithreason()
    elif reply=="FIND NUMBER OF ENTRIES WIHT SPECIFIC REASON":
        numberofentrieswithreason()
    elif reply=="FIND DIFFERENT TYPES OF REASONS":
        typesofreasons()
    elif reply=="FIND NUMBER OF DIFFERENT TYPES OF REASONS":
        numberoftypesofreason()
    elif reply=="GO BACK":
        finddata()
    elif reply=="EXIT":
        exitokari()
def finddatadate():
    choices=["FIND ENTREIS WITH A SPECIFIC DATE" ,"FIND ENTRIES BETWEEN TWO SPECIFIC DATE" ,"FIND ENTRIES AFTER A SPECIFIC DATE" ,"FIND ENTRIES BEFORE A SPECIFIC DATE","FIND ENTRIES ON AND BETWEEN TWO SPECIFIC DATES","FIND ENTRIES ON AND AFTER A SPECIFIC DATE","FIND ENTRIES ON AND BEFORE A SPECIFIC DATE","FIND NUMBER OF ENTRIES ON A SPECIFIC DATE","FIND NUMBER OF ENTRIES BETWEEN TWO SPECIFIC DATES","FIND NUMBER OF ENTRIES ON AND BETWEEN TWO SPECIFIC DATES","FIND NUMBER OF ENTRIES AFTER A SPECIFIC DATE","FIND NUMBER OF ENTRIES ON AND AFTER A SPECIFIC DATE","FIND NUMBER OF ENTRIES BEFORE A SPECIFIC DATE", "FIND NUMBER OF ENTRIES ON AND BEFORE A SPECIFIC DATE" ,"GO BACK" ,"EXIT"]
    msg="SELECT"
    reply=choicebox(msg, choices = choices)
    if reply=="FIND ENTREIS WITH A SPECIFIC DATE":
        entriesbydate()
    elif reply=="FIND ENTRIES BETWEEN TWO SPECIFIC DATE":
        entriesbetweentwodates()
    elif reply=="FIND ENTRIES AFTER A SPECIFIC DATE":
        entriesafteraspecificdate()
    elif reply=="FIND ENTRIES BEFORE A SPECIFIC DATE":
        entriesbeforeaspecificdate()
    elif reply=="FIND ENTRIES ON AND BETWEEN TWO SPECIFIC DATES":
        onbetweentwodates()
    elif reply=="FIND ENTRIES ON AND AFTER A SPECIFIC DATE":
        onaftersepcificdate()
    elif reply=="FIND ENTRIES ON AND BEFORE A SPECIFIC DATE":
        onbeforespecificdate()
    elif "FIND NUMBER OF ENTRIES ON A SPECIFIC DATE":
        numofentriesonaspecificdate()
    elif reply=="FIND NUMBER OF ENTRIES BETWEEN TWO SPECIFIC DATES":
        numofentriesbetweentwospecificdates()
    elif reply=="FIND NUMBER OF ENTRIES ON AND BETWEEN TWO SPECIFIC DATES":
        numofentriesonandbetweentwodates()
    elif reply=="FIND NUMBER OF ENTRIES AFTER A SPECIFIC DATE":
        numberofentriesafteraspecificdate()
    elif reply=="FIND NUMBER OF ENTRIES ON AND AFTER A SPECIFIC DATE":
        numberofentriesonafteraspecificdate()
    elif reply=="FIND NUMBER OF ENTRIES BEFORE A SPECIFIC DATE":
        numberofentriesbeforeaspecificdate()
    elif reply=="FIND NUMBER OF ENTRIES ON AND BEFORE A SPECIFIC DATE":
        numberofentriesonbeforeaspecificdate()
    elif reply=="GO BACK":
        finddata()
    elif reply=="EXIT":
        exitokari()
        
'''FINDDATANAMEAA'''
#Option1
def maxamountbyperson():
    text = "ENTER THE NAME OF THE PERSON"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT MAX(amount) AS maximum FROM expenditure WHERE name=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for i in result:
        maximum = i[0]
    message=maximum
    title="EXPENDITURE"
    output = msgbox(message, title)
    finddataname()

#Option2
def minamountbyperson():
    text = "ENTER THE NAME OF THE PERSON"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT MIN(amount) AS minimum FROM expenditure WHERE name=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for i in result:
        minimum= i[0]
    message=minimum
    title="EXPENDITURE"
    output = msgbox(message, title)
    finddataname()

#Option3
def sumamountbyperson():
    text = "ENTER THE NAME OF THE PERSON"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT SUM(amount) AS sum FROM expenditure WHERE name=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for i in result:
        sum=i[0]
    message=sum
    title="EXPENDITURE"
    output = msgbox(message, title)
    finddataname()

#Option4
def allentriesbyaperson():
    text = "ENTER THE NAME OF THE PERSON"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT*FROM expenditure WHERE name=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataname()

#Option5
def allentriesbyapersoninincreasingorderofamount():
    text = "ENTER THE NAME OF THE PERSON"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT name,amount,reason,date FROM expenditure WHERE name=%s ORDER BY amount"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataname()

#Option6
def allentriesbyapersonindecreasingorderofamount():
    text = "ENTER THE NAME OF THE PERSON"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT name,amount,reason,date FROM expenditure WHERE name=%s ORDER BY amount DESC"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataname()

#Option7
def numberofentriesbyaperson():
    text = "ENTER THE NAME OF THE PERSON"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT COUNT(name) FROM expenditure WHERE name=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    output = msgbox(message, title)
    finddataname()

#Option8
def namesofallpersons():
    sql="SELECT DISTINCT name FROM expenditure"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataname()

'''FINDDATAAMOUNTBB'''

#Option1
def maxamount():
    sql="SELECT MAX(amount) from expenditure"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    output = msgbox(message, title)
    finddataamount()

#Option2
def minamount():
    sql="SELECT MIN(amount) from expenditure"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    output = msgbox(message, title)
    finddataamount()

#Option3
def entrymaxamount():
    sql="SELECT*FROM expenditure WHERE amount=(select max(amount) FROM expenditure)"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamount()

#Option4
def entryminamount():
    sql="SELECT*FROM expenditure WHERE amount=(select min(amount) FROM expenditure)"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamount()

#Option5
def entriesamountinincreasingorder():
    sql="SELECT name, amount, reason, date FROM expenditure ORDER BY amount"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamount()

#Option6
def entriesamountindecreasingorder():
    sql="SELECT name, amount, reason, date FROM expenditure ORDER BY amount DESC"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamount()
        
#Option7
def entriesamountgreater():
    text = "ENTER THE GREATER THAN AMOUNT"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT*FROM expenditure WHERE amount>%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamount()

#Option8
def entriesamountlesser():
    text = "ENTER THE LESSER THAN AMOUNT"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT*FROM expenditure WHERE amount<%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamount()

#Option9
def entiresamountgreaterthanequalto():
    text = "ENTER THE GREATER THAN EQUAL TO AMOUNT"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT*FROM expenditure WHERE amount>=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamount()

#Option10
def entriesamountlesserthanequalto():
    text = "ENTER THE LESSER THAN EQUAL TO AMOUNT"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT*FROM expenditure WHERE amount<=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamount()

#option11
def entriesamountgreaterthanlesserthan():
    text = "ENTER THE GREATER THAN AMOUNT"
    title="EXPENDITURE"
    a=enterbox(text, title)
    text = "ENTER THE LESSER THAN AMOUNT"
    title="EXPENDITURE"
    b=enterbox(text, title)
    sql="SELECT*FROM expenditure WHERE amount>%s and amount<%s"
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamount()

#Option12
def entriesamountgreaterthaneqaltolesserthanequalto():
    text = "ENTER THE GREATER THAN EQUAL TO AMOUNT"
    title="EXPENDITURE"
    a=enterbox(text, title)
    text = "ENTER THE LESSER THAN EQUAL TO AMOUNT"
    title="EXPENDITURE"
    b=enterbox(text, title)
    sql="SELECT*FROM expenditure WHERE amount>=%s and amount<=%s"
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamount()

#Option13
def entrieswithamount():
    text = "ENTER THE AMOUNT"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT*FROM expenditure WHERE amount=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamount()

#Option14
def numberofentrieswithamount():
    text="ENTER THE AMOUNT"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT COUNT(amount) FROM expenditure where amount=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    output = msgbox(message, title)
    finddataamount()

'''FINDDATAREASONCC'''
#Option1
def entrieswithreason():
    text = "ENTER THE REASON"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT*FROM expenditure WHERE reason=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatareason()

#Option2
def numberofentrieswithreason():
    text = "ENTER THE REASON"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT COUNT(reason) FROM expenditure WHERE reason=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    output = msgbox(message, title)
    finddatareason()

#Option3
def typesofreasons():
    sql="SELECT DISTINCT (reason) FROM expenditure"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatareason()

#Option4
def numberoftypesofreason():
    sql="SELECT COUNT(DISTINCT (reason)) FROM expenditure"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    output = msgbox(message, title)
    finddatareason()

'''FINDDATADATEDD'''
#Option1
def entriesbydate():
    text = "ENTER THE DATE"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT*FROM expenditure WHERE date=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadate()
#Option2
def entriesbetweentwodates():
    text = "ENTER THE STARTING DATE"
    title="EXPENDITURE"
    a=enterbox(text, title)
    text = "ENTER THE ENDING DATE"
    title="EXPENDITURE"
    b=enterbox(text, title)
    sql="SELECT*FROM expenditure WHERE date>=%s and date<=%s "
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadate()

#Option3
def entriesafteraspecificdate():
    text = "ENTER THE DATE"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT*FROM expenditure WHERE date>%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadate()

#Option4
def entriesbeforeaspecificdate():
    text = "ENTER THE DATE"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT*FROM expenditure WHERE date<%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadate()
        
#Option5
def onbetweentwodates():
    text = "ENTER THE STARTING DATE"
    title="EXPENDITURE"
    a=enterbox(text, title)
    text = "ENTER THE ENDING DATE"
    title="EXPENDITURE"
    b=enterbox(text, title)
    sql="SELECT*FROM expenditure WHERE date>=%s and date<=%s "
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadate()

#Option6
def onaftersepcificdate():
    text = "ENTER THE DATE"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT*FROM expenditure WHERE date>=%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadate()

#Option7
def onbeforespecificdate():
    text = "ENTER THE STARTING DATE"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT*FROM expenditure WHERE date<=%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadate()

#Option8
def numofentriesonaspecificdate():
    text = "ENTER THE DATE"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT COUNT(date)FROM expenditure WHERE date=%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    output = msgbox(message, title)
    finddatadate()

#Option9
def numofentriesbetweentwospecificdates():
    text = "ENTER THE STARTING DATE"
    title="EXPENDITURE"
    a=enterbox(text, title)
    text = "ENTER THE ENDING DATE"
    title="EXPENDITURE"
    b=enterbox(text, title)
    sql="SELECT COUNT(date)FROM expenditure WHERE date BETWEEN %s and %s"
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    output = msgbox(message, title)
    finddatadate()

#Option10
def numofentriesonandbetweentwodates():
    text = "ENTER THE STARTING DATE"
    title="EXPENDITURE"
    a=enterbox(text, title)
    text = "ENTER THE ENDING DATE"
    title="EXPENDITURE"
    b=enterbox(text, title)
    sql="SELECT COUNT(date )FROM expenditure WHERE date>=%s and date<=%s"
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    output = msgbox(message, title)
    finddatadate()

#Option11
def numberofentriesafteraspecificdate():
    text = "ENTER THE DATE"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT COUNT(date)FROM expenditure WHERE date>%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    output = msgbox(message, title)
    finddatadate()

#Option12
def numberofentriesonafteraspecificdate():
    text = "ENTER THE DATE"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT COUNT(date)FROM expenditure WHERE date>=%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    output = msgbox(message, title)
    finddatadate()

#Option13
def numberofentriesbeforeaspecificdate():
    text = "ENTER THE DATE"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT COUNT(date)FROM expenditure WHERE date<%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    output = msgbox(message, title)
    finddatadate()

#Option14
def numberofentriesonbeforeaspecificdate():
    text = "ENTER THE DATE"
    title="EXPENDITURE"
    a=enterbox(text, title)
    sql="SELECT COUNT(date)FROM expenditure WHERE date<=%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    output = msgbox(message, title)
    finddatadate()

'''SHOW DATA'''
def showdata():
    cursor = mycon.cursor()
    cursor.execute("SELECT * FROM expenditure")
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EXPENDITURE"
    final=tabulate(message)
    output = msgbox(final, title)
    optionsforexpen1()
        

#earnings#


'''START'''
def optionsforexpen1i() :
    choices = ["ENTER DATA", "UPDATE DATA", "DELETE DATA", "FIND DATA", "SHOW DATA", "GO BACK", "EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)
    if reply=="ENTER DATA":
        enterdatai()
    elif reply=="UPDATE DATA":
        updatedatai()
    elif reply=="DELETE DATA":
        deletedatai()
    elif reply=="FIND DATA":
        finddatai()
    elif reply=="SHOW DATA":
        showdatai()
    elif reply=="GO BACK":
        okari()
    elif reply=="EXIT":
        exitokari() 

'''ENTERDATA'''
def enterdatai():
    
    text = "ENTER THE NAME OF THE ENTRY"
    title="EARNINGS"
    a=enterbox(text, title)
    
    text = "ENTER THE AMOUNT OF THE ENTRY"
    title="EARNINGS"
    b=enterbox(text, title)
    
    text = "ENTER THE REASON OF THE ENTRY"
    title="EARNINGS"
    c=enterbox(text, title)
    
    text = "ENTER THE DATE OF THE ENTRY"
    title="EARNINGS"
    d=enterbox(text, title)
    
    sql = "INSERT INTO earnings(name, amount, reason, date) VALUES (%s, %s, %s,%s)"
    val= [a, b, c, d]
    cursor.execute(sql,val)
    mycon.commit ()
    optionsforexpen1i()


'''UPDATE DATA'''
def updatedatai():
    choices = ["NAME", "AMOUNT", "REASON", "DATE", "GO BACK", "EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)
    if reply=="NAME":
        namei()
    elif reply=="AMOUNT":
        amounti()
    elif reply=="REASON":
        reasoni()
    elif reply=="DATE":
        datei()
    elif reply=="GO BACK":
        optionsforexpen1i()
    elif reply=="EXIT":
        exitokari()
        
def namei():
    text = "ENTER THE NAME TO BE UPDATED"
    title="EARNINGS"
    a=enterbox(text, title)
    
    text = "ENTER THE AMOUNT OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EARNINGS"
    b=enterbox(text, title)
    
    text = "ENTER THE REASON OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EARNINGS"
    c=enterbox(text, title)
    
    text = "ENTER THE DATE OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EARNINGS"
    d=enterbox(text, title)
    sql = "UPDATE earnings SET name =%s WHERE amount=%s AND reason =%s AND date=%s"
    cursor.execute(sql, (a, b,c,d)) 
    mycon.commit()
    updatedatai()

def amounti():
   text = "ENTER THE AMOUNT TO BE UPDATED"
   title="EARNINGS"
   a=enterbox(text, title)
   
   text = "ENTER THE NAME OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
   title="EARNINGS"
   b=enterbox(text, title)
   
   text = "ENTER THE REASON OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
   title="EARNINGS"
   c=enterbox(text, title)
   
   text = "ENTER THE DATE OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
   title="EARNINGS"
   d=enterbox(text, title)
   sql = "UPDATE earnings SET amount =%s WHERE name=%s AND reason =%s AND date=%s"
   cursor.execute(sql, (a, b,c,d)) 
   mycon.commit()
   updatedatai()

def reasoni():
    text = "ENTER THE REASON TO BE UPDATED"
    title="EARNINGS"
    a=enterbox(text, title)
    
    text = "ENTER THE NAME OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EARNINGS"
    b=enterbox(text, title)
    
    text = "ENTER THE AMOUNT OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EARNINGS"
    c=enterbox(text, title)
    
    text = "ENTER THE DATE OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EARNINGS"
    d=enterbox(text, title)

    sql = "UPDATE earnings SET reason =%s WHERE name=%s AND amount =%s AND date=%s"
    cursor.execute(sql, (a, b,c,d)) 
    mycon.commit()
    updatedatai()
    
def datei():
    text = "ENTER THE DATE TO BE UPDATED"
    title="EARNINGS"
    a=enterbox(text, title)
    
    text = "ENTER THE NAME OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EARNINGS"
    b=enterbox(text, title)
    
    text = "ENTER THE AMOUNT OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EARNINGS"
    c=enterbox(text, title)
    
    text = "ENTER THE REASON OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="EARNINGS"
    d=enterbox(text, title)
    sql = "UPDATE earnings SET date =%s WHERE name=%s AND amount =%s AND reason=%s"
    cursor.execute(sql, (a, b,c,d)) 
    mycon.commit()
    updatedatai()

'''DELETE DATA'''
def deletedatai():
    choices = ["DELETE A ENTRY", "DELETE ENTRIES WITH SPECIFIC NAME", "DELETE ENTRIES WITH SPECIFIC AMOUNT", "DELETE ENTRIES WITH SPECIFIC REASON", "DELETE ENTRIES WITH SPECIFIC DATE", "DELETE ALL ENTRIES","GO BACK","EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)

    if reply=="DELETE A ENTRY":
        aaonei()
    elif reply=="DELETE ENTRIES WITH SPECIFIC NAME":
        aatwoi()
    elif reply=="DELETE ENTRIES WITH SPECIFIC AMOUNT":
        aathreei()
    elif reply=="DELETE ENTRIES WITH SPECIFIC REASON":
        aafouri()
    elif reply=="DELETE ENTRIES WITH SPECIFIC DATE":
        aafivei()
    elif reply=="DELETE ALL ENTRIES":
        aasixi()
    elif reply=="GO BACK":
        optionsforexpen1i()
    elif reply=="EXIT":
        exitokari()
def aaonei():
    text = "ENTER THE NAME OF THE ENTRY"
    title="EARNINGS"
    a=enterbox(text, title)
    text = "ENTER THE AMOUNT OF THE ENTRY"
    title="EARNINGS"
    b=enterbox(text, title)
    text = "ENTER THE REASON OF THE ENTRY"
    title="EARNINGS"
    c=enterbox(text, title)
    text = "ENTER THE DATE OF THE ENTRY"
    title="EARNINGS"
    d=enterbox(text, title)
    sql = "DELETE FROM earnings WHERE name =%s AND amount=%s AND reason =%s AND date=%s "
    cursor.execute(sql, [a, b,c,d])
    mycon.commit()
    deletedatai()

def aatwoi():
    text = "ENTER THE NAMEs OF THE ENTRIES TO BE DELETEDY"
    title="EARNINGS"
    a=enterbox(text, title)
    sql = "DELETE FROM earnings WHERE name=%s"
    cursor.execute(sql,[a])
    mycon.commit()
    deletedatai()

def aathreei():
    text = "ENTER THE AMOUNT OF THE ENTRIES TO BE DELETED"
    title="EARNINGS"
    a=enterbox(text, title)
    sql = "DELETE FROM earnings WHERE amount=%s"
    cursor.execute(sql,[a])
    mycon.commit()
    deletedatai()

def aafouri():
    text = "ENTER THE REASON OF THE ENTRIES TO BE DELETED"
    title="EARNINGS"
    a=enterbox(text, title)
    sql = "DELETE FROM earnings WHERE reason=%s"
    cursor.execute(sql,[a])
    mycon.commit()
    deletedatai()

def aafivei():
    text = "ENTER THE DATE OF THE ENTRIES TO BE DELETED"
    title="EARNINGS"
    a=enterbox(text, title)
    sql = "DELETE FROM earnings WHERE date=%s"
    cursor.execute(sql,[a])
    mycon.commit()
    deletedatai()
    
def aasixi():
    sql = "DELETE FROM income"
    cursor.execute(sql)
    mycon.commit()
    deletedatai()
    
'''FIND DATA'''

def finddatai():
    choices = ["FIND A ENTRIES REALTED TO NAME", "FIND ENTRIES RELATED TO AMOUNT", "FIND ENTRIES RELATED TO A REASON", "FIND ENTRIES RELATED TO A DATE", "GO BACK", "EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)
    if reply=="FIND A ENTRIES REALTED TO NAME":
        finddatanamei()
    elif reply=="FIND ENTRIES RELATED TO AMOUNT":
        finddataamounti()
    elif reply=="FIND ENTRIES RELATED TO A REASON":
        finddatareasoni()
    elif reply=="FIND ENTRIES RELATED TO A DATE":
        finddatadatei()
    elif reply=="GO BACK":
        optionsforexpen1i()
    elif reply=="EXIT":
        exitokari()

def finddatanamei():
    choices = ["FIND MAXIMUM earnings BY A PERSON", "FIND MINIMUM AMOUNT BY A PERSON", "FIND TOTAL earnings BY A PERSON", "FIND ALL ENTRIES BY A PERSON", "FIND ALL ENTRIES BY A PERSON IN INCREASING ORDER", "FIND ALL ENTRIES BY A PERSON IN DECREASING ORDER", "FIND NUMBER OF earningsS BY A PERSON", "FIND NAMES OF ALL PEOPLE", "GO BACK", "EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)
    if reply=="FIND MAXIMUM earnings BY A PERSON":
        maxamountbypersoni()
    elif reply=="FIND MINIMUM earnings BY A PERSON":
        minamountbypersoni()
    elif reply=="FIND TOTAL earnings BY A PERSON":
        sumamountbypersoni()
    elif reply=="FIND ALL ENTRIES BY A PERSON":
        allentriesbyapersoni()
    elif reply=="FIND ALL ENTRIES BY A PERSON IN INCREASING ORDER":
        allentriesbyapersoninincreasingorderofamounti()
    elif reply=="FIND ALL ENTRIES BY A PERSON IN INCREASING ORDER":
        allentriesbyapersonindecreasingorderofamounti()
    elif reply=="FIND NUMBER OF earningsS BY A PERSON":
        numberofentriesbyapersoni()
    elif reply=="FIND NAMES OF ALL PEOPLE":
        namesofallpersonsi()
    elif reply=="GO BACK":
        finddatai()
    elif reply=="EXIT":
        exitokari()
        
def finddataamounti():
    choices = ["FIND MAXIMUM AMOUNT", "FIND MINIMUM AMOUNT", "FIND ENTRY WITH MAXIMUM AMOUNT", "FIND ENTRY WITH MINIMUM AMOUNT", "FIND ENTRIES WITH AMOUNT IN INCREASING ORDER", "FIND ENTRIES WITH AMOUNT IN DECREASING ORDER", "FIND ENTRIES WITH AMOUNT GREATER THAN A SPECIFIC AMOUNT", "FIND ENTRIES WITH AMOUNT LESSER THAN A SPECIFIC AMOUNT", "FIND ENTRIES WITH AMOUNT GREATER THAN EQUAL TO A SPECIFIC AMOUNT", "FIND ENTRIES WITH AMOUNT LESSER THAN EQUAL TO A SPECIFIC AMOUNT", "FIND ENTIES WITH AMOUNT GREATER THAN AND LESSER THAN A SPECIFIC AMOUNT", "FIND ENTIES WITH AMOUNT GREATER THAN EQUAL TO AND LESSER THAN EQUAL TO A SPECIFIC AMOUNT", "FIND ENTRIES WITH SPECIFIC AMOUNT", "FIND NUMBER OF ENTRIES WITH SPECIFIC AMOUNT","GO BACK", "EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)

    if reply=="FIND MAXIMUM AMOUNT":
        maxamounti()
    elif reply=="FIND MINIMUM AMOUNT":
        minamounti()
    elif reply=="FIND ENTRY WITH MAXIMUM AMOUNT":
        entrymaxamounti()
    elif reply=="FIND ENTRY WITH MINIMUM AMOUNT":
        entryminamounti()
    elif reply=="FIND ENTRIES WITH AMOUNT IN INCREASING ORDER":
        entriesamountinincreasingorderi()
    elif reply=="FIND ENTRIES WITH AMOUNT IN DECREASING ORDER":
        entriesamountindecreasingorderi()
    elif reply=="FIND ENTRIES WITH AMOUNT GREATER THAN A SPECIFIC AMOUNT":
        entriesamountgreateri()
    elif reply=="FIND ENTRIES WITH AMOUNT LESSER THAN A SPECIFIC AMOUNT":
        entriesamountlesseri()
    elif reply=="FIND ENTRIES WITH AMOUNT GREATER THAN EQUAL TO A SPECIFIC AMOUNT":
        entiresamountgreaterthanequaltoi()
    elif reply=="FIND ENTRIES WITH AMOUNT LESSER THAN EQUAL TO A SPECIFIC AMOUNT":
        entriesamountlesserthanequaltoi()
    elif reply=="FIND ENTIES WITH AMOUNT GREATER THAN AND LESSER THAN A SPECIFIC AMOUNT":
        entriesamountgreaterthanlesserthani()
    elif reply=="FIND ENTIES WITH AMOUNT GREATER THAN EQUAL TO AND LESSER THAN EQUAL TO A SPECIFIC AMOUNT":
        entriesamountgreaterthaneqaltolesserthanequaltoi()
    elif reply=="FIND ENTRIES WITH SPECIFIC AMOUNT":
        entrieswithamounti()
    elif reply=="FIND NUMBER OF ENTRIES WITH SPECIFIC AMOUNT":
        numberofentrieswithamounti()
    elif reply=="GO BACK":
        finddatai()
    elif reply=="EXIT":
        exitokari()
    
def finddatareasoni():
    choices = ["FIND ENTRIES WITH SPECIFIC REASON", "FIND NUMBER OF ENTRIES WIHT SPECIFIC REASON", "FIND DIFFERENT TYPES OF REASONS", "FIND NUMBER OF DIFFERENT TYPES OF REASONS", "GO BACK", "EXIT"]
    msg="SELECT"
    reply=choicebox(msg, choices = choices)
    if reply=="FIND ENTRIES WITH SPECIFIC REASON":
        entrieswithreasoni()
    elif reply=="FIND NUMBER OF ENTRIES WIHT SPECIFIC REASON":
        numberofentrieswithreasoni()
    elif reply=="FIND DIFFERENT TYPES OF REASONS":
        typesofreasonsi()
    elif reply=="FIND NUMBER OF DIFFERENT TYPES OF REASONS":
        numberoftypesofreasoni()
    elif reply=="GO BACK":
        finddatai()
    elif reply=="EXIT":
        exitokari()
def finddatadatei():
    choices=["FIND ENTREIS WITH A SPECIFIC DATE" ,"FIND ENTRIES BETWEEN TWO SPECIFIC DATE" ,"FIND ENTRIES AFTER A SPECIFIC DATE" ,"FIND ENTRIES BEFORE A SPECIFIC DATE","FIND ENTRIES ON AND BETWEEN TWO SPECIFIC DATES","FIND ENTRIES ON AND AFTER A SPECIFIC DATE","FIND ENTRIES ON AND BEFORE A SPECIFIC DATE","FIND NUMBER OF ENTRIES ON A SPECIFIC DATE","FIND NUMBER OF ENTRIES BETWEEN TWO SPECIFIC DATES","FIND NUMBER OF ENTRIES ON AND BETWEEN TWO SPECIFIC DATES","FIND NUMBER OF ENTRIES AFTER A SPECIFIC DATE","FIND NUMBER OF ENTRIES ON AND AFTER A SPECIFIC DATE","FIND NUMBER OF ENTRIES BEFORE A SPECIFIC DATE", "FIND NUMBER OF ENTRIES ON AND BEFORE A SPECIFIC DATE" ,"GO BACK" ,"EXIT"]
    msg="SELECT"
    reply=choicebox(msg, choices = choices)
    if reply=="FIND ENTREIS WITH A SPECIFIC DATE":
        entriesbydatei()
    elif reply=="FIND ENTRIES BETWEEN TWO SPECIFIC DATE":
        entriesbetweentwodatesi()
    elif reply=="FIND ENTRIES AFTER A SPECIFIC DATE":
        entriesafteraspecificdatei()
    elif reply=="FIND ENTRIES BEFORE A SPECIFIC DATE":
        entriesbeforeaspecificdatei()
    elif reply=="FIND ENTRIES ON AND BETWEEN TWO SPECIFIC DATES":
        onbetweentwodatesi()
    elif reply=="FIND ENTRIES ON AND AFTER A SPECIFIC DATE":
        onaftersepcificdatei()
    elif reply=="FIND ENTRIES ON AND BEFORE A SPECIFIC DATE":
        onbeforespecificdatei()
    elif "FIND NUMBER OF ENTRIES ON A SPECIFIC DATE":
        numofentriesonaspecificdatei()
    elif reply=="FIND NUMBER OF ENTRIES BETWEEN TWO SPECIFIC DATES":
        numofentriesbetweentwospecificdatesi()
    elif reply=="FIND NUMBER OF ENTRIES ON AND BETWEEN TWO SPECIFIC DATES":
        numofentriesonandbetweentwodatesi()
    elif reply=="FIND NUMBER OF ENTRIES AFTER A SPECIFIC DATE":
        numberofentriesafteraspecificdatei()
    elif reply=="FIND NUMBER OF ENTRIES ON AND AFTER A SPECIFIC DATE":
        numberofentriesonafteraspecificdatei()
    elif reply=="FIND NUMBER OF ENTRIES BEFORE A SPECIFIC DATE":
        numberofentriesbeforeaspecificdatei()
    elif reply=="FIND NUMBER OF ENTRIES ON AND BEFORE A SPECIFIC DATE":
        numberofentriesonbeforeaspecificdatei()
    elif reply=="GO BACK":
        finddatai()
    elif reply=="EXIT":
        exitokari()
        
'''FINDDATANAMEAA'''
#Option1
def maxamountbypersoni():
    text = "ENTER THE NAME OF THE PERSON"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT MAX(amount) AS maximum FROM earnings WHERE name=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for i in result:
        maximum = i[0]
    message=maximum
    title="EARNINGS"
    output = msgbox(message, title)
    finddatanamei()

#Option2
def minamountbypersoni():
    text = "ENTER THE NAME OF THE PERSON"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT MIN(amount) AS minimum FROM earnings WHERE name=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for i in result:
        minimum= i[0]
    message=minimum
    title="EARNINGS"
    output = msgbox(message, title)
    finddatanamei()

#Option3
def sumamountbypersoni():
    text = "ENTER THE NAME OF THE PERSON"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT SUM(amount) AS sum FROM earnings WHERE name=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for i in result:
        sum=i[0]
    message=sum
    title="EARNINGS"
    output = msgbox(message, title)
    finddatanamei()

#Option4
def allentriesbyapersoni():
    text = "ENTER THE NAME OF THE PERSON"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM earnings WHERE name=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatanamei()

#Option5
def allentriesbyapersoninincreasingorderofamounti():
    text = "ENTER THE NAME OF THE PERSON"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT name,amount,reason,date FROM earnings WHERE name=%s ORDER BY amount"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatanamei()

#Option6
def allentriesbyapersonindecreasingorderofamounti():
    text = "ENTER THE NAME OF THE PERSON"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT name,amount,reason,date FROM earnings WHERE name=%s ORDER BY amount DESC"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatanamei()

#Option7
def numberofentriesbyapersoni():
    text = "ENTER THE NAME OF THE PERSON"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT COUNT(name) FROM earnings WHERE name=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    output = msgbox(message, title)
    finddatanamei()

#Option8
def namesofallpersonsi():
    sql="SELECT DISTINCT name FROM earnings"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatanamei()

'''FINDDATAAMOUNTBB'''

#Option1
def maxamounti():
    sql="SELECT MAX(amount) from earnings"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    output = msgbox(message, title)
    finddataamounti()

#Option2
def minamounti():
    sql="SELECT MIN(amount) from earnings"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    output = msgbox(message, title)
    finddataamounti()

#Option3
def entrymaxamounti():
    sql="SELECT*FROM earnings WHERE amount=(select max(amount) FROM earnings)"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamounti()

#Option4
def entryminamounti():
    sql="SELECT*FROM earnings WHERE amount=(select min(amount) FROM earnings)"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamounti()

#Option5
def entriesamountinincreasingorderi():
    sql="SELECT name, amount, reason, date FROM earnings ORDER BY amount"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamounti()

#Option6
def entriesamountindecreasingorderi():
    sql="SELECT name, amount, reason, date FROM earnings ORDER BY amount DESC"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamounti()
        
#Option7
def entriesamountgreateri():
    text = "ENTER THE GREATER THAN AMOUNT"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM earnings WHERE amount>%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamounti()

#Option8
def entriesamountlesseri():
    text = "ENTER THE LESSER THAN AMOUNT"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM earnings WHERE amount<%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamounti()

#Option9
def entiresamountgreaterthanequaltoi():
    text = "ENTER THE GREATER THAN EQUAL TO AMOUNT"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM earnings WHERE amount>=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamounti()

#Option10
def entriesamountlesserthanequaltoi():
    text = "ENTER THE LESSER THAN EQUAL TO AMOUNT"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM earnings WHERE amount<=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamounti()

#option11
def entriesamountgreaterthanlesserthani():
    text = "ENTER THE GREATER THAN AMOUNT"
    title="EARNINGS"
    a=enterbox(text, title)
    text = "ENTER THE LESSER THAN AMOUNT"
    title="EARNINGS"
    b=enterbox(text, title)
    sql="SELECT*FROM earnings WHERE amount>%s and amount<%s"
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamounti()

#Option12
def entriesamountgreaterthaneqaltolesserthanequaltoi():
    text = "ENTER THE GREATER THAN EQUAL TO AMOUNT"
    title="EARNINGS"
    a=enterbox(text, title)
    text = "ENTER THE LESSER THAN EQUAL TO AMOUNT"
    title="EARNINGS"
    b=enterbox(text, title)
    sql="SELECT*FROM earnings WHERE amount>=%s and amount<=%s"
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamounti()

#Option13
def entrieswithamounti():
    text = "ENTER THE AMOUNT"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM earnings WHERE amount=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamounti()

#Option14
def numberofentrieswithamounti():
    text = "ENTER THE AMOUNT"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT COUNT(amount) FROM earnings where amount=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    output = msgbox(message, title)
    finddataamounti()

'''FINDDATAREASONCC'''
#Option1
def entrieswithreasoni():
    text = "ENTER THE REASON"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM earnings WHERE reason=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatareasoni()

#Option2
def numberofentrieswithreasoni():
    text = "ENTER THE REASON"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT COUNT(reason) FROM earnings WHERE reason=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    output = msgbox(message, title)
    finddatareasoni()

#Option3
def typesofreasonsi():
    sql="SELECT DISTINCT (reason) FROM earnings"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatareasoni()

#Option4
def numberoftypesofreasoni():
    sql="SELECT COUNT(DISTINCT (reason)) FROM earnings"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    output = msgbox(message, title)
    finddatareasoni()

'''FINDDATADATEDD'''
#Option1
def entriesbydatei():
    text = "ENTER THE DATE"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM earnings WHERE date=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadatei()
#Option2
def entriesbetweentwodatesi():
    text = "ENTER THE STARTING DATE"
    title="EARNINGS"
    a=enterbox(text, title)
    
    text = "ENTER THE ENDING DATE"
    title="EARNINGS"
    b=enterbox(text, title)
    sql="SELECT*FROM earnings WHERE date BETWEEN %s and %s"
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadatei()

#Option3
def entriesafteraspecificdatei():
    text = "ENTER THE DATE"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM earnings WHERE date>%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadatei()

#Option4
def entriesbeforeaspecificdatei():
    text = "ENTER THE DATE"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM earnings WHERE date<%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadatei()
        
#Option5
def onbetweentwodatesi():
    text = "ENTER THE STARTING DATE"
    title="EARNINGS"
    a=enterbox(text, title)
    text = "ENTER THE ENDING DATE"
    title="EARNINGS"
    b=enterbox(text, title)
    sql="SELECT*FROM earnings WHERE date>=%s and date<=%s "
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadatei()

#Option6
def onaftersepcificdatei():
    text = "ENTER THE DATE"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM earnings WHERE date>=%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadatei()

#Option7
def onbeforespecificdatei():
    text = "ENTER THE STARTING DATE"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM earnings WHERE date<=%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadatei()

#Option8
def numofentriesonaspecificdatei():
    text = "ENTER THE DATE"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT COUNT(date)FROM earnings WHERE date=%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    output = msgbox(message, title)
    finddatadatei()

#Option9
def numofentriesbetweentwospecificdatesi():
    text = "ENTER THE STARTING DATE"
    title="EARNINGS"
    a=enterbox(text, title)
    text = "ENTER THE ENDING DATE"
    title="EARNINGS"
    b=enterbox(text, title)
    sql="SELECT COUNT(date)FROM earnings WHERE date BETWEEN %s and %s"
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    output = msgbox(message, title)
    finddatadatei()

#Option10
def numofentriesonandbetweentwodatesi():
    text = "ENTER THE STARTING DATE"
    title="EARNINGS"
    a=enterbox(text, title)
    text = "ENTER THE ENDING DATE"
    title="EARNINGS"
    b=enterbox(text, title)
    sql="SELECT COUNT(date )FROM earnings WHERE date>=%s and date<=%s"
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    output = msgbox(message, title)
    finddatadatei()

#Option11
def numberofentriesafteraspecificdatei():
    text = "ENTER THE DATE"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT COUNT(date)FROM earnings WHERE date>%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    output = msgbox(message, title)
    finddatadatei()

#Option12
def numberofentriesonafteraspecificdatei():
    text = "ENTER THE DATE"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT COUNT(date)FROM earnings WHERE date>=%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    output = msgbox(message, title)
    finddatadatei()

#Option13
def numberofentriesbeforeaspecificdatei():
    text = "ENTER THE DATE"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT COUNT(date)FROM earnings WHERE date<%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    output = msgbox(message, title)
    finddatadatei()

#Option14
def numberofentriesonbeforeaspecificdatei():
    text = "ENTER THE DATE"
    title="EARNINGS"
    a=enterbox(text, title)
    sql="SELECT COUNT(date)FROM earnings WHERE date<=%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    output = msgbox(message, title)
    finddatadatei()

'''SHOW DATA'''
def showdatai():
    cursor = mycon.cursor()
    cursor.execute("SELECT * FROM earnings")
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="EARNINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    optionsforexpen1i()

#SAVINGS#



'''START'''
def optionsforexpen1ii () :
    choices = ["ENTER DATA", "UPDATE DATA", "DELETE DATA", "FIND DATA", "SHOW DATA", "GO BACK", "EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)
    if reply=="ENTER DATA":
        enterdataii()
    elif reply=="UPDATE DATA":
        updatedataii()
    elif reply=="DELETE DATA":
        deletedataii()
    elif reply=="FIND DATA":
        finddataii()
    elif reply=="SHOW DATA":
        showdataii()
    elif reply=="GO BACK":
        okari()
    elif reply=="EXIT":
        exitokari() 

'''ENTERDATA'''
def enterdataii():
    
    text = "ENTER THE NAME OF THE ENTRY"
    title="SAVINGS"
    a=enterbox(text, title)
    
    text = "ENTER THE AMOUNT OF THE ENTRY"
    title="SAVINGS"
    b=enterbox(text, title)
    
    text = "ENTER THE REASON OF THE ENTRY"
    title="SAVINGS"
    c=enterbox(text, title)
    
    text = "ENTER THE DATE OF THE ENTRY"
    title="SAVINGS"
    d=enterbox(text, title)
    
    sql = "INSERT INTO SAVINGS(name, amount, reason, date) VALUES (%s, %s, %s,%s)"
    val= [a, b, c, d]
    cursor.execute(sql,val)
    mycon.commit ()
    optionsforexpen1ii()


'''UPDATE DATA'''
def updatedataii():
    choices = ["NAME", "AMOUNT", "REASON", "DATE", "GO BACK", "EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)
    if reply=="NAME":
        nameii()
    elif reply=="AMOUNT":
        amountii()
    elif reply=="REASON":
        reasonii()
    elif reply=="DATE":
        dateii()
    elif reply=="GO BACK":
        optionsforexpen1ii()
    elif reply=="EXIT":
        exitokari()
        
def nameii():
    text = "ENTER THE NAME TO BE UPDATED"
    title="SAVINGS"
    a=enterbox(text, title)
    
    text = "ENTER THE AMOUNT OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="SAVINGS"
    b=enterbox(text, title)
    
    text = "ENTER THE REASON OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="SAVINGS"
    c=enterbox(text, title)
    
    text = "ENTER THE DATE OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="SAVINGS"
    d=enterbox(text, title)
    sql = "UPDATE SAVINGS SET name =%s WHERE amount=%s AND reason =%s AND date=%s"
    cursor.execute(sql, (a, b,c,d)) 
    mycon.commit()
    updatedataii()

def amountii():
   text = "ENTER THE AMOUNT TO BE UPDATED"
   title="SAVINGS"
   a=enterbox(text, title)
   
   text = "ENTER THE NAME OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
   title="SAVINGS"
   b=enterbox(text, title)
   
   text = "ENTER THE REASON OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
   title="SAVINGS"
   c=enterbox(text, title)
   
   text = "ENTER THE DATE OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
   title="SAVINGS"
   d=enterbox(text, title)
   sql = "UPDATE SAVINGS SET amount =%s WHERE name=%s AND reason =%s AND date=%s"
   cursor.execute(sql, (a, b,c,d)) 
   mycon.commit()
   updatedataii()

def reasonii():
    text = "ENTER THE REASON TO BE UPDATED"
    title="SAVINGS"
    a=enterbox(text, title)
    
    text = "ENTER THE NAME OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="SAVINGS"
    b=enterbox(text, title)
    
    text = "ENTER THE AMOUNT OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="SAVINGS"
    c=enterbox(text, title)
    
    text = "ENTER THE DATE OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="SAVINGS"
    d=enterbox(text, title)

    sql = "UPDATE SAVINGS SET reason =%s WHERE name=%s AND amount =%s AND date=%s"
    cursor.execute(sql, (a, b,c,d)) 
    mycon.commit()
    updatedataii()
    
def dateii():
    text = "ENTER THE DATE TO BE UPDATED"
    title="SAVINGS"
    a=enterbox(text, title)
    
    text = "ENTER THE NAME OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="SAVINGS"
    b=enterbox(text, title)
    
    text = "ENTER THE AMOUNT OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="SAVINGS"
    c=enterbox(text, title)
    
    text = "ENTER THE REASON OF THE ENTRY WHERE YOU WANT TO UPDATE THE NAME"
    title="SAVINGS"
    d=enterbox(text, title)
    sql = "UPDATE SAVINGS SET date =%s WHERE name=%s AND amount =%s AND reason=%s"
    cursor.execute(sql, (a, b,c,d)) 
    mycon.commit()
    updatedataii()

'''DELETE DATA'''
def deletedataii():
    choices = ["DELETE A ENTRY", "DELETE ENTRIES WITH SPECIFIC NAME", "DELETE ENTRIES WITH SPECIFIC AMOUNT", "DELETE ENTRIES WITH SPECIFIC REASON", "DELETE ENTRIES WITH SPECIFIC DATE", "GO BACK","EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)

    if reply=="DELETE A ENTRY":
        aaoneii()
    elif reply=="DELETE ENTRIES WITH SPECIFIC NAME":
        aatwoii()
    elif reply=="DELETE ENTRIES WITH SPECIFIC AMOUNT":
        aathreeii()
    elif reply=="DELETE ENTRIES WITH SPECIFIC REASON":
        aafourii()
    elif reply=="DELETE ENTRIES WITH SPECIFIC DATE":
        aafiveii()
    elif reply=="DELETE ALL ENTRIES":
        aasixii()
    elif reply=="GO BACK":
        optionsforexpen1ii()
    elif reply=="EXIT":
        exitokari()
def aaoneii():
    text = "ENTER THE NAME OF THE ENTRY"
    title="SAVINGS"
    a=enterbox(text, title)
    text = "ENTER THE AMOUNT OF THE ENTRY"
    title="SAVINGS"
    b=enterbox(text, title)
    text = "ENTER THE REASON OF THE ENTRY"
    title="SAVINGS"
    c=enterbox(text, title)
    text = "ENTER THE DATE OF THE ENTRY"
    title="SAVINGS"
    d=enterbox(text, title)
    sql = "DELETE FROM SAVINGS WHERE name =%s AND amount=%s AND reason =%s AND date=%s "
    cursor.execute(sql, [a, b,c,d])
    mycon.commit()
    deletedataii()

def aatwoii():
    text = "ENTER THE NAMEs OF THE ENTRIES TO BE DELETEDY"
    title="SAVINGS"
    a=enterbox(text, title)
    sql = "DELETE FROM SAVINGS WHERE name=%s"
    cursor.execute(sql,[a])
    mycon.commit()
    deletedataii()

def aathreeii():
    text = "ENTER THE AMOUNT OF THE ENTRIES TO BE DELETED"
    title="SAVINGS"
    a=enterbox(text, title)
    sql = "DELETE FROM SAVINGS WHERE amount=%s"
    cursor.execute(sql,[a])
    mycon.commit()
    deletedataii()

def aafourii():
    text = "ENTER THE REASON OF THE ENTRIES TO BE DELETED"
    title="SAVINGS"
    a=enterbox(text, title)
    sql = "DELETE FROM SAVINGS WHERE reason=%s"
    cursor.execute(sql,[a])
    mycon.commit()
    deletedataii()

def aafiveii():
    text = "ENTER THE DATE OF THE ENTRIES TO BE DELETED"
    title="SAVINGS"
    a=enterbox(text, title)
    sql = "DELETE FROM SAVINGS WHERE date=%s"
    cursor.execute(sql,[a])
    mycon.commit()
    deletedataii()
    
def aasixii():
    sql = "DELETE FROM savings"
    cursor.execute(sql)
    mycon.commit()
    deletedata()
'''FIND DATA'''

def finddataii():
    choices = ["FIND A ENTRIES REALTED TO NAME", "FIND ENTRIES RELATED TO AMOUNT", "FIND ENTRIES RELATED TO A REASON", "FIND ENTRIES RELATED TO A DATE", "GO BACK", "EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)
    if reply=="FIND A ENTRIES REALTED TO NAME":
        finddatanameii()
    elif reply=="FIND ENTRIES RELATED TO AMOUNT":
        finddataamountii()
    elif reply=="FIND ENTRIES RELATED TO A REASON":
        finddatareasonii()
    elif reply=="FIND ENTRIES RELATED TO A DATE":
        finddatadateii()
    elif reply=="GO BACK":
        optionsforexpen1ii()
    elif reply=="EXIT":
        exitokari()

def finddatanameii():
    choices = ["FIND MAXIMUM SAVINGS BY A PERSON", "FIND MINIMUM AMOUNT BY A PERSON", "FIND TOTAL SAVINGS BY A PERSON", "FIND ALL ENTRIES BY A PERSON", "FIND ALL ENTRIES BY A PERSON IN INCREASING ORDER", "FIND ALL ENTRIES BY A PERSON IN DECREASING ORDER", "FIND NUMBER OF SAVINGSS BY A PERSON", "FIND NAMES OF ALL PEOPLE", "FIND SAVINGS OF A PERSON BY COMPARING EXPENDITURE AND EARNINGS","GO BACK", "EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)
    if reply=="FIND MAXIMUM SAVINGS BY A PERSON":
        maxamountbypersonii()
    elif reply=="FIND MINIMUM SAVINGS BY A PERSON":
        minamountbypersonii()
    elif reply=="FIND TOTAL SAVINGS BY A PERSON":
        sumamountbypersonii()
    elif reply=="FIND ALL ENTRIES BY A PERSON":
        allentriesbyapersonii()
    elif reply=="FIND ALL ENTRIES BY A PERSON IN INCREASING ORDER":
        allentriesbyapersoninincreasingorderofamountii()
    elif reply=="FIND ALL ENTRIES BY A PERSON IN INCREASING ORDER":
        allentriesbyapersonindecreasingorderofamountii()
    elif reply=="FIND NUMBER OF SAVINGSS BY A PERSON":
        numberofentriesbyapersonii()
    elif reply=="FIND NAMES OF ALL PEOPLE":
        namesofallpersonsii()
    elif reply=="FIND SAVINGS OF A PERSON BY COMPARING EXPENDITURE AND EARNINGS":
        checkforaperson()
    elif reply=="GO BACK":
        finddataii()
    elif reply=="EXIT":
        exitokari()
        
def finddataamountii():
    choices = ["FIND MAXIMUM AMOUNT", "FIND MINIMUM AMOUNT", "FIND ENTRY WITH MAXIMUM AMOUNT", "FIND ENTRY WITH MINIMUM AMOUNT", "FIND ENTRIES WITH AMOUNT IN INCREASING ORDER", "FIND ENTRIES WITH AMOUNT IN DECREASING ORDER", "FIND ENTRIES WITH AMOUNT GREATER THAN A SPECIFIC AMOUNT", "FIND ENTRIES WITH AMOUNT LESSER THAN A SPECIFIC AMOUNT", "FIND ENTRIES WITH AMOUNT GREATER THAN EQUAL TO A SPECIFIC AMOUNT", "FIND ENTRIES WITH AMOUNT LESSER THAN EQUAL TO A SPECIFIC AMOUNT", "FIND ENTIES WITH AMOUNT GREATER THAN AND LESSER THAN A SPECIFIC AMOUNT", "FIND ENTIES WITH AMOUNT GREATER THAN EQUAL TO AND LESSER THAN EQUAL TO A SPECIFIC AMOUNT", "FIND ENTRIES WITH SPECIFIC AMOUNT", "FIND NUMBER OF ENTRIES WITH SPECIFIC AMOUNT","GO BACK", "EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)

    if reply=="FIND MAXIMUM AMOUNT":
        maxamountii()
    elif reply=="FIND MINIMUM AMOUNT":
        minamountii()
    elif reply=="FIND ENTRY WITH MAXIMUM AMOUNT":
        entrymaxamountii()
    elif reply=="FIND ENTRY WITH MINIMUM AMOUNT":
        entryminamountii()
    elif reply=="FIND ENTRIES WITH AMOUNT IN INCREASING ORDER":
        entriesamountinincreasingorderii()
    elif reply=="FIND ENTRIES WITH AMOUNT IN DECREASING ORDER":
        entriesamountindecreasingorderii()
    elif reply=="FIND ENTRIES WITH AMOUNT GREATER THAN A SPECIFIC AMOUNT":
        entriesamountgreaterii()
    elif reply=="FIND ENTRIES WITH AMOUNT LESSER THAN A SPECIFIC AMOUNT":
        entriesamountlesserii()
    elif reply=="FIND ENTRIES WITH AMOUNT GREATER THAN EQUAL TO A SPECIFIC AMOUNT":
        entiresamountgreaterthanequaltoii()
    elif reply=="FIND ENTRIES WITH AMOUNT LESSER THAN EQUAL TO A SPECIFIC AMOUNT":
        entriesamountlesserthanequaltoii()
    elif reply=="FIND ENTIES WITH AMOUNT GREATER THAN AND LESSER THAN A SPECIFIC AMOUNT":
        entriesamountgreaterthanlesserthanii()
    elif reply=="FIND ENTIES WITH AMOUNT GREATER THAN EQUAL TO AND LESSER THAN EQUAL TO A SPECIFIC AMOUNT":
        entriesamountgreaterthaneqaltolesserthanequaltoii()
    elif reply=="FIND ENTRIES WITH SPECIFIC AMOUNT":
        entrieswithamountii()
    elif reply=="FIND NUMBER OF ENTRIES WITH SPECIFIC AMOUNT":
        numberofentrieswithamountii()
    elif reply=="GO BACK":
        finddataii()
    elif reply=="EXIT":
        exitokari()
    
def finddatareasonii():
    choices = ["FIND ENTRIES WITH SPECIFIC REASON", "FIND NUMBER OF ENTRIES WIHT SPECIFIC REASON", "FIND DIFFERENT TYPES OF REASONS", "FIND NUMBER OF DIFFERENT TYPES OF REASONS", "GO BACK", "EXIT"]
    msg = "SELECT"
    reply = choicebox(msg, choices = choices)
    if reply=="FIND ENTRIES WITH SPECIFIC REASON":
        entrieswithreasonii()
    elif reply=="FIND NUMBER OF ENTRIES WIHT SPECIFIC REASON":
        numberofentrieswithreasonii()
    elif reply=="FIND DIFFERENT TYPES OF REASONS":
        typesofreasonsii()
    elif reply=="FIND NUMBER OF DIFFERENT TYPES OF REASONS":
        numberoftypesofreasonii()
    elif reply=="GO BACK":
        finddatai()
    elif reply=="EXIT":
        exitokari()
def finddatadateii():
    choices=["FIND ENTREIS WITH A SPECIFIC DATE" ,"FIND ENTRIES BETWEEN TWO SPECIFIC DATE" ,"FIND ENTRIES AFTER A SPECIFIC DATE" ,"FIND ENTRIES BEFORE A SPECIFIC DATE","FIND ENTRIES ON AND BETWEEN TWO SPECIFIC DATES","FIND ENTRIES ON AND AFTER A SPECIFIC DATE","FIND ENTRIES ON AND BEFORE A SPECIFIC DATE","FIND NUMBER OF ENTRIES ON A SPECIFIC DATE","FIND NUMBER OF ENTRIES BETWEEN TWO SPECIFIC DATES","FIND NUMBER OF ENTRIES ON AND BETWEEN TWO SPECIFIC DATES","FIND NUMBER OF ENTRIES AFTER A SPECIFIC DATE","FIND NUMBER OF ENTRIES ON AND AFTER A SPECIFIC DATE","FIND NUMBER OF ENTRIES BEFORE A SPECIFIC DATE", "FIND NUMBER OF ENTRIES ON AND BEFORE A SPECIFIC DATE" ,"GO BACK" ,"EXIT"]
    msg="SELECT"
    reply=choicebox(msg, choices = choices)
    if reply=="FIND ENTREIS WITH A SPECIFIC DATE":
        entriesbydateii()
    elif reply=="FIND ENTRIES BETWEEN TWO SPECIFIC DATE":
        entriesbetweentwodatesii()
    elif reply=="FIND ENTRIES AFTER A SPECIFIC DATE":
        entriesafteraspecificdateii()
    elif reply=="FIND ENTRIES BEFORE A SPECIFIC DATE":
        entriesbeforeaspecificdateii()
    elif reply=="FIND ENTRIES ON AND BETWEEN TWO SPECIFIC DATES":
        onbetweentwodatesii()
    elif reply=="FIND ENTRIES ON AND AFTER A SPECIFIC DATE":
        onaftersepcificdateii()
    elif reply=="FIND ENTRIES ON AND BEFORE A SPECIFIC DATE":
        onbeforespecificdateii()
    elif "FIND NUMBER OF ENTRIES ON A SPECIFIC DATE":
        numofentriesonaspecificdateii()
    elif reply=="FIND NUMBER OF ENTRIES BETWEEN TWO SPECIFIC DATES":
        numofentriesbetweentwospecificdatesii()
    elif reply=="FIND NUMBER OF ENTRIES ON AND BETWEEN TWO SPECIFIC DATES":
        numofentriesonandbetweentwodatesii()
    elif reply=="FIND NUMBER OF ENTRIES AFTER A SPECIFIC DATE":
        numberofentriesafteraspecificdateii()
    elif reply=="FIND NUMBER OF ENTRIES ON AND AFTER A SPECIFIC DATE":
        numberofentriesonafteraspecificdateii()
    elif reply=="FIND NUMBER OF ENTRIES BEFORE A SPECIFIC DATE":
        numberofentriesbeforeaspecificdateii()
    elif reply=="FIND NUMBER OF ENTRIES ON AND BEFORE A SPECIFIC DATE":
        numberofentriesonbeforeaspecificdateii()
    elif reply=="GO BACK":
        finddataii()
    elif reply=="EXIT":
        exitokari()
        
'''FINDDATANAMEAA'''
#Option1
def maxamountbypersonii():
    text = "ENTER THE NAME OF THE PERSON"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT MAX(amount) AS maximum FROM SAVINGS WHERE name=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for i in result:
        maximum = i[0]
    message=maximum
    title="SAVINGS"
    output = msgbox(message, title)
    finddatanameii()

#Option2
def minamountbypersonii():
    text = "ENTER THE NAME OF THE PERSON"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT MIN(amount) AS minimum FROM SAVINGS WHERE name=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for i in result:
        minimum= i[0]
    message=minimum
    title="SAVINGS"
    output = msgbox(message, title)
    finddatanameii()

#Option3
def sumamountbypersonii():
    text = "ENTER THE NAME OF THE PERSON"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT SUM(amount) AS sum FROM SAVINGS WHERE name=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for i in result:
        sum=i[0]
    message=sum
    title="SAVINGS"
    output = msgbox(message, title)
    finddatanameii()

#Option4
def allentriesbyapersonii():
    text = "ENTER THE NAME OF THE PERSON"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM SAVINGS WHERE name=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatanameii()

#Option5
def allentriesbyapersoninincreasingorderofamountii():
    text = "ENTER THE NAME OF THE PERSON"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT name,amount,reason,date FROM SAVINGS WHERE name=%s ORDER BY amount"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatanameii()

#Option6
def allentriesbyapersonindecreasingorderofamountii():
    text = "ENTER THE NAME OF THE PERSON"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT name,amount,reason,date FROM SAVINGS WHERE name=%s ORDER BY amount DESC"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatanameii()

#Option7
def numberofentriesbyapersonii():
    text = "ENTER THE NAME OF THE PERSON"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT COUNT(name) FROM SAVINGS WHERE name=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    output = msgbox(message, title)
    finddatanameii()

#Option8
def namesofallpersonsii():
    sql="SELECT DISTINCT name FROM SAVINGS"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatanameii()
    
#option9
def checkforaperson():
    text = "ENTER THE NAME OF THE PERSON"
    title="SAVINGS"
    a=enterbox(text, title)
    sqlexpen="SELECT SUM(amount) AS sum FROM expenditure WHERE name=%s"
    cursor.execute(sqlexpen,[a])
    resultexpen=cursor.fetchall()
    for i in resultexpen:
        sumexpen=i[0]
    sqlinc="SELECT SUM(amount) AS sum FROM Earnings WHERE name=%s"
    cursor.execute(sqlinc,[a])
    resultinc = cursor.fetchall()
    for i in resultinc:
        suminc=i[0]
    result=suminc-sumexpen
    if result<0:
        message=" Expenditure was more than Earnings of the person"
        resultmessage=str(result)+message
        title ="SAVINGS"
        output = msgbox(resultmessage, title)
    elif result>0:
        message=" Earnings was more than Expenditure of the person"
        resultmessage=str(result)+message
        title ="SAVINGS"
        output = msgbox(resultmessage, title)
    elif result==0:
        message=" Expenditure and Earnings was same for the person"
        resultmessage=str(result)+message
        title ="SAVINGS"
        output = msgbox(resultmessage, title)
    finddatanameii()

'''FINDDATAAMOUNTBB'''

#Option1
def maxamountii():
    sql="SELECT MAX(amount) from SAVINGS"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    output = msgbox(message, title)
    finddataamountii()

#Option2
def minamountii():
    sql="SELECT MIN(amount) from SAVINGS"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    output = msgbox(message, title)
    finddataamountii()

#Option3
def entrymaxamountii():
    sql="SELECT*FROM SAVINGS WHERE amount=(select max(amount) FROM SAVINGS)"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamountii()

#Option4
def entryminamountii():
    sql="SELECT*FROM SAVINGS WHERE amount=(select min(amount) FROM SAVINGS)"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamountii()

#Option5
def entriesamountinincreasingorderii():
    sql="SELECT name, amount, reason, date FROM SAVINGS ORDER BY amount"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamountii()

#Option6
def entriesamountindecreasingorderii():
    sql="SELECT name, amount, reason, date FROM SAVINGS ORDER BY amount DESC"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamountii()
        
#Option7
def entriesamountgreaterii():
    text = "ENTER THE GREATER THAN AMOUNT"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM SAVINGS WHERE amount>%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamountii()

#Option8
def entriesamountlesserii():
    text = "ENTER THE LESSER THAN AMOUNT"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM SAVINGS WHERE amount<%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamountii()

#Option9
def entiresamountgreaterthanequaltoii():
    text = "ENTER THE GREATER THAN EQUAL TO AMOUNT"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM SAVINGS WHERE amount>=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamountii()

#Option10
def entriesamountlesserthanequaltoii():
    text = "ENTER THE LESSER THAN EQUAL TO AMOUNT"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM SAVINGS WHERE amount<=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamountii()

#option11
def entriesamountgreaterthanlesserthanii():
    text = "ENTER THE GREATER THAN AMOUNT"
    title="SAVINGS"
    a=enterbox(text, title)
    text = "ENTER THE LESSER THAN AMOUNT"
    title="SAVINGS"
    b=enterbox(text, title)
    sql="SELECT*FROM SAVINGS WHERE amount>%s and amount<%s"
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamountii()

#Option12
def entriesamountgreaterthaneqaltolesserthanequaltoii():
    text = "ENTER THE GREATER THAN EQUAL TO AMOUNT"
    title="SAVINGS"
    a=enterbox(text, title)
    text = "ENTER THE LESSER THAN EQUAL TO AMOUNT"
    title="SAVINGS"
    b=enterbox(text, title)
    sql="SELECT*FROM SAVINGS WHERE amount>=%s and amount<=%s"
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamountii()

#Option13
def entrieswithamountii():
    text = "ENTER THE AMOUNT"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM SAVINGS WHERE amount=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddataamountii()

#Option14
def numberofentrieswithamountii():
    text = "ENTER THE AMOUNT"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT COUNT(amount) FROM SAVINGS where amount=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    output = msgbox(message, title)
    finddataamountii()

'''FINDDATAREASONCC'''
#Option1
def entrieswithreasonii():
    text = "ENTER THE REASON"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM SAVINGS WHERE reason=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatareasonii()

#Option2
def numberofentrieswithreasonii():
    text = "ENTER THE REASON"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT COUNT(reason) FROM SAVINGS WHERE reason=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    output = msgbox(message, title)
    finddatareasonii()

#Option3
def typesofreasonsii():
    sql="SELECT DISTINCT (reason) FROM SAVINGS"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatareasonii()

#Option4
def numberoftypesofreasonii():
    sql="SELECT COUNT(DISTINCT (reason)) FROM SAVINGS"
    cursor.execute(sql)
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    output = msgbox(message, title)
    finddatareasonii()

'''FINDDATADATEDD'''
#Option1
def entriesbydateii():
    text = "ENTER THE DATE"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM SAVINGS WHERE date=%s"
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadateii()
#Option2
def entriesbetweentwodatesii():
    text = "ENTER THE STARTING DATE"
    title="SAVINGS"
    a=enterbox(text, title)
    text = "ENTER THE ENDING DATE"
    title="SAVINGS"
    b=enterbox(text, title)
    sql="SELECT*FROM SAVINGS WHERE date BETWEEN %s and %s"
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadateii()

#Option3
def entriesafteraspecificdateii():
    text = "ENTER THE DATE"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM SAVINGS WHERE date>%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadateii()

#Option4
def entriesbeforeaspecificdateii():
    text = "ENTER THE DATE"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM SAVINGS WHERE date<%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadateii()
        
#Option5
def onbetweentwodatesii():
    text = "ENTER THE STARTING DATE"
    title="SAVINGS"
    a=enterbox(text, title)
    text = "ENTER THE ENDING DATE"
    title="SAVINGS"
    b=enterbox(text, title)
    sql="SELECT*FROM SAVINGS WHERE date>=%s and date<=%s "
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadateii()

#Option6
def onaftersepcificdateii():
    text = "ENTER THE DATE"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM SAVINGS WHERE date>=%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadateii()

#Option7
def onbeforespecificdateii():
    text = "ENTER THE STARTING DATE"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT*FROM SAVINGS WHERE date<=%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    finddatadateii()

#Option8
def numofentriesonaspecificdateii():
    a=enterbox(text, title)
    text = "ENTER THE DATE"
    title="SAVINGS"
    sql="SELECT COUNT(date)FROM SAVINGS WHERE date=%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    output = msgbox(message, title)
    finddatadateii()

#Option9
def numofentriesbetweentwospecificdatesii():
    b=enterbox(text, title)
    text = "ENTER THE ENDING DATE"
    a=enterbox(text, title)
    text = "ENTER THE ENDING DATE"
    title="SAVINGS"
    b=enterbox(text, title)
    sql="SELECT COUNT(date)FROM SAVINGS WHERE date BETWEEN %s and %s"
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    output = msgbox(message, title)
    finddatadateii()

#Option10
def numofentriesonandbetweentwodatesii():
    text = "ENTER THE STARTING DATE"
    title="SAVINGS"
    a=enterbox(text, title)
    text = "ENTER THE ENDING DATE"
    title="SAVINGS"
    b=enterbox(text, title)
    sql="SELECT COUNT(date )FROM SAVINGS WHERE date>=%s and date<=%s"
    cursor.execute(sql,[a,b])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    output = msgbox(message, title)
    finddatadateii()

#Option11
def numberofentriesafteraspecificdateii():
    text = "ENTER THE DATE"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT COUNT(date)FROM SAVINGS WHERE date>%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    output = msgbox(message, title)
    finddatadateii()

#Option12
def numberofentriesonafteraspecificdateii():
    text = "ENTER THE DATE"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT COUNT(date)FROM SAVINGS WHERE date>=%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    output = msgbox(message, title)
    finddatadateii()

#Option13
def numberofentriesbeforeaspecificdateii():
    text = "ENTER THE DATE"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT COUNT(date)FROM SAVINGS WHERE date<%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    output = msgbox(message, title)
    finddatadateii()

#Option14
def numberofentriesonbeforeaspecificdateii():
    text = "ENTER THE DATE"
    title="SAVINGS"
    a=enterbox(text, title)
    sql="SELECT COUNT(date)FROM SAVINGS WHERE date<=%s "
    cursor.execute(sql,[a])
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    output = msgbox(message, title)
    finddatadateii()

'''SHOW DATA'''
def showdataii():
    cursor = mycon.cursor()
    cursor.execute("SELECT * FROM SAVINGS")
    result = cursor.fetchall()
    for message in [result]:
        print("")
    title="SAVINGS"
    final=tabulate(message)
    output = msgbox(final, title)
    optionsforexpen1ii()
    


okari()
