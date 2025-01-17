import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Ravinder Kaur - Portfolio", page_icon="💼", layout="centered")

# Sidebar for navigation
st.sidebar.title("Navigation")
sections = ["Home", "About Me", "Skills", "Education", "Experience", "Projects", "Contact"]
selection = st.sidebar.radio("Go to", sections)

# Home Section
if selection == "Home":
    st.title("Welcome to My Portfolio!")
    st.subheader("Hello! I am Ravinder Kaur 👩‍💻")
    st.markdown(
        """
        I am a passionate and dedicated Computer Science Engineering student.  
        My aim is to grow as a **Web Developer**, contributing to impactful projects and constantly learning new technologies.
        """
    )
    st.image("https://via.placeholder.com/400x200.png?text=Welcome+to+My+Portfolio", use_column_width=True)

# About Me Section
elif selection == "About Me":
    st.header("About Me")
    st.markdown(
        """
        - 🎓 **B.Tech in Computer Science Engineering** (1st year).  
        - 📚 Actively learning web development, AI, and ML.  
        - 💡 Enthusiastic about research and innovative projects.  
        - 🏅 Participated in hackathons and competitions like **Smart India Hackathon** and **Innotech**.
        """
    )

# Skills Section
elif selection == "Skills":
    st.header("Skills")
    st.markdown(
        """
        - **Frontend Development**: HTML, CSS, JavaScript, React  
        - **Backend Development**: PHP, Flask  
        - **Programming**: Python, C++, Java  
        - **Database**: SQL, MySQL  
        - **Tools**: XAMPP, Bootstrap, Canva, Video Editing
        """
    )

# Education Section
elif selection == "Education":
    st.header("Education")
    st.markdown(
        """
        - **B.Tech in Computer Science Engineering** - [GNDEC] (Current)  
        - **1-Year ITI Course in Computer Science**  
        - Completed certifications in **ReactJS, Angular, and HTML/CSS/JS**.
        """
    )

# Experience Section
elif selection == "Experience":
    st.header("Experience")
    st.markdown(
        """
        - 📍 **Infosys Springboard Internship**: React Web Development  
        - 📍 **NCC Air Wing**: Gained leadership and teamwork experience  
        - 📍 **90.8 FM Radio Community**: Technical Executive, Video Editing, Certificate Management
        """
    )

# Projects Section
elif selection == "Projects":
    st.header("Projects")
    st.markdown(
        """
        - **PropertyHub**: Web platform for buying, selling, and renting properties.  
        - **Sign Language Recognition System**: Translate real-time signs into text.  
        - **E-bin**: Smart dustbin with automatic lid and garbage level tracking.  
        - **PixelGen**: Pixel-based generative model for AI-driven images.  
        - **Hackathon Projects**: AI-powered legal documentation and generative AI solutions.
        """
    )

# Contact Section
elif selection == "Contact":
    st.header("Contact Me")
    st.markdown(
        """
        - 📧 Email: [ravinderkaur@example.com](mailto:ravinderkaur@example.com)  
        - 💼 LinkedIn: [linkedin.com/in/ravinderkaur](https://linkedin.com/in/ravinderkaur)  
        - 🌐 GitHub: [github.com/ravinderkaur](https://github.com/ravinderkaur)  
        - 📍 Location: Punjab, India
        """
    )
    st.text("Feel free to reach out to me for collaboration or opportunities!")

