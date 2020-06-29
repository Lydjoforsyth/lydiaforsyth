from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if 'total_gold' not in request.session or 'activities' not in request.session:
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')

def process_money(request):
    if request.method == "POST":
        if request.POST['place'] == 'farm':
            gold = random.randint(10,21)
            request.session['activities'].append('You earned' + ' ' + str(gold) + ' ' + 'golds from the' + ' ' + request.POST['place'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['place'] == 'cave':
            gold = random.randint(5,11)
            request.session['activities'].append('You earned' + ' ' + str(gold) + ' ' + 'golds from the' + ' ' + request.POST['place'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['place'] =='house':
            gold = random.randint(2,6)
            request.session['activities'].append('You earned' + ' ' + str(gold) + ' ' + 'golds from the' + ' ' + request.POST['place'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['place'] == 'casino':
            gold = random.randint(-50,51)
            if gold >=0:
                request.session['activities'].append('Entered a casino and earned' + ' ' + str(gold) + ' ' + 'gold' + ' '+ '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
            else:
                request.session['activities'].append('Entered a casino and lost' + ' ' + str(gold) + ' ' + 'gold, yikes!' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        request.session['total_gold'] += gold

    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')



