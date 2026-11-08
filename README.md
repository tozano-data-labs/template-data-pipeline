# template-data-pipeline

Dépôt modèle pour créer un pipeline de données reproductible : structure, CI
partagée, Docker, pre-commit et tests prêts à l'emploi.

> Utiliser ce dépôt comme *template repository* GitHub, puis adapter les noms.

## Structure

```text
.
├── .github/workflows/ci.yml   # CI via shared-workflows@v1
├── pipelines/                 # code Python d'ingestion
├── transformation/            # projet dbt
├── Dockerfile
├── docker-compose.yml
├── .pre-commit-config.yaml
└── docs/adr/                  # décisions d'architecture
```

## Démarrage

```bash
cp .env.example .env
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
pre-commit install
pytest
```

```bash
docker compose run --rm pipeline
```

## CI

`.github/workflows/ci.yml` appelle :

- `ci-python` (ruff + pytest, couverture ≥ 80 %)
- `ci-dbt` (dbt deps, parse, build)
- `docker-build` (build, hadolint, Trivy)
- `dependency-review` et `pr-title` sur les PR

Tous proviennent de
[`tozano-data-labs/shared-workflows`](https://github.com/tozano-data-labs/shared-workflows) `@v1`.

## Règles

- Commits : `<gitmoji> <type>(<scope>): <description en anglais>`.
- `.env` n'est jamais commité ; seul `.env.example` l'est.
- Données d'exemple publiques ou synthétiques uniquement.
- Un changement = un test.
