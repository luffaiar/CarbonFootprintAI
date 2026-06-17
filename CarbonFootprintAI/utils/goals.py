def get_goal_status(score):

    target = 20

    if score <= target:
        return "🎉 Goal Achieved!"

    return f"Reduce {score-target:.2f} points to reach your target."