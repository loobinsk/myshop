from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

@login_required
def office(request):
    return render(request, 'account/office.html', {'section': 'office'})

def register(request):
	message = ''
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
            # Create a new user object but avoid saving it yet
			new_user = user_form.save(commit=False)
            # Set the chosen password
			new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
			new_user.save()
			login(request, new_user)
			return redirect('office')
			print(user_form.errors)
		else:
			if user_form.errors == '<ul class="errorlist"><li>username<ul class="errorlist"><li>Пользователь с таким именем уже существует.</li></ul></li></ul>':
				message = 'Пользователь с таким именем уже существует.'
			else:
				message = 'возникла ошибка.'

	else:
		user_form = UserRegistrationForm()
	return render(request, 'account/register.html', {'user_form': user_form, 'message': message})