import requests
import streamlit as st
from PIL import Image
img = Image.open("images/g1.jpg")
st.set_page_config(page_title="LAN THIT EDUCATION SERVICES", page_icon = img, layout="wide")
page = st.sidebar.selectbox("Select a page", ["Home", "About Us", "Available Programs","Free Online Learning Resources"])

if page == "Home":
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("styles/style.css")

    img0 = Image.open("images/img1.jpg")

    with st.container():
        c1,c2 = st.columns(2)
        with c1:
            st.title("LAN THIT EDUCATION SERVICES ")
            st.subheader("Since 2023")
        with c2:
            img1 = Image.open("images/Logo.png")
            st.image(img1, width= 400)

    with st.container():
        st.write("-----")
        st.subheader("What's our priority?")
        st.subheader("We work hard to help you become a better you with BRIGHTER FUTURE!!")
        st.write(
            """
        Our company’s vision 
        - To provide affordable quality education, equipping students with knowledge and skills in their chosen stream.
       
        - To provide opportunities and shape them into future leaders, entrepreneurs and above all good human beings.
           """
        )
    

    with st.container():
        st.write("-----")
        col1, col2 = st.columns(2)
        with col1:
            st.header("Our Mission")
            st.write("##")
            st.write(
            """
             - To improve Myanmar students of all ages

             - To improve their lives and also their life-long commitment to learning. 
             
             - To achieve their potential to the fullest and help build self-confidence, both in traditional values and modern thinking. 
            
            """
            )
        with col2:
            st.empty()
  
    with st.container():
        st.write("---")
        st.header("Take the following survey to know how we can be of your best assistance.")
        edu = st.multiselect("Enter your educational background ", ['High School Graduate','College student','Has a career'])
        st.selectbox("If you have a career, please choose what your profession is ", ['None','Marketing','Engineer/technician','Teacher','Others','Rather not say'])
        st.selectbox("What kind of service are you interested in purchasing?",['Online mentoring','Tutoring for exams','Guide for taking free online courses','IELTS test preparation'])
    
    with st.container():
        st.write("---")
        st.subheader("Contact Us")
        contact_form = """
    <form action="https://formsubmit.co/mrstarkismyidol@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="text" name="age" placeholder="Enter your age" required>
        <input type="email" name="email" placeholder="Your email" required>
        <select name="background" required>
        <option value="" disabled selected>Choose your educational background</option>
        <option value="High school graduate">High school graduate</option>
        <option value="College/University student">College/University student</option>
        <option value="Has a career">Has a career</option>
        </select>
        <input type="text" name="Profession" placeholder="Type the profession option you chose above" required>
        <input type="text" name="Program" placeholder="Type the program you chose above" required>
        <button type="submit">Send</button>
    </form>
    """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()


elif page == "About Us":
    img1 = Image.open("images/SHP.jpg")
    img2 = Image.open("images/TPL.png")
    img3 = Image.open("images/HAT.png")
    img4 = Image.open("images/MKK.jpg")
    img5 = Image.open("images/HZH.png")
    st.header("About Us")
    col3,col4 = st.columns((2,1))
    with col3:
        st.write("""Lan Thit is an educational guide services company that provides academic and career technical training, as well as other workforce development training, primarily to at-risk youths and adults 
                 """)
    with col4:
       st.empty()
    st.container()
    st.write("---")
    s1,s2 = st.columns((1,2))
    with s1:
        st.image(img1)
    with s2:
        st.subheader("Swam Htet Paing")
        st.write("""
        (Manager, course instructor)
        Higher Diploma in Mechanical Engineering
        """)
        st.write("Email : SwamHtetMET@gmail.com")
    t1,t2 = st.columns((1,2))
    with t1:
        st.image(img2)
    with t2:
        st.subheader("Thar Phyo Linn")
        st.write("""
        (Director, consultant)
        Higher Diploma in Infrastructure and Network
        """)
        st.write("Email : tharphyolinn@st.auston.edu.mm")
    h1,h2 = st.columns((1,2))
    with h1:
        st.image(img3)
    with h2:
        st.subheader("Hnin Aye Thu")
        st.write("""
        (Consultant)
        Higher Diploma in Infrastructure and Network
        """)
        st.write("Email : koonmyatmay@gmail.com")
    m1,m2 = st.columns((1,2))
    with m1:
        st.image(img4)
    with m2:
        st.subheader("Min Khant Kyawe")
        st.write("""
        (Head of marketing)
        Higher Diploma in Infrastructure and Network
        """)
        st.write("Email : minkhantkyawe@st.auston.edu.mm")
    h1,h2 = st.columns((1,2))
    with h1:
        st.image(img5)
    with h2:
        st.subheader("Hein Zay Htet")
        st.write("""
        (Coach, course supervisor)
        Higher Diploma in Mechanical Engineering
        """)
        st.write("Email : heinzayhtet@st.auston.edu.mm")

elif page == "Available Programs":
    st.header("Courses we offer ")
    st.write("All on this list has great feedbacks and we're working on creating more as the demand grows")
    img1 = Image.open("images/oc.jpg")
    img2 = Image.open("images/oc2.jpg")
    img3 = Image.open("images/oc3.jpg")
    img4 = Image.open("images/oc5.jpg")
    c1,c2 = st.columns(2)
    with c1:
        st.image(img1)
        st.subheader("Online Mentoring")
        st.write("We arrange to give you the best mentors suitable with your needs, studying plans and career goals.")

    with c2:
        st.image(img4)
        st.subheader("Test preparation")
        st.write("We ask you for your permission to be part of your successful academic life by giving you the best tutor to help with your upcoming exams and tutorials.")

    c1,c2 = st.columns(2)
    with c1:
        st.image(img3)
        st.subheader("Guide for taking free courses")
        st.write("In today's digital age, tons of online resources are available to learn but choosing the right materials can sometimes be overwhelming. We offer you a personal guide for helping you decide which courses suit you best.")

    with c2:
        st.image(img2)
        st.subheader("IELTS test preparation")
        st.write("An effective 3-4 months class specifically designed based on the needs of the students to get their desired band scores.")

elif page == "Free Online Learning Resources":
    st.header("The following are reputable resources for self-learning students")
    img1 = Image.open("images/calculus.jpg")
    img2 = Image.open("images/ml.jpg")
    img3 = Image.open("images/MIT.jpg")
    img4 = Image.open("images/burmaacademy.png")
    img5 = Image.open("images/khan academy.png")
    img6 = Image.open("images/classical.jpg")
    img7 = Image.open("images/Brilliant.jpg")
    img8 = Image.open("images/cs502.jpg")
    img9 = Image.open("images/laplace.jpg")

    
    c1,c2 = st.columns((1,2))
    with c1:
        st.image(img1)
    with c2:
        st.subheader("Full College Calculus")
        st.write("Informative calculus 1-3 course taught by well-known math professor Lenoard.")
        st.write("[Go to course>](https://youtu.be/fYyARMqiaag)")
    
    c1,c2 = st.columns((1,2))
    with c1:
        st.image(img2)
    with c2:
        st.subheader("Machine Learning Specialization")
        st.write("A concise course taught by famous AI researcher, teacher Andrew Ng providing valuable machine learning knowledge and insights of how ML algorithms work.")
        st.write("[Go to Course>](https://www.coursera.org/specializations/machine-learning-introduction)")

    c1,c2 = st.columns((1,2))
    with c1:
        st.image(img4)
    with c2:
        st.subheader("Cyber Security")
        st.write("Free cyber security course by Burma Academy.")
        st.write("[Go to Course>](https://burma.ac/courses/course-v1:SpringUniversityMyanmar+CS001+2022_CS001/about)")

    c1,c2 = st.columns((1,2))
    with c1:
        st.image(img5)
    with c2:
        st.subheader("Electrical Engineering")
        st.write("Introductory course about EE from Khan Academy including topics such as circuit analysis, signal processing etc.")
        st.write("[Go to Course>](https://www.khanacademy.org/science/electrical-engineering)")

    c1,c2 = st.columns((1,2))
    with c1:
        st.image(img6)
    with c2:
        st.subheader("Classical Control Theory")
        st.write("Best free control course available online from youtube channel'Brian Douglas.'")
        st.write("[Go to Course>](https://www.youtube.com/watch?v=oBc_BHxw78s)")

    c1,c2 = st.columns((1,2))
    with c1:
        st.image(img3)
    with c2:
        st.subheader("MIT Physics 801")
        st.write("College physics course taught by Dutch astrophysicist Dr.Walter Lewin.")
        st.write("[Go to Course>](https://youtu.be/wWnfJ0-xXRE)")
    
    c1,c2 = st.columns((1,2))
    with c1:
        st.image(img7)
    with c2:
        st.subheader("Complex numbers")
        st.write("Free course from brilliant about complex numbers, imaginary numbers and more.")
        st.write("[Go to Course>](https://brilliant.org/wiki/complex-numbers/)")

    c1,c2 = st.columns((1,2))
    with c1:
        st.image(img8)
    with c2:
        st.subheader("CS50 Computer Science Course")
        st.write("Free college level CS course from CS50 teaching topics such as intro to programming, web development, data structures and algorithms and more.")
        st.write("[Go to Course>](https://youtu.be/8mAITcNt710)")

    c1,c2 = st.columns((1,2))
    with c1:
        st.image(img9)
    with c2:
        st.subheader("Laplace Transform")
        st.write("Arguably the best Laplace transform video on YouTube taught by youtuber 'blackpenredpen.'")
        st.write("[Go to Course>](https://youtu.be/ftnpM_RO0Jc)")




