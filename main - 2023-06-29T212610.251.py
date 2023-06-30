import time

def check_stress_level():
    # Simulated function to check stress level (you can replace this with your own logic)
    stress_level = input("On a scale of 1 to 10, how stressed do you feel right now? ")
    return int(stress_level)

def remind_to_relax():
    print("Your stress level is high. Take a break and engage in healthy activities for 30 minutes.")

def main():
    while True:
        stress_level = check_stress_level()

        if stress_level > 3:
            remind_to_relax()

        time.sleep(3600)  # Check stress level every hour

if __name__ == "__main__":
    main()
