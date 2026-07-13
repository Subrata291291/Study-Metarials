username = "Subrata"
password = "Python123"

print("Username:", username)
print("Password:", password)

username_length = len(username)
password_length = len(password)

print("Username length:", username_length)
print("Password length:", password_length)

username = username.upper()
print("Username in uppercase:", username)

password = password.upper()
print("Password in uppercase:", password)

print(username[0])  # First character of username
print(password[0])  # First character of password

print(username[-1])  # Last character of username
print(password[-1])  # Last character of password


for i in range(0, username_length):
    print(username[i], end=" ")
print()  # Newline after printing username characters

for i in range(0, password_length):
    print(password[i], end=" ")
print()  # Newline after printing password characters

for i in range(0, len(username)):
    print(i, username[i])
print()  # Newline after printing username characters with indices