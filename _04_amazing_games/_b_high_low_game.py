from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)
lives = 10
    # 2. Print out the random variable that you made in step #1
    # 3. Code a for loop to run steps 4-10, 10 times
for i in range(10):
    q1 = simpledialog.askinteger(title='', prompt='Guess a random number between 1 and 100')
    if random_num == q1:
        messagebox.showinfo(message= 'Congrats you win!')
        sys.exit(0)
    if random_num < q1:
        print('The random number is less than:')
        print(q1)
        lives -= 1
    if random_num > q1:
        print('The random number is greater than:')
        print(q1)
        lives -= 1
    print('Lives:')
    print(lives)
messagebox.showinfo(message= 'You have lost.')
print('The correct answer was:')
print(random_num)
        # 4. Ask the user for a guess using a pop-up window, and save their response
        # 5. If the guess is correct
            # 6. Win. Use 'sys.exit(0)' to end the program

        # 7. if the guess is high
            # 8. Tell them it's too high
        # 9. Else if the guess is low
            # 10. Tell them it's too low

    #11. Outside of the loop, tell the user they lost

window.mainloop()
