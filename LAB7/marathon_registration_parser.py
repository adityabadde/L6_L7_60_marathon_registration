def format_bib_name(name):
    """
    Upper-cases a runner's name and cuts it to 12 characters for the bib.
    Invalid non-string inputs return an empty string.
    """
    if not isinstance(name, str):
        return ""
    return name.strip().upper()[:12]


def parse_finish_time(text):
    """
    Converts a valid H:MM:SS finish time into seconds.
    Returns None when the input is invalid.
    """
    if not isinstance(text, str):
        return None

    parts = text.split(":")
    if len(parts) != 3 or not all(part.isdigit() for part in parts):
        return None

    hours, minutes, seconds = map(int, parts)
    if minutes >= 60 or seconds >= 60:
        return None

    return hours * 3600 + minutes * 60 + seconds


def average_split(text):
    """
    Averages non-negative whole-number split times separated by spaces.
    Returns None when the input is invalid or empty.
    """
    if not isinstance(text, str) or not text.strip():
        return None

    try:
        splits = [int(value) for value in text.split()]
    except ValueError:
        return None

    if not splits or any(value < 0 for value in splits):
        return None

    return sum(splits) / len(splits)


def main():
    print("==== Running format_bib_name ====")
    value = input("Enter the name to print on the bib: ")
    print("Bib name:", format_bib_name(value))

    print("\n==== Running parse_finish_time ====")
    value = input("Enter a finish time as H:MM:SS (e.g. 3:45:10): ")
    print("Finish time in seconds:", parse_finish_time(value))

    print("\n==== Running average_split ====")
    value = input(
        "Enter your 5 km split times in minutes separated by spaces "
        "(e.g. 25 26 24): "
    )
    print("Average split (minutes):", average_split(value))


if __name__ == "__main__":
    main()
