import streamlit as st
from PIL import Image
from pydub import AudioSegment
from io import BytesIO

# 페이지 제목
st.title("С днем рождения, моя девушка!!")

# 여자친구 사진 추가
image = Image.open("Birthday_image.jpeg")
st.image(image, caption='Happy Birthday!', use_column_width=True)

# 음악 추가
audio_file = open("happy_birthday.mp3", "rb").read()

# 스트림릿 버튼 추가
if st.button("Play Birthday Song"):
    st.audio(audio_file, format="audio/mp3")

# 페이지에 메시지 추가
st.write("""
    ### 너무너무 귀엽고 예쁘고 사랑스러운 나의 소중한 여자친구에게,

안뇽 우리자기 오늘 너무너무 생일 축하해! 벌써 우리가 알게된지 1년이 넘었네

그때부터 지금까지 함께한 모든 순간이 너무 소중해

우리 지금은 너무 멀리 있지만 매일 영상통화로 우리 귀여둥이 목소리도 듣고 

얼굴도 봐서 하루하루가 너무 행복해

우리가 함께한 날들, 함께 먹은 맛있는 음식, 너와 나눈 소소한 이야기들

힘들 때, 네가 나를 위로해줬던 그 순간들이 기억에 남아

서로가 어떻게 변해가는지, 우리 같이 공부하고 일하고 노력하고 같이 성장하는게 좋아

너랑 함께하는 모든 순간이 나에게는 소중한 기억이야. 너랑 같이 있을때 나는 제일 행복하니까!

지금은 멀리 떨어져 있지만, 우리의 사랑은 더 커지고 있는 것 같아

너와의 미래를 상상하면서 더 행복한 일들이 기다리고 있을 것 같아

빨리 한국에 와서 우리 같이 행복하게 할 생각하니까 기대된당 앞으론 더 많은 추억을 만들어갈거니까

생일 축하해, 오늘 맛있는거 많이먹고 푹 쉬고 행복한 하루 보내 ㅎㅎ

Я Тебя люблю!

""")

# 페이지 갱신 시 자동으로 음악 재생
st.write("""
    <style>
        body {
            background-color: #e60000; /* 빨강 */
            color: #ffffff; /* 화이트 */
            font-family: 'Arial', sans-serif;
        }
        audio {
            animation: bounce 5s infinite;
        }
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {
                transform: translateY(0);
            }
            40% {
                transform: translateY(-30px);
            }
            60% {
                transform: translateY(-15px);
            }
        }
    </style>
""", unsafe_allow_html=True)
