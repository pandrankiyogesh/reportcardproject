from django.shortcuts import render,redirect
from vege.models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q,Sum
from django.conf import settings
from django.core.mail import send_mail
def receipes(request):
    #to use frontend data to the backend we use the method post
    # to use backend data to the context we ust context={}
    if request.method=="POST":
       data=request.POST
       receipe=data.get('receipe_name')
       receipe_description=data.get('receipe_discription')
       receipe_image=request.FILES.get('receipe_image') #we have to access file data
       Recepe.objects.create(receipe=receipe,receipe_description=receipe_description,receipe_image=receipe_image)
       return redirect("/receipe/")
    
    queryset=Recepe.objects.all()

    data1=request.GET.get('search')
    if data1:
        queryset=queryset.filter(receipe__icontains=data1)

    context={'receipes':queryset}
    return render(request,'receipes.html',context)


def delete_receipe(request,id):
    #this id is very important we never name this is as (id) but automatic consideration by django like value parameter in input tag
    query=Recepe.objects.get(id=id)
    query.delete()
    return redirect("/receipe/")


def updating(request,id):
    query=Recepe.objects.get(id=id)
    context={'queryset':query}
    if request.method=="POST":
        #the get method is mainly due to the (name of the input box field)
        data=request.POST
        receipe=data.get('receipe_name')
        receipe_description=data.get('receipe_discription')
        receipe_image=request.FILES.get('receipe_image')
        query.receipe=receipe
        query.receipe_description=receipe_description
        query.receipe_image=receipe_image
        query.save()
        return redirect("/receipe/")

    return render(request,"update.html",context)

def login_page(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.info(request, "INVALID CREDENTIALS")
            return redirect("/login_page/")
        else:
            # Use the 'login' function correctly
            print("coreeectttttttt")
            print("User successfully logged in.")
            login(request,user) 
            return redirect("/cards")  # Redirect to the appropriate URL
    return render(request, 'login.html')

def log_out(request):
    print("FUck off")
    logout(request)
    return redirect("/login_page/")

def register_page(request):
    userlist=[]
    for i in range(len(User.objects.all())):
        userlist.append(User.objects.all()[i].username)
    if request.method=='POST':
        data=request.POST
        first_name=data.get('firstname')
        last_name=data.get('lastname')
        username=data.get('username')
        email=data.get('email')
        password=data.get('password')
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"already username exits")
            return redirect("/register_page/")
        user=User.objects.create(
             first_name=first_name,
             last_name=last_name,
             username=username,
             email=email
            )
        user.set_password(raw_password=password)
        user.save()
        messages.info(request,'account created successfully')
        return redirect('/register_page/')
    return render(request,"register.html")

@login_required(redirect_field_name='next',login_url="/login_page/")
def report_card(request):
    queryset=student.objects.all()
    if request.GET.get("search"):
        value=request.GET.get("search")
        queryset=student.objects.filter(student_name__icontains=value)
    paginator = Paginator(queryset, 10)  # Show 25 contacts per page.
    page_number = request.GET.get("page",1) #default 1st page
    page_obj = paginator.get_page(page_number)
    return render(request,"reportcard\card.html",context={'query':page_obj})


#page for seeing the marks
def marks_of_student(request,student_id):
    global ans,Rank,MarkList
    queryset=Subject_Marks.objects.filter(students__studentid__student_id=student_id)
    ans=0
    MarkList=[]
    for i in queryset:
        ans+=i.marks
        MarkList.append(i.marks)
    sonemail=queryset[0].students.student_email
    femail=queryset[0].students.father_email
    ids=studentId.objects.all()
    d={}
    for i in ids:
        marks_obj=Subject_Marks.objects.filter(students__studentid__student_id=i.student_id)
        total_marks=0
        passed_exam=True
        for j in marks_obj:
            #minimum marks for the of the semister is 20
            if j.marks<=20:
                passed_exam=False

        if passed_exam:
            for j in marks_obj:
                total_marks+=j.marks
            d[total_marks]=i.student_id
    rank=1
    keys=list(d.keys())
    values=list(d.values())
    sort_total=sorted(keys,reverse=True)
    d1={}
    for i in sort_total:
        d1[d[i]]=rank
        rank=rank+1
    finaldict={}

    for id in ids:
        if id.student_id not in values:
            finaldict[id.student_id]="No rank!! STATUS:FAILED"
        else:
            finaldict[id.student_id]="{} Rank||STATUS:PASSED".format(d1[id.student_id])
    Rank=finaldict[student_id]
    return render(request,"reportcard\marks.html",context={'query':queryset,'smail':sonemail,'id':student_id,'femail':femail,'S_marks':ans,'finaldict':finaldict[student_id]})


def sending(request,student_id,student_email,father_email):
    subject = 'MARKS'
    message = '''TOTAL MARKS: {} 
                 RANK: {}
                 INDIVIDUAL MARKS:
                 MATHS: {}
                 PHYSICS: {} 
                 COMPUTERS: {}
                 ENGLISH: {}
                 DSA: {}
                 PYTHON: {}'''.format(ans,Rank,MarkList[0],MarkList[1],MarkList[2],MarkList[3],MarkList[4],MarkList[5])
    from_email = 'yogeswararaopandranki@gmail.com'
    recipient_list = [student_email]
    send_mail(subject, message, from_email, recipient_list)
    return redirect("/marks_student/{}".format(student_id))

