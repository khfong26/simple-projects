with open("story.txt", "r", encoding="utf-8") as f:
    story = f.read()  # Read the story content
    
words = set()
start_of_word = -1
start = "<"
end = ">"
for i, char in enumerate(story):
    if char == start:
        start_of_word = i
    if char == end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}
for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)
