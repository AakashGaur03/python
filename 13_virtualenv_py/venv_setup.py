# # ✅ Step 1: Create a virtual environment named `.venv`
# python3 -m venv .venv

# # ✅ Step 2: Activate the virtual environment (for macOS/Linux)
# source .venv/bin/activate

# # ✅ Step 3: Check Python version inside venv
# python --version
# # Output: Python 3.13.3

# # ✅ Step 4: Check installed packages (should only show pip initially)
# pip list
# # Output:
# # Package Version
# # ------- -------
# # pip     25.1.1

# # ✅ Step 5: Install required packages (example: pymongo)
# pip install pymongo

# # ✅ Step 6: Confirm package installation
# pip list
# # Output:
# # Package   Version
# # --------- -------
# # dnspython 2.7.0
# # pip       25.1.1
# # pymongo   4.13.2

# # ✅ Step 7: Export installed packages to a requirements file
# pip freeze > requirements.txt

# # ✅ Step 8: Reinstall all packages from requirements file (useful for others or re-setup)
# pip install -r requirements.txt

# # In final to exit venv environemt
# deactivate