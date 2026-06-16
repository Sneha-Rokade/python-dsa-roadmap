# LOGGING IN PYTHON

## What is Logging?

Logging is the process of recording events that happen while a program runs.
Example: print("User Logged In")
This works during development.

But in production systems: logging.info("User Logged In")
is preferred.

# Why Not Use print()?

Imagine:
print("Database Connected")
print("User Logged In")
print("Payment Success")

Problems:
* No timestamps
* No log levels
* Difficult debugging
* Not suitable for production
Logging solves all these issues.

# Real World Usage

Logging is used in:
* Django
* Flask
* FastAPI
* Banking Systems
* E-Commerce Applications
* Microservices
Every production application uses logging.

# Import Logging Module

import logging
Built into Python.
No installation required.

# Basic Logging Example

import logging

logging.warning(
    "This is a warning"
)

Output: WARNING:root:This is a warning

# Logging Levels

Python provides 5 main logging levels.
DEBUG
INFO
WARNING
ERROR
CRITICAL

# DEBUG

Used during development.
import logging

logging.debug(
    "Debug Message"
)

# INFO

General information.
import logging

logging.info(
    "User Logged In"
)

# WARNING

Potential issue.
import logging

logging.warning(
    "Password Expiring Soon"
)

Output: WARNING:root:Password Expiring Soon

# ERROR

Application error.
import logging

logging.error(
    "Database Connection Failed"
)

Output: ERROR:root:Database Connection Failed

# CRITICAL

Very serious issue.
import logging

logging.critical(
    "Server Down"
)

Output: CRITICAL:root:Server Down

# Logging Levels Hierarchy

CRITICAL
ERROR
WARNING
INFO
DEBUG
Severity decreases from top to bottom.

# Configure Logging

Example:
import logging
logging.basicConfig(
    level=logging.DEBUG
)
Now all levels are shown.

# Default Behavior

Without configuration:
logging.warning()
logging.error()
logging.critical()
appear.

But:
logging.info()
logging.debug()
usually do not.

# Example
import logging

logging.basicConfig(
    level=logging.DEBUG
)

logging.debug("Debug")
logging.info("Info")
logging.warning("Warning")

Output:
DEBUG:root:Debug
INFO:root:Info
WARNING:root:Warning

# Custom Log Format

Example:
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logging.info(
    "Application Started"
)

Output: INFO: Application Started

# Add Timestamp

Example:
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

logging.info(
    "User Logged In"
)

Output: 2025-01-01 10:00:00 - User Logged In

# Log to File

Instead of console.

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info(
    "Application Started"
)

Generated: app.log

# Example app.log

INFO:root:Application Started

# Logging Exceptions

Example:

import logging

try:
    print(10 / 0)
except Exception as error:
    logging.error(error)

Output: ERROR:root:division by zero

# Logging Exception Traceback

Example:

import logging
try:
    print(10 / 0)
except Exception:
    logging.exception(
        "Exception Occurred"
    )

Shows full traceback.
Very useful.

# Real World Login Example

import logging

username = "alex"

logging.info(

    f"{username} Logged In"
)

Output: INFO: alex Logged In

# Real World Payment Example

import logging

logging.error(
    "Payment Failed"
)

Output: ERROR: Payment Failed

# Real World API Example

import logging

logging.info(
    "API Request Received"
)

Used in every backend system.

# Create Logger Object

Instead of: logging.info()
Create logger.
import logging

logger = logging.getLogger(
    __name__
)

logger.info(
    "Application Started"
)

Professional approach.

# Why Use Logger Objects?

Benefits:
* Better organization
* Module-specific logging
* Large application support
Common in Django.

# Multiple Loggers

Example:
auth_logger
payment_logger
api_logger
Used in enterprise systems.

# Django Logging Example

import logging

logger = logging.getLogger(
    __name__
)

logger.info(
    "User Created"
)
Common Django pattern.

# Django Error Logging

try:
    user.save()
except Exception as error:
    logger.error(error)
Used everywhere.

# Logging User Activity

logger.info(

    "User Updated Profile"
)
Useful for auditing.

# Logging Database Operations

logger.info(
    "Database Connected"
)
Production systems log database events.

# Logging Configuration Example

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format=
    "%(asctime)s - "
    "%(levelname)s - "
    "%(message)s"
)

logging.info(
    "Application Started"
)

Output:
2025-01-01 10:00:00
INFO
Application Started

# Common Mistakes

## Using print Instead of Logging

Bad: print("Error")
Good:
logging.error(
    "Error"
)

## Logging Sensitive Data

Bad: logging.info(password)
Never log:

* Passwords
* Tokens
* Secrets

## Ignoring Exceptions

Bad: except:
       pass
Good:
except Exception as error:
    logging.error(error)

# Best Practices

### Use Appropriate Level

Debug: logging.debug()
Information: logging.info()
Error: logging.error()

### Log Important Events

Examples:

* Login
* Logout
* Payment
* API Calls
* Database Errors

### Store Logs in Files

Production systems use log files.

### Never Log Secrets

Avoid:
* Passwords
* API Keys
* JWT Tokens

# Career Accelerator Platform Example

User Registration:
logger.info(
    "New User Registered"
)

Login Failure:
logger.warning(
    "Invalid Login Attempt"
)

Database Error:
logger.error(
    "Database Error"
)

# Interview Questions

### Q1. What is Logging?

Answer: Recording application events and errors.

### Q2. Why Use Logging Instead of print()?

Answer: Logging provides levels, timestamps, and production-ready monitoring.

### Q3. Name Logging Levels.

Answer:
DEBUG
INFO
WARNING
ERROR
CRITICAL

### Q4. Highest Logging Level?

Answer: CRITICAL

### Q5. Lowest Logging Level?

Answer: DEBUG

### Q6. Which Function Configures Logging?

Answer: logging.basicConfig()

### Q7. How To Write Logs To File?

Answer: filename="app.log"

### Q8. Which Method Logs Exceptions?

Answer: logging.exception()

### Q9. What is getLogger()?

Answer: Creates logger objects.

### Q10. Is Logging Used in Django?

Answer: Yes, extensively.

# Practice Questions

1. Configure logging.
2. Log DEBUG message.
3. Log INFO message.
4. Log ERROR message.
5. Create log file.
6. Add timestamp format.
7. Log exception.
8. Create logger object.
9. Log user login activity.
10. Build mini application logger.

# Summary

Important Concepts:

* Logging
* Log Levels
* Logger Objects
* File Logging
* Exception Logging

Important Methods:

logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()
logging.exception()
logging.getLogger()

Used In:

* Django
* Flask
* FastAPI
* Banking Systems
* Enterprise Applications

Logging is a critical production skill because real-world applications rely on logs to monitor, debug, and maintain systems efficiently.
