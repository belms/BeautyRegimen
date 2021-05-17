from whoosh.fields import Schema, TEXT
import os
from src.whoosh import index


def load_docs(writer):
    print(f'Importing documents')
    path = f'collections'
    for files in os.walk(path, topdown=False):

        for file in files[2]:
            with open(f'{path}/{file}') as f:
                contents = f.read()
                writer.add_document(content=contents)


def create_schema_and_load_docs():
    schema = Schema(content=TEXT(stored=True))
    if not os.path.exists("my_index"):
        os.mkdir("my_index")
    ix = index.create_in("my_index", schema)
    w = ix.writer()
    load_docs(w)
    w.commit()
