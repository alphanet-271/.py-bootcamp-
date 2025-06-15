# This script logs user input into a file called log.txt

fileName = "log.txt"

print("Type something to log it. Type 'exit' to stop.")

while True:
    userInput = input("Enter text: ")

    if userInput.lower() == "exit":
        print("Logging stopped.")
        break

    with open(fileName, "a") as file:
        file.write(userInput + "\n")

    print("Saved to log.txt.")
