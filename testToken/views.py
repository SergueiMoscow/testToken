from django.contrib.auth import login
from django.shortcuts import render, redirect

from testToken.backends import TokenBackend


def main(request):
    if request.GET.get('token'):
        token = request.GET.get('token')
        user = TokenBackend().authenticate(request=request, token=token, backend='bitza.backends.TokenBackend')
        if user is None:
            return render(request, 'app1/protected.html', {'error': 'Invalid token'})
        else:
            user.backend = 'bitza.backends.TokenBackend'
            print(f'Main: user before login(): {user.username}, id: {user.id}')
            login(request, user)
            print(f'Main: user after login(): {user.username}, id: {user.id}')
            # return redirect('protected1')
            return render(request, 'app1/protected.html', {'title': main, 'username': user.username, 'error': 'нет'})
    else:
        user = request.user
