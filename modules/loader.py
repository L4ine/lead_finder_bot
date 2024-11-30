from fastapi import FastAPI

from sqladmin import Admin

from admin.auth import AdminAuth
from admin.views import UserbotView, SettingsAdmin, \
	RecordAdmin, SourceAdmin

from data.config import SECRET_KEY, APP_URL, APP_TITLE

from db.db_api import engine, async_session

from modules.upload import router as upload_router


app = FastAPI()
app.include_router(upload_router)

auth_backend = AdminAuth(secret_key=SECRET_KEY)
admin = Admin(
	app=app,
	engine=engine,
	session_maker=async_session,
	base_url=f'{APP_URL}',
	title=APP_TITLE,
	templates_dir='admin/templates',
	authentication_backend=auth_backend
)

admin.add_view(UserbotView)
admin.add_view(RecordAdmin)
admin.add_view(SourceAdmin)
admin.add_view(SettingsAdmin)
