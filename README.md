# AI agent learning workspace

Small, local Python examples maintained by [Đào Hữu Trọng](https://github.com/DaoHuuTrong2404), an Artificial Intelligence student at Can Tho University.

This is an educational prototype. It runs without an API key or model service and is intended for studying tool dispatch, task handoffs, retrieval and simulated UI actions.

[Tiếng Việt](docs/README.vi.md) · [Contributing](CONTRIBUTING.md) · [Roadmap](docs/ROADMAP.md) · [MIT license](LICENSE)

## Try it

Requires Python 3.10 or newer. No runtime or test dependencies are required.

```sh
git clone https://github.com/DaoHuuTrong2404/autonomous-ai-agents-workspace.git
cd autonomous-ai-agents-workspace
python examples/quickstart.py
python examples/academic_researcher.py
python -m unittest discover -s tests -v
```

Optional editable installation:

```sh
python -m pip install --no-build-isolation -e .
```

The source-tree commands above work without installation. Editable installation needs setuptools 61 or newer.

## What is implemented

| Module | Current behavior | Limits |
| --- | --- | --- |
| `ReActAgent` | Routes a task using keyword rules to a calculator, text statistics or a small built-in glossary; records a trace | No LLM, planning or iterative reasoning. Unknown tasks receive a placeholder response. A completed status is not a correctness guarantee. |
| `GNAPSwarm` | Records named roles, tasks and handoffs in memory | Does not run workers, use Git, save state or verify artifacts |
| `VisionCUAAgent` | Creates a simulated click record using caller-supplied labels and boxes | No screenshot recognition, browser connection or real input; status is `SIMULATED` |
| `HybridRAG` | Ranks text chunks by lexical TF-IDF | Historical class name; no embeddings, BM25, generation or semantic retrieval |

## Example: local document search

```python
from agents import HybridRAG

search = HybridRAG()
search.add_document("notes", "Agents can call tools and record observations.")
search.add_document("other", "A binary search requires sorted input.")
print(search.search("tools", top_k=1)[0]["id"])  # notes
```

A query with no matching terms returns an empty list. `top_k=0` returns no results; negative and non-integer limits raise `ValueError`.

## Validation and intended use

The test suite covers the existing demos and regression cases for non-interactive UI targets and retrieval limits. Run it for the current checkout; a demonstration or badge does not prove production readiness.

The calculator currently uses character-restricted Python evaluation. Do not expose it to untrusted remote input or use this project as an execution sandbox. UI boxes are caller supplied and should be validated by an integration before real interaction. No external integrations are included.

The examples use manually supplied text. Search output is a retrieval result, not verified research or a generated academic citation.

## Related work

The [maintainer profile](https://github.com/DaoHuuTrong2404) indexes separate projects, coursework and upstream forks. Those repositories retain their own histories and licensing. This project does not bundle their code or claim their usage as its own.

## Contact and license

Open a GitHub issue with a minimal reproducible example. For sensitive reports, follow [SECURITY.md](SECURITY.md).

MIT © 2026 Dao Huu Trong. See [LICENSE](LICENSE).
