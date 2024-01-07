def mad_libs():
    print("Welcome to Mad Libs!")

    # Story template with placeholders for different parts of speech
    story_template = "Once upon a time, there was a {adjective} {noun} who loved to {verb} in the {place}. One day, they found a {adjective} {noun} and decided to {verb} it. It turned out to be a magical {noun} that granted them {number} wishes. They wished for {adjective} {noun}, {adjective} {noun}, and a lifetime supply of {noun}. The end!"

    # Prompt user for words
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    number = input("Enter a number: ")

    # Fill in the story template with user's input
    filled_story = story_template.format(adjective=adjective, noun=noun, verb=verb, place=place, number=number)

    # Display the completed Mad Libs story
    print("\nHere's your Mad Libs story:\n")
    print(filled_story)

if __name__ == "__main__":
    mad_libs()
