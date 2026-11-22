import unittest

import selection


def candidate(start=0, end=125, score=90):
    return {"start": start, "end": end, "topic": "Une seule idée.", "score": score,
            "reason": "Une question suivie d'une réponse complète."}


class CandidateTests(unittest.TestCase):
    def test_bounds(self):
        for start, end, ok in [(0, 120, True), (0, 119.999, False), (0, 119.9999, False), (0, 300, True),
                               (0, 300.001, False), (-1, 125, False), (189, 310, False),
                               (125, 1, False), (10, 130, True)]:
            with self.subTest(start=start, end=end):
                self.assertEqual(not selection.validate_bounds(candidate(start, end), 0, 300), ok)

    def test_overlap_and_fusion(self):
        first = candidate(0, 150)
        self.assertTrue(selection.overlaps(first, candidate(120, 270)))
        self.assertFalse(selection.overlaps(first, candidate(120.001, 270.001)))
        self.assertTrue(selection.overlaps(first, candidate(5, 140)))
        best = candidate(0, 150, 99)
        kept, refused = selection.merge([first, best, candidate(150, 290)], 15)
        self.assertEqual(len(kept), 2)
        self.assertEqual(kept[0], best)
        self.assertEqual(len(refused), 1)

    def test_maximum(self):
        rows = [candidate(i*150, i*150+125) for i in range(16)]
        kept, rejected = selection.merge(rows, 15)
        self.assertEqual((len(kept), len(rejected)), (15, 1))
