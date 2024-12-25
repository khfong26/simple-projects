import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

FONT_LARGE = pygame.font.Font(None, 74)
FONT_SMALL = pygame.font.Font(None, 36)

word_bank = ["hello", "world", "computer", "house", "pilot"]
word = ""
temp_word = []
guesses = []
wrong_guesses = 0
incorrect_guesses = []
max_wrong_guesses = 6
error_message = ""

# Hangman structure and body parts
hangman_structure = [
    ((100, 400), (100, 50)),
    ((100, 50), (250, 50)),
    ((250, 50), (250, 100)),
]

# Hangman body parts
hangman_parts = [
    (250, 130, 30),
    ((250, 160), (250, 250)),
    ((250, 180), (200, 220)),
    ((250, 180), (300, 220)),
    ((250, 250), (200, 320)),
    ((250, 250), (300, 320)),
]

# Input box variables
input_text = ""
input_active = True
entering_word = True

# Function to reset the game state
def reset_game():
    global word, temp_word, guesses, wrong_guesses, incorrect_guesses, error_message, input_text, entering_word
    word = ""
    temp_word = []
    guesses = []
    wrong_guesses = 0
    incorrect_guesses = []
    error_message = ""
    input_text = ""
    entering_word = True

reset_game()

# Game loop
running = True
while running:
    screen.fill(WHITE)

    if entering_word:
        # Prompt for word input
        prompt_text = FONT_SMALL.render("Enter a word (or leave empty for random):", True, BLACK)
        screen.blit(prompt_text, (WIDTH // 2 - prompt_text.get_width() // 2, 300))
        
        # Draw input box
        input_box = pygame.Rect(WIDTH // 2 - 150, 350, 300, 50)
        pygame.draw.rect(screen, GRAY, input_box, border_radius=5)
        pygame.draw.rect(screen, BLACK, input_box, 2, border_radius=5)
        input_text_render = FONT_SMALL.render(input_text, True, BLACK)
        screen.blit(input_text_render, (input_box.x + 10, input_box.y + 10))
        
        # Display instructions
        instructions_text = FONT_SMALL.render("Press Enter to confirm.", True, BLUE)
        screen.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, 420))
    else:
        # Draw the gallows
        for part in hangman_structure:
            pygame.draw.line(screen, BLACK, part[0], part[1], 5)

        # Display the word
        display_word = " ".join(temp_word)
        word_text = FONT_LARGE.render(display_word, True, BLACK)
        screen.blit(word_text, (WIDTH // 2 - word_text.get_width() // 2, 450))

        # Display wrong guesses
        wrong_text = FONT_SMALL.render(f"Wrong guesses: {', '.join(incorrect_guesses)}", True, RED)
        screen.blit(wrong_text, (50, 400))

        # Display number of tries left
        tries_left = max_wrong_guesses - wrong_guesses
        tries_text = FONT_SMALL.render(f"Tries left: {tries_left}", True, BLUE)
        screen.blit(tries_text, (50, 450))

        # Draw input box
        input_box = pygame.Rect(WIDTH // 2 - 150, 520, 300, 50)
        pygame.draw.rect(screen, GRAY, input_box, border_radius=5)
        pygame.draw.rect(screen, BLACK, input_box, 2, border_radius=5)
        input_text_render = FONT_SMALL.render(input_text, True, BLACK)
        screen.blit(input_text_render, (input_box.x + 10, input_box.y + 10))

        # Display error message
        if error_message:
            error_text = FONT_SMALL.render(error_message, True, RED)
            screen.blit(error_text, (WIDTH // 2 - error_text.get_width() // 2, 580))

        # Draw hangman parts based on wrong guesses
        for i in range(wrong_guesses):
            part = hangman_parts[i]
            if len(part) == 2:
                pygame.draw.line(screen, BLACK, part[0], part[1], 5)
            elif len(part) == 3:
                pygame.draw.circle(screen, BLACK, (part[0], part[1]), part[2], 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if entering_word:
                if event.key == pygame.K_RETURN:
                    if not input_text.strip():
                        word = random.choice(word_bank)
                    else:
                        word = input_text.lower()
                    temp_word = ["_"] * len(word)
                    input_text = ""  # Clear input box after word is set
                    entering_word = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
            elif input_active:
                if event.key == pygame.K_RETURN:
                    guess = input_text.lower()
                    if len(guess) != 1 or not guess.isalpha():
                        error_message = "Invalid input! Enter a single letter."
                    elif guess in guesses:
                        error_message = "You already guessed that!"
                    else:
                        error_message = ""
                        guesses.append(guess)
                        if guess in word:
                            for i, letter in enumerate(word):
                                if letter == guess:
                                    temp_word[i] = guess
                        else:
                            incorrect_guesses.append(guess)
                            wrong_guesses += 1
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    if not entering_word:
        # Display the word 
        display_word = " ".join(temp_word)
        word_text = FONT_LARGE.render(display_word, True, BLACK)
        screen.blit(word_text, (WIDTH // 2 - word_text.get_width() // 2, 450))

        if "_" not in temp_word:
            end_text = FONT_LARGE.render("You Win!", True, BLUE)
            screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2))
            pygame.display.update()
            pygame.time.wait(2000)
            reset_game()
        elif wrong_guesses == max_wrong_guesses:
            end_text = FONT_LARGE.render(f"You Lose! The word was {word}", True, RED)
            screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2))
            pygame.display.update()
            pygame.time.wait(2000)
            reset_game()

    pygame.display.flip()

pygame.quit()
sys.exit()
