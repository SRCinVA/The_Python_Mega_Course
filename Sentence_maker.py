
# My solution

# def sentenceGlue(string):
#     sentence = input("Say something: ")
#     paragraph = []
#     for sentence in paragraph:
#         sentence.capitalize() + "."
#         paragraph.append(sentence)
#         if sentence == "end":
#             print(paragraph)

# sentenceGlue()

# You don't need to cram everything into one function.
# you probably could have done so, but his is more readable
# this way.

def sentenceGlue(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

# his approach was to transform the phrases first, then concatenate them
# he also used a list, created outside the loop.
results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":  # you want to check if it's an "end" statement before adding it to the list.
        break
    else:
        results.append(sentenceGlue(user_input)) 
        # above is what made the difference:
        # he calls sentenceGlue and puts user_input through that, then
        # appends those to results.
print(" ".join(results)) # this concatenates the list items in "results" into one object.