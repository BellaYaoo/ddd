import warnings
import streamlit as st
import matplotlib.pyplot as plt # 确保 matplotlib 已通过 requirements.txt 安装

# Must be the first Streamlit command
st.set_page_config(page_title="personalsite", layout="wide")

# Import pages from the new directory
from page_content.home import home_page
from page_content.experience import experience_page
from page_content.education import education_page
from page_content.resume import resume_page
from page_content.contact import contact_page

# Import components
from components.footer import display_footer
from components.styles import load_css

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        # Load custom CSS
        load_css()

        st.sidebar.markdown("## Main Menu")
        app = st.sidebar.radio(
            "Navigation", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")

        app["function"]()
        
        # Display footer at the bottom of each page
        display_footer()

# Initialize the app
app = MultiApp()

# Add pages to the app
app.add_app("Home Page", home_page)
app.add_app("Education Page", education_page)
app.add_app("Experience Page", experience_page)
app.add_app("Resume Page", resume_page)
app.add_app("Contact Page", contact_page)

# Run the app
app.run()

# 例如，一个简单的页面导航
PAGES = {
    "Home": home_page,
    "Experience": experience_page,
    "Education": education_page,
    "Resume": resume_page,
    "Contact": contact_page
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page() # 调用选定页面的函数
