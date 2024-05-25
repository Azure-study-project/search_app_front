import streamlit as st
from typing import Dict, List, Union

# 型定義
ImageResult = Dict[str, Union[str, int]]
SearchResults = Dict[str, List[ImageResult]]

# モックデータの定義
mock_results: SearchResults = {
    'images': [
        {'id': str(i+1), 'url': 'https://logomarkmania.up.seesaa.net/sports/adidas_logo.jpg', 'title': f'Image {i+1}', 'classification': f'Category {chr(65+i)}', 'features': f'Feature {i+1}'} for i in range(10)
    ]
}

def search_images(query: str) -> SearchResults:
    # モックデータの返却
    return mock_results

def get_columns(num_items: int, max_cols: int = 3) -> int:
    # 一行に最大で4列表示
    num_cols = min(max_cols, num_items)
    return num_cols

# ページのヘッダー
st.title("画像検索アプリケーション")
st.header("画像一覧")

# チャット入力
query: str = st.chat_input("どんな画像を取得したいか入力してください。")

if query:
    results: SearchResults = search_images(query)
    if results:
        # 検索結果の画像一覧表示
        images: List[ImageResult] = results['images']
        num_images: int = len(images)
        num_cols: int = get_columns(num_images)
        cols = st.columns(num_cols)
        
        for idx, result in enumerate(images):
            col = cols[idx % num_cols]  # 画像を列に割り当てる
            with col:
                st.image(result['url'], use_column_width=True)
                st.write(result['title'])
                with st.expander(f"詳細表示: {result['title']}"):
                    st.write(f"タイトル: {result['title']}")
                    st.write(f"分類: {result['classification']}")
                    st.write(f"特徴: {result['features']}")
    else:
        st.error("検索結果を取得できませんでした。")
