from django.shortcuts import render, redirect
from .models import Food, Consumer
from .forms import ItemForm
# Create your views here.

def index(request):
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consumer(user=user,food_consumed=consume)
        consume.save()
        foods = Food.objects.all() 
        
    else:
        foods = Food.objects.all() 
    consumed_food = Consumer.objects.filter(user=request.user)
    return render(request,'myapp/index.html',{'foods':foods,'consumed_food':consumed_food})

def delete_consume(request,id):
    consumed_food = Consumer.objects.get(pk=id)
    if request.method == "POST":
        consumed_food.delete()
        return redirect('/')
    return render(request,'myapp/delete.html')


def add_food(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'myapp/item-form.html',{'form':form})