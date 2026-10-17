# Software-Testing

Automation test scripts for **AttendX**, a student attendance application.
Maintained by the QA team in Git so scripts are no longer shared over email or pen drives.

## Scripts

| File | What it tests |
|------|---------------|
| `login_test.py` | Faculty user can log in and reach the Dashboard |
| `attendance_marking_test.py` | Faculty can mark a student present for a lecture and save it |

## Tools
- Python 3
- Selenium WebDriver (Chrome)

## How to run
```
pip install selenium
python login_test.py
python attendance_marking_test.py
```
