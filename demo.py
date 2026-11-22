"""Classe cinq propositions fictives issues d'une vidéo de dix minutes."""
from selection import merge, validate_bounds


def main():
    video_duration = 600
    candidates = [
        {"topic": "Monter le prototype", "start": 10, "end": 145, "score": 97},
        {"topic": "Assembler le boîtier", "start": 45, "end": 185, "score": 92},
        {"topic": "Tester le servo", "start": 180, "end": 330, "score": 89},
        {"topic": "Comparer deux réglages", "start": 360, "end": 500, "score": 84},
        {"topic": "Ranger les outils", "start": 540, "end": 580, "score": 60},
    ]
    valid = []
    invalid = []
    for candidate in candidates:
        error = validate_bounds(candidate, 0, video_duration)
        if error:
            invalid.append(f"{candidate['topic']} - {error}")
        else:
            valid.append(candidate)

    kept, rejected = merge(valid, limit=2)
    print("Extraits retenus")
    for row in kept:
        print(f"  {row['start']:>3}–{row['end']:<3} s   {row['score']}/100   {row['topic']}")
    print("\nExtraits écartés")
    for message in rejected + invalid:
        print(f"  {message}")


if __name__ == "__main__":
    main()
