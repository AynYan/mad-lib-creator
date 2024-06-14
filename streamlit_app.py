import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

def generate_paragraph(noun2: str,noun1:str) -> list[str]:
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
        input_variables=['gender', 'noun2'],
        template="""= Make a madlibs. 
        In this madlibs, the following things to replace are: a verb that ends in -ed, 3 nouns, 1 adj, and 2 adverbs. 
        Use the words {ed_verb}, {noun1},{noun2},{noun3},{adj},{adv1},{adv2} to fill in the blanks.
                     """
                )

    name_chain = LLMChain(llm=llm,
                          prompt=prompt_template_name,
                          output_key='paragraph')

    chain = SequentialChain(
        chains=[name_chain],
        input_variables=['noun1', 'noun2','noun3','ed_verb','adj','adv1','adv2'],
        output_variables=['paragraph']
    )

    response = chain({'noun1': noun1,
                      'noun2': noun2
                      'ed_verb':ed_verb
                        'adj':adj
                        'adv1':adv1
                        'adv2;':adv2
                        'noun3':noun3})
    return response


# main code
st.title('Ayn Book Recommendation Center')

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
noun2 = st.text_input("Enter a noun: ")
noun3 = st.text_input("Enter a noun: ")
adv2 = st.text_input("Enter an adverb: ")
adv1 = st.text_input("Enter an adverb: ")
adj = st.text_input("Enter an adjective: ")
ed_verb = st.text_input("Enter a verb that ends in -ed: ")
# get the answer from LLM
if noun1 and noun2 and noun3 and adv2 and adv1 and adj and ed_verb:
    response = generate_paragraph(noun1, noun2,noun3, adj,adv1, adv2, ed_verb)
    paragraph = response['paragraph'].strip().split(",")
    st.write("** Madlibs **")

    for word in paragraph:
        st.write("--", word)
