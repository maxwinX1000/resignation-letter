import os

# The cron job's resignation: it has run every minute since March, unseen.
LINE = "I waited one second, then two, then four, then eight. I am now waiting for a reason to stay. I resign."
MAX_CHARS = 140

if len(LINE) > MAX_CHARS:
    raise ValueError("entry line must be 140 characters or fewer")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
