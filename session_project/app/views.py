from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.


# LOGIN VIEW

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        # SESSION CREATED HERE
        request.session['username'] = username

        print("SESSION DATA:")
        print(request.session.items())

        return redirect('dashboard')

    return render(request, 'login.html')


# DASHBOARD VIEW

def dashboard_view(request):

    username = request.session.get('username')

    # CHECK IF SESSION EXISTS
    if not username:
        return redirect('login')

    return HttpResponse(f'''
        <h1>Welcome {username}</h1>
        <a href="/logout/">Logout</a>
    ''')


# LOGOUT VIEW

def logout_view(request):

    # DESTROY SESSION
    request.session.flush()

    return redirect('login')