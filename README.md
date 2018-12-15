## Synopsis

A simple huffman encoder/decoder written in Python. Also includes a very basic Priority Queue implementation.

## Details

Given input text builds variable length Huffman codes using a binary tree based on character frequency. With the Huffman tree constructed text can be encoded or decoded.

Encoded text produces a bytes string prepended with a serialized representation of the code table. This allows the decode function to read in this table, reconstruct the original tree and decode the input.

After some testing it seems the compression ratio is around 1.8:1. Since the code table is prepended to the encoded text, it's not worth encoding shorter length strings. In order to achieve a compression ratio >1:1 it requires an input where the characters are repeated at least 6 times on average.

To encode text:
```python
from huffman import HuffmanTree
str = "This is a test string"
tree = HuffmanTree()
tree.build_tree(str)
encoded_text = tree.encode(str)
```

Then to decode text:
```python
new_tree = HuffmanTree()
decoded_text = new_tree.decode(encoded_text)
```

You can also print out the code table:
```python
tree.print_code_table()
```

## Author

Matthew Emerson

## License

Released under MIT License.