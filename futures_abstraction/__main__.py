import ast
from _ast import Import
from asyncio import Queue
from pathlib import Path
from typing import NamedTuple, Set
from typing import List, Iterator, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    Query_Q = Queue[Union[str, None]]
    Result_Q = Queue[List[str]]


print(Query_Q, Result_Q)

class ImportResult(NamedTuple):
    path: Path
    imports: Set[str]

    @property
    def focus(self) -> bool:
        return "typing" in self.imports


class ImportVisitor(ast.NodeVisitor):
    def __init__(self):
        self.imports: Set[str] = set()

    def visit_Import(self, node: Import) -> None:
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


