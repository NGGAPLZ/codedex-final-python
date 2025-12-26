import random
# A little art piece XP
print("==================================")
print("####  ####  ####  ####  ####  ####")
print("#     #     #     #  #  #  #  #   ")
print("####  ####  #     ####  ####  ####")
print("#        #  #     #  #  #     #   ")
print("####  ####  ####  #  #  #     ####")
print("==================================")
# Flags / state
scene2a = False
scene2b = False
scene3  = False
scene4  = False
scene5  = False

ending1 = False
ending2 = False
ending3 = False

weapon_pistol = False
MedPatch = False
HP = 10
# Intro & first choice
print("You wake up in twisted metal and smoke.")
print("You: Shit... still breathing.")
print("Your prisoner cuff is half-melted. Sirens howl in the distance.")
print("-------------------------------------------------------------")
print("1. Search the wreckage for supplies")
print("2. Slip into the jungle before some alien shows up.")
choice1 = int(input("Input (1) or (2) to decide: "))
while choice1 < 1 or choice1 > 2:
    print("Invalid Choice")
    choice1 = int(input("Input (1) or (2) to decide: "))
if choice1 == 1:
    scene2a = True
else:
    scene2b = True
# Router Loop
while True:

    # Endings
    if ending1 or ending2 or ending3:
        if ending1:
            print("Portal Escape Victory")
        elif ending2:
            print("Ship Theft(Bonus Victory)")
        else:
            print("Captured, Back to prison you go")
        break

    # -------- Scene 2A --------
    if scene2a == True:
        print("You dig through panels and ash.")
        print("You: Come on, give me something that isn't cooked.")
        print("You find a busted plasma pistol and a MedPatch.")
        print("-------------------------------------------------------------")
        print("1. Try to fix the damn pistol and head into the jungle")
        print("   Roll chance: success -> working pistol ; fail -> stays busted")
        print("2. Pocket the MedPatch and bail to the jungle.")
        choice2a = int(input("Input (1) or (2) to decide: "))
        while choice2a < 1 or choice2a > 2:
            print("Invalid Choice")
            choice2a = int(input("Input (1) or (2) to decide: "))

        if choice2a == 1:
            dice_roll = random.randint(1, 2)
            if dice_roll == 1:
                print("Success!!!")
                weapon_pistol = True
            else:
                print("Fail!!!")
                weapon_pistol = False
                MedPatch = True
        else:
            MedPatch = True

        scene2a = False
        scene3 = True
        continue

    # -------- Scene 2B --------
    if scene2b == True:
        print("You slip into neon leaves and buzzing bugs.")
        print("You: Great.. Space mosquitoes. Perfect.")
        print("Vines swallow the crash site behind you.")
        print("-------------------------------------------------------------")
        print("1. Circle back to scavenge quickly.")
        print("2. Keep moving, ears open.")
        choice2b = int(input("Input (1) or (2) to decide: "))
        while choice2b < 1 or choice2b > 2:
            print("Invalid Choice")
            choice2b = int(input("Input (1) or (2) to decide: "))

        if choice2b == 1:
            scene2b = False
            scene2a = True   # circle back works now
        else:
            scene2b = False
            scene3 = True
        continue

    # -------- Scene 3 --------
    if scene3 == True:
        print("A seven foot alien with tusks drops from a branch.")
        if weapon_pistol == True:
            print("1. Aim and fire.")
            print("2. Back away slowly.")
            print("Roll: hit = alien flees wounded; miss = you take damage move forward.")
            choice3a = int(input("Input (1) or (2) to decide: "))
            while choice3a < 1 or choice3a > 2:
                print("Invalid Choice")
                choice3a = int(input("Input (1) or (2) to decide: "))

            if choice3a == 1:
                dice_roll = random.randint(1, 2)
                if dice_roll == 1:
                    print("Hit!!!")
                else:
                    print("Miss!!!")
                    HP = HP - 2
                    print("You lost 2 HP")
                    print(f"You now have {HP} HP left")
            else:
                print("You back away, keeping your eyes on it.")
        else:
            print("1. Throw a rock and run.")
            print("Roll: success = escape; fail = scratched, HP loss.")
            print("2. Stand tall and growl at it.")
            choice4 = int(input("Input (1) or (2) to decide: "))
            while choice4 < 1 or choice4 > 2:
                print("Invalid Choice")
                choice4 = int(input("Input (1) or (2) to decide: "))

            if choice4 == 1:
                dice_roll = random.randint(1, 2)
                if dice_roll == 1:
                    print("Success!!! You escape unscathed")
                else:
                    print("Fail!!!")
                    HP = HP - 2
                    print("You lost 2 HP")
                    print(f"You now have {HP} HP left")
            else:
                print("The alien blinks, confused, then lopes off.")
                print("You: Yeah, RUN!! STUPID ALIEN!!!")

        scene3 = False
        scene4 = True
        continue

    # -------- Scene 4 --------
    if scene4 == True:
        print("You reach a ravine rim.")
        print("Below, an alien patrol scans with drones.")
        print("A humming portal obelisk glows beyond them..")
        print("-------------------------------------------------------------")
        print("1. Sneak across the bridge and hide. (Roll)")
        print("2. Ambush the patrol. (Better with weapon) (Roll)")
        print("3. Create a distraction. (Roll)")
        choice4b = int(input("Input (1), (2) or (3) to decide: "))
        while choice4b != 1 and choice4b != 2 and choice4b != 3:
            print("Invalid Choice")
            choice4b = int(input("Input (1), (2) or (3) to decide: "))

        if choice4b == 1:
            dice_roll = random.randint(1, 2)
            if dice_roll == 1:
                print("Success!!!")
                ending1 = True
            else:
                print("Fail!!!")
                scene5 = True

        elif choice4b == 2:
            if weapon_pistol == True:
                dice_roll = random.randint(1, 5)
                if dice_roll > 2:
                    print("Success!!!")
                    ending2 = True
                else:
                    print("Fail!!!")
                    ending3 = True
            else:
                print("I have no weapon but I'll try anyway.")
                dice_roll = random.randint(1, 5)
                if dice_roll > 4:
                    print("Success!!!")
                    ending2 = True
                else:
                    print("Fail!!! You were captured")
                    ending3 = True
        else:
            dice_roll = random.randint(1, 5)
            if dice_roll > 3:
                print("Success!!!")
                ending1 = True
            else:
                print("Fail!!!")
                scene5 = True

        scene4 = False
        continue

    # -------- Scene 5 --------
    if scene5 == True:
        print("Sirens shriek, A drone zips at your face.")
        print("You: OK now we are really screwed!!")
        print("-------------------------------------------------------------")
        print("1. Sprint for the portal.")
        print("2. LAST STAND!!!")
        choice5 = int(input("Input (1) or (2) to decide: "))
        while choice5 < 1 or choice5 > 2:
            print("Invalid Choice")
            choice5 = int(input("Input (1) or (2) to decide: "))

        if choice5 == 1:
            if HP > 6:
                dice_roll = random.randint(1, 6)
                if dice_roll > 2:
                    print("Success!!!")
                    ending2 = True
                else:
                    print("Fail!!!")
                    ending3 = True
            else:
                dice_roll = random.randint(1, 10)
                if dice_roll > 7:
                    print("Success!!!")
                    ending2 = True
                else:
                    print("Fail!!!")
                    ending3 = True
        else:
            if weapon_pistol == True:
                dice_roll = random.randint(1, 6)
                if dice_roll > 3:
                    print("Success!!!")
                    ending2 = True
                else:
                    print("Fail!!!")
                    ending3 = True
            else:
                print("You try to swing a pipe like an idiot")
                ending3 = True

        scene5 = False
        continue

    #If we somehow have no active scenes and no ending, end gracefully
    break
