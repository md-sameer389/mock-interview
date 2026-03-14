-- Add C Programming Skill if not exists
INSERT OR IGNORE INTO skills (skill_name, keywords) VALUES ('C Programming', 'c,malloc,free,pointers,struct');

-- Python Hard Questions (Skill ID 1)
INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type, topic, code_snippet, companies, hints)
VALUES (
    1,
    'Write a Python function to find the longest substring without repeating characters.',
    'Hard',
    'sliding window,set,dictionary,substring',
    'coding',
    'Algorithms',
    'def lengthOfLongestSubstring(s: str) -> int:\n    # Your code here\n    pass',
    '["Google", "Amazon", "Facebook"]',
    '["Use a sliding window approach.", "Keep track of visited characters in a set or dictionary."]'
);

INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type, topic, code_snippet, companies, hints)
VALUES (
    1,
    'Implement a function to merge k sorted lists in Python.',
    'Hard',
    'heap,priority queue,merge',
    'coding',
    'Data Structures',
    'import heapq\n\ndef mergeKLists(lists):\n    # Your code here\n    pass',
    '["Microsoft", "Amazon", "Airbnb"]',
    '["Use a min-heap to keep track of the smallest element among the k lists."]'
);

-- Java Hard Questions (Skill ID 2)
INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type, topic, code_snippet, companies, hints)
VALUES (
    2,
    'Write a Java program to implement an LRU Cache.',
    'Hard',
    'hashmap,doubly linked list,lru,cache',
    'coding',
    'System Design',
    'class LRUCache {\n    public LRUCache(int capacity) {\n        \n    }\n    \n    public int get(int key) {\n        return -1;\n    }\n    \n    public void put(int key, int value) {\n        \n    }\n}',
    '["Google", "Amazon", "Microsoft"]',
    '["Use a HashMap for O(1) access and a Doubly Linked List to maintain order."]'
);

INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type, topic, code_snippet, companies, hints)
VALUES (
    2,
    'Implement the Median of Two Sorted Arrays algorithm in Java.',
    'Hard',
    'binary search,partition,median',
    'coding',
    'Algorithms',
    'class Solution {\n    public double findMedianSortedArrays(int[] nums1, int[] nums2) {\n        return 0.0;\n    }\n}',
    '["Google", "Apple", "Adobe"]',
    '["Try to find the partition point in both arrays such that elements on left are smaller than elements on right."]'
);

-- C++ Hard Questions (Skill ID 20)
INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type, topic, code_snippet, companies, hints)
VALUES (
    20,
    'Write a C++ program to solve the N-Queens problem.',
    'Hard',
    'backtracking,recursion,queens',
    'coding',
    'Algorithms',
    '#include <vector>\n#include <string>\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<vector<string>> solveNQueens(int n) {\n        \n    }\n};',
    '["Facebook", "Amazon", "Microsoft"]',
    '["Use backtracking to place queens one by one in different columns."]'
);

INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type, topic, code_snippet, companies, hints)
VALUES (
    20,
    'Implement a Trie (Prefix Tree) in C++.',
    'Hard',
    'trie,prefix tree,insert,search',
    'coding',
    'Data Structures',
    'class Trie {\npublic:\n    Trie() {\n        \n    }\n    \n    void insert(string word) {\n        \n    }\n    \n    bool search(string word) {\n        return false;\n    }\n    \n    bool startsWith(string prefix) {\n        return false;\n    }\n};',
    '["Google", "Microsoft", "Twitter"]',
    '["Uses a tree-like structure where each node represents a character."]'
);

-- C Programming Hard Questions (New Skill)
INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type, topic, code_snippet, companies, hints)
VALUES (
    (SELECT id FROM skills WHERE skill_name='C Programming'),
    'Write a C program to reverse a linked list using recursion.',
    'Hard',
    'linked list,recursion,reverse,pointer',
    'coding',
    'Data Structures',
    'struct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nstruct ListNode* reverseList(struct ListNode* head) {\n    // Your code here\n}',
    '["Amazon", "Adobe", "Intel"]',
    '["Recursive step: reverse the rest of the list and then link the current node to the end."]'
);

INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type, topic, code_snippet, companies, hints)
VALUES (
    (SELECT id FROM skills WHERE skill_name='C Programming'),
    'Implement a memory allocator (malloc/free) in C.',
    'Hard',
    'malloc,free,memory management,pointer',
    'coding',
    'Systems',
    '#include <stddef.h>\n\nvoid* my_malloc(size_t size) {\n    // Implementation\n    return NULL;\n}\n\nvoid my_free(void* ptr) {\n    // Implementation\n}',
    '["Google", "Facebook", "Systems"]',
    '["Manage a free list of memory blocks. Use first-fit or best-fit strategy."]'
);
