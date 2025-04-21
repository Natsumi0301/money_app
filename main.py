#必要なモジュールをインポート
import streamlit as st
import openai
from openai import OpenAI 
from dotenv import load_dotenv
import os
from gtts import gTTS
from tempfile import NamedTemporaryFile
from audio_recorder_streamlit import audio_recorder

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
# Whisper & Chat用のOpenAIクライアント作成
client = OpenAI(api_key=api_key)

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
        st.title('マネとも～お金の大切さを学ぼう～～')
        st.write('はたらいてゲットしたお金を、きみはどうつかう？')
        st.image('image/title.png', width=500)
        st.button('スタート', on_click = change_page_to_job_select)
    
    #ジョブ選択に遷移するためのsession_stateの設定
    def change_page_to_job_select():
        st.session_state["page_control"] = 1
    
    #ジョブ選択画面
    def job_select():
        st.header('おしごとをえらぼう！')
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("image/driver.png",width=200)
            st.write("バスのうんてんしゅ")
            st.button("このおしごとにする！", key="driver",on_click = change_page_to_bus_driver)
        with col2:
            st.image("image/writer.png",width=200)
            st.write("しょうせつか")
            st.button("このおしごとにする！", key="writer",on_click = change_page_to_writer)
        with col3:
            st.image("image/staff.png",width=200)
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
        # 初期化（必要な状態すべて）
        if "page" not in st.session_state:
            st.session_state.page = "select_passenger"
        if "passenger" not in st.session_state:
            st.session_state.passenger = ""
        if "destination" not in st.session_state:
            st.session_state.destination = ""

        # ① 誰をのせる？
        if st.session_state.page == "select_passenger":
            st.title("🚌 バスのうんてんしゅたいけん！")
            st.markdown("きょうは バスのうんてんしゅ。おきゃくさんを のせて もくてきちに つれていこう！")

            st.session_state.passenger = st.selectbox("だれを のせる？", ["おじいちゃん", "おともだち", "おかあさん", "せんせい"])

            if st.button("📍 つぎへ（どこに行く？）"):
                st.session_state.page = "select_destination"

        # ② どこに行く？
        elif st.session_state.page == "select_destination":
            st.header("🗺️ どこにいく？")
            st.session_state.destination = st.selectbox("どこまでバスでいく？", ["どうぶつえん", "デパート", "ゆうえんち", "がっこう"])

            if st.button("🛣うんてんスタート！"):
                st.session_state.page = "on_the_road"

        # ③ 運転中
        elif st.session_state.page == "on_the_road":
            st.subheader(f"{st.session_state.passenger}を のせに バスがしゅっぱつ！🚍💨")

        # 出発の画像を追加
            st.image("スクリーンショット 2025-04-20 150006.png", caption="バスが出発！")
          
            if st.button("🧍おきゃくさんを のせる"):
                st.session_state.page = "boarding"

        # ④ 乗車シーン
        elif st.session_state.page == "boarding":
            st.subheader(f"{st.session_state.passenger}がバスにのったよ！🧍")
            if st.button("🏁 もくてきちに とうちゃく！"):
                st.session_state.page = "goal"

        # ⑤ 到着 → お給料ゲット！
        elif st.session_state.page == "goal":
            st.balloons()
            st.success(f"{st.session_state.passenger}を {st.session_state.destination} に つれていけたよ！すごい！")
            st.markdown("おきゅうりょうをゲットしたよ💰")
            st.markdown("またあしたも がんばろう！🚏")

        # 到着の画像を追加
            st.image("スクリーンショット 2025-04-20 150033.png", caption=f"{st.session_state.destination}に到着！")
    


            if st.button("もういちどやる！"):
                # 状態リセット
                st.session_state.page = "select_passenger"
                st.session_state.passenger = ""
                st.session_state.destination = ""
        st.button('おしごとしゅうりょう！', on_click=change_page_to_get_money)

    def writer():
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")

        # ✅ OpenAI APIキーを環境変数などから取得
        openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = api_key

        # タイトル
        st.title("しょうせつか体験ゲーム📚")

        st.markdown("きみだけのものがたりをつくって、本にしよう！🎉")

        # 🧒 子どもの名前入力
        user_name = st.text_input("あなたのなまえをいれてね")

        # 🎭 話のテーマ選択
        theme = st.radio("どんなテーマのものがたりにする？", ["ぼうけん", "ゆうじょう", "ひみつ", "ふしぎ"])

        # 🌲 場面の選択
        scene = st.selectbox("ものがたりのばめんをえらんでね", ["もり", "がっこう", "うちゅう", "うみ", "まち"])

        # ボタンで生成
        if st.button("ものがたりをつくる"):
            if not user_name:
                st.warning("なまえをいれてね！")
            else:
                with st.spinner("きみのアイデアで本をかいてるよ...📖"):

                    # プロンプトを構成
                    prompt = f"""
                    あなたは小学生向けの児童文学作家です。
                    以下の条件で、主人公「{user_name}」による短い物語をやさしい日本語で書いてください。
            
                    【条件】
                    - 舞台は「{scene}」
                    - テーマは「{theme}」
                    - ストーリーは3〜4文で完結
                    - 最後に「つづきが気になる！」と思わせる終わり方
                    物語：
                    """

                    # GPT呼び出し
                    response = openai.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": prompt}]
                    )

                    story = response.choices[0].message.content

                    # 結果表示
                    st.markdown(f"### 📘 『{user_name}の{theme}ものがたり』")
                    st.write(story)

                    # 本が売れてお給料ゲット
                    st.success(f"おめでとう！{user_name}の本は大ヒット！📚✨")
                    st.balloons()
                    st.markdown("たくさんうれて、おきゅうりょうをゲットしたよ💰")

                    st.markdown("また ちがうおはなしを つくってみよう！⬇️")
        st.button('おしごとしゅうりょう！', on_click=change_page_to_get_money)
    
    def shop_staff():
        

        # 初期化
        if "messages" not in st.session_state:
            st.session_state.messages = [{"role": "system", "content": "ハンバーガー屋に来た４０代女性のお客さんです。挨拶されたら挨拶したこんにちわと挨拶したうえで、おすすめを聞いてください。"
            "おすすめのメニューを紹介されたらそれにすると返事してください。金額を言われたらはいどうぞ、と伝えて、ありがとうと伝えてください。"
            "それ以外はお客さんになりきって臨機応変に対応し、できれば３往復で会話を終わらせ、難しければ５往復以内で会話を終わらせてください。"}]

        # タイトル表示
        st.title("ハンバーガーやさんになってみよう！")
        st.image("image/customer.png",width=200)
        st.write("お！おきゃくさんだ！")
        st.empty()
        st.write("じゅんびができたら　マイクをおして「いらっしゃいませ」といってみよう！")

        # 音声録音
        audio_bytes = audio_recorder("おしてね ⇒")

        # 音声があれば裏でテキスト化してGPTに投げる
        if audio_bytes:
            # 一時ファイルに保存（Whisper用）
            with NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
                temp_audio.write(audio_bytes)
                temp_path = temp_audio.name

            # Whisperでテキスト化
            with open(temp_path, "rb") as audio_file:
                transcription = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )
                user_text = transcription.text

            os.remove(temp_path)  # 一時ファイル削除

            # テキストをGPTに送信
            st.session_state.messages.append({"role": "user", "content": user_text})
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": reply})

            tts = gTTS(reply, lang='ja')  # 日本語なら lang='ja'
            with NamedTemporaryFile(delete=False, suffix=".mp3") as tts_file:
                tts.save(tts_file.name)
                audio_path = tts_file.name


            # 表示
            st.markdown("🔊 **音声での返答:**")
            st.audio(audio_path, format='audio/mp3')

        st.button('おしごとしゅうりょう！', on_click=change_page_to_get_money)
    
    #お金ゲット画面のためのsession_stateの設定
    def change_page_to_get_money():
        st.session_state["page_control"] = 5
    
    #お金ゲット画面
    def get_money():
        st.header('おきゅうりょう日！')
        st.write('おしごとして　お金をゲットしたよ！')
        st.image('image/get_money.png', width=500)
        st.button('つぎへ', on_click=change_page_to_how_to_use_money)

    #お金の使い方画面のためのsession_stateの設定
    def change_page_to_how_to_use_money():
        st.session_state["page_control"] = 6
    
    #お金の使い方選択画面（イラストは後で差し替え）
    def how_to_use_money():
        # 手紙を生成する関数
        def generate_future_letter(dream, use_type):
            system_prompt = (
                "あなたは小学校低学年の子どもに向けて、10年後の自分から届いた手紙を書くお手伝いをするアシスタントです。"
                "やさしく、ポジティブで、あたたかい言葉で書いてください。"
                "コメントはバランスの取れたお金の使い方をほめる要素を含み、冒頭には必ず『おしごとがんばってすごいね！』と入れてください。"
                "手紙の長さは150文字以内にしてください。"
            )

            user_prompt = f"""
        将来の夢: {dream}
        お金の使い方: {use_type}

        この子に向けて、10年後の自分からのやさしい手紙を書いてください。
        """

            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=200,
                temperature=0.8,
            )

            return response.choices[0].message.content

        # Streamlit アプリ
        st.title("10ねんごのじぶんからのてがみがとどいたよ！ 💌")
        st.write("おかねのつかいかたと、しょうらいのゆめをおしえてね！")

        # 入力欄
        dream = st.text_input("しょうらいのゆめは？（たとえば：けいさつかん、パティシエ、サッカーせんしゅ など）")

        use_type = st.radio("おかねのつかいかたはどれ？", [
            "① ぜんぶつかっちゃう（おかしやガチャ）",
            "② けいけんに使う（りょこうやコンサートなど）",
            "③ あとでつかうためにためる（ちょきんばこ など）"
        ])

        # ボタンで手紙を生成
        if st.button("てがみをよむ"):
            if dream and use_type:
                with st.spinner("てがみをかいているよ…"):
                    letter = generate_future_letter(dream, use_type)
                st.success("📨 てがみがとどいたよ！")
                st.image("https://cdn.pixabay.com/photo/2020/05/01/16/34/letter-5110634_1280.png", width=200)
                st.markdown(f"### 💌 {letter}")
            else:
                st.warning("しょうらいのゆめ と おかねのつかいかた をえらんでね！")
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
    else:
        st.session_state["page_control"] = 0
        title()


    #divを閉じる
    st.markdown("</div>", unsafe_allow_html=True)