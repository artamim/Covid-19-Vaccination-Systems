from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import vaccination
# Create your views here.
def registration(request):
    if request.method == 'POST':
        nid=request.POST['nid']
        date=request.POST['date']
        phone=request.POST['phone']
        service=request.POST['service']
        extra1=request.POST['extra1']
        if service=="Military and paramilitary defence forces":
            vaccin=vaccination(NID_Number=nid,Birth_Date=date,Phone=phone,Service=service,Extra_Info=extra1)
            vaccin.save()
            print('user created')
            return redirect('/registration')
        else:
            vaccin=vaccination(NID_Number=nid,Birth_Date=date,Phone=phone,Service=service)
            vaccin.save()
            print('user created')
            return redirect('/registration')
    else:    
        return render(request,'registration.html')

def status(request):
    if request.method == 'POST':
        nid=request.POST['nid']
        date=request.POST['date']
        phone=request.POST['phone']

        if vaccination.objects.filter(NID_Number=nid).exists():
            if vaccination.objects.filter(Status=False):
                print('Your files are not ready yet')
                return redirect('/status')
            else:
                print('Your files are ready')
                return redirect('/status')  
        else:
            print('invalid credential')
            return redirect('/status')
    else:    
        return render(request,'status.html')



def certification(request):
    if request.method == 'POST':
        nid=request.POST['nid']
        date=request.POST['date']
        phone=request.POST['phone']
        
        if vaccination.objects.filter(NID_Number=nid).exists():
            vas=vaccination.objects.filter(NID_Number=nid)
            for va in vas:
                if va.Certificate_Status==0:
                    print('Your Certificate is not ready yet')
                    return redirect('/certification')
                else:
                    print('Your Certificate is ready')
                    return render(request, 'c_picture.html',{'picture':vas})  
        else:
            print('invalid credential')
            return redirect('/certification')
    else:    
        return render(request,'certification.html')

  


def vaccine_card(request):
    if request.method == 'POST':
        nid=request.POST['nid']
        date=request.POST['date']
        phone=request.POST['phone']
        
        if vaccination.objects.filter(NID_Number=nid).exists():
            vas=vaccination.objects.filter(NID_Number=nid)
            for va in vas:
                if va.VaccineCard_Status==0:
                    print('Your VaccineCard is not ready yet')
                    return redirect('/vaccine_card')
                else:
                    print('Your VaccineCard is ready')
                    return render(request, 'vc_picture.html',{'picture':vas})  
        else:
            print('invalid credential')
            return redirect('/vaccine_card')
    else:    
        return render(request,'vaccine_card.html') 


    
