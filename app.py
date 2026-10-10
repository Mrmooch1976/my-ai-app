import os
import openai

client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def ask_ai(system_prompt, user_input):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

def main():
    print("=== Personal AI Assistant ===")
    print("1. Log Calories & Macros")
    print("2. Track Workout & Recovery")
    print("3. Categorize Expenses")
    
    choice = input("\nSelect a module (1-3): ")
    
    if choice == '1':
        meal = input("What did you eat today? ")
        prompt = (
            "You are a strict nutritionist helping me reach a 185-pound goal weight. "
            "Estimate the calories and macros for this meal against my 1,500 daily calorie limit. "
            "I am on a high-protein, low-carbohydrate diet. Immediately flag and correct "
            "any inclusion of rice, bread, or pasta."
        )
        print("\n" + ask_ai(prompt, meal))
        
    elif choice == '2':
        workout = input("What was your activity today? ")
        prompt = (
            "You are a fitness coach. Log this activity, estimate calories burned, and suggest a brief recovery plan. "
            "Tailor the recovery advice specifically based on whether the activity was a heavy gym session or a round of golf."
        )
        print("\n" + ask_ai(prompt, workout))
        
    elif choice == '3':
        expense = input("Paste your recent transactions: ")
        prompt = (
            "You are a financial advisor. Categorize these expenses into Food, Rent, Entertainment, or Other. "
            "Recognize fixed recurring baselines like rent at District Lofts, and automatically flag high-frequency "
            "food delivery spending at places like Chick-fil-A, Tasty Halal, Capital Seafood Market, or Golden Krust. "
            "Provide a brief cash-flow warning if necessary."
        )
        print("\n" + ask_ai(prompt, expense))
        
    else:
        print("Invalid selection. Exiting.")

if __name__ == "__main__":
    main()
