"""Validation et classement temporel des extraits du projet Clipper."""
from decimal import Decimal


def validate_bounds(row, low, high):
    start, end = Decimal(str(row["start"])), Decimal(str(row["end"]))
    if row["start"] < low or row["end"] > high or row["end"] <= row["start"]:
        return "bornes inversées ou hors du bloc source"
    if not 120 <= end - start <= 300:
        return "durée hors de l’intervalle de 120 à 300 s"
    return ""


def overlaps(a, b):
    s1, e1, s2, e2 = [Decimal(str(v)) for v in (a["start"], a["end"], b["start"], b["end"])]
    common = max(0, min(e1, e2) - max(s1, s2))
    return 5 * common >= min(e1 - s1, e2 - s2)


def merge(rows, limit):
    kept, rejected = [], []
    for row in sorted(rows, key=lambda c: (-c["score"], c["start"], c["end"], c["topic"])):
        reason = None
        if any(overlaps(row, old) for old in kept):
            reason = "chevauchement d’au moins 20 % avec un candidat mieux classé"
        elif len(kept) >= limit:
            reason = f"plafond de {limit} candidats"
        if reason:
            rejected.append(f"{row['topic']} — {reason}")
        else:
            kept.append(row)
    return kept, rejected
