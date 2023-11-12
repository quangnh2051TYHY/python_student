# Sử dụng image Python 3.8
FROM python:3.8

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Sao chép file requirements.txt vào container
COPY requirements.txt .

# Cài đặt các gói cần thiết
RUN pip install -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Chạy ứng dụng
CMD ["python", "Application.py"]
