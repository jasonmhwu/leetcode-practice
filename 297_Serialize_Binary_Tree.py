# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # use "" for null and ',' for seperator
        # encode just as leetcode format
        if not root:
            return ''
        
        ans = str(root.val) + ','
        queue = collections.deque([root])
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node.left:
                    ans += str(node.left.val) + ','
                    queue.append(node.left)
                else:
                    ans += ','
                if node.right:
                    ans += str(node.right.val) + ','
                    queue.append(node.right)
                else:
                    ans += ','
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        
        data = data.split(',')[::-1]
        root = TreeNode(str(data.pop()))
        queue = collections.deque([root])
        while queue and data:
            node = queue.popleft()
            left, right = data.pop(), data.pop()
            if left != '':
                node.left = TreeNode(int(left))
                queue.append(node.left)
            if right != '':
                node.right = TreeNode(int(right))
                queue.append(node.right)
        return root
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
