#!/usr/bin/python3.8
# coding: utf-8

from typing import Any, Iterable, TypeVar, ItemsView
from typing_extensions import Self
from json import dumps

X_SPACE = 2
Y_SPACE = 0
X_INDENT = ' ' * X_SPACE
X_STROKE = '─' * X_SPACE
DECO_WEIGHT = "\x1b[33m"
DECO_VALUE = "\x1b[35m"
EOL = '\n'
END = "\x1b[0m"
TNode = TypeVar("TNode", bound="Node")


class CodeSet(set):
    """A CodeSet mapping an Huffman Tree

    Just the corresponding set of (bin, item) of a Huffman Tree
    """

    def __from_tuple__(self, content, bin_str: str) -> None:
        if isinstance(content, tuple):
            self.__from_tuple__(content[0], f"{bin_str}0")
            self.__from_tuple__(content[1], f"{bin_str}1")
        else:
            self.add((bin_str, content))

    @classmethod
    def from_tuple(cls, content: tuple) -> 'CodeSet':
        codeSet = cls()
        codeSet.__from_tuple__(content[0], '0')
        codeSet.__from_tuple__(content[1], '1')
        return codeSet

    def encode(self, decoded: Iterable) -> bin:
        """Encode some Iterable

        Args:
            decoded (Iterable): Some iterable data

        Returns:
            bin: The encoded data
        """

        encoded = "1"  # need first bit to 1 to save the first 0 binary
        for item in decoded:
            for k, v in self:
                if v == item:
                    encoded += k
        return int(encoded, 2).to_bytes(len(encoded) // 8 +1, byteorder=BYTES_ORDER)  # turn to binary data

    def decode(self, encoded: bin) -> tuple:
        """Decode some binary

        Args:
            decoded (bin): Some binary data

        Returns:
            list: The decoded data
        """

        decoded = ()
        binBuffer = ""
        for bit in str(encoded)[3:]:  # return to string
            binBuffer += bit
            for k, v in self:
                if k == binBuffer:
                    encoded += k
                    decoded += (v,)
                    binBuffer = ""
        return decoded


class Leaf:

    def __init__(self, weight: int, content: Any):
        """A Leaf of the Huffman Tree

        Create a leaf of the Huffman Tree

        Args:
            weight (int): The leaf weight
            content (Any): His corresponding content
        """
        self.weight: int = weight
        self.content: Any = content

    def __add__(self, item: Self | TNode) -> TNode:
        """Adding function

        The sum symbol implementation

        Args:
            item (Self | Leaf): Some part of the tree

        Returns:
            Node: A new Node contaning itself and the tree's part
        """

        return Node(self.weight + item.weight, self, item)

    def __tree__(self, lineOffset: str) -> str:
        """Build visual tree

        Finnaly build a line of the leaf of the visual tree

        Args:
            lineOffset (str): The line offset

        Returns:
            str: The leaf line
        """

        return f" {DECO_WEIGHT}{self.weight}{END} {X_STROKE}╼ {DECO_VALUE}{dumps(self.content)}{END}"

    def __depth__(self, depthOffset: int) -> int:
        """Found Depth

        Finally found the Leaf depth relative to a parent Node

        Args:
            depthOffset (int): The relative depth to the parent Node

        Returns:
            int: The final relative depth to the parent Node
        """

        return depthOffset + 1

    def setBin(self, codeSet: CodeSet, binary: str):
        """Set binary

        Finally set the binary coreesponding to the leaf

        Args:
            codeSet (CodeSet): The CodeSet mapping the tree
            binary (str): The Leaf binary
        """

        codeSet.add((binary, self.content))

    def to_tuple(self) -> str:
        return self.content


class Node:

    def __init__(self, weight: int, left: Self | Leaf, right: Self | Leaf):
        """A Node of the Huffman Tree

        Create a node of the tree

        Args:
            weight (int): The node weight
            left (Self | Leaf): The left part
            right (Self | Leaf): The right part
        """

        self.weight: int = weight
        self.left: Node | Leaf = left
        self.right: Node | Leaf = right

    def __add__(self, item: Self | Leaf) -> Self:
        """Adding function

        The sum symbol implementation

        Args:
            item (Self | Leaf): Some part of the tree

        Returns:
            Node: A new Node contaning itself and the tree's part
        """

        return Node(self.weight + item.weight, self, item)

    def __tree__(self, lineOffset: str) -> str:
        """Spread tree build function

        Spread the recurent function to build the visual tree

        Args:
            lineOffset (str): The line offset

        Returns:
            str: The generated trunc
        """

        yIndent = f"""{lineOffset}{f"│{EOL + lineOffset}" * Y_SPACE}"""
        return f"""┮ {DECO_WEIGHT}{self.weight}{END}\n{yIndent}├{X_STROKE}{self.left.__tree__(f"{lineOffset}│{X_INDENT}")}\n{yIndent}└{X_STROKE}{self.right.__tree__(f"{lineOffset} {X_INDENT}")}"""

    def __depth__(self, depthOffset: int) -> int:
        """Spread depth founder

        Spread the recurent function to find maximal depth

        Args:
            depthOffset (int): Parent depth 

        Returns:
            int: His max depth
        """

        depthOffset += 1
        return max(self.left.__depth__(depthOffset), self.right.__depth__(depthOffset))

    @property
    def depth(self) -> int:
        """Get his depth

        Found his maximal depth of his extensions

        Returns:
            int: His max depth
        """

        return self.__depth__(0)

    def setBin(self, codeSet: CodeSet, binary: str):
        """Set binary

        Spread the binary generation in a CodeSet to his extension

        Args:
            codeSet (CodeSet): The CodeSet mapping the tree
            binary (str): The binary already generated

        """
        self.right.setBin(codeSet, f"{binary}0")
        self.left.setBin(codeSet, f"{binary}1")

    def to_tuple(self) -> tuple:
        """Convert to tuple

        Returns:
            tuple[tuple | Any]: The node in tuple format
        """
        return (self.left.to_tuple(), self.right.to_tuple())


class Root(Node):

    def __init__(self, occurence: dict):
        """The Root of the Huffman Tree

        Build an simple Huffman tree based on Leafs & Nodes

        Args:
            occurence (dict): Some Iterable occurences (at least 2)
        """

        nodes = [Leaf(v, k) for k, v in occurence]
        lenght = len(nodes)
        # Sum every time the 2 lightest nodes / leafs
        while lenght > 2:
            left = nodes[0]
            right = nodes[1]
            il = 0
            ir = 1
            i = 2
            while i < lenght:
                if (nodes[i].weight < left.weight):
                    left = nodes[i]
                    il = i
                elif (nodes[i].weight < right.weight):
                    right = nodes[i]
                    ir = i
                i += 1
            nodes.pop(il)
            nodes.pop(ir - 1 if il < ir else ir)
            nodes.append(left + right)
            lenght -= 1
        super().__init__(nodes[0].weight + nodes[1].weight, nodes[0], nodes[1])

    @property
    def tree(self) -> str:
        """A visual tree

        Create a visual representation of the tree

        Returns:
            str: The tree
        """

        return self.__tree__('')

    @property
    def codeSet(self) -> CodeSet:
        """Get his CodeSet

        Generate the CodeSet mapping the tree

        Returns:
            CodeSet: His CodeSet
        """

        codeSet = CodeSet()
        self.setBin(codeSet, '')
        return codeSet


def occurence(content: Iterable) -> ItemsView:
    """Get occurences

    Loop over content and get their apparition frequency

    Args:
        content (Iterable): The object you want to analyse 

    Returns:
        ItemsView: The results in form of: dict_items([{item, occurence}, ...])
    """

    occ = {}
    for item in content:
        if item in occ:
            occ[item] += 1
        else:
            occ[item] = 1
    return occ.items()


if __name__ == "__main__":

    import timeit
    # For bytes manipulation
    BYTES_CODEMAP = 3
    BYTES_ORDER = "big"

    def encode():
        with open("tour_du_monde.txt") as file:
            text = file.read()
            # import re
            # text = [w for w in re.split(r"(\s+)|(\n)", text) if w != None]
            root = Root(occurence(text))
            # print(root.tree)
            codemap = str(root.to_tuple()).encode("utf-8")
            with open("tour_du_monde_compressed.bin", 'wb') as file:
                # root = hufftree(occurence(bytes_))
                # codemap = str(root.to_tuple()).encode("utf-8")
                file.write((len(codemap)).to_bytes(BYTES_CODEMAP, byteorder=BYTES_ORDER) + codemap + root.codeSet.encode(text))

    def decode():
        with open("tour_du_monde_compressed.bin", "rb") as file:
            encoded = file.read()
            code_len = int.from_bytes(
                encoded[0:BYTES_CODEMAP], byteorder=BYTES_ORDER) + BYTES_CODEMAP
            codemap = CodeSet.from_tuple(eval(encoded[BYTES_CODEMAP:code_len]))
            with open("tour_du_monde_uncompressed.txt", 'w') as file:
                file.write(''.join(v for v in codemap.decode(encoded[code_len:])))

    print(f"Encoding took approximatly {timeit.timeit(encode, number=1)} ms")
    print(f"Decoding took approximatly {timeit.timeit(decode, number=1)} ms")