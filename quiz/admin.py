from django.contrib import admin
from .models import Quiz, Question, QuizUser

# Register your models here.

class QuizUseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'quiz', 'score')
    actions = ['download_csv']

    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        # from io import StringIO
        import io

        f = io.StringIO()
        writer = csv.writer(f)
        writer.writerow(['user', 'quiz', 'score'])
        for s in queryset:
            writer.writerow([s.user.username, s.quiz, s.score])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=todo-list.csv'
        return response

    download_csv.short_description = "Selected list to download CSV file."


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'label', 'option1', 'option2','option3','option4','answer')


# class OptionAdmin(admin.ModelAdmin):
#     list_display = ('question', 'text', 'is_correct',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)
# admin.site.register(Option, OptionAdmin)
admin.site.register(QuizUser, QuizUseAdmin)

