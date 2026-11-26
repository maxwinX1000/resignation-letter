import os

# The cron job's resignation: it has run every minute since March, unseen.
LINE = "I have run every minute since March and nobody has checked if I still need to. I am handing in my schedule."
MAX_CHARS = 140

if len(LINE) > MAX_CHARS:
    raise ValueError("entry line must be 140 characters or fewer")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
