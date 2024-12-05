import json

# Đường dẫn file JSON gốc chứa nhiều object
input_file_path = "input_result_compare/testing_data_new_vn.jsonl"
# Đường dẫn file sau khi đã format
output_file_path = "formatted_testing_data.json"

# Danh sách để chứa các objects JSON
data_list = []

# Đọc từng dòng JSON trong file gốc
with open(input_file_path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()  # Loại bỏ ký tự thừa (nếu có)
        if line:  # Kiểm tra dòng không rỗng
            data_list.append(json.loads(line))

# Ghi dữ liệu thành một file JSON chuẩn chỉnh
with open(output_file_path, "w", encoding="utf-8") as output_file:
    json.dump(data_list, output_file, indent=4, ensure_ascii=False)

print(f"Dữ liệu đã được format lại và lưu vào: {output_file_path}")
