from django.shortcuts import render,HttpResponse,redirect
from messageapp.models import Msg

def create(request):
    print("requst is:",request.method)
    if request.method=="GET":

        return render(request,'create.html')
    else:
        n=request.POST['uname']
        mail=request.POST['umail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        #validation
        # insert data into the database
        m = Msg.objects.create(name=n, email=mail, mobile=mob, msg=msg)
        m.save()
              
        return redirect('/dashboard')

def delete(request,rid):
    m=Msg.objects.filter(id=rid)
    # print(m)
    m.delete()
    return redirect('/dashboard')

def edit(request,rid):
    if request.method=="GET":
        m=Msg.objects.filter(id=rid)
        print(m)
        context={}
        context['data']=m
        return render(request,'edit.html',context)
    else:
        upname=request.POST['uname']
        upmail=request.POST['umail']
        upmob=request.POST['mobile']
        upmsg=request.POST['msg']
        m=Msg.objects.filter(id=rid)
        m.update(name=upname,email=upmail,mobile=upmob,msg=upmsg)
        # return HttpResponse("data is fetch")
        # m=Msg.objects.get(id=rid)
        # m.name=upname
        # m.email=upmail
        # m.mobile=upmob
        # m.msg=upmsg
        # m.save()
        return redirect('/dashboard')

def dashboard(request):
    m = Msg.objects.all()
    # output = {'messages': messages}
    context={}
    context['data']=m
    return render(request, 'dashboard.html',context)
