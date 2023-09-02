__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import os
from langchain.document_loaders import UnstructuredFileLoader
from langchain.indexes import VectorstoreIndexCreator

if os.getenv("OPENAI_API_KEY") is None:
    #please enter your openai api key here
    os.environ["OPENAI_API_KEY"] = 
from langchain.document_loaders import UnstructuredFileLoader
loader = UnstructuredFileLoader(f'./Kartheek_RESUME.pdf')
from langchain.indexes import VectorstoreIndexCreator
index = VectorstoreIndexCreator().from_loaders([loader])
def get_response(user_input):
    return index.query(user_input)
st = 'True'
while st!= '' or st.lower() != "stop":
    st = input('Human: ')
    print('AI: ' + get_response(st))