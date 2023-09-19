from django.shortcuts import render
from .forms import SqrtForm
def home(request):
    if request.POST.get("num"):
        num=float(request.POST.get("num"))
        if num >=0.0:
            ans=num**0.5
            ans=round(ans,2)
            msg="sqrt of "+str(num)+"="+str(ans)
            fm=SqrtForm()
            return render(request,"home.html",{"fm":fm,"msg":msg})
        else:
            msg="-ve number not allowed"
            fm=SqrtForm()
            return render(request,"home.html",{"fm":fm,"msg":msg})
    else:
        fm=SqrtForm()
        return render(request,"home.html",{"fm":fm})