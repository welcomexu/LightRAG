from lightrag import LightRAG, QueryParam

rag = LightRAG(working_dir="./dickens")

with open("./book.txt") as f:
    rag.insert(f.read())

# Perform naive search
print(rag.query("What are the top themes in this story?", param=QueryParam(mode="naive")))

# Perform local search
print(rag.query("What are the top themes in this story?", param=QueryParam(mode="local")))

# Perform global search
print(rag.query("What are the top themes in this story?", param=QueryParam(mode="global")))

# Perform hybird search
print(rag.query("What are the top themes in this story?", param=QueryParam(mode="hybird")))