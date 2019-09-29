from typing import List, Tuple, Sequence, Dict, GenericMeta, Union
from itertools import chain
from collections import defaultdict, namedtuple
from zss import simple_distance
from zss import Node as zssNode
from copy import deepcopy
from itertools import combinations


class Node(zssNode):
    labels = {}

    def __init__(self, name):
        if name not in Node.labels:
            Node.labels[name] = len(Node.labels)
        super().__init__(name)

    @staticmethod
    def to_tree(x):
        if (
            callable(x)
            and not isinstance(x, GenericMeta)
            and hasattr(x, "__annotations__")
        ):
            node = Node(f"Fn")
            anno = deepcopy(x.__annotations__)
            if "return" in anno:
                ret = Node("return")
                ret.addkid(Node.to_tree(anno.pop("return")))
                node.addkid(ret)
            for key, val in anno.items():
                node.addkid(Node.to_tree(val))
        elif isinstance(x, GenericMeta):
            node = Node(x.__origin__)
            for child in (
                (Node.to_tree(c) for c in x.__args__) if hasattr(x, "__args__") else []
            ):
                node.addkid(child)
        else:
            node = Node(x)
        return node

    def prefix(self):
        ret = [Node.labels[self.label]]
        for c in self.children:
            ret += list(c.prefix())
        return tuple(ret)

    def deletes(self, n_done=0, max_deletes=3):
        seen = set()
        if n_done < max_deletes:
            # delete root, consider only children & grandma -<>- child
            for child in self.children:
                if child.prefix() not in seen:
                    yield child
                    seen.add(child.prefix())
                for x in child.deletes(n_done=n_done + 1, max_deletes=max_deletes):
                    if x.prefix() not in seen:
                        yield x
                        seen.add(x.prefix())
            # delete up to n children
            deletable_children = list(range(len(self.children)))
            for delete_n in range(max_deletes - n_done + 1):
                for deleted in combinations(deletable_children, delete_n):
                    n = deepcopy(self)
                    n.children = [
                        c for i, c in enumerate(n.children) if i not in deleted
                    ]
                    if n.prefix() not in seen:
                        yield n
                        seen.add(n.prefix())
                    for x in n.deletes(n_done=n_done + 1, max_deletes=max_deletes):
                        if x.prefix() not in seen:
                            yield x
                            seen.add(x.prefix())


Entry = namedtuple("Entry", "fn prefix dist is_original")


class Index:
    def __init__(self):
        self.index = defaultdict(set)

    def add(self, fn):
        fntree = Node.to_tree(fn)
        prefix = fntree.prefix()
        self.index[prefix].add(Entry(fn, prefix, 0, True))
        for delete in fntree.deletes():
            self.index[delete.prefix()].add(
                Entry(fn, delete.prefix(), simple_distance(fntree, delete), False)
            )

    def find(self, fn):
        fntree = Node.to_tree(fn)
        found = set()
        found |= self.index.get(fntree.prefix(), set())
        for delete in fntree.deletes():
            found |= self.index.get(delete.prefix(), set())
        results = {}
        for entry in sorted(found, key=lambda x: (x.dist, x.is_original)):
            if entry.fn not in results or (
                entry.fn in results and entry.dist <= results[entry.fn].dist
            ):
                results[entry.fn] = entry
        return list(results.values())


if __name__ == "__main__":

    def fn(x: Dict[str, List[int]], y: float) -> float:
        return 1

    def q(x: Dict[str, List[int]], y: float) -> int:
        return 1

    index = Index()
    index.add(fn)
    for i in index.find(q):
        print(i)
