import streamlit as st

def show_profile():
    st.write("# Profile")

    st.markdown("## Vaibhav Mahajan")
    st.markdown("B.Tech Student in AI and Data Science")
    st.markdown("Nagpur, India")

    social_cols = st.columns(3)
    with social_cols[0]:
        st.markdown("[GitHub](https://github.com/10Vaibhav)")
    with social_cols[1]:
        st.markdown("[Twitter/X](https://x.com/Vaibhav04102004)")
    with social_cols[2]:
        st.markdown("[Email](mailto:vaibhavmahajan43810@gmail.com)")


    st.markdown("### About Me")
    st.write("""
    I am a B.Tech student specializing in Artificial Intelligence and Data Science from Nagpur, India. 
    I'm passionate about exploring new technologies and developing practical applications.
    This Mortgage Repayments Calculator is my first web application built using Streamlit.
    """)

    st.markdown("### Education")
    st.write("**B.Tech in AI and Data Science**")
    st.write("*University/College Name, Nagpur*")
    st.write("Expected Graduation: 20XX")

    st.markdown("### Skills")
    skills = ["Python", "Data Science", "Machine Learning", "Streamlit", "Data Visualization"]

    skill_cols = st.columns(3)
    for i, skill in enumerate(skills):
        with skill_cols[i % 3]:
            st.markdown(f"- {skill}")

    st.markdown("### Projects")
    st.write("**Mortgage Repayments Calculator**")
    st.write("A Streamlit web application to calculate mortgage payments based on loan amount, interest rate, and loan term.")


if __name__ == "__main__":
    show_profile()