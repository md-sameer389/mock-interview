
TECHNICAL_KEYWORDS = {
    "python": [
        "gil", "global interpreter lock", "memory management", "garbage collection", "reference counting",
        "decorator", "generator", "iterator", "list comprehension", "context manager", "with statement",
        "dynamic typing", "duck typing", "pip", "virtualenv", "asyncio", "threading", "multiprocessing",
        "pandas", "numpy", "scipy", "scikit-learn", "flask", "django", "fastapi", "sqlalchemy",
        "lambda", "map", "filter", "reduce", "args", "kwargs", "magic methods", "dunder",
        "pickling", "serialization", "unit test", "pytest", "mock", "patch",
        "cprofile", "optimization", "bottleneck", "profiling", "complexity",
        "mutable default", "bound", "io bound", "cpu bound", "vectorization", "broadcasting"
    ],
    "sql": [
        "select", "insert", "update", "delete", "join", "inner join", "left join", "right join",
        "cross join", "union", "group by", "order by", "having", "limit", "offset",
        "index", "b-tree", "clustering", "primary key", "foreign key", "constraint",
        "normalization", "denormalization", "acid", "atomicity", "consistency", "isolation", "durability",
        "transaction", "commit", "rollback", "lock", "deadlock", "query plan", "execution plan",
        "stored procedure", "trigger", "view", "materialized view", "nosql", "sharding", "partitioning"
    ],
    "machine learning": [
        "supervised", "unsupervised", "reinforcement", "regression", "classification", "clustering",
        "neural network", "deep learning", "cnn", "rnn", "lstm", "transformer", "attention",
        "gradient descent", "backpropagation", "loss function", "cost function", "optimizer", "adam", "sgd",
        "overfitting", "underfitting", "bias", "variance", "regularization", "l1", "l2", "dropout",
        "train test split", "cross validation", "k-fold", "hyperparameter", "grid search", "random search",
        "precision", "recall", "f1 score", "roc", "auc", "confusion matrix", "accuracy",
        "feature engineering", "normalization", "standardization", "pca", "dimensionality reduction"
    ],
    "java": [
        "jvm", "jre", "jdk", "bytecode", "garbage collector", "heap", "stack", "memory leak",
        "object oriented", "inheritance", "polymorphism", "encapsulation", "abstraction",
        "interface", "abstract class", "collections", "list", "set", "map", "hashmap", "arraylist",
        "concurrency", "thread", "runnable", "synchronized", "volatile", "executor service",
        "stream api", "lambda expression", "optional", "exception handling", "try-catch",
        "spring", "hibernate", "maven", "gradle", "dependency injection", "ioc container"
    ],
    "javascript": [
        "es6", "let", "const", "var", "arrow function", "destructuring", "spread operator",
        "promise", "async", "await", "callback", "closure", "scope", "hoisting", "this",
        "prototype", "inheritance", "event loop", "call stack", "microtask", "callback queue",
        "dom", "virtual dom", "event bubbling", "event capturing", "delegation",
        "npm", "yarn", "webpack", "babel", "react", "angular", "vue", "node.js"
    ],
    "react": [
        "component", "props", "state", "hook", "useeffect", "usestate", "usecontext", "usereducer",
        "virtual dom", "reconciliation", "fiber", "jsx", "fragment", "portal",
        "lifecycle", "mounting", "updating", "unmounting", "higher order component", "hoc",
        "render props", "context api", "redux", "mobx", "flux", "store", "action", "reducer"
    ],
    "cpp": [
        "pointer", "reference", "memory management", "new", "delete", "malloc", "free",
        "class", "object", "inheritance", "polymorphism", "virtual function", "pure virtual",
        "template", "stl", "vector", "map", "set", "algorithm", "iterator",
        "raii", "smart pointer", "unique_ptr", "shared_ptr", "weak_ptr",
        "move semantics", "rvalue reference", "lambda", "exception", "const", "static"
    ],
    "data structures": [
        "array", "linked list", "stack", "queue", "hash table", "hash map", "tree", "binary tree",
        "bst", "heap", "priority queue", "graph", "trie", "matrix",
        "bfs", "dfs", "sorting", "searching", "binary search", "merge sort", "quick sort",
        "dynamic programming", "recursion", "memoization", "greedy", "complexity", "big o"
    ],
    "behavioral": [
        "situation", "task", "action", "result", "star method", "team", "conflict",
        "communication", "leadership", "deadline", "mistake", "learning", "feedback",
        "improvement", "collaboration", "initiative", "challenge", "solution", "impact",
        "responsibility", "ownership", "agile", "scrum"
    ]
}

def get_keywords_for_skill(skill_name):
    """Retrieve keywords for a given skill (case-insensitive)"""
    skill_lower = skill_name.lower().strip()
    
    # Direct match
    if skill_lower in TECHNICAL_KEYWORDS:
        return TECHNICAL_KEYWORDS[skill_lower]
        
    # Partial match / Aliases
    if "data" in skill_lower and "structure" in skill_lower:
        return TECHNICAL_KEYWORDS["data structures"]
    if "js" in skill_lower or "node" in skill_lower:
        return TECHNICAL_KEYWORDS["javascript"]
    if "ml" in skill_lower:
        return TECHNICAL_KEYWORDS["machine learning"]
        
    return []
