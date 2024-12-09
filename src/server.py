import asyncio
import grpc
#from proto import content_pb2_grpc
from concurrent import futures
import proto.content_pb2_grpc as content
from services.content_service import ContentService
from config.settings import GRPC_PORT

async def serve():
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    content.add_ContentServiceServicer_to_server(ContentService(), server)
    server.add_insecure_port(f'[::]:{GRPC_PORT}')
    
    print(f'啟動服務器在端口 {GRPC_PORT}...')
    await server.start()
    await server.wait_for_termination()

if __name__ == '__main__':
    asyncio.run(serve()) 