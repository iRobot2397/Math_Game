import time
import random
def game():
  guesses = 10
  score = 0
  
  while guesses != 0:
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    operation = random.randint(1,3)
    output_operation = "+" if operation == 1 else "-" if operation == 2 else "x"
  
    answer = num1 + num2 if operation == 1 else num1 - num2 if operation == 2 else num1 * num2
    x = time.time()
   
    guess = int(input("What is {} {} {}:  ".format(num1, output_operation, num2)))
    x = time.time() - x
    x = int(x)
    if x >= 10:
      print("Times Up! You Have Taken More Than 10 Seconds")
      guesses -= 1
      score += 0
    else:
      if guess == answer:
        print("Congragulations, You Got It Right!")
        guesses -= 1
        score += 1
      else:
        print("The Correct Answer Was {}.".format(answer))
        guesses -= 1
        score += 0
      
  print("Game Over!")
  percent = score * 10
  print("Your Score Is {}%".format(percent))
  again = input("Would You Like To Play Again(y/n): ")
  again = again.lower()
  if again == "y":
    game()
  elif again == "n":
    print("Thank You For Playing!")
  else:
    print("Invalid Input")
    again = input("Would You Like To Play Again(y/n): ")
    again = again.lower()

game()