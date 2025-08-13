
# Email Verification 

This project is a **Python-based email verification tool** that validates the format of an email address using logical checks—no external APIs required.  
It ensures that the entered email meets common standards like length, starting character, presence of `@`, and correct domain formatting.

## Features

- ✅ Checks minimum email length (>= 6 characters)
- ✅ Ensures the first character is an alphabet
- ✅ Validates that `@` is present exactly once
- ✅ Ensures the `.` (dot) is in the correct position (3rd or 4th from the end)
- ✅ Rejects:
  - Spaces
  - Uppercase letters
  - Special characters other than `_`, `.`, and `@`
- ✅ Works for both Gmail and general email formats


## Example Run

**Valid email:**

Enter your Email : [shreya@gmail.com](mailto:shreya@gmail.com)
Right email

**Invalid email (space inside):**

Enter your Email : shreya @gmail.com
Wrong email 5 (contains space, capital letter, or invalid character)

## How It Works

1. **Length Check** – Email must be at least 6 characters.
2. **First Character Check** – Must be an alphabet letter.
3. **@ Validation** – Must contain `@` exactly once.
4. **Dot Position Check** – Must have a dot either 3 or 4 characters from the end.
5. **Character Validation** – Only allows lowercase alphabets, digits, `_`, `.`, and `@`.

## Technologies Used

* **Language**: Python 3.x
* **Modules**: No external dependencies (pure Python)

## How to Run

1. Clone the repository:

   git clone https://github.com/shreyakesharwani-7/Email_Varification.git
   cd Email_Varification

2. Run the script:

   python gmail.py
   
3. Enter an email address when prompted.

## Author

**Shreya Kesharwani**
🎓 B.Tech (2023–2027) @ AKTU
📧 Email: [shreyakesharwani5524@gmail.com](mailto:shreyakesharwani5524@gmail.com)
📱 Contact: 7054429293
💻 GitHub: [shreyakesharwani-7](https://github.com/shreyakesharwani-7)
💼 LinkedIn: [Shreya Kesharwani](https://www.linkedin.com/in/shreyakesharwani70/)
🌐 GeeksforGeeks: [Profile](https://www.geeksforgeeks.org/user/shreyakesharwani/)

## License

This project is open-source and free to use for educational and personal purposes.
