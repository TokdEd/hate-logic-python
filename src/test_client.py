import grpc
from proto import content_pb2
from proto import content_pb2_grpc
def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = content_pb2_grpc.ContentServiceStub(channel)
        
        # 測試用戶註冊
        response = stub.RegisterUser(
            content_pb2.RegisterRequest(
                username="testuser",
                password="password123"
            )
        )
        print(f"Response: {response}")

if __name__ == '__main__':
    run()