import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

def generate_paragraph(noun2: str,noun1:str,noun3:str,adv1:str,adv2:str,adj:str,ed_verb: str) -> list[str]:
    """
    Generate a list of 5 baby names

    Parameters:
    noun2 (str): a
    noun1 (str) : b
    noun3 (str): f
    adv1 (str) : e
    adv2 (str) : c
    ed_verb (str) :  d
    adj(str): g
    

    Returns:
    paragraph: madlibs filled in paragraph
    """

    prompt_template_name = PromptTemplate(
        input_variables=['noun1', 'noun2','noun3','adv1','adv2','adj','ed_verb'],
        template="""= Write a fun paragraph. Randomly replace a 3 nouns, a verb ending in ed, 2 adverbs, and an adjective with what i give you.
3 nouns - {},{},{}
verb ending in -ed - {}
2 adverbs - {},{}
adjective - {}""".format(noun1,noun2,noun3,ed_verb,adv1,adv2,adj)
                )

    name_chain = LLMChain(llm=llm,
                          prompt=prompt_template_name,
                          output_key='paragraph')

    chain = SequentialChain(
        chains=[name_chain],
        input_variables=[],
        output_variables=['paragraph']
    )
    response = chain({})

    return response
# main code
st.title('MadLibs')

# DO NOT CHANGE BELOW ----
# get open AI key from user
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    
# initialize Open AI
import os
os.environ['OPENAI_API_KEY'] = openai_api_key
llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature = 0.6)

# DO NOT CHANGE ABOVE ----


# ask user for what they want
noun1 = st.text_input("Enter a noun: ")
noun2 = st.text_input("Enter another noun: ")
noun3 = st.text_input("Enter yet another noun: ")
adv2 = st.text_input("Enter an adverb: ")
adv1 = st.text_input("Enter another adverb: ")
adj = st.text_input("Enter an adjective: ")
ed_verb = st.text_input("Enter a verb that ends in -ed: ")
# get the answer from LLM
if noun1 and noun2 and noun3 and adv2 and adv1 and adj and ed_verb:
    response = generate_paragraph(noun1, noun2,noun3, adj,adv1, adv2, ed_verb)
    #paragraph = response['paragraph'].strip().split(",")
    paragraph = response['paragraph']

    st.write("** Madlibs **")
    st.write(paragraph)
