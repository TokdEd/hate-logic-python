import os
from datetime import timedelta

# MongoDB 配置
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/content_system')
DATABASE_NAME = 'content_system'

# JWT 配置
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_generated_secret_key')
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

# gRPC 配置
GRPC_PORT = os.getenv('GRPC_PORT', '50051')

# 密碼加密配置
BCRYPT_ROUNDS = 12 