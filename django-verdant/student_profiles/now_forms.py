# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import re

from django import forms
from django.forms.formsets import formset_factory

from rca.help_text import help_text
from rca.models import RcaNowPage, NewStudentPage
from rca.models import AREA_CHOICES
from .forms import OrderedFormset


class PageForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        
        instance = kwargs.get('instance')
        if instance:
            initial = kwargs.get('initial', {})
            initial['tags'] = ','.join([t.name for t in instance.tags.all()])
            
            # parse out the introduction here
            r = re.compile('^(<h1>(.*?)</h1>)')
            if r.search(instance.body):
                match_groups = r.search(instance.body).groups()
                intro_all = match_groups[0]
                intro = match_groups[1]
                initial['intro_text'] = intro
                initial['body'] = instance.body[len(intro_all):]
            
            if NewStudentPage.objects.filter(live=True, title=instance.author).exists():
                initial['by'] = 'single'
                initial['author_single'] = NewStudentPage.objects.get(live=True, title=instance.author)
            
            kwargs['initial'] = initial
        
        super(PageForm, self).__init__(*args, **kwargs)
    
    intro_text = forms.CharField(
        label="Introduction",
        required=False,
        widget=forms.Textarea,
    )
    
    by = forms.ChoiceField(
        label='by',
        required=False,
        choices=(
            ('single', 'Single student'),
            ('group', 'Group of students'),
        ),
        initial='group',
    )
    
    author_single = forms.ModelChoiceField(
        label='Author',
        required=False,
        queryset=NewStudentPage.objects.filter(live=True).order_by('last_name', 'first_name'),
        widget=forms.Select(attrs={'width': '100%'})
    )

    def clean_twitter_feed(self):
        if self.cleaned_data.get('twitter_feed'):
            handle = self.cleaned_data.get('twitter_feed', '')
            if handle.startswith('@'):
                return handle[1:]
            else:
                return handle
        else:
            return ''

    def clean(self):
        intro_text = self.cleaned_data.get('intro_text', '')
        body = self.cleaned_data.get('body', '')
        
        self.cleaned_data['body'] = '<h1>{intro}</h1>{body}'.format(
            intro=intro_text,
            body=body
        )
        
        if self.cleaned_data.get('by') == 'single' and self.cleaned_data.get('author_single'):
            self.cleaned_data['author'] = self.cleaned_data.get('author_single').title
        
        return self.cleaned_data
    
    class Meta:
        model = RcaNowPage
        fields = [
            'title',
            'intro_text',
            'body',
            'by',
            'author_single',
            'author',
            'date',
            'school',
            'programme',
            'twitter_feed',
            'tags',
        ]


class RelatedLinkForm(forms.Form):
    link = forms.URLField(
        required=False,    # because we'll only save those that are there anyway
        error_messages={'invalid': 'Please enter a full URL, including the ‘http://’!'},
        widget=forms.TextInput,
    )

    def clean_link(self):
        link = self.cleaned_data.get('link')
        if not link:
            return None
        if not link.startswith('http://') or link.startswith('https://'):
            return 'http://' + link
        else:
            return link
RelatedLinkFormset = formset_factory(RelatedLinkForm, extra=1, formset=OrderedFormset)
RelatedLinkFormset.title = 'Web links'
RelatedLinkFormset.help_text = 'Paste in the URL of the website in full, including the ‘http://’'


class AreaForm(forms.Form):
    area = forms.ChoiceField(
        choices=(('', '---------'),) + AREA_CHOICES,
    )
AreaFormSet = formset_factory(AreaForm, extra=1, formset=OrderedFormset)
AreaFormSet.title = 'Areas'
AreaFormSet.help_text = help_text=help_text('rca.RcaNowPageArea', 'area')