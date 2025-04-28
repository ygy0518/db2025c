class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end='->')

if __name__ == '__main__': # 이 파일을 직접 실행했을 때만, number를 가지고 트리를 만들고 post_order로 출력.
    numbers = [10, 15, 8, 3, 9]
    root = None

    node = TreeNode()
    node.data = numbers[0]
    root = node

    for number in numbers[1:]:
        node = TreeNode()
        node.data = number
        current = root
        while True:
            if number < current.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right
    print("BST 구성 완료")

    post_order(root)
