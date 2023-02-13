# Constants
from typing import final


DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def add_with_ceil(ceil: int):
    # Returns the sum modulo ceil and the integer division
    return lambda *args: (sum(args) % ceil, sum(args)//ceil)


add_minutes = add_with_ceil(60)
add_hours = add_with_ceil(24)


def converter_12h_to_24h(raw_time: str) -> str:
    time, noon = raw_time.strip().split(" ")
    hours, minutes = time.split(":")
    # there might be a bug with 12:00 AM and 12:00 PM
    if int(hours) != 12:
        return time if noon == "AM" else f"{int(hours) + 12}:{minutes}"
    else:
        return time if noon == "PM" else f"{str(int(hours) - 12).zfill(2)}:{minutes}"


def converter_24h_to_12h(raw_time: str) -> str:
    hours, minutes = raw_time.strip().split(":")
    hours = int(hours)
    if hours == 0:
        return f"{'12'}:{minutes} AM"
    elif hours < 12:
        return f"{hours}:{minutes} AM"
    elif hours == 12:
        return f"{hours}:{minutes} PM"
    else:
        return f"{hours % 12}:{minutes} PM"


def add_time(start: str, duration: str, day_of_week: str = "") -> str:
    # Defining all the variables to do the sum
    initial_time = converter_12h_to_24h(start.strip())
    initial_hours, initial_minutes = [int(x) for x in initial_time.split(":")]
    plus_hours, plus_minutes = [int(x) for x in duration.strip().split(":")]
    # Doing the sum
    final_minutes, rem_hours = add_minutes(initial_minutes, plus_minutes)
    final_hours, rem_days = add_hours(initial_hours, plus_hours, rem_hours)
    final_time = f"{str(final_hours).zfill(2)}:{str(final_minutes).zfill(2)}"
    final_time = converter_24h_to_12h(final_time)
    # adding (n) days later string
    if rem_days < 1:
        days_later_str = ""
    elif rem_days == 1:
        days_later_str = " (next day)"
    else:
        days_later_str = f" ({rem_days} days later)"
    # additional strings
    if len(day_of_week) == 0:
        weekday_str = ""
    else:
        day_index = DAYS.index(day_of_week.lower())
        current_day_index = (rem_days + day_index) % len(DAYS)
        weekday_str = f", {DAYS[current_day_index].capitalize()}"
    
    return f"{final_time}{weekday_str}{days_later_str}".strip()

print(add_time("9:15 PM", "5:30"))