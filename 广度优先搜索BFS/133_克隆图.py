# !/usr/bin/python
# -*- coding: utf-8 -*-
import collections


class Solution:
    def cloneGraph(self, node):
        if not node:
            return node

        visited = dict()
        queue = collections.deque()

        while queue:
            node_u = queue.popleft()
            for node_v in node_u.neighbors:
                if node_v not in visited:
                    visited[node_v] = Node(node_v.val, [])
                    queue.append(node_v)

                visited[node_u].neighbors.append(visited[node_v])

        return visited[node]
