import subprocess
import sys
import os
from colorama import init, Fore, Style

init(autoreset=True)

def print_color(text, color):
    print(color + text + Style.RESET_ALL)

def run_cmd(cmd, shell=True):
    print_color(f"> {cmd}", Fore.CYAN)
    result = subprocess.run(cmd, shell=shell)
    if result.returncode != 0:
        print_color("❌ Command failed. Exiting.", Fore.RED)
        sys.exit(1)

def main():
    # Check if python is in PATH (just a sanity check)
    try:
        subprocess.run(["python", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception:
        print_color("⚠️ Python is not installed or not in PATH.", Fore.RED)
        print_color("Please install Python from https://python.org and try again.", Fore.RED)
        input("Press Enter to exit...")
        sys.exit(1)

    print_color("🎯 Creating virtual environment...", Fore.GREEN)
    run_cmd("python -m venv tsp_env")

    # Path to python in venv
    venv_python = os.path.join("tsp_env", "Scripts", "python.exe")
    if not os.path.exists(venv_python):
        # On some systems the Scripts folder may be called bin
        venv_python = os.path.join("tsp_env", "bin", "python")

    print_color("⬇️ Installing/upgrading pip and dependencies...", Fore.YELLOW)
    run_cmd(f'"{venv_python}" -m pip install --upgrade pip')
    run_cmd(f'"{venv_python}" -m pip install -r requirements.txt')

    print_color("🚀 Running the TSP program...", Fore.GREEN)
    run_cmd(f'"{venv_python}" tsp_compare.py')

    print_color("✅ Done. Press Enter to exit.", Fore.CYAN)
    input()

if __name__ == "__main__":
    main()
