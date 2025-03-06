#include <cstddef>
#include <unordered_map>

using namespace std;

// Definition for a Node.
class Node {
public:
  int val;
  Node *next;
  Node *random;

  Node(int _val) {
    val = _val;
    next = NULL;
    random = NULL;
  }
};

class Solution {
public:
  Node *copyRandomList(Node *head) {
    unordered_map<Node *, Node *> copied;
    Node *current = head;

    while (current != nullptr) {
      if (copied.find(current) == copied.end()) {
        copied[current] = new Node(head->val);
      }

      Node *node = copied[current];
      if (current->next != nullptr) {
        if (copied.find(current->next) == copied.end()) {
          copied[current->next] = new Node(current->next->val);
        }
        node->next = copied[current->next];
      }

      if (current->random != nullptr) {
        if (copied.find(current->random) == copied.end()) {
          copied[current->random] = new Node(current->random->val);
        }
        node->random = copied[current->random];
      }

      current = current->next;
    }

    return copied[head];
  }
};
