from django.shortcuts import render # render will use for showing the html file on browser
from .models import Prime #Prime is models that is requre to import data to database from here
import datetime
def checkprime(x):  #it is function that check is it prime or not
    if x<=1:
        return 0
    else:
        for y in range(2,x):
            if x%y==0:
                return 0
        return 1


def index(request): #it is the index function when directory in main that function can run using urls in urls.py
    return render(request, 'index.html')
def calculate(request):
    if request.method == "POST":
        totalprime = ""
        a = request.POST.get('f_int','')
        b = request.POST.get('s_int','')
        try:         # we have use try except when we can not change into int and it is give error when type conversion str to int
            int(a)
            int(b)
        except ValueError:
            return render(request,'error.html') # when something is missing then run error.html
        c=int(a)
        d=int(b)
        timea = datetime.datetime.now()
        for i in range(c,d):
            if checkprime(i)==1:
                totalprime +=str(i) + "  "

        timeb = datetime.datetime.now()
        totaltime=(int(timeb.strftime("%H"))-int(timea.strftime("%H")))*60.0*60.0+(int(timeb.strftime("%M"))-int(timea.strftime("%M")))*60.0+(int(timeb.strftime("%S"))-int(timea.strftime("%S")))+(int(timeb.strftime("%f"))-int(timea.strftime("%f")))*0.000001
        timelaps = str(totaltime) #total time calculate using diffrence in starting time and ending time of this program
        contact = Prime(prime_f=a, prime_s=b, times=timea,timelaps=timelaps, totalprime=totalprime)
        contact.save()   #we have save the data in database
    else :
        return render(request, 'index.html')
    params = {'purpose': totalprime,'a':a,'b':b} #these parameters we have use to show the total prime no. in html page
    return render(request,'calculate.html',params)