from flask import Flask, request, jsonify

app = Flask(__name__)

# 全域變數：目前偵測到的號碼
current_number = "000"

@app.route("/number", methods=["GET"])
def get_number():
    """查詢目前號碼（App 用）"""
    return jsonify({"number": current_number})

@app.route("/update", methods=["POST"])
def update_number():
    """YOLO 偵測程式傳入最新號碼"""
    global current_number
    data = request.get_json()  # 例如 {"number": "025"}
    if "number" in data:
        current_number = data["number"]
        return jsonify({"message": "更新成功", "number": current_number})
    else:
        return jsonify({"error": "缺少 number 參數"}), 400


