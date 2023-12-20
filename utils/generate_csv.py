import csv
import sys
import faker
import random
import datetime

# Fakerライブラリの初期化
fake = faker.Faker()


def generate_slot_test_data():
    # ヘッダーレコード
    header = ["ID", "名称", "Seq", "開始時刻", "終了時刻", "指定外"]

    # テストデータ生成
    test_data = []
    for i in range(1, 1001):
        id = i
        name = fake.company()
        seq = i
        start_time = fake.date_time_between(
            start_date='-1y', end_date='now', tzinfo=None
        )
        end_time = start_time + datetime.timedelta(
            days=random.randint(1, 30)
        )
        specified = random.choice([True, False])
        row = [id, name, seq, start_time, end_time, specified]
        test_data.append(row)

    # ファイルに書き込み
    with open('test_data.tsv', 'w', newline='') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t')
        writer.writerow(header)
        writer.writerows(test_data)

    print('テストデータが生成され、test_data.tsvに保存されました。')


def generate_user_group_test_data():
    # テストデータ生成
    test_data = []
    for i in range(1, 1001):
        user_id = i
        username = fake.company()
        permission = random.choice(["admin", "一般ユーザ", "管理者"])
        row = [user_id, username, permission]
        test_data.append(row)

    # ファイルに書き込み
    with open('test_data.tsv', 'w', newline='') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t')
        writer.writerow(["ID", "名称", "権限名"])
        writer.writerows(test_data)

    print('テストデータが生成され、test_data.tsvに保存されました。')


def generate_user_test_data():
    # ヘッダーレコード
    header = ["ID", "名前", "メールアドレス", "ユーザーグループID", "ユーザグループ名", "パスワード"]

    # テストデータ生成
    test_data = []
    for i in range(1, 1001):
        id = i
        name = fake.name()
        email = fake.email()
        user_group_id = fake.random_int(min=1, max=10)
        user_group_name = f"ユーザグループ名{user_group_id}"
        password = fake.password()
        row = [id, name, email, user_group_id, user_group_name, password]
        test_data.append(row)

    # ファイルに書き込み
    with open('test_data.tsv', 'w', newline='') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t')
        writer.writerow(header)
        writer.writerows(test_data)

    print('テストデータが生成され、test_data.tsvに保存されました。')


def generate_segment_test_data():
    # テストデータ生成
    test_data = []
    for i in range(1, 1001):
        id = i
        address = fake.address().replace("\n", "")
        row = [id, address, '']
        test_data.append(row)

    # ファイルに書き込み
    with open('test_data.tsv', 'w', newline='') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t')
        writer.writerow(["ID", "名称", "配送エリアID"])
        writer.writerows(test_data)

    print('テストデータが生成され、test_data.tsvに保存されました。')


def main():
    if len(sys.argv) < 2:
        print(
            "Usage: python test_data_generator.py [user|user_group|slot|segment]")
        return
    command = sys.argv[1]
    if command == "user":
        generate_user_test_data()
    elif command == "user_group":
        generate_user_group_test_data()
    elif command == "slot":
        generate_slot_test_data()
    elif command == "segment":
        generate_segment_test_data()
    else:
        print("Unknown command:", command)


main()
