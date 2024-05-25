import streamlit as st

# メインページの設定
st.set_page_config(page_title="Image Search App", layout="wide")

# カスタムCSSスタイル
st.markdown("""
    <style>
    .main {
        background-color: #f7f7f7;
        padding: 2rem;
    }
    .title {
        font-size: 3rem;
        color: #ff6f61;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #555555;
        text-align: center;
        margin-top: -1rem;
        font-family: 'Arial', sans-serif;
    }
    .description {
        font-size: 1rem;
        color: #333333;
        text-align: center;
        margin: 1rem 0 2rem 0;
        font-family: 'Arial', sans-serif;
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin: 2rem 0;
    }
    .btn,
    a.btn,
    button.btn {
      font-size: 1.6rem;
      font-weight: 700;
      line-height: 1.5;
      position: relative;
      display: inline-block;
      padding: 1rem 4rem;
      cursor: pointer;
      -webkit-user-select: none;
      -moz-user-select: none;
      -ms-user-select: none;
      user-select: none;
      -webkit-transition: all 0.3s;
      transition: all 0.3s;
      text-align: center;
      vertical-align: middle;
      text-decoration: none;
      letter-spacing: 0.1em;
      color: #212529;
      border-radius: 0.5rem;
    }

    a.btn-gradient {
      font-weight: normal;
      color: #fff;
      border-radius: 0;
      background-image: -webkit-gradient(
        linear,
        left top,
        right top,
        color-stop(40%, #ff3cac),
        to(#562b7c)
      );
      background-image: -webkit-linear-gradient(left, #ff3cac 40%, #562b7c 100%);
      background-image: linear-gradient(90deg, #ff3cac 40%, #562b7c 100%);
    }

    a.btn-gradient:after {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      content: "";
      -webkit-transition: all 0.5s;
      transition: all 0.5s;
      background-image: -webkit-gradient(
        linear,
        left top,
        right top,
        from(#ff3cac),
        color-stop(#562b7c),
        to(#2b86c5)
      );
      background-image: -webkit-linear-gradient(left, #ff3cac, #562b7c, #2b86c5);
      background-image: linear-gradient(90deg, #ff3cac, #562b7c, #2b86c5);
    }

    a.btn-gradient span {
      position: relative;
      z-index: 1;
    }

    a.btn-gradient:hover {
      color: #fff;
    }

    a.btn-gradient:hover:after {
      opacity: 0;
    }
    </style>
""", unsafe_allow_html=True)

# コンテンツ
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("<div class='title'>Welcome to the Image Search App</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Azure 勉強会のプロジェクトへようこそ</div>", unsafe_allow_html=True)
st.markdown("<div class='description'>このアプリケーションは、Microsoftの新卒が集まったグループ「Azure 勉強会」によって作成されました。画像検索機能を通じて、さまざまな画像を簡単に検索し、詳細情報を閲覧することができます。</div>", unsafe_allow_html=True)

# 検索ボタン
st.markdown("<div class='button-container'><a href='/Search_Page' class='btn btn-gradient'><span>検索はこちら→</span></a></div>", unsafe_allow_html=True)

# コンテンツ終了
st.markdown("</div>", unsafe_allow_html=True)
