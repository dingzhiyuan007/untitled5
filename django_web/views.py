from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404,HttpResponseRedirect

# Create your views here.
def v1(request):
    return HttpResponse("nihao")

def v2_exp(request):
    raise Http404
    pass

def v3(request):
    return HttpResponseRedirect('/index/v4')

def v4(request):
    return HttpResponse('这是v3')

def v5(request):
    rst = ''
    for key,value in request.GET.items():
        rst += key + '-----' + value

    return HttpResponse(rst)

def v6(request):
    rst = ''
    print(request.POST)
    for key,value in request.POST.items():
        if key !='uhobby':
            rst += key + '-----' + value
            rst += ','
        else:
            list1 = request.POST.getlist('uhobby')
            print(list1)



    return HttpResponse(rst)

def v7(request):
    return render_to_response('web1.html')
    # return HttpResponse('a')