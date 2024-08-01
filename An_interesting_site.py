import streamlit,base64,time,random
from PIL import Image
page = streamlit.sidebar.radio("侧栏",["图片反色","单词查找","留言区"])
def img_change(img):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            R = img_array[x,y][0]
            G = img_array[x,y][1]
            B = img_array[x,y][2]
            img_array[x,y] = (255-R,255-G,255-B)
    return img
def bar_bg(img):
    last = "jpg"
    streamlit.markdown(f"""<style>[data-testid='stSidebar']>div:first-child{{background:url(data:img/{last};base64,{base64.b64encode(open(img,"rb").read()).decode()});}}</style>""",unsafe_allow_html=True)
def page_bg1(img):
    last = "jpg"
    streamlit.markdown(f"""<style>.stApp{{background:url(data:img/{last};base64,{base64.b64encode(open(img,"rb").read()).decode()});background-size: cover}}</style>""",unsafe_allow_html=True)
bar_bg("colorful.jpg")
page_bg1("colorful.jpg")
def page_1():
    streamlit.write("<span style='font-size:20px;color:white'>图片反色</span>",unsafe_allow_html=True)
    uploaded_file = streamlit.file_uploader("",type=["png","jpeg","jpg"])
    if uploaded_file:
        roading = streamlit.progress(0,"开始反色")
        time.sleep(random.randint(int(2.1),int(3.2)))
        roading.progress(0,"正在反色 "+str(0)+"%")
        time.sleep(random.randint(int(2),int(2.5)))
        p1 = random.randint(int(10),int(37))
        roading.progress(p1,"正在反色 "+str(p1)+"%")
        time.sleep(random.randint(int(1.2),int(1.8)))
        img = Image.open(uploaded_file)
        p2 = random.randint(int(38),int(55))
        roading.progress(p2,"正在反色 "+str(p2)+"%")
        time.sleep(random.randint(int(1.1),int(1.7)))
        p3 = random.randint(int(56),int(72))
        roading.progress(p3,"正在反色 "+str(p3)+"%")
        time.sleep(random.randint(int(1.3),int(2.4)))
        p4 = random.randint(int(73),int(98))
        roading.progress(p4,"正在反色 "+str(p4)+"%")
        time.sleep(random.randint(int(1.7),int(2.9)))
        roading.progress(100,"正在反色 "+str(99)+"%")
        streamlit.image(img_change(img))
        roading.progress(100,"反色完毕!")
def page_2():
    not_find = 0
    streamlit.write("<span style='font-size:20px;color:white'>单词查找</span>",unsafe_allow_html=True)
    with open("words_space.txt","r",encoding="utf-8") as f:
        words_list = f.read().split("\n")
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
    with open("check_out_times.txt","r",encoding="utf-8") as f:
        times_list = f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    streamlit.write("<span style='font-size:20px;color:white'>请输入要查找的单词: </span>",unsafe_allow_html=True)
    word = streamlit.text_input("")
    if word in words_dict:
        if word == "":
            pass
        else:
            streamlit.write(f"<span style='font-size:20px;color:white'>{words_dict[word][1]}</span>",unsafe_allow_html=True)
            n = words_dict[word][0]
            if n in times_dict:
                times_dict[n] += 1
            else:
                times_dict[n] = 1
            with open("check_out_times.txt","w",encoding="utf-8") as f:
                message = ""
                for k,v in times_dict.items():
                    message += str(k) + "#" + str(v) + "\n"
                message = message[:-1]
                f.write(message)
            streamlit.write(f"<span style='font-size:20px;color:white'>此单词已被查询{times_dict[n]}次</span>",unsafe_allow_html=True)
    if word == "作者是谁?":
        streamlit.write("<span style='font-size:20px;color:white'>作者: 陈佳轶</span>",unsafe_allow_html=True)
    elif word == "balloons":
        if word not in words_dict:
            streamlit.write("<span style='font-size:20px;color:white'>词库中找不到该单词</span>",unsafe_allow_html=True)
            streamlit.balloons()
            not_find = 1
        else:
            streamlit.balloons()
    elif word == "snow":
        if word not in words_dict:
            streamlit.write("<span style='font-size:20px;color:white'>词库中找不到该单词</span>",unsafe_allow_html=True)
            streamlit.snow()
            not_find = 1
        else:
            streamlit.snow()
    elif word == "百宝箱":
        page_4()
    elif word == "":
        pass
    elif word not in words_dict and not_find == 0:
        streamlit.write("<span style='font-size:20px;color:white'>词库中找不到该单词</span>",unsafe_allow_html=True)
    else:
        not_find = 0
def page_3():
    with open("leave_messages.txt","r",encoding="utf-8") as f:
        messages_list = f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    for i in messages_list:
        if i[1] == "阿短":
            with streamlit.chat_message("😉"):
                streamlit.write(i[1],":",i[2])
        elif i[1] == "编程猫":
            with streamlit.chat_message("😸"):
                streamlit.write(i[1],":",i[2])
    name = streamlit.selectbox("我是: ",["阿短","编程猫"])
    new_message = streamlit.text_input("我想说的话: ")
    if streamlit.button("留言"):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open("leave_messages.txt","w",encoding="utf-8") as f:
            message = ""
            for j in messages_list:
                message += j[0] + "#" + j[1] + "#" + j[2] + "\n"
            message = message[:-1]
            f.write(message)
def page_4():
    go = streamlit.selectbox("千万别点",["千万别点"])
    if go == "千万别点":
        streamlit.link_button("千万别点","https://cznull.github.io/vsbm")
if page == "图片反色":
    page_1()
elif page == "单词查找":
    page_2()
elif page == "留言区":
    page_3()