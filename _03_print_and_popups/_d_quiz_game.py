from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
    
    # Make a new window variable, window = Tk()
window = Tk()
    # Hide the window using the window's .withdraw() method
window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
score=0
    # ASK A QUESTION AND CHECK THE ANSWER
messagebox.showinfo(message="This is a quiz game where every question will give you a point for a correct answer and you will lose a point for an incorrect answer.")
    #      // 2.  Ask the user a question 
q1 = simpledialog.askstring(title='', prompt='How many days can a mosquito live?')
    #      // 3.  Use an if statement to check if their answer is correct
if q1 == '1' or q1 == '1 day' or q1 == '1 Day' or q1 == '1 dAy' or q1 == '1 daY' or q1 == '1day' or q1 == '1 DAy':
    messagebox.showinfo(message="That is correct!")
    score = score+1
else:
    score = score - 1
    messagebox.showinfo(message="That answer is incorrect")
    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
q2 = simpledialog.askstring(title='', prompt='What is the biggest animal alive today (use capitals)')
if q2 == 'Blue Whale' or q2 == 'The Blue Whale':
    messagebox.showinfo(message="That is correct!")
    score = score+1
else:
    score = score - 1
    messagebox.showinfo(message="That answer is incorrect")
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function
print("Your score is:")
print(score)
    # Run the window's .mainloop() method
window.mainloop()
