# I MADE THIS FILE- KRITISHMA
from django.http import HttpResponse
from django.shortcuts import render
from calculateapp.models import userHistory

def index(request):
    return render(request, 'index.html')

def about(request):
    input_text1 = request.GET.get('number1')            # extracts number from the webpage
    input_text1a = float(input_text1)
    input_text2 = request.GET.get('number2')  
    input_text2a = float(input_text2)   
    username = request.GET.get('username', 'guest') 
    if request.method == 'GET':
        operation = request.GET.get('operation')
        # Perform the operation based on the button clicked
        if operation == 'addition':
            result = input_text1a + input_text2a
        elif operation == 'subtraction':
            result = input_text1a - input_text2a
        elif operation == 'multiplication':
            result = input_text1a * input_text2a
        elif operation == 'division':
            result = input_text1a / input_text2a
        elif operation == 'modular':
            result = input_text1a % input_text2a
        elif operation == 'concatinate':
            result = str(input_text1) +str(input_text2)
    userHistoryObj = userHistory(username = username, num1 = input_text1a, num2 = input_text2a, result= result)
    userHistoryObj.save()
    inputs ={ 'num1' : input_text1a, 'num2' : input_text2a,  'results': result}                                                                       
    return render(request, 'about.html', inputs)

