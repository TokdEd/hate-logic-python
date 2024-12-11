# Content Management System

這是一個基於 gRPC 的內容管理系統，使用 Python 實現，支持用戶註冊、內容提交和審核功能。

## 功能特點

- 用戶註冊和認證
- 內容提交
- 管理員內容審核
- 基於 JWT 的身份驗證
- MongoDB 數據存儲

## 系統要求

- Python 3.7+
- MongoDB
- gRPC

## 安裝依賴 
```
pip install -r requirements.txt
```

## 環境變量

可以通過環境變量或 `config/settings.py` 配置以下參數：

- `MONGO_URI`: MongoDB 連接字符串（默認：mongodb://localhost:27017/content_system）
- `JWT_SECRET_KEY`: JWT 加密密鑰
- `GRPC_PORT`: gRPC 服務端口（默認：50051）

## 項目結構
```
src/
├── config/
│ └── settings.py # 配置文件
├── models/
│ ├── submission.py # 提交內容模型
│ └── user.py # 用戶模型
├── proto/
│ ├── content.proto # Protocol Buffers 定義
│ ├── content_pb2.py # 生成的 protobuf 代碼
│ └── content_pb2_grpc.py
├── services/
│ └── content_service.py # gRPC 服務實現
├── utils/
│ └── auth.py # 認證相關工具
└── server.py # 主服務器
```
## 啟動服務
```
python server.py
```

## API 功能

### 用戶相關
- RegisterUser: 用戶註冊

### 內容相關
- CreateSubmission: 提交內容
- ReviewSubmission: 審核內容（需要管理員權限）

## 安全性

- 使用 JWT 進行身份驗證
- 密碼使用 bcrypt 加密存儲
- 基於角色的權限控制

## 開發說明

1. 修改 Protocol Buffers 定義後需要重新生成代碼：
```
python -m grpc_tools.protoc -I=proto --python_out=proto --grpc_python_out=proto proto/content.proto
```

2. 確保 MongoDB 服務正在運行

## 錯誤處理

系統實現了完整的錯誤處理機制：
- 用戶認證錯誤
- 權限驗證
- 數據驗證
- 服務器錯誤

## 貢獻指南

1. Fork 本項目
2. 創建特性分支
3. 提交更改
4. 推送到分支
5. 創建 Pull Request

## JWT 配置

在運行服務之前，請確保設置 JWT 密鑰：

1. 生成新的密鑰：
```python
import secrets
jwt_secret = secrets.token_hex(32)
```

2. 設置環境變量：
```bash
export JWT_SECRET_KEY='your_generated_secret_key'
```

注意：請妥善保管密鑰，不要將其提交到版本控制系統。


