# n = int(input())
# for i in range(n):
#     #각층을 따라 내려오면서 알게된 먹이정보
#     s = list(map(int,input().split()))
#
n = int(input())
class Trie:
    def __init__(self):
        self.root={}    #루트 dictionary로 설정

    def insert(self,words):
        cur_node = self.root
        for word in words:
            if word not in cur_node:
                cur_node[word] = {}
            cur_node = cur_node[word]
        cur_node['*'] = {}

    def print_trie(self, num, cur_node = None): ####none?
        if num == 0:
            cur_node = self.root
        for word in sorted(cur_node.keys()):
            if word != '*':
                print('--'*num , word, sep='' )
            self.print_trie(num+1,cur_node[word])

trie = Trie()
for _ in range(n):
    data = list(input().split())
    trie.insert(data[1:])
trie.print_trie(0)

