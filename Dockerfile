# 1. 使用基礎 Python 映像
FROM python:3.9-slim

# 2. 設置環境變數
ENV PYTHONUNBUFFERED=1

# 3. 設置工作目錄
WORKDIR /app

# 4. 安裝系統依賴（如果需要編譯 Protobuf）
RUN apt-get update && apt-get install -y \
    build-essential \
    protobuf-compiler \
    && rm -rf /var/lib/apt/lists/*

# 5. 複製需求文件並安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. 複製整個專案到容器
COPY src/ ./src/

# 7. 暴露服務端口（例如 gRPC 默認 50051）
EXPOSE 50051

# 8. 設置啟動命令
CMD ["python", "src/server.py"]