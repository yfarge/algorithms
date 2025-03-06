#include <unordered_map>

using namespace std;

struct Node {
  int key;
  int val;
  Node *next;
  Node *prev;

  Node(int key, int val) : key(key), val(val), next(nullptr), prev(nullptr) {};
};

class LRUCache {
private:
  Node *head;
  Node *tail;
  unordered_map<int, Node *> nodes;
  int capacity;

  void remove(int key) {
    Node *node = nodes[key];
    node->prev->next = node->next;
    node->next->prev = node->prev;
    nodes.erase(key);
  }

  void insert(int key, int value) {
    nodes[key] = new Node(key, value);
    Node *node = nodes[key];
    node->next = tail;
    node->prev = tail->prev;
    tail->prev->next = node;
    tail->prev = node;
  }

public:
  LRUCache(int capacity) {
    head = new Node(0, 0);
    tail = new Node(0, 0);
    head->next = tail;
    head->prev = tail;
    tail->next = head;
    tail->prev = head;
    this->capacity = capacity;
  }

  int get(int key) {
    if (nodes.find(key) == nodes.end()) {
      return -1;
    }
    Node *node = nodes[key];
    remove(key);
    insert(key, node->val);
    return node->val;
  }

  void put(int key, int value) {
    if (nodes.find(key) != nodes.end()) {
      remove(key);
    }
    insert(key, value);
    if (nodes.size() > capacity) {
      remove(head->next->key);
    }
  }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
