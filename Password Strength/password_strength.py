import re

def assess_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None

    # Calculate strength score
    strength_score = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_criteria])

    # Determine strength level
    if strength_score == 5:
        strength_level = "Very Strong"
    elif strength_score == 4:
        strength_level = "Strong"
    elif strength_score == 3:
        strength_level = "Moderate"
    elif strength_score == 2:
        strength_level = "Weak"
    else:
        strength_level = "Very Weak"

    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_criteria:
        feedback.append("Password should include at least one special character.")

    return strength_level, feedback

def main():
    print("Welcome to the Password Strength Assessment Tool!")
    password = input("Enter your password: ").strip()

    strength_level, feedback = assess_password_strength(password)

    print(f"Password Strength: {strength_level}")
    if feedback:
        print("Feedback:")
        for comment in feedback:
            print(f"- {comment}")

if __name__ == "__main__":
    main()
