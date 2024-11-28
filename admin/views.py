from sqladmin import ModelView, BaseView, expose

from db.models import Setting, Record, Source


class UserbotView(BaseView):
	name = "Userbot"
	icon = "fa-solid fa-gears"

	@expose("/userbot", methods=["GET"])
	async def report_page(self, request):
		return await self.templates.TemplateResponse(request, "userbot.html")


class SettingsAdmin(ModelView, model=Setting):
	name = 'Settings'
	name_plural = 'Settings'
	icon = 'fa-solid fa-gear'

	column_list = [Setting.id, Setting.name, Setting.value]
	column_labels = {
		Setting.id: 'ID',
		Setting.sys_name: 'Sys. Name',
		Setting.name: 'Name',
		Setting.value: 'Value',
	}


class RecordAdmin(ModelView, model=Record):
	name = 'Record'
	name_plural = 'Records'
	icon = 'fa-solid fa-copy'
	page_size_options = [50, 100]

	column_list = [
		Record.id, Record.source,
		Record.tg_id, Record.publish_datetime
	]
	column_labels = {
		Record.id: 'ID',
		Record.source: 'Source',
		Record.tg_id: 'Record TG ID',
		Record.publish_datetime: 'Publication date'
	}
	column_sortable_list = [Record.publish_datetime, Record.source]
	column_searchable_list = [Record.publish_datetime, Record.source]


class SourceAdmin(ModelView, model=Source):
	name = 'Source'
	name_plural = 'Sources'
	icon = 'fa-solid fa-user-group'
	page_size_options = [50, 100]

	column_list = [Source.id, Source.username, Source.is_active]
	column_labels = {
		Source.id: 'ID',
		Source.username: 'TG ID / Username',
		Source.is_active: 'Is active?'
	}
	column_sortable_list = [Source.username, Source.is_active]
	column_searchable_list = [Source.username, Source.is_active]
