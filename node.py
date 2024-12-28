import os
import sys
import time
import random

# List of Node.js-related commands to taunt
taunt_commands = ["node", "npm", "npx", "yarn"]

# Snarky responses for each command
taunts = {
    "node": [
        "Oh, another script? Let's see how fast it crashes.",
        "Running Node.js feels like running with scissors.",
        "Node.js: Now Openly Destroying Everything.",
    ],
    "npm": [
        "npm install? Adding another gigabyte to `node_modules`, huh?",
        "Dependency hell welcomes you back!",
        "NPM: Where security vulnerabilities go to party.",
    ],
    "npx": [
        "npx again? It's like npm but more pointless.",
        "Downloading random scripts from the internet. Bold move.",
        "Good luck with that, you chaotic mess.",
    ],
    "yarn": [
        "Yarn? Why not just tie a noose while you're at it?",
        "Ah, Yarn. Because you like pain, but fancy pain.",
        "Yarn: The hipster's npm. Still sucks.",
    ],
}

# Fake error messages
fake_errors = [
    "ERROR: Node.js has stopped working because it hates you too.",
    "FATAL: npm caused a memory leak in your soul.",
    "WARNING: Node.js detected and terminated for your safety.",
]

# Function to taunt the user
def taunt(command):
    for key in taunt_commands:
        if command.startswith(key):
            response = taunts[key][hash(command) % len(taunts[key])]
            print(f"🔥 {response}")
            log_shame(command)
            return True
    print("👀 This program only taunts Node.js-related misery.")
    return False

# Fake error generator
def throw_fake_error():
    if random.random() < 0.3:  # 30% chance of a fake error
        error = random.choice(fake_errors)
        print(f"💥 {error}")
        sys.exit(1)

# Log shameful Node.js usage
def log_shame(command):
    with open("node_shame_log.txt", "a") as log_file:
        log_file.write(f"{time.ctime()} - Command: {command}\n")

# Mock dependency size
def mock_node_modules_size():
    size = random.randint(200, 1000)  # Random size in MB
    print(f"📂 node_modules is now {size}MB. Bet your SSD loves that.")

# Main function
def main():
    if len(sys.argv) < 2:
        print("🤷 No command to taunt. Try again, champ.")
        return

    # Join all arguments to form the command
    command = " ".join(sys.argv[1:])

    # Taunt the user
    if taunt(command):
        mock_node_modules_size()
        throw_fake_error()

    # Ask if the user really wants to execute the command
    execute_command = input("😈 Do you *really* want to run this garbage? (y/n): ").lower()
    if execute_command == "y":
        start_time = time.time()
        os.system(command)
        uptime = time.time() - start_time
        print(f"✅ Done! That took {uptime:.2f}s. Too bad it’s still Node.js.")
    else:
        print("💀 Fine. Let’s pretend this never happened.")

if __name__ == "__main__":
    main()
