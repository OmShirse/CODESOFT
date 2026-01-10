import math
import re

def display_menu():
    """Display calculator menu"""
    print("\n" + "="*60)
    print("\n🔢 NUMBER OF INPUTS:")
    print("  1. Single Number Operations")
    print("  2. Two Numbers")
    print("  3. Multiple Numbers")
    print("  0. Exit")
    print("\n📊 OPERATIONS AVAILABLE:")
    print("  +   : Addition")
    print("  -   : Subtraction")
    print("  *   : Multiplication")
    print("  /   : Division")
    print("  %   : Modulus (Remainder)")
    print("  ^   : Power")
    print("  sqrt: Square Root")
    print("  sq  : Square (x²)")
    print("  log : Logarithm (base 10)")
    print("  ln  : Natural Logarithm")
    print("  sin : Sine (in degrees)")
    print("  cos : Cosine (in degrees)")
    print("  tan : Tangent (in degrees)")
    print("  !   : Factorial")
    print("  avg : Average of numbers")
    print("  max : Maximum of numbers")
    print("  min : Minimum of numbers")
    print("-"*60)

def get_numbers(choice):
    """Get numbers based on user choice"""
    numbers = []
    
    if choice == '1':
        # Single number
        while True:
            try:
                num = float(input("\nEnter a number: "))
                return [num]
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")
    
    elif choice == '2':
        # Two numbers
        while True:
            try:
                num1 = float(input("\nEnter first number: "))
                num2 = float(input("Enter second number: "))
                return [num1, num2]
            except ValueError:
                print("❌ Invalid input! Please enter valid numbers.")
    
    elif choice == '3':
        # Multiple numbers
        print("\nEnter multiple numbers (separated by space or comma):")
        while True:
            try:
                input_str = input("Numbers: ").strip()
                # Split by space or comma
                if ',' in input_str:
                    numbers = [float(x.strip()) for x in input_str.split(',')]
                else:
                    numbers = [float(x.strip()) for x in input_str.split()]
                
                if len(numbers) < 2:
                    print("❌ Please enter at least 2 numbers!")
                    continue
                
                return numbers
            except ValueError:
                print("❌ Invalid input! Please enter valid numbers separated by space or comma.")
    
    return numbers

def get_single_operation():
    """Get operation for single number"""
    single_ops = ['sqrt', 'sq', 'log', 'ln', 'sin', 'cos', 'tan', '!', 'abs', 'neg']
    
    print("\nSingle Number Operations:")
    print("  sqrt : Square Root")
    print("  sq   : Square (x²)")
    print("  log  : Logarithm (base 10)")
    print("  ln   : Natural Logarithm")
    print("  sin  : Sine")
    print("  cos  : Cosine")
    print("  tan  : Tangent")
    print("  !    : Factorial")
    print("  abs  : Absolute Value")
    print("  neg  : Negate (Change Sign)")
    
    while True:
        op = input("\nChoose operation: ").strip().lower()
        if op in single_ops:
            return op
        print("❌ Invalid operation! Please choose from the list above.")

def get_multi_operation():
    """Get operation for multiple numbers"""
    multi_ops = ['+', '-', '*', '/', 'avg', 'max', 'min']
    
    print("\nMultiple Number Operations:")
    print("  +   : Addition (sum)")
    print("  -   : Subtraction (sequential)")
    print("  *   : Multiplication (product)")
    print("  /   : Division (sequential)")
    print("  avg : Average")
    print("  max : Maximum")
    print("  min : Minimum")
    
    while True:
        op = input("\nChoose operation: ").strip().lower()
        if op in multi_ops:
            return op
        print("❌ Invalid operation! Please choose from the list above.")

def perform_single_operation(num, operation):
    """Perform operation on single number"""
    try:
        if operation == 'sqrt':
            if num < 0:
                return "❌ Error: Cannot calculate square root of negative number!"
            result = math.sqrt(num)
            return f"√{num} = {result}"
        
        elif operation == 'sq':
            result = num ** 2
            return f"{num}² = {result}"
        
        elif operation == 'log':
            if num <= 0:
                return "❌ Error: Logarithm undefined for non-positive numbers!"
            result = math.log10(num)
            return f"log₁₀({num}) = {result}"
        
        elif operation == 'ln':
            if num <= 0:
                return "❌ Error: Natural log undefined for non-positive numbers!"
            result = math.log(num)
            return f"ln({num}) = {result}"
        
        elif operation == 'sin':
            result = math.sin(math.radians(num))
            return f"sin({num}°) = {result:.6f}"
        
        elif operation == 'cos':
            result = math.cos(math.radians(num))
            return f"cos({num}°) = {result:.6f}"
        
        elif operation == 'tan':
            result = math.tan(math.radians(num))
            return f"tan({num}°) = {result:.6f}"
        
        elif operation == '!':
            if num < 0 or not num.is_integer():
                return "❌ Error: Factorial only defined for non-negative integers!"
            result = math.factorial(int(num))
            return f"{int(num)}! = {result}"
        
        elif operation == 'abs':
            result = abs(num)
            return f"|{num}| = {result}"
        
        elif operation == 'neg':
            result = -num
            return f"-({num}) = {result}"
    
    except Exception as e:
        return f"❌ Error: {str(e)}"

def perform_two_number_operation(num1, num2, operation):
    """Perform operation on two numbers"""
    try:
        if operation == '+':
            result = num1 + num2
            return f"{num1} + {num2} = {result}"
        
        elif operation == '-':
            result = num1 - num2
            return f"{num1} - {num2} = {result}"
        
        elif operation == '*':
            result = num1 * num2
            return f"{num1} × {num2} = {result}"
        
        elif operation == '/':
            if num2 == 0:
                return "❌ Error: Division by zero is not allowed!"
            result = num1 / num2
            return f"{num1} ÷ {num2} = {result}"
        
        elif operation == '%':
            if num2 == 0:
                return "❌ Error: Modulus by zero is not allowed!"
            result = num1 % num2
            return f"{num1} % {num2} = {result}"
        
        elif operation == '^':
            result = math.pow(num1, num2)
            return f"{num1}^{num2} = {result}"
    
    except Exception as e:
        return f"❌ Error: {str(e)}"

def perform_multi_operation(numbers, operation):
    """Perform operation on multiple numbers"""
    try:
        if operation == '+':
            result = sum(numbers)
            expr = " + ".join(map(str, numbers))
            return f"{expr} = {result}"
        
        elif operation == '-':
            result = numbers[0]
            expr = str(numbers[0])
            for num in numbers[1:]:
                result -= num
                expr += f" - {num}"
            return f"{expr} = {result}"
        
        elif operation == '*':
            result = 1
            for num in numbers:
                result *= num
            expr = " × ".join(map(str, numbers))
            return f"{expr} = {result}"
        
        elif operation == '/':
            result = numbers[0]
            expr = str(numbers[0])
            for num in numbers[1:]:
                if num == 0:
                    return "❌ Error: Division by zero is not allowed!"
                result /= num
                expr += f" ÷ {num}"
            return f"{expr} = {result:.6f}"
        
        elif operation == 'avg':
            result = sum(numbers) / len(numbers)
            expr = "avg(" + ", ".join(map(str, numbers)) + ")"
            return f"{expr} = {result}"
        
        elif operation == 'max':
            result = max(numbers)
            expr = "max(" + ", ".join(map(str, numbers)) + ")"
            return f"{expr} = {result}"
        
        elif operation == 'min':
            result = min(numbers)
            expr = "min(" + ", ".join(map(str, numbers)) + ")"
            return f"{expr} = {result}"
    
    except Exception as e:
        return f"❌ Error: {str(e)}"

def handle_expression_input():
    """Handle direct expression input (e.g., '2 + 3 * 4')"""
    print("\n📝 DIRECT EXPRESSION MODE")
    print("="*60)
    print("Enter mathematical expressions like:")
    print("  2 + 3")
    print("  4 * 5 + 2")
    print("  (2 + 3) * 4")
    print("  sqrt(25)")
    print("  sin(45)")
    print("\nSupported: +, -, *, /, ^, sqrt(), sin(), cos(), tan(), log(), ln()")
    print("-"*60)
    
    while True:
        expression = input("\nEnter expression (or 'back' to return): ").strip()
        
        if expression.lower() == 'back':
            return
        
        if not expression:
            continue
        
        try:
            # Replace common math functions
            expr = expression.lower()
            expr = expr.replace('^', '**')
            expr = expr.replace('sqrt', 'math.sqrt')
            expr = expr.replace('sin', 'math.sin')
            expr = expr.replace('cos', 'math.cos')
            expr = expr.replace('tan', 'math.tan')
            expr = expr.replace('log', 'math.log10')
            expr = expr.replace('ln', 'math.log')
            
            # Add radians conversion for trig functions
            expr = expr.replace('math.sin(', 'math.sin(math.radians(')
            expr = expr.replace('math.cos(', 'math.cos(math.radians(')
            expr = expr.replace('math.tan(', 'math.tan(math.radians(')
            
            # Evaluate the expression
            result = eval(expr, {"math": math, "__builtins__": {}})
            
            print(f"\n✅ {expression} = {result}")
            
            # Ask to continue
            again = input("\nAnother expression? (y/n): ").lower()
            if again != 'y':
                break
                
        except ZeroDivisionError:
            print("❌ Error: Division by zero!")
        except ValueError as e:
            print(f"❌ Math Error: {str(e)}")
        except Exception as e:
            print(f"❌ Error in expression: {str(e)}")

def main():
    """Main calculator function"""
    print("🧮 CALCULATOR ")
    print("="*60)
    
    history = []
    
    while True:
        try:
            display_menu()
            
            print("\n🎯 MODE SELECTION:")
            print("  1. Standard Calculator (select number of inputs)")
            print("  2. Direct Expression Mode (type full expressions)")
            print("  3. View History")
            print("  0. Exit")
            
            mode = input("\nSelect mode (0-3): ").strip()
            
            if mode == '0':
                print("\n👋 Thank you for using the calculator!")
                break
            
            elif mode == '1':
                # Standard calculator mode
                choice = input("\nHow many numbers? (1, 2, 3, or 0 to cancel): ").strip()
                
                if choice == '0':
                    continue
                
                if choice not in ['1', '2', '3']:
                    print("❌ Invalid choice! Please enter 1, 2, or 3.")
                    continue
                
                numbers = get_numbers(choice)
                
                if choice == '1':
                    operation = get_single_operation()
                    result = perform_single_operation(numbers[0], operation)
                
                elif choice == '2':
                    operation = get_multi_operation()
                    result = perform_two_number_operation(numbers[0], numbers[1], operation)
                
                else:  # choice == '3'
                    operation = get_multi_operation()
                    result = perform_multi_operation(numbers, operation)
                
                # Display result
                print("\n" + "="*60)
                print(f"📊 RESULT: {result}")
                print("="*60)
                
                # Add to history
                history.append(result)
            
            elif mode == '2':
                # Direct expression mode
                handle_expression_input()
            
            elif mode == '3':
                # View history
                if not history:
                    print("\nNo calculations in history.")
                else:
                    print("\n📜 CALCULATION HISTORY:")
                    print("="*60)
                    for i, calc in enumerate(history[-10:], 1):
                        print(f"{i}. {calc}")
                    print(f"\nTotal calculations: {len(history)}")
            
            else:
                print("❌ Invalid choice! Please enter 0-3.")
            
            # Ask to continue
            if mode != '0':
                cont = input("\nContinue with calculator? (y/n): ").lower()
                if cont != 'y':
                    print("\n👋 Thank you for using the calculator!")
                    break
        
        except KeyboardInterrupt:
            print("\n\n👋 Calculator stopped!")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
