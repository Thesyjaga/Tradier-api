import os
import subprocess

# Get the full path to the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the file
file_path = os.path.join(current_dir, "tradier.py")

# Open the file in read mode
with open(file_path, "r") as file:
    lines = file.readlines()

# Extract the dictionary content
data_line = lines[18]

# Extract the value corresponding to 'symbol' key
ticker = data_line.split("'symbol': '")[1].split("'")[0]

# Extract the value corresponding to 'side' key
side = data_line.split("'side': '")[1].split("'")[0]

# Extract the value corresponding to 'quantity' key
quantity = data_line.split("'quantity': '")[1].split("'")[0]

# Display the current ticker, side, and quantity
print("Current ticker:", ticker)
print("Current side:", side)
print("Current quantity:", quantity)

# Prompt the user to enter the new ticker
new_ticker = input("Enter the new ticker: ")

# Prompt the user to choose the side
new_side = input("Do you want to change the side to 'buy' or 'sell'? (buy/sell): ")

# Prompt the user to enter the quantity and validate if it's a number
while True:
    new_quantity = input("Enter the new quantity: ")
    if new_quantity.isdigit():
        break
    else:
        print("Invalid input. Quantity must be a number.")

# Update the data line with the new ticker, side, and quantity
new_data_line = "data={'class': 'equity', 'symbol': '" + new_ticker + "', 'side': '" + new_side + "', 'quantity': '" + new_quantity + "', 'type': 'market', 'duration': 'day'},\n"

# Update the lines list with the modified data line
lines[18] = new_data_line

# Open the file in write mode and write the modified contents
with open(file_path, "w") as file:
    file.writelines(lines)
    print("File updated successfully.")

# Ask for confirmation before proceeding with the changes
confirmation = input("Type 'confirm' to proceed with the changes: ")
if confirmation.lower() == "confirm":
    # Run the updated tradier.py
    subprocess.run(["python", file_path])
else:
    print("Changes were not confirmed. Exiting without running the script.")
