"""Module 3/Task1"""

from datetime import datetime


def get_days_from_today(user_date: str) -> int:
    """Calculate the difference between user_date and today"""
    # Pattern for converting user_date into datetime obj
    pattern = "%Y-%m-%d"
    try:
        # Conver user_date into datetime obj
        user_date_as_datetime_obj = datetime.strptime(user_date, pattern).date()
    except ValueError:
        return "Enter the date in format like: yyyy-month-day. Example 2021-10-09"
    except TypeError:
        return f"user_date should be a string. Actual type: {type(user_date)}"
    except Exception:
        return f"Something went wrong with input: {user_date}"

    # Get today date
    today_datetime = datetime.now().date()

    # Get difference in days between user_date and today
    difference_in_days = (user_date_as_datetime_obj - today_datetime).days

    # Return difference in days as int
    return difference_in_days


if __name__ == "__main__":
    print(get_days_from_today("2024-04-15"))
