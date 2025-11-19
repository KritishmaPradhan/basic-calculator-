# I MADE THIS FILE- KRITISHMA
from django.http import HttpResponse
from django.shortcuts import render

def index(self):
    return render(self, 'index.html')

def about(self):
    input_text1 = self.GET.get('number1')            # extracts number from the webpage
    input_text1a = float(input_text1)
    print(input_text1a)                                  # prints the number entered by user in webpage, in our terminal
    input_text2 = self.GET.get('number2')  
    input_text2a = float(input_text2)        
    print(input_text2)
    if self.method == 'GET':
        operation = self.GET.get('operation')
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

    inputs ={ 'num1' : input_text1a, 'num2' : input_text2a,  'results': result}                                                                       
    return render(self, 'about.html', inputs)

