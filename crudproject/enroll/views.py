from django.shortcuts import render,HttpResponseRedirect
from enroll.forms import s_registration
from enroll.models import User
# Create your views here.
# Add and Show Data

def add(req):
    if(req.method=='POST'):
        fm=s_registration(req.POST)
        if(fm.is_valid()):
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm=s_registration()
        

    else:
         fm=s_registration()
    stud=User.objects.all()
    return render(req,'add.html',{'form':fm,'stu':stud})

# delete
def delete(req,id):
    if(req.method=='POST'):
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

#update
def update(req,id):
    if req.method=='POST':
        pi=User.objects.get(pk=id)
        fm=s_registration(req.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=s_registration(instance=pi)
    return render(req,'update.html',{'form':fm})




    
