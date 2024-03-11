from django.shortcuts import render, redirect
from crudapp.forms import StudentsForm
from crudapp.models import Students
def emp(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = StudentsForm()
    return render(request,'index.html',{'form':form})
def show(request):
    crudapps = Students.objects.all()
    return render(request,"show.html",{'crudapps':crudapps})
def edit(request, id):
    crudapp = Students.objects.get(id=id)
    return render(request,'edit.html', {'crudapp':crudapp})
def update(request, id):
    crudapp = Students.objects.get(id=id)
    form = StudentsForm(request.POST, instance = crudapp)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'crudapp': crudapp})
def destroy(request, id):
    employee = Students.objects.get(id=id)
    employee.delete()
    return redirect("/show")
