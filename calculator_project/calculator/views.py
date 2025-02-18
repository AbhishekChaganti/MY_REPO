from django.shortcuts import render

def calculator_view(request):
    result = None

    if request.method == "POST":
        num1 = request.POST.get("num1")
        operation = request.POST.get("operation")
        num2 = request.POST.get("num2")

        if num1 and num2:
            try:
                num1 = float(num1)
                operation = chr(operation)
                num2 = float(num2)

                if operation == "+":
                    result = num1 + num2
                elif operation == "-":
                    result = num1 - num2
                elif operation == "x":
                    result = num1 * num2
                elif operation == "/":
                    result = num1 / num2 if num2 != 0 else "Cannot divide by zero"

            except ValueError:
                result = "Invalid input"

    return render(request, "calculator/calculator.html", {result})  # Ensure correct path
