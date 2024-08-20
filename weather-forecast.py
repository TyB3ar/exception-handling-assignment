'''
Task 1: Start 
Begin by asking the user to enter the temperature in Fahrenheit.

Task 2: Temperature Conversion 
Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

Use a try block to catch any potential errors during the conversion process. What happens if they type out "thirty" instead of doing 30?

Task 3: User Experience 
Implement an else block that prints the converted temperature in a user-friendly format. 

Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.
''' 


def temp_conversion(): 
    while True:
        try: 
            temp_input = input("Please enter the current temperature in Fahrenheit: ")  # start loop asking user to enter temp in F
            try: 
                num_temp = float(temp_input)
                temp_celsius = round(((num_temp - 32) * 5/9), 2)    # start by trying to convert input to a float, then converting that float from F to C 
            except Exception: 
                print("Unexcpected error occured. Temperature needs to be a number.")   # If any error occurs, print error message then continue to ask user to enter temp 
            else:
                print(f"{temp_input} degrees Fahrenheit is {temp_celsius} degrees Celsius.")  # else print message showing conversions 
        finally: 
            print("Thank you so much for using this weather forecast application. Have a nice day!")  
            break  # after all end with goodbye message, then break the loop 


temp_conversion() 