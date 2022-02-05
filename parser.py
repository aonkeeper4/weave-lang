from lexer import lexer

class SyntaxNode:
    def __init__(self, type, val, subnodes):
        self.type = type
        self.val = val
        self.left = None
        self.right = None
        self.key = repr(self)

    def __repr__(self):
        return f"{self.type} {self.val}"

    def display(self):
        lines, *_ = self._display_aux()
        return "\n".join(lines)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

def parser(tokens):
    tokens = list(map(lambda token: SyntaxNode(token[0], token[1], []), tokens))
    # build tree top-down?
    # ok but how

    # ok so
    # start with lists of tokens
    # start merging them in passes, ie
    # 3 + 4 
    # goes to
    # 3   4
    #  \ /
    #   +
    # and then 3 and 4 get deleted from the main list
    # so only lowest-level items are in that list
    # do passes until only 1 item is in the original list
    # but how to treat do-end blocks?

    # while len(tokens) > 1:
    #     i = 0
    #     while i < len(tokens)-1:
    #         token = tokens[i]
    #         print(i, token, len(tokens))
    #         match token.type:
    #             case "OP":
    #                 left = tokens[i-1]
    #                 right = tokens[i+1]
    #                 token.left, token.right = left, right
    #                 del tokens[i-1], tokens[i+1]
    #         i += 1

    # that didnt work sadge

if __name__ == "__main__":
    with open("test programs/big test.weave", "r") as f:
        tokens = lexer(f.read())
        parser(tokens)

