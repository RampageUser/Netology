from django.contrib import admin
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope
from django import forms


class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                counter += 1
        if counter == 0:
            raise forms.ValidationError('Укажите основной раздел')
        elif counter > 1:
            raise forms.ValidationError('Основным может быть только один раздел')
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 5
    formset = ScopeInlineFormSet


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    list_filter = ['published_at']
    inlines = [ScopeInline]

    # def get_tags(self, object):
    #     tags = object.scopes.all()
    #     print(tags)
    #     return tags



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

