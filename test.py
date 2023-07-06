user_code = input("Enter Python code: ")

try:
    exec(user_code)
except Exception as e:
    print("An error occurred:", e)