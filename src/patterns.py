import re

PATTERNS = {
    "%Y-%m-%d": re.compile(r"^\d{4}-\d{2}-\d{2}$"),
    "%-m/%-d/%-y": re.compile(r"^\d{1,2}/\d{1,2}/\d{1,2}$"),
    "%b %-d, %Y": re.compile(r"^\w{3} \d{1,2}, \d{4}$"),
}
