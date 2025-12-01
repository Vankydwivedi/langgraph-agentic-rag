import os
import streamlit as st
from langchain_groq import ChatGroq


class GroqLLM:
    # 👇 keep the argument name EXACTLY as used in the call sites
    def __init__(self, user_contols_input: dict):
        # but inside we can store it with any name we like
        self.user_contols_input = user_contols_input

    def get_llm_model(self):
        try:
            # model selected from the sidebar
            selected_groq_model = self.user_contols_input.get(
                "selected_groq_model", "llama-3.1-8b-instant"
            )

            # read key from environment (local env or HF Secrets)
            groq_api_key = os.getenv("GROQ_API_KEY")

            if not groq_api_key:
                st.error(
                    "Server error: GROQ_API_KEY is not set. "
                    "Please configure it in your environment / Hugging Face Space secrets."
                )
                st.stop()

            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)

        except Exception as e:
            raise ValueError(f"Error occurred while creating Groq LLM: {e}")

        return llm
