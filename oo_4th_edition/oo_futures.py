import ast
import time
from asyncio import futures
from pathlib import Path
from typing import NamedTuple, Set

from oo_helper_funcs import all_source


class ImportResult(NamedTuple):
    path: Path
    imports: Set[str]

    @property
    def focus(self) -> bool:
        return "typing" in self.imports


class ImportVisitor(ast.NodeVisitor):
    def __init__(self):
        self.imports: Set[str] = set()

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            self.imports.add(alias.name)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        if node.module:
            self.imports.add(node.module)


def find_imports(path: Path) -> ImportResult:
    tree = ast.parse(path.read_text())
    iv = ImportVisitor()
    iv.visit(tree)
    return ImportResult(path, iv.imports)


def main():
    start = time.perf_counter()
    base = Path.cwd().parent

    with futures.ThreadPoolExecutor(24) as pool:
        analyzers = [
            pool.submit(find_imports, path) for path in all_source(base, "*.py")
        ]
        analyzed = (worker.result() for worker in futures.as_completed(analyzers))
        for example in sorted(analyzed):
            print(
                f"{'->' if example.focus else '':2s} "
                f"{example.path.relative_to(base)} {example.imports}"
            )
        end = time.perf_counter()
        rate = 1000 * (end - start) / len(analyzers)
        print(f"Searched {len(analyzers)} files at {rate:.3f}ms/file")





