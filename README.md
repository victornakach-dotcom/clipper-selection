# Clipper · Sélection d’extraits vidéo

Dans Clipper, plusieurs passages d’une même vidéo peuvent raconter presque la même chose. Ce module Python reprend les règles du projet qui choisissent les passages à garder pour le montage. Il travaille sur des propositions déjà horodatées et notées.

## Essayer avec cinq passages

Avec Python 3.10 ou une version plus récente, depuis le dossier du dépôt, exécute ces deux commandes. Seule la bibliothèque standard de Python est utilisée.

```sh
python demo.py
python -m unittest -v
```

La démo simule une vidéo de dix minutes consacrée à un prototype. Avec deux places disponibles, elle retient **Monter le prototype** (10 à 145 s) et **Tester le servo** (180 à 330 s). Elle explique aussi pourquoi chaque autre passage est écarté. Tu peux modifier les propositions ou la limite dans [demo.py](demo.py).

## Comment les passages sont choisis

1. Vérifier que le passage se trouve dans la vidéo et dure entre 120 et 300 secondes, bornes incluses.
2. Classer les propositions par note décroissante. En cas d’égalité, départager par début, puis par fin et par titre, en ordre croissant.
3. Écarter le passage si sa portion commune avec un passage déjà retenu atteint **20 % de la durée du plus court**. Par exemple, deux passages de 150 secondes dont 30 secondes communes atteignent exactement ce seuil.
4. Conserver les passages restants jusqu’à la limite demandée.

Les trois fonctions de [selection.py](selection.py) et les tests de bornes, de chevauchement et de capacité viennent du projet Clipper. La démo utilise des données fictives. La transcription, l’attribution des notes et le rendu vidéo relèvent de l’application complète.
