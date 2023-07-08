from django.shortcuts import render


def protected(request):
    user = request.user
    context = {
        'title': 'Protected 1',
        'username': user.username
    }
    return render(request, 'app1/protected.html')
