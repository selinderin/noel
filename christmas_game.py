import random

def home_alone():
    print("WELCOME TO HOME ALONE! You are Kevin!")
    print("\nStory:")
    print("Kevin McCallister, an inventive and resourceful kid, has been left home alone while his family is away on vacation. \nHowever, trouble is brewing as two notorious thieves, Harry and Marv, have targeted his house! It's up to Kevin to protect his home by setting clever traps to fend off the intruders. \nUse your wits, but be careful—Kevin's health is on the line if traps backfire. \nCan you outsmart the thieves and save the day?")

    print("\nYour mission is to defend your house from thieves by setting traps. Be careful, Kevin's health is at risk too!")
    print("Characters:")
    print("Kevin: The protagonist, a clever kid with a knack for booby traps.")
    print("Harry: A crafty thief, but not the brightest. He deals more damage when attacking.")
    print("Marv: Harry's partner, clumsier and more gullible than Harry. He is more prone to mistakes.")

    rooms_list = ["Living Room", "Bedroom", "Kids' Room", "Bathroom", "Hall", "Kitchen", "Dining Room", "Attic", "Basement"]
    traps = {"1": 15, "2": 30, "3": 50}  # 1: Small 2: Medium 3: Big
    trap_penalties = {"1": -5, "2": -10, "3": -20}  

    points = 0
    hp = 100
    police_called = False

    # Thieves HP 
    thieves = {"Harry": 100, "Marv": 100}

    for room in rooms_list:
        print(f"\nSetting traps in the {room}.")
        print("Choose a trap:")
        print("1: Small (Low damage, high success rate) - A simple but effective trap.")
        print("2: Medium (Medium damage, medium success rate) - A more complicated setup, but more damaging.")
        print("3: Big (High damage, low success rate) - A risky but powerful trap.")
        trap_type = input("Enter the number of your choice (1, 2, or 3): ")

        if trap_type in traps:
            success = trap_results(trap_type)
            thief = random.choice(list(thieves.keys()))
            
            if success:
                thieves[thief] -= traps[trap_type]
                points += traps[trap_type]
                print(f"Trap worked! {thief} took {traps[trap_type]} damage.")
                print(f"Your Points: {points}, {thief}'s HP: {thieves[thief]}.")
                
                if thieves[thief] <= 0:
                    print(f"Great job! {thief} has been taken out of the game!")
                    del thieves[thief]
                    if not thieves:
                        print("All thieves have been stopped! You win!")
                        break
            else:
                penalty = random.randint(trap_penalties[trap_type] - 2, trap_penalties[trap_type] + 2)
                points += penalty
                hp += penalty
                print(f"Trap failed! Kevin got hurt and lost {-penalty} HP.")
                print(f"Your Points: {points}, Kevin's HP: {hp}.")

                if hp <= 0:
                    print("Kevin has been caught by the thieves! Game Over.")
                    break

            thief_attack_success = thief_attack(thief)
            if thief_attack_success:
                attack_damage = random.randint(10, 20) + (5 if thief == "Harry" else 0)
                hp -= attack_damage
                print(f"Oh no! {thief} attacked Kevin with a dangerous item causing {attack_damage} damage! Kevin's HP: {hp}")

                if hp <= 0:
                    print("Kevin has been overwhelmed by the thieves! Game Over.")
                    break
            else:
                counter_damage = random.randint(10, 20)
                thieves[thief] -= counter_damage
                print(f"{thief}'s attack backfired! Kevin countered and dealt {counter_damage} damage. {thief}'s HP: {thieves[thief]}.")

                if thieves[thief] <= 0:
                    print(f"Great job! {thief} has been taken out of the game!")
                    del thieves[thief]
                    if not thieves:
                        print("All thieves have been stopped! You win!")
                        break

        else:
            print("Invalid trap choice! Please select 1, 2, or 3.")

        # Police can be called if points reach 100 or more
        if points >= 100 and not police_called:
            police_called = True
            print("\nYou have enough points to call the police!")
            print("The police arrive and catch the thieves. You successfully defended your home!")
            break

    if hp > 0 and thieves and not police_called:
        print("\nThe game is over. Here's how you did:")
        if points >= 100:
            print("Excellent job defending your home! Final Score:", points)
        elif points >= 50:
            print("Good effort! Your final score is:", points)
        else:
            print("You need to improve your strategy. Final Score:", points)

    elif hp > 0 and not thieves:
        print("\nKevin successfully defended his home from all the thieves! Great job!")

    elif hp <= 0:
        print("\nKevin has been hospitalized due to injuries from the traps. Better luck next time!")

def trap_results(trap_type):
    success_rates = {  
        "1": 60,   
        "2": 50,  
        "3": 40    
    }
    roll = random.randint(1, 100)  
    return roll <= success_rates.get(trap_type, 0)

def thief_attack(thief):
    # Harry has a higher attack chance, Marv is more prone to failing
    success_rate = 60 if thief == "Harry" else 40
    roll = random.randint(1, 100)
    return roll <= success_rate

home_alone()
