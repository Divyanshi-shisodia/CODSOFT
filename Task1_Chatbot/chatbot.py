import random
print("=" * 50)
print("🎓 Welcome to CampusBot")
print("Your Student Assistant Chatbot")
print("Type 'bye' to exit")
print("=" * 50)

questions_count = 0

responses = {
    "attendance": [
        "Try to maintain at least 75% attendance.",
        "Regular attendance helps you understand concepts better.",
        "Don't wait until the end of the semester to improve attendance."
    ],

    "exam": [
        "Revise regularly and solve previous year papers.",
        "Focus on important topics and practice numerical problems.",
        "Make short notes for quick revision."
    ],

    "internship": [
        "Build projects and keep your GitHub updated.",
        "Learn skills that match your career goals.",
        "Create a strong LinkedIn profile and portfolio."
    ],

    "placement": [
        "Focus on DSA, aptitude, and communication skills.",
        "Practice coding questions regularly.",
        "Work on your resume and interview skills."
    ],

    "python": [
        "Python is widely used in AI and Machine Learning.",
        "Python is beginner-friendly and powerful.",
        "Python is useful for automation and data science."
    ]
}

while True:

    user = input("\nYou: ").lower()

    questions_count += 1

    if user in ["hello", "hi", "hey"]:
        print("CampusBot: Hello! How can I help you today?")

    elif user == "bye":
        print("CampusBot: Goodbye! Best of luck with your studies.")
        break

    else:
        found = False

        for keyword in responses:

            if keyword in user:
                print("CampusBot:", random.choice(responses[keyword]))
                found = True
                break

        if not found:
            print("CampusBot: Sorry, I don't understand that yet.")

print(f"\nTotal Questions Asked: {questions_count}")