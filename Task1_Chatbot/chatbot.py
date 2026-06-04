import random
from datetime import datetime

print("=" * 50)
print("🎓 Welcome to CampusBot")
print("Your Student Assistant Chatbot")
print("Type 'help' to see available commands")
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
    ],

    "study": [
        "Study consistently instead of cramming before exams.",
        "Use active recall and spaced repetition techniques.",
        "Practice questions regularly to improve retention."
    ],

    "github": [
        "Keep your repositories organized and documented.",
        "Make regular commits to show your progress.",
        "A good README makes your project look professional."
    ],

    "motivation": [
        "Small daily progress leads to big achievements.",
        "Consistency beats intensity.",
        "Focus on progress, not perfection."
    ]
}

while True:

    user = input("\nYou: ").lower().strip()

    if user == "bye":
        print("CampusBot: Goodbye! Best of luck with your studies.")
        break

    questions_count += 1

    if user in ["hello", "hi", "hey"]:
        print("CampusBot: Hello! How can I help you today?")

    elif user == "help":
        print("""
Available Topics:
- attendance
- exam
- internship
- placement
- python
- study
- github
- motivation
- date
- time
- bye
""")

    elif "time" in user:
        print("CampusBot:", datetime.now().strftime("%H:%M:%S"))

    elif "date" in user:
        print("CampusBot:", datetime.now().strftime("%d-%m-%Y"))

    else:
        found = False

        for keyword in responses:

            if keyword in user:
                print("CampusBot:", random.choice(responses[keyword]))
                found = True
                break

        if not found:
            print("CampusBot: Sorry, I don't understand that yet.")
            print("CampusBot: Type 'help' to see available topics.")

print(f"\nTotal Questions Asked: {questions_count}")
print("Thank you for using CampusBot!")