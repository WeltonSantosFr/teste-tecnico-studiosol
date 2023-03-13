import re

def check_password_rules(password, rules):
    no_match = []
    for rule in rules:
        if rule['rule'] == 'minSize' and len(password) < rule['value']:
            no_match.append('minSize')
        elif rule["rule"] == "minUppercase":
            uppercase_count = 0
            for char in password:
                if char.isupper():
                    uppercase_count += 1
            if uppercase_count < rule['value']:
                no_match.append('minUppercase')
        elif rule["rule"] == 'minLowercase':
            lowercase_count = 0
            for char in password:
                if char.islower():
                    lowercase_count += 1
            if lowercase_count < rule['value']:
                no_match.append('minLowercase')
        elif rule['rule'] == 'minSpecialChars' and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            no_match.append('minSpecialChars')
        elif rule['rule'] == 'noRepeated':
            for i in range(1, len(password)):
                if password[i] == password[i-1]:
                    no_match.append('noRepeated')
        elif rule['rule'] == 'minDigit' and sum(c.isdigit() for c in password) < rule['value']:
            no_match.append('minDigit')
    return {
        'verify': len(no_match) == 0,
        'noMatch': no_match
    }
