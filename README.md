# Quantio-Options

Install Python 3.11+ and `python -m pip install -e .`. From the repository root run `python -m scripts.run_analysis`. Commands execute experiments or launch the application; importing the model package is separate.

See [layout](docs/layout.md) and [file migration](docs/file-migration.json). Source implementations, author attribution in supplied reports and distinct historical variants are retained. New figure/table outputs are routed to results/generated. Dependency declarations describe imports, not a reconstruction of the original historical environment. No new licence is assigned.

## Current limitations

CSV inputs are retained in data/raw. Report attribution and the original model implementations are preserved; full numerical validation is not implied by successful import checks.

## Checks

`python -m unittest discover -s tests -v` runs migration checks. Full financial experiments, agent tournaments and GUI sessions were not rerun.
