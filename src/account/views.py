from django.shortcuts import render


def accountList(request):
    context= {

    }
    return render(request , 'account/accountList.html', context)


