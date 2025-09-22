from flask import Flask, jsonify

app = Flask(__name__)

# 全域變數：目前號碼
current_number = 0

@app.route("/number", methods=["GET"])
def get_number():
    """查詢目前號碼"""
    return jsonify({"number": f"{current_number:03d}"})

@app.route("/next", methods=["POST"])
def next_number():
    """叫下一號"""
    global current_number
    current_number += 1
    return jsonify({"number": f"{current_number:03d}"})

@app.route("/reset", methods=["POST"])
def reset_number():
    """重置號碼為 000"""
    global current_number
    current_number = 0
    return jsonify({"number": f"{current_number:03d}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

