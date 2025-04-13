def email_validator(email):
    if "." not in email or "@" not in email:
        print("유효하지 않음")
    else:
        print("유효함")


email_validator("user@example.com")

email_validator("user@example")
