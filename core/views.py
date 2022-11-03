from django.http import JsonResponse
from django.shortcuts import render
from .forms import StudentForm
from .models import Student, Book, Records
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage


def Company(request):
    return render(request, 'core/company.html')


def file_upload(request):
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    email = request.POST.get("email")
    phone_number = request.POST.get("phone_number")
    file = request.FILES.get("file")

    print('First Name is',fname)

    fss = FileSystemStorage()
    filename = fss.save(file.name, file)
    url = fss.url(filename)
    print(file.name)

    a = Book(fname=fname, lname=lname, email=email, phone=phone_number, attachment=file)
    a.save()

    return JsonResponse({"status":1})


def tech(request):
    return render(request, 'core/tech.html')


def techAjax(request):
    if request.method == 'POST':
        a = request.POST.getlist('fn[]')
        b = request.POST.getlist('ln[]')
        c = request.POST.getlist('op[]')


        print('Fist name is',a);
        print('Last name is',b);
        print('Opinion is',c);

        if(len(a) == 1):
            a = Records(firstname=a[0], lastname=b[0], opinion=c[0])
            a.save()
            return JsonResponse({'status':1})
        else:
            for x,y,z in zip(a,b,c):
                a = Records(firstname=x, lastname=y, opinion=z)
                a.save()
            return JsonResponse({'status':1})
  


def motech(request):
    return render(request, 'core/motech.html')



def home(request):
    form = StudentForm()
    stu = Student.objects.all()
    context = {'form':form, 'stu':stu}
    return render(request, 'core/home.html', context)


#@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            course = request.POST['course']


            if(sid == ''):
                s = Student(name=name, email=email, course=course)
            else:
                s = Student(id=sid, name=name, email=email, course=course)         
            s.save()

            stud = Student.objects.values()
            print(stud)
            student_data = list(stud)
            return JsonResponse({'status':'Save', 'student_data':student_data})
        else:
            return JsonResponse({'status':0})    


def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        print(id)
        pi = Student.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        student = Student.objects.get(pk=id)
        student_data = {'id':student.id, 'name':student.name, 'email':student.email, 'course':student.course}
        return JsonResponse(student_data)







