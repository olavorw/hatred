import os
import sys
import time

# List of Node.js-related commands to taunt
taunt_commands = ["node", "npm", "npx", "yarn"]

# Snarky responses for each command
taunts = {
    "node": [
        "Oh, you wanna run some JavaScript? Good luck not crashing.",
        "Node.js, huh? Are we still pretending this is a good idea?",
        "Sure, let's waste more CPU cycles on this garbage.",
    ],
    "npm": [
        "Installing packages again? How’s that dependency hell treating you?",
        "NPM: Nearly Painful Maintenance.",
        "Let me guess, another `node_modules` folder bigger than your SSD?",
    ],
    "npx": [
        "Running scripts with npx? Living dangerously, are we?",
        "npx: Not Particularly Xciting.",
        "Yeah, just download random crap from the internet. Great idea.",
    ],
    "yarn": [
        "Ah, Yarn. For when npm isn’t painful enough.",
        "Yarn? More like... ugh, why bother?",
        "Fancy a little package manager drama today?",
    ],
}

# Function to taunt the user
def taunt(command):
    for key in taunt_commands:
        if command.startswith(key):
            response = taunts[key][hash(command) % len(taunts[key])]
            print(f"🔥 {response}")
            log_shame(command)
            return
    print("👀 This program only taunts Node.js-related misery.")

# Log shameful Node.js usage
def log_shame(command):
    with open("node_shame_log.txt", "a") as log_file:
        log_file.write(f"{time.ctime()} - Command: {command}\n")

# Main function
def main():
    if len(sys.argv) < 2:
        print("🤷 No command to taunt. Try again, champ.")
        return

    # Join all arguments to form the command
    command = " ".join(sys.argv[1:])

    # Taunt and optionally allow execution
    taunt(command)
    execute_command = input("😈 Want me to actually run this crap? (y/n): ").lower()

    if execute_command == "y":
        os.system(command)
    else:
        print("💀 Fine. Saving you from yourself.")

if __name__ == "__main__":
    main()
