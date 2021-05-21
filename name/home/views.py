from django.shortcuts import render,HttpResponseRedirect
from home.models import formed,academy,stu_info,student_add,certi
from . forms import student_addform, student_academy

# Create your views here.
def index(request):
    return render(request,"index.html")
def logged(request):
        if request.method=='POST':
            Name=request.POST['Name']
            Contact=request.POST['Contact']
            email=request.POST['email']
            print(Name, Contact, email)
            Plogin=formed(Name=Name  , Contact=Contact , email=email)
            Plogin.save()
            print("Successfully Saved")
            return render(request,"plogin.html")
        else:
            return render(request,"plogin.html")

def data(request):
    return render(request,'viewdata.html')

def slogin(request):
    return render(request,"slogin.html")

def personalinfo(request):
    if request.method == 'POST':
        idNumber = request.POST['idNumber']
        roll = request.POST['roll']
        department = request.POST['department']  
        student_name = request.POST['student_name']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        last_name = request.POST['last_name']
        photo = request.POST['photo']
        sign = request.POST['sign']
        dob = request.POST['dob']
        student_email = request.POST['student_email']
        phone = request.POST['phone']
        completion_year = request.POST['completion_year']
        current_year = request.POST['current_year']
        address = request.POST['address']
        country = request.POST['country']
        state = request.POST['state']
        district = request.POST['district']
        email_mother = request.POST['email_maother']
        email_father = request.POST['email_father']
        number_father = request.POST['number_father']
        number_mother = request.POST['number_mother']
        designation_mother = request.POST['designation_mother']
        designation_father = request.POST['designation_father']
        personal = stu_info(idNumber = idNumber,roll = roll,department = department, student_name = student_name,father_name = father_name,mother_name = mother_name,last_name = last_name,photo = photo,
        sign = sign,dob = dob, student_email = student_email,phone = phone,completion_year = completion_year,current_year = current_year, address = address,country = country, state = state,district = district, email_mother =email_mother,
        email_father = email_father,number_father = number_father,number_mother = number_mother,designation_mother = designation_mother,designation_father = designation_father)
        personal.save() 
        return render(request,"succes.html")
    else:
        return render(request,'spersonalinfo.html')

def student_academics(request):
    if request.method == 'POST':
        am = student_academy(request.POST)
        if am.is_valid():
            cgpa = am.cleaned_data['cgpa'] 
            percentage = am.cleaned_data['percentage'] 
            subject1 = am.cleaned_data['subject1']
            subject2 = am.cleaned_data['subject2']
            subject3 = am.cleaned_data['subject3']
            subject4 = am.cleaned_data['subject4']
            subject5 = am.cleaned_data['subject5']
            kt = am.cleaned_data['kt']
            acc = academy( cgpa = cgpa ,percentage = percentage ,subject1= subject1,
            subject2= subject2,subject3= subject3,subject4= subject4,subject5= subject5,kt=kt)
            acc.save()    
            am = student_academy()
    else:
        am = student_academy()
    acad  = academy.objects.all()
    return render(request,"academics.html" , {'form':am , 'acad':acad})


def certifications(request):
    if request.method == 'POST':
        internship = request.POST['internship']
        course = request.POST['course']
        cer = certi(internship = internship , course = course)
        cer.save()
        return render(request, "certifications.html")
    else:
        return render(request,"certifications.html")

def proctor(request):
    return render(request,"proctor.html")

def succes(request):
    return render(request,"succes.html")

def pmain_base(request):
    return render(request,'pmain_base.html')

def pmain_add(request):
    if request.method == 'POST':
        fm = student_addform(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            number =fm.cleaned_data['number']
            reg = student_add(name = name , number = number)
            reg.save()
            fm = student_addform()
    else:
        fm = student_addform()
    stud = student_add.objects.all()
    return render(request,"pmain_add.html" , {'form':fm , 'stu':stud})

def search1(request):
    return render(request,"search1.html")

def chart2(request):
    return render(request,"chart2.html")

def delete_data(request,id):
    if request.method == 'POST':
        pi = student_add.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/pmain_add')

   #Update the student information 
def update_data(request,id):
    if request.method == 'POST':
        pi = student_add.objects.get(pk=id)
        fm = student_addform(request.POST , instance = pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = student_add.objects.get(pk=id)
        fm = student_addform(instance = pi)
    return render(request,'pmain_update.html',{'form':fm})