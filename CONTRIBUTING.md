# Contributing

Start by reading the implemented behavior and limits in the README. Small documentation fixes, reproducible bug reports and focused improvements are welcome.

1. Open an issue describing the behavior, expected result and a minimal example. Discuss API changes before implementation.
2. Create a branch for one change. Keep existing public imports compatible or explain any migration.
3. Add a regression test for a behavior change. Prefer deterministic, offline tests.
4. Run `python -m unittest discover -s tests -v` and both example scripts.
5. Open a pull request with the problem, resulting behavior and commands actually tested.

Do not include credentials, personal records, generated engagement, or unverified claims about performance or adoption. Preserve attribution when adapting outside code.

Contributions are offered under this repository's MIT license. Report sensitive issues using SECURITY.md.
