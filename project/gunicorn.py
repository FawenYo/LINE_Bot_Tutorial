import os

# Gunicorn settings
port = int(os.getenv("PORT", 8001))
bind = f"0.0.0.0:{port}"

profile = os.getenv("profile", "production")
if profile == "production":
    loglevel = "info"
else:
    # Development
    loglevel = "debug"

workers = 4
threads = 4