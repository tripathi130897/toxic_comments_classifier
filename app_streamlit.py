from fastai.text.all import *
import streamlit as st
path = Path(__file__).parent
learn = load_learner(path/'saved'/'export_win10.pkl')

st.header('Comments')


padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)


st.markdown(f'''
<style>

.comment-author {{
  font-weight: 600;
font-size: 17px;
letter-spacing: 0.5px;
color: #547ef8;
 }}

.comment-time {{
  font-size: 11px;
    margin-left: 10px;
    color: #a7a5a5;
    border-bottom: 1px solid #ddd;
  }}

.comment-content {{
  font-size: 16px;
  font-weight: 100;
  padding-bottom: 0px;
  line-height: 25px;
  letter-spacing: 1px;
      color: #888888;
}}

</style>''', unsafe_allow_html = True)



col1, col2 = st.beta_columns((1,13))
with col1:
    img = st.image("https://cdn.iconscout.com/icon/free/png-256/avatar-375-456327.png")
with col2:
    st.markdown(f'''<p><span class='comment-author'>Rajesh Gupta</span>   <span class='comment-time'>30 minutes ago</span></p>
                    <p class="comment-content">Maecenas eu maximus tellus, vel placerat massa. Nullam neque magna, ac lacinia in, consequat nec ipsum. Vivamus tincidunt fringilla diam et sagittis. Suspendisse tincidunt hendrerit nisi, sit amet aliquet enim ornare at.</p>''',
                unsafe_allow_html = True)
    st.write('')



col1, col2, col3 = st.beta_columns((1.1,1.1,13))
with col2:
    img = st.image("https://cdn.iconscout.com/icon/free/png-256/avatar-366-456318.png")
with col3:
    st.markdown(f'''<p><span class='comment-author'>Amit Pradhan</span>   <span class='comment-time'>10 minutes ago</span></p>
                    <p class="comment-content">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>''',
                unsafe_allow_html = True)
    st.write('')


    
col1, col2 = st.beta_columns((1,13))
with col1:
    img = st.image("https://cdn.iconscout.com/icon/free/png-256/avatar-375-456327.png")
with col2:
    st.markdown(f'''<p><span class='comment-author'>Rajesh Gupta</span>   <span class='comment-time'>5 minutes ago</span></p>
                    <p class="comment-content">Nullam neque magna, hendrerit ac lacinia in, consequat nec ipsum. Vivamus tincidunt fringilla diam et sagittis. Suspendisse tincidunt hendrerit nisi, sit amet aliquet enim ornare at.</p>''',
                unsafe_allow_html = True)
    st.write('')


cont = st.beta_container()

def show_user_comment(text):
    col1, col2 = cont.beta_columns((1,13))
    with col1:
        img = st.image("https://cdn.iconscout.com/icon/free/png-256/avatar-370-456322.png")
                
    with col2:
        st.markdown(f'''<p><span class='comment-author'>You</span>   <span class='comment-time'>now</span></p>
                                <p class="comment-content">{text}</p>''',
                                unsafe_allow_html = True)
        st.write('')    
    


if 'texts' not in st.session_state:
    st.session_state.texts = []
else:
    for txt in st.session_state.texts:
       show_user_comment(txt) 


with st.form('Form', clear_on_submit=True): 
    text = st.text_area("Write what's on your mind")
    btn = st.form_submit_button('Comment')
    

if btn and text is not '':
    toxic = list(learn.predict(text)[0])
    if toxic:
        st.error(f"Failed: Your comment seems to be {' , '.join([i.upper() for i in toxic])}. Posting such comments are not allowed here.")
    else:
        st.session_state.texts.append(text)
        show_user_comment(text)
        st.success('Your Comment has been posted')

with st.sidebar:
    st.header('Identify Toxic Comments')
    st.write('The threat of abuse and harassment online means that many people stop expressing themselves and give up on seeking different opinions.')
    st.write('This Demo app shows how we can restrict users from posting such toxic comments online')
    st.write('Types of Toxicity:')
    for i in ['toxic','severe_toxic','obscene','threat','insult','identity_hate']:
        st.text(f' \t --{i}')
    
    with st.beta_expander('Dataset Link'):
        st.write('https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data')          
