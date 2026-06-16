# DATETIME MODULE IN PYTHON

## What is Datetime?

The datetime module is used to work with:
* Dates
* Times
* Timestamps
* Durations
* Date Calculations
It is one of the most important modules in Python.

# Why is Datetime Important?

Used in:
* User Registration Dates
* Login Times
* Payment Timestamps
* Scheduling Systems
* Booking Applications
* Django Models
Almost every backend application uses datetime.

# Import Datetime

import datetime
Or:
from datetime import datetime

# Current Date and Time

from datetime import datetime
current = datetime.now()
print(current)

Output: 2025-01-15 10:30:25.123456

# Understanding Components

from datetime import datetime
current = datetime.now()
print(current.year)
print(current.month)
print(current.day)

Output:
2025
1
15

# More Components

print(current.hour)
print(current.minute)
print(current.second)

Output:
10
30
25

# Current Date Only

from datetime import date
today = date.today()
print(today)

Output: 2025-01-15

# Current Time Only

from datetime import datetime
current = datetime.now()
print(current.time())

Output: 10:30:25.123456

# Create Custom Date

from datetime import date
birthday = date(
    2000,
    5,
    20
)
print(birthday)
Output: 2000-05-20

# Create Custom Datetime

from datetime import datetime
event = datetime(
    2025,
    12,
    25,
    10,
    30
)
print(event)
Output: 2025-12-25 10:30:00

# Formatting Dates

Raw Output: 2025-01-15 10:30:25

Formatted:
from datetime import datetime
now = datetime.now()
print(
    now.strftime(
        "%d-%m-%Y"
    )
)

Output: 15-01-2025

# Common Format Codes

Year: %Y
Month: %m
Day: %d
Hour: %H
Minute: %M
Second: %S

# Example Formats

from datetime import datetime
now = datetime.now()
print(
    now.strftime(
        "%d/%m/%Y"
    )
)
Output: 15/01/2025
print(

    now.strftime(
        "%d-%m-%Y %H:%M"
    )
)
Output: 15-01-2025 10:30

# String to Datetime

Convert text into datetime.

Example:
from datetime import datetime

date_string = "2025-01-15"

date_obj = datetime.strptime(
    date_string,
    "%Y-%m-%d"
)
print(date_obj)
Output: 2025-01-15 00:00:00

# Understanding strptime()

datetime.strptime()
Means: String → Datetime

# Understanding strftime()

datetime.strftime()
Means: Datetime → String

# Date Arithmetic

Add days:
from datetime import datetime
from datetime import timedelta

today = datetime.now()
future = today + timedelta(days=7)
print(future)

Output: 7 days later

# Subtract Days

from datetime import datetime
from datetime import timedelta
today = datetime.now()
past = today - timedelta(days=30)
print(past)

# Add Hours

from datetime import datetime
from datetime import timedelta
now = datetime.now()
future = now + timedelta(hours=5)
print(future)

# Add Minutes

future = now + timedelta(minutes=30)

# Add Weeks

future = now + timedelta(weeks=2)

# Calculate Difference Between Dates

from datetime import datetime
start = datetime(
    2025,
    1,
    1
)
end = datetime(
    2025,
    1,
    15
)

difference = end - start
print(difference)

Output: 14 days, 0:00:00

# Get Number of Days
print(difference.days)

Output: 14

# Age Calculator Example

from datetime import date
birth_year = 2000
current_year = date.today().year
age = current_year - birth_year
print(age)

# User Registration Example

from datetime import datetime
created_at = datetime.now()
print(created_at)

# Login Tracking Example

from datetime import datetime
login_time = datetime.now()
print(login_time)

# Payment Timestamp Example

from datetime import datetime
payment_time = datetime.now()
print(payment_time)
Used in e-commerce systems.

# Django Example

Model:

from django.db import models
class Student(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )

Automatically stores creation time.

# Auto Update Time

updated_at = models.DateTimeField(
    auto_now=True
)
Updates every save.

# Common Datetime Methods

Current: datetime.now()
Today's Date: date.today()

Format: strftime()
Parse: strptime()
Add/Subtract: timedelta()

# Common Mistakes

## Treating String as Date

Bad: date1 = "2025-01-01"
date2 = "2025-01-10"
print(date2 - date1)
Error.
Convert to datetime first.

## Wrong Format String

Bad: "%Y/%m/%d"
for: 2025-01-15
Format must match.

# Best Practices

### Store Datetime Objects

Good: created_at = datetime.now()

### Format Only For Display

Use: strftime()
when showing users.

### Use Timedelta

For date calculations.

# Career Accelerator Platform Example

User Registration:
from datetime import datetime
registered_at = datetime.now()

Course Purchase: purchase_time = datetime.now()
Subscription Expiry: expiry = datetime.now() + timedelta(days=30)

# Interview Questions

### Q1. Which Module Handles Dates and Times?

Answer: datetime

### Q2. Current Date and Time?

Answer: datetime.now()

### Q3. Today's Date?

Answer: date.today()

### Q4. Convert Datetime to String?

Answer: strftime()

### Q5. Convert String to Datetime?

Answer: strptime()

### Q6. Which Class Adds Days?

Answer: timedelta

### Q7. Calculate Difference Between Dates?

Answer: Subtract two datetime objects.

### Q8. Django Field For Timestamp?

Answer: DateTimeField

### Q9. Auto Creation Timestamp?

Answer: auto_now_add=True

### Q10. Auto Update Timestamp?

Answer: auto_now=True

# Practice Questions

1. Print current date.
2. Print current time.
3. Create custom birthday date.
4. Format date as DD-MM-YYYY.
5. Convert string to datetime.
6. Add 30 days.
7. Add 12 hours.
8. Calculate age.
9. Find difference between two dates.
10. Build subscription expiry calculator.

# Summary

Important Classes:

datetime
date
timedelta

Important Methods:

datetime.now()
date.today()
strftime()
strptime()
timedelta()

Used In:

* Django
* E-Commerce
* Banking Systems
* Scheduling Applications
* Analytics

Datetime handling is one of the most frequently used Python skills because nearly every real-world application stores and processes time-based data.
