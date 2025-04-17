import random

# Personal details
name = "Piyush Raj"
admission_number = "21JE0655"

# Extract first name for personalization
first_name = name.split()[0]

print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮")

# Define valid moods and corresponding fortunes
fortunes = {
    "happy": [
        f"✨ Your fortune: Embrace the sunshine, {first_name}! Opportunities bloom at every turn. ✨",
        f"✨ Your fortune: Your laughter is a magnet for good things, {first_name}—keep it ringing. ✨"
    ],
    "sad": [
        f"✨ Your fortune: Even the darkest night fades, {first_name}. Your resilience will light the way. ✨",
        f"✨ Your fortune: This moment is just a chapter, {first_name}—better pages await. ✨"
    ],
    "neutral": [
        f"✨ Your fortune: You seem at ease today, {first_name}. Let this calm carry you toward fresh ideas and unexpected joys. ✨",
        f"✨ Your fortune: Balance is your secret strength, {first_name}. Trust its quiet wisdom. ✨"
    ],
    "stressed": [
        f"✨ Your fortune: Take a slow breath, {first_name}—you've got this under control. ✨",
        f"✨ Your fortune: Pressure can forge diamonds, {first_name}. You're shaping up beautifully. ✨"
    ]
}

valid_moods = list(fortunes.keys())

# Prompt user input
mood = input(f"How are you feeling today? ({'/'.join(valid_moods)}) | leave blank for random :) ").strip().lower()

# Choose random mood if no input
if mood == "":
    mood = random.choice(valid_moods)
    print(f"🤖 No mood entered. Picking one for you... Let's go with: {mood}")
    
if mood in fortunes:
    print(random.choice(fortunes[mood]))
else:
    print(f"⚠️ Sorry, I don't recognize the mood '{mood}'. Try one of: {', '.join(valid_moods)}.")
