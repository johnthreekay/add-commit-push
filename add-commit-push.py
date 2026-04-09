import subprocess
import sys
import argparse


def run_command(command):
    """Prints the command, skips a line, and then prints the results of executing that command."""
    print(command)
    print()
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout + result.stderr
    print(output)
    return result


def main():
    parser = argparse.ArgumentParser(description="Git add, commit, and push in one step.")
    parser.add_argument("-m", type=str, default="Updated files", help="Commit message")
    parser.add_argument("-f", action="store_true", help="Force mode: skip confirmation prompt")
    args = parser.parse_args()

    message = args.m
    force = args.f

    # Print git status
    print("git status:")
    status_result = subprocess.run("git status", shell=True, capture_output=True, text=True)
    print(status_result.stdout + status_result.stderr)

    # Define the commands to run
    commands = [
        "git add .",
        f'git commit -m "{message}"',
        "git push",
    ]

    # Show queued commands
    print("The following commands will be executed:")
    for cmd in commands:
        print(f"  {cmd}")
    print()

    # Confirm unless force flag is set
    if not force:
        confirm = input("Proceed? (y/n): ").strip().lower()
        if confirm != "y":
            print("Aborted.")
            sys.exit(0)

    print()

    # Execute each command
    for cmd in commands:
        result = run_command(cmd)
        if result.returncode != 0:
            print(f"Command failed with exit code {result.returncode}. Stopping.")
            sys.exit(result.returncode)

    print("Done.")

# Come DIE!!!!!!!!!!!!!!
if __name__ == "__main__":
    main()
