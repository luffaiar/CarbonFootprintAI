def get_badge(score):

    if score < 15:
        return "🌿 Green Hero"

    elif score < 30:
        return "🌱 Eco Warrior"

    else:
        return "♻ Carbon Fighter"