from langchain.llms import OpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.pydantic_v1 import BaseModel, Field
from constants import OPEN_AI_API_KEY

model = OpenAI(temperature=0.6, openai_api_key=OPEN_AI_API_KEY)


class InputObj(BaseModel):
    cntx: str = Field(..., description="""Extract the question given by the input and make it a question which includes
                                          the described problem. If there is assumption by the user 
                                          make it look so in the question too.
                                          You can fix syntax/grammar mistakes""")
    db_search: str = Field(..., description="""In the text there's going to be a descriptive intro.
                                               Create a better descriptive text that
                                               can be used for similarity search.
                                               If there is assumption by the user keep that in account.""")


def get_parsed_input(user_input):
    parser = PydanticOutputParser(pydantic_object=InputObj)
    prompt = PromptTemplate(
        template="You are an expert in analyzing the text and splitting it into what is required below,"
                 " by carefully following the descriptions in the JSON format which will be given below."
                 "\n{format_instructions}\n{query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    chain = prompt | model
    output = chain.invoke({"query": user_input})
    out = parser.invoke(output)
    return out
