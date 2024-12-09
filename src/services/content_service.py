import grpc
from concurrent import futures
from typing import Optional

from proto import content_pb2
from proto import content_pb2_grpc
from models.user import User
from models.submission import Submission
from utils.auth import create_token, verify_token
print(dir(content_pb2_grpc)) 
class ContentService(content_pb2_grpc.ContentServiceServicer):
    async def RegisterUser(self, request, context):
        try:
            user = await User.create(
                username=request.username,
                password=request.password
            )
            
            return content_pb2.RegisterResponse(
                success=True,
                message="註冊成功",
                user_id=str(user['_id'])
            )
        except ValueError as e:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details(str(e))
            return content_pb2.RegisterResponse(
                success=False,
                message=str(e)
            )

    async def CreateSubmission(self, request, context):
        # 驗證用戶token
        token = context.invocation_metadata().get('authorization')
        if not token:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, '未提供認證信息')
        
        user_data = verify_token(token)
        if not user_data:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, '無效的認證信息')

        submission = await Submission.create(
            user_id=user_data['user_id'],
            content=request.content
        )

        return content_pb2.Submission(
            id=str(submission['_id']),
            user_id=submission['user_id'],
            content=submission['content'],
            status=submission['status'],
            created_at=submission['created_at'].isoformat()
        )

    async def ReviewSubmission(self, request, context):
        # 驗證管理員權限
        token = context.invocation_metadata().get('authorization')
        user_data = verify_token(token)
        
        if not user_data or user_data['role'] != 'admin':
            context.abort(grpc.StatusCode.PERMISSION_DENIED, '需要管理員權限')

        submission = await Submission.update_status(
            submission_id=request.submission_id,
            status=request.status,
            admin_id=user_data['user_id']
        )

        return content_pb2.Submission(
            id=str(submission['_id']),
            user_id=submission['user_id'],
            content=submission['content'],
            status=submission['status'],
            created_at=submission['created_at'].isoformat(),
            reviewed_by=submission['reviewed_by'],
            reviewed_at=submission['reviewed_at'].isoformat() if submission['reviewed_at'] else None
        ) 