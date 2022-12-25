from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

def index(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('users:dashboard')
  else:
    form = AuthenticationForm()
  context = {'form': form}
  return render(request, "pages/index.html", context)