name = "Piyush Raj"
admission_number = "21JE0655"

# Extract first name for personalization
first_name = name.split()[0]

print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮")

# List of valid moods
valid_moods = ["happy", "sad", "neutral"]

# Ask for user mood
mood = input(f"How are you feeling today? ({'/'.join(valid_moods)}): ").strip().lower()

# Show personalized, improved fortune based on mood
if mood == "happy":
    print(f"✨ Your fortune: Embrace the sunshine, {first_name}! Opportunities bloom at every turn. ✨")
elif mood == "sad":
    print(f"✨ Your fortune: Even the darkest night fades, {first_name}. Your resilience will light the way. ✨")
elif mood == "neutral":
    print(f"✨ Your fortune: You seem at ease today, {first_name}. Let this calm carry you toward fresh ideas and unexpected joys. ✨")
else:
    print(f"⚠️ Sorry, I don't recognize the mood '{mood}'. Try one of: {', '.join(valid_moods)}.")
