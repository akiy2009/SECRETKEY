from cryptography.fernet import Fernet

# キーを生成（初回実行時に一度だけ）
def generate_key():
    return Fernet.generate_key()

# トークンを暗号化する関数
def encrypt_token(message, key):
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())  # メッセージを暗号化
    return encrypted

# トークンを復号化する関数
def decrypt_token(encrypted_token, key):
    try:
        f = Fernet(key)
        decrypted_token = f.decrypt(encrypted_token).decode()  # トークンを復号化
        return decrypted_token
    except Exception as e:
        print(f"復号化エラー: {str(e)}")
        return None

# キーの保存
def save_key(key, filename="secret.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)

# キーの読み込み
def load_key(filename="secret.key"):
    with open(filename, "rb") as key_file:
        return key_file.read()

# 使用例
if __name__ == "__main__":
    try:
        # 既存のキーをロードする（ファイルが存在する場合）
        key = load_key()
        print("既存のキーをロードしました。")
    except FileNotFoundError:
        # キーが存在しない場合、新しいキーを生成して保存
        key = generate_key()
        save_key(key)  # 新しいキーをファイルに保存
        print("新しいキーを生成して保存しました。")

    # メッセージの暗号化
    message = "message"
    encrypted_token = encrypt_token(message, key)
    print(f"Encrypted: {encrypted_token}")

    # メッセージの復号化
    decrypted_message = decrypt_token(encrypted_token, key)
    if decrypted_message:
        print(f"Decrypted: {decrypted_message}")
    else:
        print("復号化に失敗しました。")
