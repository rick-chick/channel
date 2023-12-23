import sys
import json

# コマンドライン引数の数を確認
if len(sys.argv) < 2:
    print("Usage: python script.py <token>")
    sys.exit(1)

# コマンドライン引数からトークンを取得
token_str = sys.argv[1]

# 文字列から '=' の右側の値を取得する
token_str = token_str.split('\n')[0].strip()
token_str = token_str.split("=")[1].strip("'")

# 結果を表示
print(token_str)
