# ADR 0001 — Un template reproductible avant tout

- **Statut** : accepté
- **Date** : 2026-11-07

## Contexte

Chaque nouveau pipeline doit démarrer avec la même structure, la même CI et les
mêmes garde-fous, sans recopier de configuration au cas par cas.

## Décision

Ce dépôt sert de *template repository*. Il fournit :

- une structure `pipelines/` + `transformation/` ;
- une CI mutualisée via `shared-workflows@v1` ;
- Docker, pre-commit et tests prêts à l'emploi.

## Conséquences

- Les nouveaux dépôts partent de ce template puis remplacent les modèles d'exemple.
- Toute amélioration du socle est reportée ici d'abord.
- Les secrets restent hors du dépôt ; seul `.env.example` est versionné.
