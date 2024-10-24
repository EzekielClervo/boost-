import os
import random
import string
import requests
import time

# Color definitions
LIGHT_VIOLET = '\033[94m'
LIGHT_GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Function to generate a random key
def generate_random_key(length=16):
    characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    return ''.join(random.choice(characters) for _ in range(length))

# Function to fetch approved keys from GitHub
def fetch_approved_keys():
    url = "https://raw.githubusercontent.com/EzekielClervo/isaac/a9bc94eb702023f2f7054c0e81823b55c59927b5/Approval.txt"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text.strip().splitlines()  # Split lines into a list
    except requests.RequestException as e:
        print(f"{LIGHT_VIOLET}Error fetching approved keys: {e}{RESET}")
        return []

# Function to approve and save the key
def approve_and_save_key(key):
    approved_keys = fetch_approved_keys()
    
    if key in approved_keys:
        print(f"{LIGHT_GREEN}Generated Key: {key}{RESET}")
        print("Key is approved!")
        save_key(key)  # Save the key after approval
        print(f"{LIGHT_VIOLET}Key approved and saved!{RESET}")
        return True
    else:
        print(f"{LIGHT_VIOLET}Key is not approved.{RESET}")
        return False

# Function to save the key to a file
def save_key(key):
    key_file_path = '/sdcard/BOOSTINGTOOL/keys.txt'  # Adjust the path as needed
    with open(key_file_path, 'a') as key_file:
        key_file.write(key + '\n')  # Save the key

# Clear terminal function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Logo and overview function
def logo_and_overview(key=None):
    clear()  # Ensure terminal is cleared
    print(f"{CYAN}  BOOST TOOL LOGO  {RESET}")
    print(f"{CYAN}─── FRA ACCOUNTS ─── {RESET}")
    print(f"{LIGHT_GREEN}File path: /sdcard/BOOSTINGTOOL/fra.txt{RESET}")
    print(f"{CYAN}─── RPA ACCOUNTS ───{RESET}")
    print(f"{LIGHT_GREEN}File path: /sdcard/BOOSTINGTOOL/rpa.txt{RESET}")
    print(f"{CYAN}─── FRA PAGES ───{RESET}")
    print(f"{LIGHT_GREEN}File path: /sdcard/BOOSTINGTOOL/frapage.txt{RESET}")
    print(f"{CYAN}─── RPA PAGES ───{RESET}")
    print(f"{LIGHT_GREEN}File path: /sdcard/BOOSTINGTOOL/rpapage.txt{RESET}")
    
    # Display the generated key at the bottom
    if key:
        print(f"{LIGHT_VIOLET}Generated Key (for approval): {key}{RESET}")

# User agent function
def W_ueragnt():
    chrome_version = random.randint(80, 99)
    webkit_version = random.randint(500, 599)
    safari_version = random.randint(400, 499)
    windows_version = random.randint(8, 10)
    is_win64 = random.choice([True, False])
    if is_win64:
        return f'Mozilla/5.0 (Windows NT {windows_version}.0; Win64; x64) AppleWebKit/{webkit_version}.0 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/{safari_version}.0'
    else:
        return f'Mozilla/5.0 (Windows NT {windows_version}.0; WOW64) AppleWebKit/{webkit_version}.0 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/{safari_version}.0'

# Access token retrieval function
def get_access_token_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"{YELLOW}Path file not found. Creating file: {file_path}{RESET}")
        open(file_path, 'w').close()  # Create an empty file if it doesn't exist
        return []
    try:
        with open(file_path, 'r') as file:
            return file.read().strip().split('\n')
    except Exception as e:
        print(f"Error reading token file: {e}")
        return None

# Reaction function
def react():
    while True:
        logo_and_overview()  # Keep logo and overview
        print(f"{LIGHT_GREEN}──────────────────────────────{RESET}")
        print(f"{CYAN}CHOOSE FACEBOOK TO REACT:{RESET}")
        print(f"{CYAN}[1] YOUR FRA LIST{RESET}")
        print(f"{CYAN}[2] YOUR RPA LIST{RESET}")
        print(f"{CYAN}[3] YOUR FRA PAGES LIST{RESET}")
        print(f"{CYAN}[4] YOUR RPA PAGES LIST{RESET}")
        print(f"{CYAN}[0] RETURN TO MAIN MENU{RESET}")
        print(f"{LIGHT_GREEN}──────────────────────────────{RESET}")
        
        account_choose = input('Choose: ')
        
        # Choose the corresponding file based on user input
        if account_choose == '1':
            file_path = '/sdcard/BOOSTINGTOOL/fra.txt'
        elif account_choose == '2':
            file_path = '/sdcard/BOOSTINGTOOL/rpa.txt'
        elif account_choose == '3':
            file_path = '/sdcard/BOOSTINGTOOL/frapage.txt'
        elif account_choose == '4':
            file_path = '/sdcard/BOOSTINGTOOL/rpapage.txt'
        elif account_choose == '0':
            return  # Return to the main menu
        else:
            print(f"{LIGHT_VIOLET}Invalid Input!{RESET}")
            time.sleep(1.5)
            continue  # Restart the loop if invalid input

        # Get access tokens
        access_tokens = get_access_token_from_file(file_path)
        if access_tokens is None:
            return None

        clear()  # Clear terminal before entering Post ID
        logo_and_overview()  # Keep logo and overview
        post_id = input('Enter post ID (any type of post): ')  # Changed input format
        if not post_id:
            print(f"{LIGHT_VIOLET}Post ID cannot be empty.{RESET}")
            continue  # Go back to the main menu

        clear()  # Clear terminal before entering reaction type
        logo_and_overview()  # Keep logo and overview
        # Choose reaction type
        print(f"{CYAN}CHOOSE REACTION: {RESET}")
        print(f"{CYAN}[1] LIKE{RESET}")
        print(f"{CYAN}[2] LOVE{RESET}")
        print(f"{CYAN}[3] HAHA{RESET}")
        print(f"{CYAN}[4] WOW{RESET}")
        print(f"{CYAN}[5] ANGRY{RESET}")
        print(f"{CYAN}[6] SAD{RESET}")
        
        react_choice = input('Choose: ')
        reaction_types = {
            '1': 'LIKE',
            '2': 'LOVE',
            '3': 'HAHA',
            '4': 'WOW',
            '5': 'ANGRY',
            '6': 'SAD'
        }
        reaction_type = reaction_types.get(react_choice)
        if not reaction_type:
            print(f"{LIGHT_VIOLET}Invalid reaction choice.{RESET}")
            continue  # Go back to the main menu

        limit = int(input(f'Input quantity of reactions, limit is {len(access_tokens)}: '))
        
        if limit > len(access_tokens):
            print(f"{LIGHT_VIOLET}Error: The specified limit exceeds the number of available reactors.{RESET}")
            continue  # Go back to the main menu

        success_count = 0
        failure_count = 0
        for access_token in access_tokens[:limit]:
            auto_react = f'https://graph.facebook.com/{post_id}/reactions?type={reaction_type}&access_token={access_token}'
            headers_ = {
                'user-agent': W_ueragnt()
            }
            response = requests.post(auto_react, headers=headers_)
            
            if response.ok:
                print(f'{LIGHT_GREEN}( BOOST ) SUCCESS + {post_id}{RESET}')
                success_count += 1
            else:
                error_message = response.json().get('error', {}).get('message', 'Unknown error')
                print(f'{LIGHT_VIOLET}( BOOST ) FAILED + {post_id} | Error: {error_message}{RESET}')
                failure_count += 1

        print(f'{LIGHT_GREEN}TOTAL:{RESET}')
        print(f'Completed: {success_count}')
        print(f'Failed: {failure_count}')

        # Ask if user wants to put another link
        do_another = input("Do you want to put another post ID? (y/n): ")
        if do_another.lower() != 'y':
            break  # Exit the loop to return to the main menu

# Example usage
if __name__ == "__main__":
    # Generate a key and show the logo and overview
    generated_key = generate_random_key()
    logo_and_overview(generated_key)  # Display the key for approval
    approved = approve_and_save_key(generated_key)  # Check if the key is approved
    if approved:
        react()  # Proceed to the reaction function
