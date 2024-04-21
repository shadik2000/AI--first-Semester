import re

def extract_emails(text: str) -> list[str]:
    # Regular expression pattern for valid email addresses
    pattern = r'\s([a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,})'
    
    # Find all matches of the pattern in the text
    matches = re.findall(pattern, text)
    
    return matches

# Example text
t = """
 Here are some email addresses:
 john.doe@example.com, alice_smith123@gmail.com, ABC+@a-b-c.aBc,
 contact@company.org, and info@sub.domain.co.uk.
 Some invalid email addresses are:
 john@, @example.com, user@domain, us/er@email.com,
 invalid@domain.f and invalid.email@invalid@domain.com.
 """

# Extract and print the valid email addresses from the text
print(extract_emails(t))
