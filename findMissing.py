#!/usr/bin/env python3
"""
Compare your LeetCode solved problems against your local GitHub repo
to find which solutions are missing from the repo.

This version uses LeetCode's legacy REST endpoint (/api/problems/all/),
which is more stable than the GraphQL API for this purpose and only
needs your session cookie.

SETUP
-----
1. Log in to leetcode.com in your browser.
2. Open DevTools -> Application/Storage -> Cookies -> https://leetcode.com
3. Copy the value of the cookie named "LEETCODE_SESSION".
4. Paste it below, or set it as an environment variable:
     export LEETCODE_SESSION="..."
5. Set REPO_PATH to the local path of your cloned GitHub repo.

Run:
    pip install requests --break-system-packages
    python3 leetcode_repo_diff_v2.py
"""

import os
import re
import sys
import requests

# ---------- CONFIG ----------
LEETCODE_SESSION = os.environ.get(
    "LEETCODE_SESSION",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiMTUxMDE3NDgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjgzNWM4YzVjMThjNGRiZDQ4OWQxYmJhYzZlMTE4MmFjM2FkN2ZjOTUwNDllNWFiMDFmYTM2MmQxYmFhNWQxN2EiLCJzZXNzaW9uX3V1aWQiOiI3YWNhYWQ4YyIsImlkIjoxNTEwMTc0OCwiZW1haWwiOiJ5dXN1cGhkYXJib0BnbWFpbC5jb20iLCJ1c2VybmFtZSI6Inl1c3VwaC1kYXJibyIsInVzZXJfc2x1ZyI6Inl1c3VwaC1kYXJibyIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy95dXN1cGgtZGFyYm8vYXZhdGFyXzE3ODExMDE2NTUucG5nIiwicmVmcmVzaGVkX2F0IjoxNzg3NTgyNjE4LCJpcCI6IjJhMDY6NTkwMDo1NjI6NjcwMDo5MDA0Ojk2OWM6OTZkOjg0MDAiLCJpZGVudGl0eSI6ImEwYzVkYWUwOTQ2NGNiOTI3NjI2YjE4ZjU5MTE0OTBmIiwiZGV2aWNlX3dpdGhfaXAiOlsiODA1MzZhYTJiMWU3MGIzMzQ4ZTBmZWI3YjQ0ZGU1ZGIiLCIyYTA2OjU5MDA6NTYyOjY3MDA6OTAwNDo5NjljOjk2ZDo4NDAwIl0sIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0.P157OC3jEKTcU_aQIsF-gALqzlt_Tjm-pA1B-taB6IY",
)
REPO_PATH = "./Problems & solutions/"  # <-- update this
# -----------------------------

ALL_PROBLEMS_URL = "https://leetcode.com/api/problems/all/"

HEADERS = {
    "Referer": "https://leetcode.com",
    "User-Agent": "Mozilla/5.0",
}

COOKIES = {
    "LEETCODE_SESSION": LEETCODE_SESSION,
}


def fetch_all_solved():
    resp = requests.get(ALL_PROBLEMS_URL, headers=HEADERS, cookies=COOKIES, timeout=30)

    if resp.status_code != 200:
        print(f"Request failed: {resp.status_code}")
        print(resp.text[:1000])
        sys.exit(1)

    data = resp.json()
    pairs = data.get("stat_status_pairs", [])

    if not pairs:
        print("No problems returned - check your session cookie is valid and fresh.")
        sys.exit(1)

    solved = []
    any_status_seen = False
    for p in pairs:
        status = p.get("status")  # "ac" = accepted/solved, "notac", or None
        if status is not None:
            any_status_seen = True
        if status == "ac":
            stat = p["stat"]
            solved.append(
                {
                    "questionFrontendId": str(
                        stat.get("frontend_question_id", stat.get("question_id"))
                    ),
                    "title": stat.get("question__title"),
                    "titleSlug": stat.get("question__title_slug"),
                    "difficulty": ["", "Easy", "Medium", "Hard"][
                        p.get("difficulty", {}).get("level", 0)
                    ],
                }
            )

    if not any_status_seen:
        print(
            "WARNING: every problem came back with status=None, which usually means "
            "the session cookie isn't being recognized (expired, wrong value, or "
            "logged out). Solved counts will be 0. Re-copy LEETCODE_SESSION and try again."
        )

    return solved


def normalize_slug(name):
    # Strip file extension first (case-insensitive, before case changes)
    name = re.sub(
        r"\.(py|java|js|ts|cpp|c|go|rs|md|txt)$", "", name, flags=re.IGNORECASE
    )
    # Strip leading numbers like "0001-" or "0001_"
    name = re.sub(r"^\d+[\-\._]?", "", name)
    # Split camelCase / PascalCase boundaries: accountsMerge -> accounts Merge
    name = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "-", name)
    name = name.lower()
    # Collapse any remaining separators (spaces, underscores, etc.) to hyphens
    name = re.sub(r"[^a-z0-9]+", "-", name).strip("-")
    return name


def scan_repo_slugs(repo_path):
    found = set()
    for root, dirs, files in os.walk(repo_path):
        if ".git" in root:
            continue
        for d in dirs:
            found.add(normalize_slug(d))
        for f in files:
            found.add(normalize_slug(f))
    found.discard("")
    return found


def main():
    if "PASTE_YOUR" in LEETCODE_SESSION:
        print("Set LEETCODE_SESSION before running.")
        return

    print("Fetching solved problems from LeetCode...")
    solved = fetch_all_solved()
    print(f"Found {len(solved)} solved problems.\n")

    print(f"Scanning repo at {REPO_PATH}...")
    repo_slugs = scan_repo_slugs(REPO_PATH)
    print(f"Found {len(repo_slugs)} candidate slugs in repo.\n")

    missing = []
    for q in solved:
        if q["titleSlug"] not in repo_slugs:
            missing.append(q)

    missing.sort(key=lambda q: int(q["questionFrontendId"]))

    print(f"--- Missing from repo: {len(missing)} / {len(solved)} ---\n")
    for q in missing:
        print(
            f"{q['questionFrontendId']:>4}  {q['title']}  ({q['difficulty']})  -> {q['titleSlug']}"
        )

    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "missing_solutions.csv"
    )
    with open(out_path, "w") as f:
        f.write("id,title,slug,difficulty\n")
        for q in missing:
            f.write(
                f"{q['questionFrontendId']},{q['title']},{q['titleSlug']},{q['difficulty']}\n"
            )
    print(f"\nSaved full list to {out_path}")


if __name__ == "__main__":
    main()
