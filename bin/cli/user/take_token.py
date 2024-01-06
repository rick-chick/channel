import sys
import os

if len(sys.argv) < 2:
    print("Usage: python script.py <token> <refresh_token>")
    sys.exit(1)

token_str = sys.argv[1]
token = token_str.split("=")[1].strip("'")

if len(sys.argv) < 3:
    print("Usage: python script.py <token> <refresh_token>")
    sys.exit(1)

refresh_token_str = sys.argv[2]
refresh_token = refresh_token_str.split("=")[1].strip("'")

# 出力するシェルスクリプトの内容
script_content = f"""\
export token='{token}'
export refresh_token='{refresh_token}'
"""

# シェルスクリプトを出力
with open('output_script.sh', 'w') as script_file:
    script_file.write(script_content)

# 確認のために表示
print("Script content:")
print(script_content)
