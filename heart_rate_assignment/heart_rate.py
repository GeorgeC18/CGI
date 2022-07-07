from prettytable import PrettyTable

def karvonen_formula(age, resting_heart_rate):
    for i in range(55, 100, 5):
        # round was needed for the below formula to get the exact results as in the pdf
        rate = round(((220-age)-resting_heart_rate)*i/100) + resting_heart_rate 
        intensity = str(i) + "%"
        my_table.add_row([intensity, rate]) # populate the table

if __name__ == "__main__":
    
    # use a try-except to make sure that the input from the user is valid
    try:
        age = int(input("What is your age?\n"))
        resting_heart_rate = int(input("What is your resting heart rate?\n"))
        my_table = PrettyTable(["Intensity", "Rate"])
        karvonen_formula(age, resting_heart_rate)
        print(my_table)
    except ValueError: # if the input is not an integer, catch the exception
        print("Invalid input! This is not an integer!")