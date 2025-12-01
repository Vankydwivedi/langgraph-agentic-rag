import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(
            page_title="🤖 " + self.config.get_page_title(),
            layout="wide",
        )
        st.header("🤖 " + self.config.get_page_title())
        st.session_state.timeframe = ""
        st.session_state.IsFetchButtonClicked = False

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox(
                    "Select Model", model_options
                )

                # 🔐 No more API key input – use server-side env var
                st.markdown(
                    "✅ Using server-side **GROQ_API_KEY** configured by the app owner."
                )

                # Optional: small check to warn YOU if the env var is missing
                if not os.getenv("GROQ_API_KEY"):
                    st.error(
                        "Server error: GROQ_API_KEY is not set. "
                        "Please configure it in the environment / Hugging Face secrets."
                    )

            # Usecase selection
            self.user_controls["selected_usecase"] = st.selectbox(
                "Select Usecases", usecase_options
            )

            if self.user_controls["selected_usecase"] in (
                "Chatbot With Web",
                "AI News",
            ):
                # 🔐 No Tavily key input – use server-side env var
                st.markdown(
                    "✅ Using server-side **TAVILY_API_KEY** configured by the app owner."
                )

                if not os.getenv("TAVILY_API_KEY"):
                    st.error(
                        "Server error: TAVILY_API_KEY is not set. "
                        "Please configure it in the environment / Hugging Face secrets."
                    )

            if self.user_controls["selected_usecase"] == "AI News":
                st.subheader("📰 AI News Explorer ")

                time_frame = st.selectbox(
                    "📅 Select Time Frame",
                    ["Daily", "Weekly", "Monthly"],
                    index=0,
                )

                if st.button("🔍 Fetch Latest AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame

        return self.user_controls
