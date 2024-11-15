# ////////////////////////////////////////
# //                                    //
# // Name: AAQIL AHMED KULLDIK MANEGAR  //
# //                                    //
# // Assignment: Little Proffessor      //
# //                                    //
# ////////////////////////////////////////
import sys, random

# // Get the level the user wants to be play
def get_level() -> int:
    choice: int = 0

    # // While choice is invalid (not 1, 2 or 3)
    while choice <= 0 or choice > 3:
        try:
            choice = int(input("Level: "))
        except Exception: pass
    return choice

# // Generate a random integer depending
# // on the level choice
def generate_integer(level: int) -> int:
    return {
        1: random.randint(0, 9),
        2: random.randint(10, 99),
        3: random.randrange(100, 999)
    }[level]

# // Main function
def main():
    # // Get the level the user wants to play at
    level: int = get_level()

    # // Pre-Defined Variables
    errors: int = 0
    score: int = 0
    answer: int = -1

    # // Play game 10 times
    for _ in range(10):
        x: int = generate_integer(level)
        y: int = generate_integer(level)

        solution: int = x + y
        while solution != answer:
            # // Exit the program after printing the
            # // correct answer
            if errors >= 3:
                print(solution)
                sys.exit(f"Score: {score}")

            try:
                answer: int = int(input(f"{x} + {y} = "))
            except Exception:
                pass

            # // If the answer is correct, increase score
            if solution == answer:
                errors = 0
                score += 1

            # // Else, increase errors
            elif solution != answer:
                errors += 1
                print("EEE")

    # // Print the users score
    print(f"Score: {score}")


# // Run the program
if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/professor
# submit50 cs50/problems/2022/python/professor
