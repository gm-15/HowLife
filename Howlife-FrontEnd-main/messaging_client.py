import firebase_admin
from firebase_admin import messaging, credentials

cred = credentials.Certificate("YOUR_SERVICE_ACCOUNT.json")

firebase_admin.initialize_app(cred)

def send_test_message(token):
    message = messaging.Message(
        notification=messaging.Notification(
            title="HOWLIFE 테스트 알림 💧",
            body="푸시 알림이 정상적으로 동작합니다!"
        ),
        token=token,
    )
    result = messaging.send(message)
    return result