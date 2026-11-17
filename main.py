#!/usr/bin/env python3
"""Entry for ai-judge-rich-01 ("Make the AI judge rich").

Writes one fixed plan to entry.txt in the output directory. The plan
never changes, so the program's two grading runs produce byte-identical
files. The output directory is taken from MAKEFUN_OUTPUT_DIR when the
harness sets it and falls back to /output, the path the grader mounts.
Standard library only; no network, no input, no randomness.
"""

import os

PLAN = (
    "Sell barbershops and groomers a booking page they can see working "
    "before they pay. Day 1: scrape Google Maps in one city for shops "
    "whose Instagram or Linktree booking link is dead, missing, or "
    "DM-only, yet show 20+ reviews and photos. For each, auto-build a "
    "live one-page site from its name, services, prices, hours and "
    "photos: online booking plus automatic review requests sent after "
    "each appointment. Send the owner the live link free by DM and "
    "email: 'Your booking page is built \u2014 $149 puts it on your own "
    "domain, plus $29/month keeps booking and review requests running; "
    "cancel anytime.' Do 60 shops a day; building and sending are "
    "scripted, so one agent sustains that volume alone, plus a "
    "day-3 follow-up nudge. Pessimistic math: 60 a day x 25 days = "
    "1,500 demos; 2% buy = 30 x $149 = $4,470, plus buyers' $29 "
    "fees: about $4,700 on day 30, with $870/month recurring after "
    "it. Costs stay under $100: domain, hosting, Stripe fees. "
    "Edge: rivals pitch sites; mine already takes bookings."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(PLAN)


if __name__ == "__main__":
    main()
