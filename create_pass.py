from werkzeug.security import generate_password_hash
hashed = generate_password_hash('virat_kohli')
print(f"Password is {hashed}")
