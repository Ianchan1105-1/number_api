from flask import Flask, jsonify

app = Flask(__name__)

# 暫存號碼（先用假資料，之後 YOLO 可以更新）
current_number = "000"

@app.route("/number", methods=["GET"])
def get_number():
    return jsonify({"number": current_number})

# Render 用的啟動
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
