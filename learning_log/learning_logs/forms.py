#!/usr/bin/env python
# encoding: utf-8

from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta(object):
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta(object):
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
