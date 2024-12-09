from . import content_pb2
from . import content_pb2_grpc

# 添加调试信息
print("Available classes in content_pb2_grpc:", dir(content_pb2_grpc))

# 确保关键类可用
if not hasattr(content_pb2_grpc, 'ContentServiceServicer'):
    raise ImportError('ContentServicer not found in generated code. Available items: ' + str(dir(content_pb2_grpc)))

