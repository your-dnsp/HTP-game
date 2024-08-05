import time #for the rate limiting feature
import random # for mini games

tarot_cards = {
    "The Fool": {"upright": "Beginnings, innocence, spontaneity, a free spirit", 
                 "reversed": "Holding back, recklessness, risk-taking"},
    "The Magician": {"upright": "Manifestation, resourcefulness, power, inspired action", 
                     "reversed": "Manipulation, poor planning, untapped talents"},
    "The High Priestess": {"upright": "Intuition, sacred knowledge, divine feminine, the subconscious mind", 
                           "reversed": "Secrets, disconnected from intuition, withdrawal and silence"},
    "The Empress": {"upright": "Femininity, beauty, nature, nurturing, abundance", 
                    "reversed": "Creative block, dependence on others"},
    "The Emperor": {"upright": "Authority, structure, control, fatherhood", 
                    "reversed": "Tyranny, rigidity, coldness"},
    "The Hierophant": {"upright": "Spiritual wisdom, religious beliefs, conformity, tradition, institutions", 
                       "reversed": "Personal beliefs, freedom, challenging the status quo"},
    "The Lovers": {"upright": "Love, harmony, relationships, values alignment, choices", 
                   "reversed": "Disharmony, imbalance, misalignment of values"},
    "The Chariot": {"upright": "Control, willpower, success, action, determination", 
                    "reversed": "Lack of control, lack of direction, aggression"},
    "Strength": {"upright": "Strength, courage, patience, control, compassion", 
                 "reversed": "Weakness, self-doubt, lack of self-discipline"},
    "The Hermit": {"upright": "Soul-searching, introspection, being alone, inner guidance", 
                   "reversed": "Isolation, loneliness, withdrawal"},
    "Wheel of Fortune": {"upright": "Good luck, karma, life cycles, destiny, a turning point", 
                         "reversed": "Bad luck, resistance to change, breaking cycles"},
    "Justice": {"upright": "Justice, fairness, truth, cause and effect, law", 
                "reversed": "Unfairness, lack of accountability, dishonesty"},
    "The Hanged Man": {"upright": "Pause, surrender, letting go, new perspectives", 
                       "reversed": "Delays, resistance, stalling, indecision"},
    "Death": {"upright": "Endings, change, transformation, transition", 
              "reversed": "Resistance to change, personal transformation, inner purging"},
    "Temperance": {"upright": "Balance, moderation, patience, purpose", 
                   "reversed": "Imbalance, excess, self-healing, re-alignment"},
    "The Devil": {"upright": "Shadow self, attachment, addiction, restriction, sexuality", 
                  "reversed": "Releasing limiting beliefs, exploring dark thoughts, detachment"},
    "The Tower": {"upright": "Sudden change, upheaval, chaos, revelation, awakening", 
                  "reversed": "Personal transformation, fear of change, averting disaster"},
    "The Star": {"upright": "Hope, faith, purpose, renewal, spirituality", 
                 "reversed": "Lack of faith, despair, self-trust, disconnection"},
    "The Moon": {"upright": "Illusion, fear, anxiety, subconscious, intuition", 
                 "reversed": "Release of fear, repressed emotion, inner confusion"},
    "The Sun": {"upright": "Positivity, fun, warmth, success, vitality", 
                "reversed": "Inner child, feeling down, overly optimistic"},
    "Judgement": {"upright": "Judgement, rebirth, inner calling, absolution", 
                  "reversed": "Self-doubt, inner critic, ignoring the call"},
}


# Define game locations
locations = {
    'home': {
        'description': 'You are in your hacker hideout at home, surrounded by computers and gadgets. Spot, your trusty black lab, is by your side.',
        'options': ['hack into system', 'check emails', 'go to the park', 'shake magic 8 ball','assess malware', 'read firewall logs',  'quit']
    },
    'park': {
        'description': 'You and Spot are at the park, enjoying some fresh air.',
        'options': ['play fetch with Spot', 'hack into public WiFi', 'play duck duck goose', 'use WiGLE', 'return home', 'quit']
    },
    'cybercafe': {
        'description': 'You have arrived at a shady cybercafe, where hackers gather.',
        'options': ['meet other hackers', 'hack into high-security server', 'play CTF', 'access server room', 'leave cafe', 'quit']
    },
    'server_room': {
        'description': 'You are inside a high-security server room. The target is in sight.',
        'options': ['hack into server', 'plant a network monitor', 'escape', 'quit']
    },
    'secret_room': {
        'description': 'You have discovered a secret room filled with hacking tools and a locked safe.',
        'options': ['try to open safe', 'read the book', 'return to cybercafe', 'quit']
    },
    'hackerspace': {
        'description': 'You are in a bustling hackerspace filled with fellow hackers and cutting-edge tech.',
        'options': ['fire up 3D printer', 'study in common area', 'hack into secure network', 'explore dark web','solder badge', 'play memory match game', 'leave hackerspace', 'quit']
    },
    'infosec_conference': {
        'description': 'You are at an Infosec conference, surrounded by cybersecurity experts and vendors.',
        'options': ['attend lecture', 'network with professionals', 'visit vendor booths', 'crack passwords','answer trivia', 'grab free swag', 'head back home', 'quit']
    },
    'bookstore': {
        'description': 'You are in a bookstore filled with hacking and cybersecurity books.',
        'options': ['buy hacking book', 'buy cybersecurity book', 'read magazines', 'leave bookstore', 'quit']
    },
    'technology_store': {
        'description': 'You are at a technology store with the latest gadgets and hacking tools.',
        'options': ['buy new laptop', 'purchase hacking tools', 'browse gadgets', 'exit store', 'quit']
    },
}

#New edition of locations to be opened after getting 7 hacking skill points
new_locations = {
    'arcade': {
        'description': 'You are at the arcade, surrounded by retro video games and flashing lights.',
        'options': ['play tetris', 'try the claw machine', 'play pinball', 'play cabinet game', 'play dance game', 'return home', 'quit']
    },
    'sticker_swap': {
        'description': 'You are at the sticker swap event, where hackers exchange their coolest stickers.',
        'options': ['trade stickers', 'admire sticker collection', 'give out swag', 'return home', 'quit']
    },
    'pool_party': {
        'description': 'Wow, you found the pool on the roof. Why are there so many furries here?',
        'options': ['swim in the pool', 'chat with hackers', 'put on sunscreen', 'tan', 'return home', 'quit']
    },
    'old_bar': {
        'description': 'Y\'s bar is dark and servers pub food. There\'s a gin and tonic waiting for you... except now you remember why you don\'t drink.',
        'options': ['order a drink', 'join conversation', 'get free hot dog', 'play jukebox', 'return home', 'quit']
    },
    'casino': {
        'description': 'The lights and sounds are almost overwhelming. Please with flashing giant necklaces are walking past. A kind worker offers you are free soda and popcorn. You decide to make yourself comfortable for now.',
        'options': ['play roulette', 'play blackjack', 'get loyalty card','visit tarot reader', 'return home', 'quit']
    },    
    'hotel': {
        'description': 'There\'s a racecar in the lobby, and there\'s a sign warning not to touch.',
        'options': ['touch the car', 'attend party', 'eat at buffet', 'attend lobbycom', 'return home', 'quit']
    }, 
    'dispensary':{
        'description': 'It feels like home. Everyone is super kind, and there\'s free and chips and salsa.',
        'options': ['buy candy', 'buy flower', 'chill in lounge', 'return home', 'quit']
    },
    'speakeasy':{
        'description': 'It\'s a dark tiki bar. The drinks are strong, and there\'s fantastic music playing. It smells like lavendar.',
        'options': ['gamble', 'order a drink', 'sit at bar', 'attend secret meeting', 'return to conference', 'quit']
    }
}
locations.update(new_locations)
 
# Initialize player's location and game state
current_location = 'home'
game_over = False
secret_room_discovered = False  # Track if the secret room has been discovered
secret_room_option_unlocked = False  # Track if the 'enter secret room' option is unlocked
hacking_skills = 0  # Track player's hacking skills
ctf_unlocked_locations = False  # CTF unlocks more locations
email_check_counter = 0

 
 
# Define the encoded message in the book
encoded_message = "QmUgc3VyZSB0byBkcmluayB5b3VyIE92YWx0aW5lIQo="
#--------
def draw_tarot_card():
    card_name = random.choice(list(tarot_cards.keys()))
    print("A force calls you to pull this card.")
    print(f"You drew: {card_name}")
    # Randomly choose upright or reversed
    meaning_type = random.choice(["upright", "reversed"])
    
    print(f"Meaning ({meaning_type.capitalize()}):", tarot_cards[card_name][meaning_type])


#---------
# Main game loop
while not game_over:
    print('-' * 40)
    print(locations[current_location]['description'])
    print('-' * 40)

    def play_duck_duck_goose():
        print('You join the circle of kids and start playing Duck, Duck, Goose!')
        players = ['Player1', 'Player2', 'Player3', 'Player4', 'Player5']  # You can customize the player names
        goose_index = 0

        while True:
            print(f'{players[goose_index]} says "Duck!"')
            choice = input('Type "Duck" to continue or "Goose" to chase the next player: ').strip().lower()

            if choice == 'goose':
                print(f'You chase {players[goose_index]} around the circle!')
                winner = random.choice(players)
                print(f'Congratulations, {winner} is the winner of Duck, Duck, Goose!')
                break

            goose_index = (goose_index + 1) % len(players)

#--------
# Function to shake the Magic 8 Ball
    def shake_magic_8_ball():
        print("You shake the Magic 8 Ball...")
        response_options = [
            "The answer is yes.",
            "Not at all.",
            "Maybe.",
            "Reconsider your options.",
            "Ask again later.",
            "Look inward."
        ]
        # Randomly select and print a response
        response = random.choice(response_options)
        print("The Magic 8 Ball says:", response)
#-------
#-------
    def sticker_swap_game(player_stickers):
        npcs = {
            "Alice": {"offer": "unicorn sticker", "wants": "cat sticker"},
            "Bob": {"offer": "dragon sticker", "wants": "dog sticker"},
            "Charlie": {"offer": "robot sticker", "wants": "rabbit sticker"},
            "Diana": {"offer": "space sticker", "wants": "Common Port sticker"},
            "Ethan": {"offer": "dinosaur sticker", "wants": "Trevor sticker"},
            "Fiona": {"offer": "pirate sticker", "wants": "Cyberpathogens sticker"},
            "Grace": {"offer": "wizard sticker", "wants": "Retro sticker"},
            "Henry": {"offer": "knight sticker", "wants": "Meme sticker"},
            "Ivy": {"offer": "fairy sticker", "wants": "Goon sticker"},
            "Jack": {"offer": "zombie sticker", "wants": "squirrel sticker"},
            # Add more NPCs if needed
        }

        print("Welcome to the Sticker Swap Mini-Game!")
        print("Type 'quit' to exit the game at any time.")
        print("Your current stickers:", ", ".join(player_stickers))
        
        for npc, trade in npcs.items():
            print(f"{npc} wants to trade their {trade['offer']} for your {trade['wants']}.")
            choice = input("Do you accept the trade? (yes/no/quit) ").strip().lower()

            if choice == 'quit':
                print("Exiting the sticker swap game...")
                break

            if choice == "yes" and trade["wants"] in player_stickers:
                player_stickers.remove(trade["wants"])
                player_stickers.append(trade["offer"])
                print(f"You traded with {npc} and got a {trade['offer']}.")
            elif choice == "no":
                print("Trade declined.")
            else:
                print(f"You don't have a {trade['wants']} to trade.")

        print("Your final sticker collection:", ", ".join(player_stickers))


#-------
    def create_deck():
        ports = {
            "22": "SSH",
            "80": "HTTP",
            "443": "HTTPS",
            "53": "DNS",
            "21": "FTP"
        }
        deck = list(ports.items()) + list(ports.items())
        random.shuffle(deck)
        return deck

    def print_board(deck, revealed):
        print("  " + " ".join(str(i) for i in range(1, len(deck) // 2 + 1)))
        for i in range(0, len(deck), 2):
            line = []
            for j in range(2):
                idx = i + j
                line.append(deck[idx][1] if revealed[idx] else "?")
            print(f"{i // 2 + 1} {' '.join(line)}")

    def get_choice(deck):
        while True:
            user_input = input("Enter your choice: ")

            if user_input.lower() == 'quit':
                return 'quit'

            try:
                choice = int(user_input)
                if 0 <= choice < len(deck) and not revealed[choice]:
                    return choice
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Invalid input, please enter a number.")

    def memory_match_game():
        deck = create_deck()
        revealed = [False] * len(deck)
        matches = 0

        while matches < len(deck) // 2:
            print_board(deck, revealed)
            print("Choose a card to flip (or type 'quit' to end the game):")
            choice1 = get_choice(deck)

            # Check if the user wants to quit
            if choice1 == 'quit':
                print("Exiting game...")
                break # break or return?

            revealed[choice1] = True
            print_board(deck, revealed)

            print("Choose another card to flip:")
            choice2 = get_choice(deck)

            # Check if the user wants to quit
            if choice2 == 'quit':
                print("Exiting game...")
                break # break or return?

            revealed[choice2] = True
            print_board(deck, revealed)

            if deck[choice1][0] == deck[choice2][0]:
                print("Match found!")
                matches += 1
            else:
                print("No match. Try again.")
                revealed[choice1] = False
                revealed[choice2] = False

            input("Press Enter to continue...")

        print("Congratulations! You've matched all the cards.")

#-------

    def play_malware_detection_game(hacking_skills):
        # Sample list of process names (including fake malware)
        processes = ['systemd', 'kthreadd', 'rcu_gp', 'rcu_par_gp', 'kworker/0:1H', 'mm_percpu_wq', 'ksoftirqd/0',
                     'rcu_sched', 'migration/0', 'idle_inject/0', 'cpuhp/0', 'cpuhp/1', 'watchdog/0', 'watchdog/1',
                     'kworker/0:0H-kblockd', 'evil_malware', 'suspicious_process', 'harmful_virus']

        # Randomly mix the list
        random.shuffle(processes)

        # Select a number of processes to display
        display_count = 10
        display_processes = processes[:display_count]

        print("\nMalware Detection Mini-Game")
        print("Identify the malware from the following processes:")
        for i, process in enumerate(display_processes, 1):
            print(f"{i}. {process}")

        print("\nEnter the suspected malware numbers, separated by commas (e.g., 1,3,5).")
        print("Type 'quit' to exit the mini-game.")

        while True:
            user_input = input("Your choice: ")
            if user_input.lower() == 'quit':
                break

            try:
                suspected_indices = [int(num.strip()) - 1 for num in user_input.split(',') if num.strip().isdigit()]
                malware = ['evil_malware', 'suspicious_process', 'harmful_virus']
                score = 0

                for index in suspected_indices:
                    if index < len(display_processes) and display_processes[index] in malware:
                        print(f"Correct! {display_processes[index]} is malware.")
                        score += 1
                    else:
                        print(f"Incorrect. {display_processes[index]} is not malware.")
                        score -= 1

                hacking_skills += score
                print(f"Your score: {score}")
                print(f"Updated hacking skills points: {hacking_skills}")
                break
            except ValueError:
                print("Invalid input, please try again.")

        return hacking_skills

#-------
    def play_sunscreen_game():
        print("You're about to put on sunscreen to protect yourself from the scorching sun.")
        print("Let's play a simple game of Rock, Paper, Scissors!")

        options = ["rock", "paper", "scissors"]
        while True:
            player_choice = input("Choose 'rock', 'paper', or 'scissors' (or 'quit' to exit): ").lower()

            if player_choice == 'quit':
                print("You decided to skip sunscreen and head indoors. Good choice!")
                return False

            if player_choice not in options:
                print("Invalid choice. Try again.")
                continue

            computer_choice = random.choice(options)

            print(f"You chose: {player_choice}")
            print(f"The stranger chose: {computer_choice}")

            if player_choice == computer_choice:
                print("It's a tie!")
            elif (player_choice == "rock" and computer_choice == "scissors") or \
                 (player_choice == "paper" and computer_choice == "rock") or \
                 (player_choice == "scissors" and computer_choice == "paper"):
                print("You win! You've successfully applied sunscreen and protected yourself.")
            else:
                print("The stranger uses all of your sunscreen...")

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break

        return True
#-------
    def deal_card(deck):
        return deck.pop()

    def calculate_hand_value(hand):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        value = sum(values[card] for card in hand)
        if 'A' in hand and value > 21:
            aces = hand.count('A')
            while aces > 0 and value > 21:
                value -= 10
                aces -= 1
        return value

    def play_blackjack():
        # Initialize deck
        deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        random.shuffle(deck)
        
        # Deal initial hands
        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]
        
        while True:
            # Player's turn
            player_value = calculate_hand_value(player_hand)
            print(f"Your hand: {', '.join(player_hand)} (Value: {player_value})")
            
            if player_value == 21:
                print("Blackjack! You win!")
                break
            elif player_value > 21:
                print("Bust! You lose.")
                break
            
            action = input("Do you want to 'hit' or 'stand'? ").lower()
            if action == 'hit':
                player_hand.append(deal_card(deck))
            elif action == 'stand':
                break
            else:
                print("Invalid choice. Try again.")
        
        # Dealer's turn
        while calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(deal_card(deck))
        
        # Determine the winner
        dealer_value = calculate_hand_value(dealer_hand)
        print(f"Dealer's hand: {', '.join(dealer_hand)} (Value: {dealer_value})")
        
        if dealer_value > 21 or player_value == 21 or (player_value <= 21 and player_value > dealer_value):
            print("You win!")
        elif dealer_value == player_value:
            print("It's a tie!")
        else:
            print("Dealer wins.")
        
        # Ask if the player wants to play another round
        play_again = input("Do you want to play another round? (yes/no) ").lower()
        return play_again == 'yes'

        # Main game loop
        while True:
            choice = input("Choose 'blackjack' to play blackjack or 'quit' to exit: ").lower()
            if choice == 'blackjack':
                if not play_blackjack():
                    break
            elif choice == 'quit':
                break
            else:
                print("Invalid choice. Try again.")

#-------
# Define the solder badge challenge
    def solder_badge_challenge():
        # Initialize player's score
        score = 0

        # Define different badge types with difficulty and point values
        badges = [
            {"name": "Beginner Badge", "difficulty": "Easy", "points": 10},
            {"name": "Intermediate Badge", "difficulty": "Moderate", "points": 20},
            {"name": "Advanced Badge", "difficulty": "Difficult", "points": 30}
        ]

        # Main game loop
        while True:
            print("\nWelcome to the Solder Badge Challenge!")
            print("Choose a badge to solder:")

            # Display available badge options
            for i, badge in enumerate(badges):
                print(f"{i + 1}. {badge['name']} ({badge['difficulty']} - {badge['points']} points)")

            # Player selects a badge
            choice = input("Enter the number of the badge you want to solder (or 'finish' to exit): ")

            if choice.lower() == 'finish':
                print(f"Your final score: {score} points")
                break

            try:
                choice = int(choice)
                if 1 <= choice <= len(badges):
                    selected_badge = badges[choice - 1]
                    print(f"Soldering {selected_badge['name']}...")

                    # Simulate the soldering process (for demonstration purposes)
                    success = random.choice([True, False])  # Random success or failure
                    if success:
                        print(f"You successfully soldered {selected_badge['name']}!")
                        score += selected_badge['points']
                    else:
                        print(f"Soldering {selected_badge['name']} failed. Try again!")

                    print(f"Your current score: {score} points. Great job!")
                else:
                    print("Invalid choice. Please enter a valid badge number.")
            except ValueError:
                print("Invalid input. Please enter a valid badge number or 'quit' to exit.")


#-------
    def password_cracking_challenge():
        passwords = [
            {"password": "123456", "hint": "A simple numeric sequence."},
            {"password": "password", "hint": "It's just the word for what it is."},
            {"password": "letmein", "hint": "A common plea for access."},
            {"password": "iloveyou", "hint": "A heartfelt declaration often used."},
            {"password": "god", "hint": "a popular short password from the movie Hackers."},
            {"password": "sunshine", "hint": "A warm, bright celestial body."},
            {"password": "princess", "hint": "Royalty, but not the queen."},
            {"password": "football", "hint": "A popular sport played with an oval ball."},
            {"password": "monkey", "hint": "A playful primate."},
            {"password": "charlie", "hint": "A common name, also a nickname for Charles."},
            {"password": "dragon", "hint": "A mythical fire-breathing creature."},
            {"password": "shadow", "hint": "It follows you in the light."},
            {"password": "swordfish", "hint": "The Marx brothers gain access to a speakeasy with this."},
            {"password": "superman", "hint": "A popular comic book hero known for his cape and 'S' logo."},
            {"password": "michael", "hint": "A common first name, shared by famous singers and athletes."},
            {"password": "cookie", "hint": "A sweet treat, often with chocolate chips."},
            # Add more passwords with hints here
        ]
        random.shuffle(passwords)
        
        for challenge in passwords:
            print("Hint: " + challenge["hint"])
            print("Type 'quit' to exit the mini-game.")
            user_guess = input("Enter the password: ").lower()

            if user_guess.lower() == 'quit':
                print("Exiting the Password Cracking Challenge.")
                return  # Exit the mini-game

            if user_guess == challenge["password"]:
                print("Correct! You've cracked the password.")
            else:
                print("Incorrect. The right password was:", challenge["password"])
            
            # Add scoring or educational notes here

        print("Challenge complete! You've learned about common password vulnerabilities.")

#-------
    def cybersecurity_trivia(hacking_skills):
        questions = {
            "What does 'VPN' stand for in cybersecurity?": "Private Network",
            "What is the name for a program that protects your computer from viruses?": "Antivirus",
            "Which type of hacking is performed with permission to find vulnerabilities?": "Ethical",
            "What term describes a fake website designed to steal user information?": "Phishing",
            "What is a strong method to authenticate a user's identity besides a password?": "Biometrics",
            "Which principle involves restricting user access to only what they need?": "Least Privilege",
            "What is the process of encoding information so only authorized parties can access it?": "Encryption",
            "What term describes a program that secretly records what you do on your computer?": "Spyware",
            "Which cyber attack involves sending fraudulent communication from a reputable source?": "Phishing",
            "What is the name of the secure protocol used to send emails?": "SMTP"
        }

        score = 0

        print("Welcome to the Cybersecurity Trivia Mini-Game!")
        print("Type 'quit' to exit the game at any time.")
        print("Please answer the following questions:")

        for question, correct_answer in questions.items():
            player_answer = input(question + " ").strip().capitalize()

            if player_answer.lower() == 'quit':
                print("Exiting the game...")
                break

            if player_answer == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {correct_answer}.")

        print(f"Your score for this round is {score}.")
        hacking_skills += score
        print(f"Your updated hacking skills score is {hacking_skills}.")

        return hacking_skills
#-------
    def firewall_log_game():
        print("Firewall Log Analysis Mini-Game")
        print("Identify the dangerous connections from the following log entries:")

        log_entries = [
        "1. Jun 15 18:23:45 - Incoming connection from 192.168.1.105 on port 22",
        "2. Jun 15 18:24:10 - Unauthorized access attempt from 203.0.113.76 on port 3389",
        "3. Jun 15 18:25:30 - Connection established from 10.0.0.5 to external host 198.51.100.2 on port 80",
        "4. Jun 15 18:26:00 - Failed login attempt from 192.0.2.10 on port 22",
        "5. Jun 15 18:27:15 - Data transfer initiated from 192.168.1.105 to 203.0.113.76 on port 21"
        ]

        for entry in log_entries:
            print(entry)

        dangerous_connections = {'2', '4'}  # Example set of dangerous connections
        
        while True:
            player_input = input("Enter the numbers of dangerous connections, separated by commas: ")
            try:
                player_guesses = set(player_input.split(','))
                break  # Exit the loop if input is successfully parsed
            except ValueError:
                print("Invalid input. Please enter the numbers separated by commas.")

        score = 0
        for guess in player_guesses:
            if guess.strip() in dangerous_connections:
                print(f"Correct! Log entry {guess} is dangerous.")
                score += 1
            else:
                print(f"Incorrect. Log entry {guess} is not dangerous.")
                score -= 1

        print(f"Your score: {score}")
        return score


#-------
#-------
    # Check if new options should be added to the home location
    if hacking_skills >= 7:
        # Define the new options to be added
        new_home_options = ['go to arcade', 'visit sticker swap', 'attend pool party', 'enter old bar', 'go to casino', 'stay at hotel']
        # Append new options if they are not already present
        for option in new_home_options:
            if option not in locations['home']['options']:
                locations['home']['options'].append(option)

    # Update the options list after potentially adding new options
    options = locations[current_location]['options'].copy()

    # Style and security features
    print('Options:', ', '.join(options))
    print("~" * 40)
    choice = input('What do you want to do? ').lower()
    print("Player's choice:", choice)  # Debug print
    print("~" * 40)  # Make a good line
 
    time.sleep(1.1) # Pause 1.1 seconds between inputs to help prevent against input flooding. The .1 is to annoy scripts.
 
    # Protect against long inputs
    if len(choice) >= 32:
        print("Input too long. Please try again. You're not trying to hack a hacking game are you?")
        continue
 
    # Check if the choice contains only alphanumeric characters and spaces
    if not choice.replace(" ", "").isalnum():
        print("Invalid choice. Please enter alphanumeric characters or spaces only. You\'re not up to any funny business, are you?")
        continue  # Skip the rest of the loop and ask for input again

    # Handle 'use cell phone' option
    if choice == 'use cell phone':
        print('You check infosec.exchange for news and updates on friends. Your poll is doing well.')
        
        # Start the mini-game
        print("Mini-game: Guess the correct number between 1 and 5 to earn a hacking skill point!")
        guess = input("Enter your guess: ")
        
        # Generate a random number between 1 and 5
        correct_number = random.randint(1, 5)

        # Simple guessing game logic
        if guess.isdigit() and 1 <= int(guess) <= 5:
            if int(guess) == correct_number:
                print(f"Congratulations! The correct number was {correct_number}. You guessed correctly.")
                hacking_skills += 1
                print(f"Your hacking skills are now at {hacking_skills}.")
            else:
                print(f"Sorry, the correct number was {correct_number}. Better luck next time!")
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

        continue  # Skip the rest of the loop and start from the beginning      
 
    # Quit choice
    if choice == 'quit':
        print(f'Thanks for hacking! Game over. Your hacking score is {hacking_skills}.')
        break

    # hidden check points for debugging
    if choice == 'points':
        print(f'Wow, your hacking score is {hacking_skills}.')
        continue 

    # emergency go home
    if choice == 'go home':
        print('You rush home to let out Spot.')
        current_location = 'home'
        continue

    # Set points to 69 immediately, for debugging purposes
    if choice == 'rosebud':
        print('I\'m manifesting all things good.')
        hacking_skills = 69
        continue       
    
    # Handle Easter egg responses first
    if choice == 'remington':
        print("Remmy is a good boy, thank you for asking.")
        continue

    if choice == 'weed' or choice == '420' or choice == 'zaza':
        current_location = 'dispensary'
        print('You prefer to shop in store here.')
        continue

    if choice == 'minigames':
        print("""\
The current minigames are: 
1- Tarot Card Reading in the casino
2- Duck Duck Goose in the park
3- Magic 8 ball at home
4- Rock Paper Scissors (sunscreen game) at the pool
5- Word Unscramble at the hotel buffet
6- The Cell Phone number guessing game
7- Blackjack at the casino
8- Badge soldering at the hackerspace 
9- Password Cracking Challenge at the infosec conference 
10- Memory match game at the hackerspace
11- Gambling at the hidden speakeasy
12 - Malware assessment at home
    """)
        continue

    if choice == 'help':
        print('Hi! Are you looking for help? if you\'re stuck in a location use the emergency \'go home\' option at any time.') 
        print('There are easter eggs and cheat codes to help troubleshoot issues, if you can find them.')
        print('Try: minigames, points, or credits for clues.')
        print(f'Your current hacker skills point score is {hacking_skills}')
        if hacking_skills >= 7:
            print('You have unlocked additional options in your house, if you have found the secret room.')
        elif hacking_skills < 7:
            print('You have a ways to go, you\'ve not yet unlocked all the options')
        print('If you are receiving invalid inputs, make sure you are only entering the options presented in each input with no commas.')
        print('You can report bugs to htpgame@pm.me')
        continue

    elif choice == 'credits':
        print("A silly hacker who made a silly game. Visit their bio (https://www.flowcode.com/page/dnsp)")
        continue
 
    elif choice == 'hack the planet':
        print("HACK THE PLANET!")
        continue
 
    elif choice == 'circlecitycon':
        print("You proudly wear your CircleCityCon badge.")  # Debugging print
        print("HACK THE PLANET!!")
        current_location = 'infosec_conference'
        continue
 
    # Main Game Content
    # Handling transitions based on the player's choice
    if ctf_unlocked_locations:
        if choice == 'go to hackerspace':
            current_location = 'hackerspace'
            continue
        elif choice == 'go to infosec conference':
            current_location = 'infosec_conference'
            continue
        elif choice == 'go to bookstore':
            current_location = 'bookstore'
            continue
        elif choice == 'visit technology store':
            current_location = 'technology_store'
            continue
        elif choice == 'go to casino':
            current_location = 'casino'
            continue
        elif choice == 'stay at hotel':
            current_location = 'hotel'
            continue

    #Debugging home transports


        # Handle the choices
        #HOME LOCAITON
    if current_location == 'home':
        if choice == 'hack into system':
            print('You successfully infiltrate a corporate system.')
            hacking_skills += 1
                # Check emails function
        elif choice == 'shake magic 8 ball':
            shake_magic_8_ball()
        # Inside the game loop, where the 'assess malware' option is handled
        # Inside the main game loop
        elif choice == 'play firewall log game':  # Assuming this is the option for the mini-game
            game_score = firewall_log_game()
            hacking_skills += game_score
            print(f"Your hacking skills are now at {hacking_skills}.")

        elif choice == 'assess malware':
            hacking_skills = play_malware_detection_game(hacking_skills)
        elif choice == 'read firewall logs':
            firewall_log_game()
        elif choice == 'check emails':
            print('You check your emails.')
            email_check_counter += 1 

            if email_check_counter == 1:
                # First time checking emails, unlock the secret room
                secret_room_discovered = True
                print("A secret room has been unlocked in your home!")
            if secret_room_discovered:
                # Add "enter secret room" option
                if "enter secret room" not in locations['home']['options']:
                    locations['home']['options'].append("enter secret room")

            if email_check_counter >= 2:
                print("You have no new email.")
                continue
        
        elif choice == 'enter secret room':
            current_location = 'secret_room'

        elif choice == 'go to arcade':
            current_location = 'arcade'
        elif choice == 'visit sticker swap':
            current_location = 'sticker_swap'
        elif choice == 'attend pool party':
            current_location = 'pool_party'
        elif choice == 'enter old bar':
            current_location = 'old_bar'
        elif choice == 'go to casino':
            current_location = 'casino'
        elif choice == 'stay at hotel':
            current_location = 'hotel'
        elif choice == 'return home':
            current_location = 'home'
        elif choice == 'go to the park':
            current_location = 'park'
        else:
            print('Invalid choice. Try again.')
        continue  # Skip to the next iteration of the loop


    # Handle actions in different locations
        # Check if new options should be added to the home location
        if current_location == 'home' and hacking_skills >= 7:
            # Define the new options to be added
            new_home_options = ['go to arcade', 'visit sticker swap', 'attend pool party', 'enter old bar', 'go to casino', 'stay at hotel']
            # Append new options if they are not already present
            for option in new_home_options:
                if option not in locations['home']['options']:
                    locations['home']['options'].append(option)

            if choice == 'hack into system':
                print('You successfully infiltrate a corporate system and uncover valuable information.')
                hacking_skills += 1
                print('Your hacking skills have improved!')
        
        if choice == 'go to the park':
            current_location = 'park'
        
        if choice == 'enter secret room' and secret_room_option_unlocked:
            current_location = 'secret_room'

        elif choice == 'go to arcade':
            print('DEBUGGING')
            current_location = 'arcade'
        elif choice == 'visit sticker swap':
            current_location = 'sticker_swap'
        elif choice == 'attend pool party':
            current_location = 'pool_party'
        elif choice == 'enter old bar':
            current_location = 'old_bar'
        elif choice == 'go to casino':
            current_location = 'casino'
        elif choice == 'stay at hotel':
            current_location = 'hotel'    
        else:
                print('Invalid choice. Try again.')

        # Check if 'enter secret room' option should be available
        if secret_room_option_unlocked:
            locations['home']['options'].append('enter secret room')

 #------------------------------------------------------------------------------------------------------------
    elif current_location == 'park':
        if choice == 'play fetch with spot':
            print('Spot is happy playing fetch! He smiles at you and wags his tail, making you feel proud.')
        elif choice == 'hack into public wifi':
            print('You discreetly hack into the park\'s WiFi network.')
            hacking_skills += 1
        elif choice == 'use wigle':
            print('You use WiGLE.net to find nearby WiFi networks. You found 1337 new wireless networks, 42 Bluetooth devices, and 0 new cell networks. You\'ve scanned this area before.')
            hacking_skills += 1
        elif choice == 'return home':
            current_location = 'home'
        elif choice == 'play duck duck goose':
            play_duck_duck_goose()
        else:
            print('Invalid choice. Try again.')
    
    # Cybercafe
    elif current_location == 'cybercafe':
        if choice == 'play ctf':
            print('You had fun playing in the CTF and got second place.')
            hacking_skills += 1
            ctf_unlocked_locations = True
            print('Playing in the CTF has unlocked new locations!')
            # Append new options only for the cybercafe after playing CTF
            locations['cybercafe']['options'].extend(['visit hackerspace', 'go to infosec conference', 'go to bookstore', 'visit technology store'])
        elif choice == 'meet other hackers':
            print('You exchange hacking tips and make some new hacker friends.')
        elif choice == 'hack into high-security server':
            print('You have successfully breached a high-security server.')
            current_location = 'server_room'
        elif choice == 'play CTF':
            print('You recieve a mysterious website. Playing in the CTF has unlocked new locations!.')
            print('https://solve4flipper.s3.amazonaws.com/eulcreppilf.txt')
            hacking_skills += 1
            ctf_unlocked_locations = True
        elif choice == 'access server room':
            if hacking_skills >= 3:  # Check if player has enough skills to access the server room
                print('Your hacking skills allow you to bypass security and access the server room.')
                current_location = 'server_room'
            else:
                print('You need more hacking skills to access the server room.')
        elif choice == 'leave cafe':
            current_location = 'home'
        else:
            print('Invalid choice. Try again.')
 
    elif current_location == 'server_room':
        # Server room location choices
        if choice == 'hack into server':
            print('You successfully hack into the server and retrieve the valuable data.')
            print(f'You discover that you can gain skills points in hacking. Your hacking skills score is {hacking_skills}')
        elif choice == 'plant a network monitor':
            port = input('Enter the port number to filter for traffic related to DOOM: ')
            if port == '666':
                print('You have implanted a network monitor and filtered traffic for DOOM successfully.')
            else:
                print('Incorrect port. The network monitor is not set up.')
        elif choice == 'escape':
            current_location = 'cybercafe'
        else:
            print('Invalid choice. Try again.')
 
    elif current_location == 'secret_room':
        # Secret room location choices
        if choice == 'try to open safe':
            print('You attempt to open the locked safe, but it seems you need a code to unlock it.')
            code = input('Enter the four-digit code every hacker knows...')
            if code == '1337':
                print('Success! There\'s a couple of flash drives, SD cards, NUC, and other gear. You could use this.')
                hacking_skills += 1
            else:
                print('That code did not work, maybe you should try again.')
        elif choice == 'read the book':
            print('You pick up the book read an interesting message, but you\'re not sure what that means.')
            print('31 33 33 37')
        elif choice == 'return to cybercafe':
            current_location = 'cybercafe'
        else:
            print('Invalid choice. Try again.')
 
    elif current_location == 'hackerspace':
        # Hackerspace location choices
        if choice == 'fire up 3D printer':
            print('You come up with a brilliant idea and find the STL you\'re looking for, then modify it in the slicer. You start the print')
            hacking_skills += 1
        elif choice == 'study in common area':
            print('You find a stack of No Starch Press books, and select Practical Malware Analysis. It\'s and oldey, but a goodey.')
            hacking_skills += 1
        elif choice == 'hack into secure network':
            if hacking_skills >=5:
                print('Congratulations! You accessed the code repository for a SaaS dev team. You email them immediately to let them know what happened.')
                hacking_skills += 1
            else: 
                print('Oh oh, this is a honeypot. Yikes, and you were not using a VPN. They got your static IP, now you must rotate. You lose some hacking cred.')
            hacking_skills -= 1
        elif choice == 'explore dark web':
            print('You head to the hidden wiki and see it\'s been updated. Cool, you find some new forums to research.')
        elif choice == 'play memory match game':
            memory_match_game()
        elif choice == 'solder badge':
            solder_badge_challenge()
        elif choice == 'leave hackerspace':
            current_location = 'home'
        else:
            print('Invalid choice. Try again.')
 
    #Infosec Conference
    elif current_location == 'infosec_conference':
        if choice == 'attend lecture':
            print('The talk you are listening to is The Science of Breaking and Entering. What happened to Clippy?')
            hacking_skills += 2
        elif choice == 'network with professionals':
            print('You learn that your infosec heroes suck. But there are some cool people here too.')
            print('The old heads invite you into a speakeasy...')
            current_location = 'speakeasy'
        elif choice == 'visit vendor booths':
            print('You accidentally sign up for a marketing email list, you should have used a disposable email.')
            hacking_skills -= 1
        elif choice == 'grab free swag':
            print('There is some great free swag. There\'s also a caricature artist there, who draws a silly picture of you.')          
        elif choice == 'crack passwords':
            password_cracking_challenge()
            hacking_skills += 1
        elif choice == 'answer trivia':
            hacking_skills = cybersecurity_trivia(hacking_skills)
        elif choice == 'head back home':
            current_location = 'home'        
        else:
            print('Invalid choice. Try again.')
 
 
    # Bookstore
    elif current_location == 'bookstore':
        if choice == 'buy hacking book':
            print('You get the Metasploit book you were looking for and at a discount!')
            hacking_skills += 1
        elif choice == 'buy cybersecurity book':
            print('You read the Cybersecurity Field Manual and learn a couple of career tips.')
        elif choice == 'read magazines':
            print('There\'s there a new version of 2600 out, you buy it to support them, and take a look at the ads in the back.')          
        elif choice == 'leave bookstore':
            current_location = 'home'        
        else:
            print('Invalid choice. Try again.')
 
    # Tech Store
    elif current_location == 'technology_store':
        # Technology Store location choices
        if choice == 'buy new laptop':
            print('You purchase a GPD Pocket, a tiny 8 inch laptop that functions perfectly for hacking.')
        elif choice == 'purchase hacking tools':
            print('This store sells tools for WiFi pentesting, field kits, and hotplug attack tools. You pick up one of each.')
        elif choice == 'browse gadgets':
            print('Wow, they have a raspberry pi 4 on sale for $80!')
        elif choice == 'exit store':
            print('You could spend all day here, but it is time to go home')
            current_location = 'home'
        else:
            print('Invalid choice. Try again.')

    # Arcade  
    if current_location == 'arcade':
        if choice == 'play tetris':
            print('You are pretty darn good, but not as good as Willis Gibson')
        elif choice == 'play pinball':
            print('You play Total Nuclear Annihilation which has great thumping bass. You win the raffle at the end and get an extra game.')
            hacking_skills += 1
        elif choice == 'return home':
            current_location = 'home'
        elif choice == 'play cabinet game':
            print('The machine has unlimited credits. You play for 40 minutes without realizing that time has passed.')
        elif choice == 'play dance game':
            print('You dance along to the Waka Laka on hard mode. You make it through the song and feel proud of yourself.')
        elif choice == 'return home':
            current_location = 'home'
        elif choice == 'try the claw machine':
            if hacking_skills < 0:
                print('You absolutely crush it. You win a gaming console, a fancy watch, and many stuffies.')
                # Add any other relevant actions or consequences here
            else:
                print('You spend over twenty dollars on the claw machine but manage to get nothing except a rubber ducky')    
        else:
            print('Invalid choice. Try again.')

    # Sticker Swap
    elif current_location == 'sticker_swap':
        if choice == 'trade stickers':
            player_stickers = ["cat sticker", "dog sticker", "rabbit sticker", "Common Port sticker", "Trevor sticker"]
            sticker_swap_game(player_stickers)
        elif choice == 'admire sticker collection':
            print('There\'s a lot of stickers all collected on a mural. Your favorite is a cockroach in a milkshake.')
            hacking_skills += 1
        elif choice == 'give out swag':
            print('You used the 3D printer at the hackerspace and made plenty of swag, and included some friendship bracelets.')
            hacking_skills += 1
        elif choice == 'return home':
            current_location = 'home'
        else:
            print('Invalid choice. Try again.')

    # Pool Party
    elif current_location == 'pool_party':
        if choice == 'swim in the pool':
            print('This is not a sanitary choice... your skin itches when you get out of the pool.')
            hacking_skills -= 1
        elif choice == 'chat with hackers':
            print('You meet up with some cool people, a few of them are biohackers. They convince you to get an NFC/RFID combo implant.')
            hacking_skills += 1
        elif choice == 'put on sunscreen':
            print('You\'re wise, sunscreen is important. A stranger asks if they could borrow some.')
            play_sunscreen_game()
        elif choice == 'tan':
            print('Although you\'re not here to gain a glow, you need the vitamin D from being inside so long. The sun is warm.')
        elif choice == 'return home':
            current_location = 'home'
        else:
            print('Invalid choice. Try again.')

# ... existing game loop ...

    elif current_location == 'old_bar':
        if choice == 'order a drink':
            print('You order a refreshing drink.')
        elif choice == 'join conversation':
            print('You join a lively conversation with the locals.')
            # Add any specific game logic here
        elif choice == 'get a free hot dog':
            print('You get a free hot dog!')
            # Print an ASCII hotdog
            print(r'''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠲⡶⢶⡄
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⠕⢭⢿⡟⠁⠀⢀⢆⠃
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⡎⡹⣾⠉⡻⠐⠀⠉⠐⠎⠀
        ⠀⠀⠀⠀⠀⠀⡖⠢⣴⣉⠩⣾⠙⡳⠟⠁⠀⠀⠀⠠⠀⡸⠀
        ⠀⢐⠦⣿⣻⣯⡵⠺⣏⠙⣻⠟⠉⠀⠀⠀⠀⢀⣰⠗⢠⠃⠀
        ⣼⡟⠻⠛⠛⣁⣹⣾⡿⠟⠁⠀⠀⠀⠤⣦⡴⠂⢁⠔⠁⠀⠀
        ⡿⡖⢠⠞⠋⠉⠀⠀⠀⠀⠀⠀⣀⠴⠚⢉⠠⠊⠁⠀⠀⠀⠀
        ⠘⠚⠞⠢⢀⣀⣀⣀⣀⡐⠉⠭⠀⠂⠈⠀⠀⠀⠀⠀⠀⠀⠀

    ''')
        elif choice == 'play jukebox':
            print('You play \'Beer\' by Reel Big Fish. Everyone sings along.')
            # Add any specific game logic here
        elif choice == 'return home':
            current_location = 'home'
        else:
            print('Invalid choice. Try again.')

    elif current_location == 'casino':
        if choice == 'play roulette':
            print('You try your luck at the roulette table.')
            # Add any specific game logic here
        elif choice == 'play blackjack':
            print('You sit down for a round of blackjack.')
            play_blackjack()
            # Add in start of mini game
        elif choice == 'get loyalty card':
            print('You sign up for a casino loyalty card.')
            # Add any specific game logic here
        elif choice == 'visit tarot reader':
            draw_tarot_card()
        elif choice == 'return home':
            current_location = 'home'
        else:
            print('Invalid choice. Try again.')

    elif current_location == 'hotel':
        if choice == 'touch the car':
            print('You can’t resist touching the racecar despite the warning sign.')
            print('Hey! We warned you! It specifically has a sign that says don\'t do that!')
            print('Oh! no! you lost 10 hacking skills points!')
            hacking_skills -= 10
            print(f'Your current have {hacking_skills} points.')
            # Add any specific game logic here
        elif choice == 'attend party':
            print('You decide to join the party happening at the hotel. It\'s in someone\'s large suite. There\'s a DJ')
            # Add any specific game logic here
        elif choice == 'eat at buffet':
            print('Oh you\'re hungry. There is a huge tray of fruit.')
            print('You scoop up some fruit...')

            # Mini-Game: Word Unscramble
            import random

            # List of words for the mini-game
            word_list = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "melon", "strawberry", "blueberry", "pineapple", "mango", "peach", "pear", "plum", "lemon", "lime", "watermelon", "pomegranate", "apricot", "fig", "avocado", "coconut", "raspberry", "blackberry", "grapefruit", "cantaloupe", "guava", "kiwifruit", "tangerine", "cranberry", "papaya", "passion fruit", "dragon fruit", "starfruit", "persimmon", "boysenberry", "elderberry", "currant", "lychee"]

            # Select a random word from the list
            random_word = random.choice(word_list)

            # Scramble the word
            scrambled_word = list(random_word)
            random.shuffle(scrambled_word)
            scrambled_word = "".join(scrambled_word)

            print(f"Unscramble the word: {scrambled_word}")

            attempts = 0
            max_attempts = 3  # It's not that hard
            correct = False

            while attempts < max_attempts:
                guess = input("Enter your guess: ").lower()

                if guess == random_word:
                    print(f"Congratulations! You unscrambled the fruit '{random_word}' correctly!")
                    correct = True
                    break
                else:
                    attempts += 1

            if not correct:
                print(f"Sorry, you've reached the maximum number of attempts. The fruit was '{random_word}'. Better luck next time!")

        elif choice == 'attend lobbycom':
            print('You attend an impromptu gathering in the lobby.')
            # Add any specific game logic here
        elif choice == 'return home':
            current_location = 'home'
        else:
            print('Invalid choice. Try again.')


    elif current_location == 'dispensary':
        if choice == 'buy candy':
            print('You buy some THC-infused candy.')
            # Add any specific game logic here
        elif choice == 'buy flower':
            print('You browse and buy some quality cannabis flower.')
            # Add any specific game logic here
        elif choice == 'chill in lounge':
            print('You hit your vape and take a gummy. Your bestie with a matching tattoo sits next to you. It feels like absolute bliss.')
            hacking_skills += 1
        elif choice == 'return home':
            current_location = 'home'
        else:
            print('Invalid choice. Try again.')

    elif current_location == 'speakeasy':
        if choice == 'gamble':
            print('You can gamble your hacking skills points here.')
            print(f'Your current score is {hacking_skills}')
            while True:
                print(f"You have {hacking_skills} hacking skill points.")

                # Option for the player to continue or quit
                continue_game = input("Do you want to play the game? (yes/no): ").strip().lower()
                if continue_game != "yes":
                    print("Exiting the gambling game.")
                    break

                player_choice = input("Guess 'Sun' or 'Moon': ").strip().lower()
                
                if player_choice not in ["sun", "moon"]:
                    print("Invalid choice. Please choose 'Sun' or 'Moon'.")
                    continue
                
                game_result = random.choice(["sun", "moon"])
                print(f"The result is: {game_result.title()}")

                if player_choice == game_result:
                    hacking_skills += 1
                    print("You guessed correctly! You gain 1 point.")
                else:
                    hacking_skills -= 1
                    print("Incorrect guess. You lose 1 point.")

                if hacking_skills <= 0:
                    print("You\'re credibility has reach an all time low.")
                    break

                #return hacking_skills
            # Add any specific game logic here
            ####
        elif choice == 'order a drink':
            print('DEBUGGING.')
            # Add any specific game logic here
        elif choice == 'attend secret meeting':
            print('DEBUGGING.')
            hacking_skills += 1
        elif choice == 'sit at bar':
            print('You realize you are talking to a budtender and bartender.')
            print('They advise you that entering the magic numbers will take you to a hidden dispensary.')
        elif choice == 'return to conference':
            current_location = 'infosec_conference'
        else:
            print('Invalid choice. Try again.')

    # Handle transitions to CTF unlocked locations
    if ctf_unlocked_locations:
        if choice == 'visit hackerspace':
            current_location = 'hackerspace'
        elif choice == 'go to infosec conference':
            current_location = 'infosec_conference'
        elif choice == 'go to bookstore':
            current_location = 'bookstore'
        elif choice == 'visit technology store':
            current_location = 'technology_store'

 
# End of the game script
