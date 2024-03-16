import streamlit as st 

def main():
    st.header("Page Purpose & Description")
    st.markdown("**Strain Calculator**: Calculate principal strain/strain rate for $$45^o$$ rosette gauge")
    # st.markdown("**concate**: Concate Predict & Real Data")
    # st.markdown("**regression**: Regression tool with linear & taguchi method")
    # st.markdown("**predict**: Predict result with load trained model")

if __name__ == '__main__':

    st.title("Author & License:")

    st.markdown("**Kurt Su** (phononobserver@gmail.com)")

    # st.markdown("**This tool release under [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/) license**")

    st.markdown("               ")
    st.markdown("               ")
    
    main()