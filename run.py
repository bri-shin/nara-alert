import sys
import os
from src.setup import setup_configuration
from main import main

def show_menu():
    print("\n🤖 dain_scraper")
    print("==============")
    print("1. Start scraper")
    print("2. Configure settings")
    print("3. Exit")
    
    choice = input("\nPlease select an option (1-3): ")
    return choice

def main_menu():
    while True:
        choice = show_menu()
        
        if choice == "1":
            print("\nStarting scraper...")
            main()
        elif choice == "2":
            setup_configuration()
        elif choice == "3":
            print("\nGoodbye! 👋")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    # Check if .env exists, if not, run setup
    if not os.path.exists('.env'):
        print("First-time setup detected!")
        setup_configuration()
    
    main_menu() 