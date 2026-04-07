import random

japanese_words = {
    # Greetings & Basics
    "Konnichiwa": "Hello",
    "Ohayou gozaimasu": "Good morning",
    "Konbanwa": "Good evening",
    "Sayonara": "Goodbye",
    "Arigatou gozaimasu": "Thank you very much",
    "Sumimasen": "Sorry",
    "Hai": "Yes",
    "Iie": "No",
    "Hajimemashite": "Nice to meet you",
    "Yoroshiku onegaishimasu": "Please treat me well",

    # Technology & Study
    "Konpyuuta": "Computer",
    "Gijutsu": "Technology",
    "Dezain": "Design",
    "Kenkyuu": "Research",
    "Daigaku": "University",
    "Benkyou": "Study",
    "Jinkou chinou": "Artificial Intelligence",
    "Sofutowea": "Software",
    "Puroguramu": "Program",
    "Mirai": "Future",

    # Daily Life
    "Tabemono": "Food",
    "Mizu": "Water",
    "Densha": "Train",
    "Mise": "Shop",
    "Byouin": "Hospital",
    "Toshokan": "Library",
    "Ie": "Home",
    "Tomodachi": "Friend",
    "Kane": "Money",
    "Shigoto": "Work/job",

    # Numbers, Time & Colours
    "Ichi": "One",
    "Hyaku": "One hundred",
    "Kyou": "Today",
    "Ashita": "Tomorrow",
    "Ima": "Now",
    "Nani": "What",
    "Aka": "Red",
    "Shiro": "White",
    "Kuroi": "Black",
    "Ookii": "Big",

    # Culture & Values
    "Monozukuri": "The art of making things with care",
    "Gambatte": "Do your best",
    "Yume": "Dream",
    "Kokoro": "Heart",
    "Heiwa": "Peace",
    "Sakura": "Cherry Blossom",
    "Katachi": "Shape",
    "Chikara": "Strength",
    "Tabunka": "Multicultural",
    "Nihon": "Japan",
}

def japanese_quiz():
    score = 0
    questions = list(japanese_words.items())
    random.shuffle(questions)
    
    print("=" * 50)
    print("   JAPANESE WORD QUIZ — 50 Words")
    print("   Built by Vimal Raj Mandal | India")
    print("   Preparing for MEXT Japan Scholarship 2027")
    print("=" * 50)
    print()
    try:
      while True:
        num=int(input("HOW MANY WORDS YOU WANT TO PRACTICE (0-50): "))
        if num<50 and num>0:
              selected_questions = questions[:num]
              for word, meaning in selected_questions:
               answer = input(f"What does '{word}' mean? ")
               if answer.strip().lower() == meaning.lower():
                   print("Correct! Subarashii! (すばらしい — Excellent!)\n")
                   score += 1
               else:
                   print(f"Not quite. It means: {meaning}\n")

              print("=" * 50)
              print(f"Your final score: {score} / {num}")
    
              if score == num:
                  print("Perfect score! Nihongo ga jouzu desu!")
              elif score >= 40:
                  print("Excellent! You are ready for Japan!")
              elif score >= 25:
                  print("Good progress! Keep studying!")
              else:
                  print("Keep practicing! Gambatte!")
              print("=" * 50)
        else:
            print("Please Enter Number only between(0-50)")
              
        ask=input("Do you want to continue(yes/y): ")
        if ask.lower() not in ("yes","y"):
           break;
    except:
         print("Please Enter Number between(0-50)")
        
japanese_quiz() 

