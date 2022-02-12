from django.shortcuts import render
from .forms import UserRegForm
from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home(request):
    form = UserRegForm()
    data = User.objects.all()
    return render(request, 'C:/Users/PC/Desktop/python proj/ajaxcrud/crud/crudajaxapp/templates/home.html',
                  {'form': form, 'data': data})

@csrf_exempt
def save_data(request):
    if request.method == "POST":
        form = UserRegForm(request.POST)
        print("SAVE VEIW FUNC")
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            usr = User(name=name, email=email, password=password)
            usr.save()
            return JsonResponse({'status': 'save'})
    else:
        return JsonResponse({'status': 0})
