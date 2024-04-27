"""Module 3/Task3"""

import re


def extract_number_with_re_sub(number: str) -> str:
    """Extract number from the string with re.sub()"""
    comp = re.compile(r"[\s\\t()n-]+")
    parsed_number = comp.sub("", number)
    return parsed_number


def extract_number_with_re_findall(number: str) -> str:
    """Extract number from the string with re.findall()"""
    comp = re.compile("\+?[\d]+")
    parsed_number = "".join(comp.findall(number))
    return parsed_number


def validate_raw_phone(phone: str):
    """Validate raw number"""
    if not isinstance(phone, str):
        raise TypeError("Incorrect data type, phone should be a string!")

    if not phone:
        raise ValueError("Phone shouldn't be empty!")


def normilize_parsed_number(phone):
    """Normilize parsed number"""
    phone_length = len(phone)

    if phone[:4] == "+380" and phone_length == 13:
        return phone

    if ("+" not in phone) and (phone[:3] == "380") and (phone_length == 12):
        return "+" + phone

    if phone_length == 10 and "+" not in phone:
        return "+38" + phone

    if "+" in phone and phone_length == 11 and phone[1:3] != "38":
        return phone.replace("+", "+38")

    return f"Incorrect number. Couldn't parse phone: {phone}"


def normilize_phone(phone: str) -> str:
    """Normilize phone due to international format"""
    try:
        validate_raw_phone(phone)
    except Exception as e:
        return e

    extracted_phone = extract_number_with_re_findall(phone)

    return normilize_parsed_number(extracted_phone)


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "+0501234567"
    "3434343434343434343434",
]


if __name__ == "__main__":
    sanitized_numbers = [normilize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
