# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NewsIndex.show_in_menus'
        db.add_column(u'rca_newsindex', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'StudentPage.show_in_menus'
        db.add_column(u'rca_studentpage', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'JobPage.show_in_menus'
        db.add_column(u'rca_jobpage', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ContactUsPage.show_in_menus'
        db.add_column(u'rca_contactuspage', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ResearchInnovationPage.show_in_menus'
        db.add_column(u'rca_researchinnovationpage', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'NewsItem.show_in_menus'
        db.add_column(u'rca_newsitem', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'HomePage.show_in_menus'
        db.add_column(u'rca_homepage', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ResearchItem.show_in_menus'
        db.add_column(u'rca_researchitem', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'EventItem.external_link'
        db.add_column(u'rca_eventitem', 'external_link',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'EventItem.external_link_text'
        db.add_column(u'rca_eventitem', 'external_link_text',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'StandardPage.show_in_menus'
        db.add_column(u'rca_standardpage', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'StandardIndex.show_in_menus'
        db.add_column(u'rca_standardindex', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'JobsIndex.show_in_menus'
        db.add_column(u'rca_jobsindex', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ProgrammePage.show_in_menus'
        db.add_column(u'rca_programmepage', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GalleryPage.show_in_menus'
        db.add_column(u'rca_gallerypage', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'SchoolPage.show_in_menus'
        db.add_column(u'rca_schoolpage', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'RcaNowPage.show_in_menus'
        db.add_column(u'rca_rcanowpage', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CurrentResearchPage.show_in_menus'
        db.add_column(u'rca_currentresearchpage', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'StaffPage.show_in_menus'
        db.add_column(u'rca_staffpage', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'RcaNowIndex.show_in_menus'
        db.add_column(u'rca_rcanowindex', 'show_in_menus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NewsIndex.show_in_menus'
        db.delete_column(u'rca_newsindex', 'show_in_menus')

        # Deleting field 'StudentPage.show_in_menus'
        db.delete_column(u'rca_studentpage', 'show_in_menus')

        # Deleting field 'JobPage.show_in_menus'
        db.delete_column(u'rca_jobpage', 'show_in_menus')

        # Deleting field 'ContactUsPage.show_in_menus'
        db.delete_column(u'rca_contactuspage', 'show_in_menus')

        # Deleting field 'ResearchInnovationPage.show_in_menus'
        db.delete_column(u'rca_researchinnovationpage', 'show_in_menus')

        # Deleting field 'NewsItem.show_in_menus'
        db.delete_column(u'rca_newsitem', 'show_in_menus')

        # Deleting field 'HomePage.show_in_menus'
        db.delete_column(u'rca_homepage', 'show_in_menus')

        # Deleting field 'ResearchItem.show_in_menus'
        db.delete_column(u'rca_researchitem', 'show_in_menus')

        # Deleting field 'EventItem.external_link'
        db.delete_column(u'rca_eventitem', 'external_link')

        # Deleting field 'EventItem.external_link_text'
        db.delete_column(u'rca_eventitem', 'external_link_text')

        # Deleting field 'StandardPage.show_in_menus'
        db.delete_column(u'rca_standardpage', 'show_in_menus')

        # Deleting field 'StandardIndex.show_in_menus'
        db.delete_column(u'rca_standardindex', 'show_in_menus')

        # Deleting field 'JobsIndex.show_in_menus'
        db.delete_column(u'rca_jobsindex', 'show_in_menus')

        # Deleting field 'ProgrammePage.show_in_menus'
        db.delete_column(u'rca_programmepage', 'show_in_menus')

        # Deleting field 'GalleryPage.show_in_menus'
        db.delete_column(u'rca_gallerypage', 'show_in_menus')

        # Deleting field 'SchoolPage.show_in_menus'
        db.delete_column(u'rca_schoolpage', 'show_in_menus')

        # Deleting field 'RcaNowPage.show_in_menus'
        db.delete_column(u'rca_rcanowpage', 'show_in_menus')

        # Deleting field 'CurrentResearchPage.show_in_menus'
        db.delete_column(u'rca_currentresearchpage', 'show_in_menus')

        # Deleting field 'StaffPage.show_in_menus'
        db.delete_column(u'rca_staffpage', 'show_in_menus')

        # Deleting field 'RcaNowIndex.show_in_menus'
        db.delete_column(u'rca_rcanowindex', 'show_in_menus')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'wagtailcore.page': {
            'Meta': {'object_name': 'Page'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pages'", 'to': u"orm['contenttypes.ContentType']"}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rca.advert': {
            'Meta': {'object_name': 'Advert'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adverts'", 'to': u"orm['wagtailcore.Page']"}),
            'show_globally': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.contactuspage': {
            'Meta': {'object_name': 'ContactUsPage', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.currentresearchpage': {
            'Meta': {'object_name': 'CurrentResearchPage', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.eventitem': {
            'Meta': {'object_name': 'EventItem', '_ormbases': [u'wagtailcore.page']},
            'audience': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cost': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'date_from': ('django.db.models.fields.DateField', [], {}),
            'date_to': ('django.db.models.fields.DateField', [], {}),
            'external_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'external_link_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'listing_intro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'location_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_on_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'signup_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'specific_directions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'specific_directions_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'times': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'})
        },
        u'rca.eventitemcarouselitem': {
            'Meta': {'object_name': 'EventItemCarouselItem'},
            'embedly_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.EventItem']"})
        },
        u'rca.eventitemrelatedprogramme': {
            'Meta': {'object_name': 'EventItemRelatedProgramme'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_programmes'", 'to': u"orm['rca.EventItem']"}),
            'programme': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.eventitemrelatedschool': {
            'Meta': {'object_name': 'EventItemRelatedSchool'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_schools'", 'to': u"orm['rca.EventItem']"}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.eventitemspeaker': {
            'Meta': {'object_name': 'EventItemSpeaker'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'speakers'", 'to': u"orm['rca.EventItem']"}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rca.gallerypage': {
            'Meta': {'object_name': 'GalleryPage', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.homepage': {
            'Meta': {'object_name': 'HomePage', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.jobpage': {
            'Meta': {'object_name': 'JobPage', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.jobsindex': {
            'Meta': {'object_name': 'JobsIndex', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.newsindex': {
            'Meta': {'object_name': 'NewsIndex', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'rca.newsitem': {
            'Meta': {'object_name': 'NewsItem', '_ormbases': [u'wagtailcore.page']},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {}),
            'listing_intro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_on_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.newsitemcarouselitem': {
            'Meta': {'object_name': 'NewsItemCarouselItem'},
            'embedly_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'overlay_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.NewsItem']"}),
            'poster_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"})
        },
        u'rca.newsitemrelatedlink': {
            'Meta': {'object_name': 'NewsItemRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.NewsItem']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.newsitemrelatedprogramme': {
            'Meta': {'object_name': 'NewsItemRelatedProgramme'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_programmes'", 'to': u"orm['rca.NewsItem']"}),
            'programme': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.newsitemrelatedschool': {
            'Meta': {'object_name': 'NewsItemRelatedSchool'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_schools'", 'to': u"orm['rca.NewsItem']"}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.programmepage': {
            'Meta': {'object_name': 'ProgrammePage', '_ormbases': [u'wagtailcore.page']},
            'download_document_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'download_document_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'head_of_programme': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'head_of_programme_statement': ('wagtail.wagtailcore.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'programme_video': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'rca.programmepagecarouselitem': {
            'Meta': {'object_name': 'ProgrammePageCarouselItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.ProgrammePage']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.programmepagefacilities': {
            'Meta': {'object_name': 'ProgrammePageFacilities'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'facilities'", 'to': u"orm['rca.ProgrammePage']"}),
            'text': ('wagtail.wagtailcore.fields.RichTextField', [], {})
        },
        u'rca.programmepageoursites': {
            'Meta': {'object_name': 'ProgrammePageOurSites'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'our_sites'", 'to': u"orm['rca.ProgrammePage']"}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.programmepagerelatedlink': {
            'Meta': {'object_name': 'ProgrammePageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.ProgrammePage']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.programmepagestudentstory': {
            'Meta': {'object_name': 'ProgrammePageStudentStory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'student_stories'", 'to': u"orm['rca.ProgrammePage']"}),
            'text': ('wagtail.wagtailcore.fields.RichTextField', [], {})
        },
        u'rca.rcaimage': {
            'Meta': {'object_name': 'RcaImage'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'creator': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dimensions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medium': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'permission': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'photographer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'width': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.rcanowindex': {
            'Meta': {'object_name': 'RcaNowIndex', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.rcanowpage': {
            'Meta': {'object_name': 'RcaNowPage', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.rcarendition': {
            'Meta': {'object_name': 'RcaRendition'},
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'filter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['wagtailimages.Filter']"}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'renditions'", 'to': u"orm['rca.RcaImage']"}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        u'rca.researchinnovationpage': {
            'Meta': {'object_name': 'ResearchInnovationPage', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.researchitem': {
            'Meta': {'object_name': 'ResearchItem', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.schoolpage': {
            'Meta': {'object_name': 'SchoolPage', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'rca.staffpage': {
            'Meta': {'object_name': 'StaffPage', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.standardindex': {
            'Meta': {'object_name': 'StandardIndex', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.standardpage': {
            'Meta': {'object_name': 'StandardPage', '_ormbases': [u'wagtailcore.page']},
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.standardpagecarouselitem': {
            'Meta': {'object_name': 'StandardPageCarouselItem'},
            'embedly_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'overlay_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.StandardPage']"}),
            'poster_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"})
        },
        u'rca.standardpagerelatedlink': {
            'Meta': {'object_name': 'StandardPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.StandardPage']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.studentpage': {
            'Meta': {'object_name': 'StudentPage', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'wagtailimages.filter': {
            'Meta': {'object_name': 'Filter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spec': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['rca']