import openai
import streamlit as st
# import pyperclip

# Step 1: Obtain OpenAI API key
openai.api_key = st.secrets["API_Key"]
# openai.api_key = ""


def generate_cover_letter(prompt, model, temperature, max_tokens):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    message = completions.choices[0].text
    return message

def main():
    st.set_page_config(page_title="GPT 求职信助手 OpenAI GPT Cover Letter Generator", page_icon=":guardsman:", layout="wide")
    st.title("OpenAI GPT 求职信助手\nOpenAI GPT Cover Letter Generator")
    st.markdown("根据你的能力以及职位要求，由 OpenAI GPT 帮助你生成一封专业的求职信。要想了解更多 -> https://axton.blog \n\n OpenAI GPT will help you generate a professional cover letter based on your profile and job description. To learn more -> https://axton.blog")
    
    # Get user input
    user_profile = st.text_area("输入你的特长 Your Profile:")
    job_description = st.text_area("输入职位要求 Job Description:")
    prompt = (f"Write a cover letter for this job:\n{job_description}\n\nMy profile:\n{user_profile}")
    # prompt = (f"请用中文帮我写一封求职信，我的能力描述以及工作经验：\n{user_profile}\n\n职位描述：\n{job_description}")
    model = "text-davinci-003"
    temperature = st.slider("选择随机值 Choose Temperature:", 0.0, 1.0, 0.7)
    max_tokens = st.slider("选择求职信长度 Choose Max Tokens:", 50, 500, 1000)

    if st.button("生成求职信 Generate"):
        cover_letter = generate_cover_letter(prompt, model, temperature, max_tokens)
        st.success("大功告成！求职信已经生成了！\n Success! Your Cover Letter is Ready")
        st.markdown(cover_letter)
        st.markdown("**点击以下按钮下载求职信 Click the Button to Download**")
        
        st.download_button(
            label="下载求职信 Download",
            data=cover_letter,
            file_name='cover_letter.md',
        )
        
        # if st.button("Download"):
        #     with open("cover_letter.txt", "w") as f:
        #         f.write(cover_letter)
        #         f.close()
        #         st.markdown("Your cover letter saved as **cover_letter.txt**")
        #         st.markdown("You can also find the cover letter in the **Downloads** folder")

if __name__== "__main__":
    main()
