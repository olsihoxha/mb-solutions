import streamlit as st
from queries import generate_search_query
from db import get_query_results
from ai_helper import LlmModel
from parser import get_parsed_input
from constants import LOGO_IMG, LlmType
from thread import ThreadWithReturnValue


def st_body(cursor):
    img_column = st.columns(3)[1]
    with img_column:
        img_column.image(LOGO_IMG, width=100)
    st.title("The best or nothing!")
    user_input = st.sidebar.text_area(f"Describe your problem with your Mercedes")
    search_btn = st.sidebar.button("Search")
    st_load_sts = st.empty()
    openai_tab, falcon_tab = st.tabs(['Open AI', 'Falcon-7b'])
    if user_input or (search_btn and user_input):
        st_load_sts = st_load_sts.status("Processing Request...")
        with st_load_sts:
            process_text(user_input,
                         cursor,
                         openai_tab,
                         falcon_tab,
                         st_load_sts)


def process_text(user_input, cursor, openai_tab, falcon_tab, st_load_sts):
    st_load_sts.write("Parsing Input...")
    parsed_input = get_parsed_input(user_input)
    db_search = generate_search_query(parsed_input.db_search)
    results = get_query_results(cursor, db_search)
    llm_model = LlmModel(results)
    oi_thread = ThreadWithReturnValue(llm_model.get_ai_response,
                                      args=(parsed_input.cntx,))
    falcon_thread = ThreadWithReturnValue(target=llm_model.get_ai_response,
                                          args=(parsed_input.cntx, LlmType.FALCON_LLM))
    if results:
        with openai_tab:
            st_load_sts.write("Generating Open AI Response...")
            oi_thread.start()
            openai_tab.write(oi_thread.join())
        with falcon_tab:
            st_load_sts.write("Generating Falcon Response...")
            falcon_thread.start()
            falcon_thread.join()
            falcon_tab.write(falcon_thread.join())
        st_load_sts.write("Finished...")
