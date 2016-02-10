from django.contrib import admin

from .models import Choice, Question

admin.site.disable_action('delete_selected')
admin.AdminSite.site_header = 'Polls administration'
admin.AdminSite.site_title = 'Polls admin site'

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3
	#def has_delete_permission(self, request, obj=None): # note the obj=None
	#	return False


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']
	def has_delete_permission(self, request, obj=None): # note the obj=None
		return False

admin.site.register(Question, QuestionAdmin)
