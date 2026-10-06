## Task explanation (selected approaches and thinking)
1. Couple of approaches were tried - finally using page.locator() with data-test as locator. Roles and values worked too, but in some of the cases locator worked better with less code to make it work. So for consistency I've decided to stick to it everywhere.
2. Test is written in simple way - just direct values and checks in it. For prod-like tests I'd prefer to do it like:
- all the values as constants and then env variables for URL and other parameters, probably secrets storage for something that should not be revealed (passwords, tokens, etc.)
- Page Object Model for pages, actions, asserts
- Fixtures for pages states (user is authorised), test values, 
- Faker for generation of test data 

## Content and how to run
### Files
- test_checkout.py - Python test file
- requirements.txt - file to install necessary libraries
### How to setup
* python -m venv .venv
* .\.venv\Scripts\Activate.ps1 (on Win)
* pip install -r requirements.txt
* playwright install chromium
### How to run (to see how it peforms actions)
* pytest -v --headed --slowmo 500