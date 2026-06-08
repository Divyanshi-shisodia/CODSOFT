import random
import time
from datetime import datetime
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# ------------------ FUNCTIONS ------------------ #

def typing(text, color=Fore.CYAN):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(0.02)
    print()

def save_chat(speaker, message):
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(f"{speaker}: {message}\n")

def achievement_check(count):
    if count == 5:
        typing("🏆 Achievement Unlocked: Curious Learner (5 Questions Asked!)", Fore.YELLOW)
    elif count == 10:
        typing("🏆 Achievement Unlocked: Knowledge Explorer (10 Questions Asked!)", Fore.YELLOW)
    elif count == 20:
        typing("🏆 Achievement Unlocked: Campus Master (20 Questions Asked!)", Fore.YELLOW)

def cgpa_calculator():
    try:
        n = int(input(Fore.GREEN + "Enter number of subjects: "))
        total = 0

        for i in range(1, n + 1):
            grade = float(input(Fore.GREEN + f"Grade Point for Subject {i}: "))
            total += grade

        cgpa = total / n
        typing(f"📊 Your CGPA is: {cgpa:.2f}", Fore.MAGENTA)

    except ValueError:
        typing("Invalid Input!", Fore.RED)

def percentage_calculator():
    try:
        obtained = float(input(Fore.GREEN + "Marks Obtained: "))
        total = float(input(Fore.GREEN + "Total Marks: "))

        percentage = (obtained / total) * 100
        typing(f"📈 Percentage = {percentage:.2f}%", Fore.MAGENTA)

    except:
        typing("Invalid Input!", Fore.RED)

def career_roadmap():
    typing("""
🎯 CSE CAREER ROADMAP

📘 First Year
• Learn Python
• Learn Git & GitHub
• Basic DSA

📗 Second Year
• Advanced DSA
• Web Development
• Competitive Programming

📙 Third Year
• Build Projects
• Open Source Contributions
• Internship Preparation

📕 Fourth Year
• Placement Preparation
• Mock Interviews
• Resume Building
""", Fore.LIGHTBLUE_EX)

def project_ideas():
    ideas = [
        "AI Chatbot",
        "Expense Tracker",
        "Movie Recommendation System",
        "Face Recognition Attendance System",
        "Smart Traffic Management System",
        "Resume Analyzer",
        "Hospital Management System",
        "Online Voting System",
        "Weather Forecast App",
        "Library Management System"
    ]

    typing("💡 Project Ideas:", Fore.YELLOW)

    for i, idea in enumerate(random.sample(ideas, 5), start=1):
        print(Fore.WHITE + f"{i}. {idea}")

# ------------------ LOGO ------------------ #

print(Fore.CYAN + r"""
 ██████╗ █████╗ ███╗   ███╗██████╗ ██╗   ██╗███████╗
██╔════╝██╔══██╗████╗ ████║██╔══██╗██║   ██║██╔════╝
██║     ███████║██╔████╔██║██████╔╝██║   ██║███████╗
██║     ██╔══██║██║╚██╔╝██║██╔═══╝ ██║   ██║╚════██║
╚██████╗██║  ██║██║ ╚═╝ ██║██║     ╚██████╔╝███████║
 ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝      ╚═════╝ ╚══════╝
""")

print(Fore.YELLOW + "=" * 60)
print(Fore.YELLOW + "🎓 CAMPUSBOT AI - SMART STUDENT ASSISTANT")
print(Fore.YELLOW + "=" * 60)

# ------------------ USER PROFILE ------------------ #

name = input(Fore.GREEN + "Enter Your Name: ")
branch = input(Fore.GREEN + "Enter Your Branch: ")

hour = datetime.now().hour

if hour < 12:
    greeting = "Good Morning"
elif hour < 18:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"

typing(f"\n{greeting}, {name}! 👋", Fore.CYAN)
typing(f"Welcome {branch} Student.", Fore.CYAN)

motivation_quotes = [
    "Success comes from consistency.",
    "Small progress every day adds up.",
    "Dream big, start small, act now.",
    "Stay focused and never stop learning.",
    "Discipline beats motivation."
]

typing("\n💡 Today's Motivation:", Fore.YELLOW)
typing(random.choice(motivation_quotes), Fore.WHITE)

# ------------------ DATA ------------------ #

questions_count = 0
topic_count = {}

responses = {
    "attendance": [
        "Maintain at least 75% attendance.",
        "Regular attendance improves understanding.",
        "Don't wait till the end semester to improve attendance."
    ],

    "exam": [
        "Practice previous year papers.",
        "Make short notes for revision.",
        "Focus on important topics and concepts."
    ],

    "internship": [
        "Build projects and upload them to GitHub.",
        "Apply early and keep learning new skills.",
        "Create a strong LinkedIn profile."
    ],

    "placement": [
        "Master DSA and aptitude.",
        "Practice interview questions.",
        "Build a strong resume and projects."
    ],

    "python": [
        "Python is excellent for AI and automation.",
        "Python is beginner friendly and powerful.",
        "Practice coding daily to improve."
    ],

    "study": [
        "Study consistently.",
        "Use active recall techniques.",
        "Avoid last-minute cramming."
    ],

    "github": [
        "Keep repositories organized.",
        "Write professional READMEs.",
        "Make regular commits."
    ],

    "motivation": [
        "Consistency beats intensity.",
        "You are capable of more than you think.",
        "Every expert was once a beginner."
    ]
}

# ------------------ HELP MENU ------------------ #

typing("""
📚 Available Commands

attendance
exam
internship
placement
python
study
github
motivation

cgpa
percentage
career roadmap
project ideas

date
time
help
bye
""", Fore.LIGHTGREEN_EX)

# ------------------ CHAT LOOP ------------------ #

while True:

    user = input(Fore.GREEN + "\nYou: ").lower().strip()

    save_chat("You", user)

    if user == "bye":
        break

    questions_count += 1
    achievement_check(questions_count)

    if user in ["hi", "hello", "hey"]:
        response = f"Hello {name}! How can I help you today?"

    elif user == "help":
        response = """
attendance
exam
internship
placement
python
study
github
motivation

cgpa
percentage
career roadmap
project ideas

date
time
bye
"""

    elif "time" in user:
        response = datetime.now().strftime("Current Time: %H:%M:%S")

    elif "date" in user:
        response = datetime.now().strftime("Today's Date: %d-%m-%Y")

    elif user == "cgpa":
        cgpa_calculator()
        continue

    elif user == "percentage":
        percentage_calculator()
        continue

    elif "career" in user:
        career_roadmap()
        continue

    elif "project" in user:
        project_ideas()
        continue

    else:
        found = False

        for keyword in responses:

            if keyword in user:
                response = random.choice(responses[keyword])

                topic_count[keyword] = topic_count.get(keyword, 0) + 1

                found = True
                break

        if not found:
            response = (
                "Sorry, I don't understand that yet.\n"
                "Type 'help' to see available commands."
            )

    typing("CampusBot: " + response, Fore.CYAN)
    save_chat("CampusBot", response)

# ------------------ EXIT SUMMARY ------------------ #

print("\n" + "=" * 60)

typing(f"👋 Goodbye {name}!", Fore.YELLOW)

typing(f"📊 Total Questions Asked: {questions_count}", Fore.MAGENTA)

if topic_count:
    most_topic = max(topic_count, key=topic_count.get)
    typing(f"🔥 Most Discussed Topic: {most_topic.title()}", Fore.MAGENTA)

typing("💾 Chat history saved in chat_history.txt", Fore.GREEN)

typing("🎓 Thank you for using CampusBot AI!", Fore.CYAN)

print("=" * 60)