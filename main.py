#必要なモジュールをインポート
import streamlit as st

#HTMLで中央揃えのdivを作成
with st.container():
    st.markdown(
        """
        <div style = "display: flex; justify-content: center; flex-direction:column; align-items: center>
        """,
        unsafe_allow_html=True
    )
    
    #タイトル画面
    def title():
        st.title('（仮）お金の大切さを学ぼう')
        st.write('はたらいてゲットしたお金を、きみはどうつかう？')
        st.image('https://drive.google.com/file/d/1YB5fhYOXfBJofl1n69odRpfD_ExeAWca/view?usp=sharing', width=500)
        st.button('スタート', on_click = change_page_to_job_select)
    
    #ジョブ選択に遷移するためのsession_stateの設定
    def change_page_to_job_select():
        st.session_state["page_control"] = 1
    
    #ジョブ選択画面
    def job_select():
        st.header('おしごとをえらぼう！')
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://drive.google.com/file/d/1RW1i660tzcOa4eS8xMv1qoO_2dmxFUmi/view?usp=sharing",width=200)
            st.write("バスのうんてんしゅ")
            st.button("このおしごとにする！", key="driver",on_click = change_page_to_bus_driver)
        with col2:
            st.image("https://drive.google.com/file/d/1YnAxQRPv7sA9pO_InTMVVE1m_tHXEAqi/view?usp=sharing",width=200)
            st.write("しょうせつか")
            st.button("このおしごとにする！", key="writer",on_click = change_page_to_writer)
        with col3:
            st.image("https://drive.google.com/file/d/1wxbPecHLYbc1vjJfmbG2aIUdGMnK6YcK/view?usp=sharing",width=200)
            st.write("ハンバーガーやさん")
            st.button("このおしごとにする！", key="staff",on_click = change_page_to_shop_staff)

    #お仕事体験ゲーム遷移のためのsession_stateの設定
    def change_page_to_bus_driver():
        st.session_state["page_control"] = 2
    def change_page_to_writer():
        st.session_state["page_control"] = 3
    def change_page_to_shop_staff():
        st.session_state["page_control"] = 4          

    def driver():
        st.header('もくてきちまで　うんてんしよう！')
        st.button('おしごとしゅうりょう！', on_click=change_page_to_get_money)

    def writer():
        st.header('おはなしを　つくろう！')
        st.button('おしごとしゅうりょう！', on_click=change_page_to_get_money)
    
    def shop_staff():
        st.header('ちゅうもんされたものを　わたそう！')
        st.button('おしごとしゅうりょう！', on_click=change_page_to_get_money)
    
    #お金ゲット画面のためのsession_stateの設定
    def change_page_to_get_money():
        st.session_state["page_control"] = 5
    
    #お金ゲット画面
    def get_money():
        st.header('おきゅうりょう日！')
        st.write('おしごとして　お金をゲットしたよ！')
        st.image('https://drive.google.com/file/d/11qsthnhQurvZHiI-pkFwXeF0GQ02vhpR/view?usp=sharing', width=500)
        st.button('つぎへ', on_click=change_page_to_how_to_use_money)

    #お金の使い方画面のためのsession_stateの設定
    def change_page_to_how_to_use_money():
        st.session_state["page_control"] = 6
    
    #お金の使い方選択画面（イラストは後で差し替え）
    def how_to_use_money():
        st.header('お金のつかいかたを　えらぼう！')
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://drive.google.com/file/d/1RW1i660tzcOa4eS8xMv1qoO_2dmxFUmi/view?usp=sharing",width=200)
            st.write("浪費パターン")
            st.button("これにする！", key="pattern1",on_click = change_page_to_pattern1)
        with col2:
            st.image("https://drive.google.com/file/d/1RW1i660tzcOa4eS8xMv1qoO_2dmxFUmi/view?usp=sharing",width=200)
            st.write("経験パターン")
            st.button("これにする！", key="pattern2",on_click = change_page_to_pattern2)
        with col3:
            st.image("https://drive.google.com/file/d/1RW1i660tzcOa4eS8xMv1qoO_2dmxFUmi/view?usp=sharing",width=200)
            st.write("貯金パターン")
            st.button("これにする！", key="pattern3",on_click = change_page_to_pattern3)
    
    #結果画面遷移のためのsession_stateの設定
    def change_page_to_pattern1():
        st.session_state["page_control"] = 7
    def change_page_to_pattern2():
        st.session_state["page_control"] = 8
    def change_page_to_pattern3():
        st.session_state["page_control"] = 9
    
    #結果画面
    def pattern1():
        st.header("pattern１")
        st.button('もう一回やってみる', on_click=change_page_to_title)

    def pattern2():
        st.header("pattern２")
        st.button('もう一回やってみる', on_click=change_page_to_title)
    
    def pattern3():
        st.header("pattern３")
        st.button('もう一回やってみる', on_click=change_page_to_title)
    
    #タイトル画面に戻るためのsession_stateの設定
    def change_page_to_title():
        st.session_state["page_control"] = 0

    #ページ遷移用の関数
    if ("page_control" in st.session_state and
        st.session_state["page_control"] == 1):
        job_select()
    elif("page_control" in st.session_state and
        st.session_state["page_control"] == 2):
        driver()
    elif("page_control" in st.session_state and
        st.session_state["page_control"] == 3):
        writer()
    elif("page_control" in st.session_state and
        st.session_state["page_control"] == 4):
        shop_staff()
    elif("page_control" in st.session_state and
        st.session_state["page_control"] == 5):
        get_money()
    elif("page_control" in st.session_state and
        st.session_state["page_control"] == 6):
        how_to_use_money()
    elif("page_control" in st.session_state and
        st.session_state["page_control"] == 7):
        pattern1()
    elif("page_control" in st.session_state and
        st.session_state["page_control"] == 8):
        pattern2()
    elif("page_control" in st.session_state and
        st.session_state["page_control"] == 9):
        pattern3()    
    else:
        st.session_state["page_control"] = 0
        title()


    #divを閉じる
    st.markdown("</div>", unsafe_allow_html=True)