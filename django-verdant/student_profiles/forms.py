# -*- encoding: utf-8 -*-

from django import forms
from django.forms.formsets import BaseFormSet
from django.template.defaultfilters import filesizeformat

from PIL import Image

from rca.help_text import help_text
from rca.models import NewStudentPage, NewStudentPageShowCarouselItem
from rca.models import NewStudentPageMPhilCollaborator, NewStudentPageMPhilSponsor, NewStudentPageMPhilSupervisor
from rca.models import NewStudentPagePhDCollaborator, NewStudentPagePhDSponsor, NewStudentPagePhDSupervisor
from rca.models import RcaImage, StaffPage
from rca.models import SCHOOL_PROGRAMME_MAP, ALL_PROGRAMMES

################################################################################
## internal classes and functions

class OrderedFormset(BaseFormSet):

    def __init__(self, *args, **kwargs):
        #print args, kwargs

        #for index, value in enumerate(kwargs.get('initial', {})):
        #    value['order'] = index
        self._extra = 1

        super(OrderedFormset, self).__init__(*args, **kwargs)

    def clean(self):
        """Cleans the form and orders it by the hidden added order field."""

        order = lambda item: item.get('order', 10000)   # yes, 10000 = infinity!
        if hasattr(self, 'cleaned_data'):
            self.ordered_data = sorted(self.cleaned_data, key=order)

        return

    def add_fields(self, form, index):
        """Add the necessary hidden ordering field."""
        form.fields['order'] = forms.IntegerField(
            initial=index + 1,
            required=False,
            widget=forms.HiddenInput(attrs={'class': 'order-value'})
        )

    def get_extra(self):
        if self.initial:
            return 0
        else:
            return self._extra

    def set_extra(self, extra):
        self._extra = extra

    extra = property(get_extra, set_extra)


def make_formset(
        form, title=None, help_text=None,
        formset=OrderedFormset, extra=None,
        can_delete=False, max_num=None, validate_max=False,
        min_num=None, validate_min=False):
    """Return a FormSet for the given form class.

    This is duplicated from Django because we need a specific handling of the extra attribute, some extra attributes and
    want to set the OrderedFormset as default base.
    In our OrderedFormset, extra is a property that should only be overridden if the extra attribute is specified
    explicitly.
    """
    if min_num is None:
        min_num = 0
    if max_num is None:
        max_num = 1000
    absolute_max = max_num + 1000
    attrs = {'form': form,
             'can_order': False, 'can_delete': can_delete,
             'min_num': min_num, 'max_num': max_num,
             'absolute_max': absolute_max, 'validate_min': validate_min,
             'validate_max': validate_max,
             'title': title,
             'help_text': help_text,
             }
    if extra is not None:
        attrs['extra'] = extra
    return type(form.__name__ + str('FormSet'), (formset,), attrs)


class PhoneNumberField(forms.RegexField):
    """CharField that loosely validates phone numbers.
    
    Phone numbers start with + or 0 and continue with digits, spaces and dashes.
    That's all.
    """

    type = 'phonenumber'

    default_error_messages = {
        'invalid': 'Please enter a valid telephone number. Phone numbers can only contain digits, spaces, "+", parens and dashes.',
    }

    def __init__(self, *args, **kwargs):
        super(PhoneNumberField, self).__init__(
            r'^[+0][()\d -]+$',
            *args, **kwargs)
            
    def clean(self, value):
            if value:
                value = value.strip()
            return super(PhoneNumberField, self).clean(value)  

class BooleanField(forms.BooleanField):
    
    type = 'boolean'  # to make it easier in the template to distinguish what this is!


class ImageInput(forms.FileInput):

    def value_from_datadict(self, data, files, name):
        try:
            return int(data.get('{}_val'.format(name)))
        except (ValueError, TypeError):
            return None

    def render(self, name, value, attrs=None):
        preview = '<div class="preview_canvas"></div>'
        if value:
            try:
                value = int(value)
                image = RcaImage.objects.get(id=value)
                rendition = image.get_rendition('max-150x150')
                preview = """
                    <img src="{url}" class="preview_canvas" width="{width}" height="{height}" style="width: auto;">
                """.format(
                    url=rendition.url,
                    width=rendition.width, height=rendition.height,
                )
            except ValueError:
                pass
            except IOError:
                pass
        
        return """
            <div id="{name}" class="image-uploader-block" data-url="image/">
                <div class="preview" style="display: {preview_display};">
                    {preview}
                    <div class="progress">
                        <div class="bar" style="width: 0%; height: 3px; background: #0096ff;"></div>
                    </div> 
                    <i class="icon clearbutton action ion-android-delete" {hidden_clear} title="Remove"></i>
                </div>
                <div class="dropzone">Drop file here<br>to set image</div>
                <input type="hidden" id="id_{name}_val" name="{name}_val" value="{value_id}">

            </div>""".format(
                name=name,
                preview=preview, preview_display='block' if preview else 'none',
                value_id=value,
                hidden_clear='' if value else ' style="display: none;"',
            )
    


################################################################################
## Helper Forms

class ImageForm(forms.Form):
    """This is a simple form that validates a single image.
    
    This is used in validating image uploads, obviously. It's needed because we upload images not with the forms
    themselves but asynchronously by themselves.
    """

    def __init__(self, *args, **kwargs):

        self.max_size = None
        self.min_dim = None
        if 'max_size' in kwargs:
            self.max_size = kwargs.pop('max_size')
        if 'min_dim' in kwargs:
            self.min_dim = kwargs.pop('min_dim')

        super(ImageForm, self).__init__(*args, **kwargs)

    image = forms.ImageField()

    def clean_image(self):
        img = self.cleaned_data['image']
        if self.max_size and img.size > self.max_size:
            raise forms.ValidationError(u'Please keep file size under 10MB. Current file size {}'.format(filesizeformat(img.size)))

        if self.min_dim:
            dt = Image.open(img)
            minX, minY = self.min_dim
            width, height = dt.size
            if (width < minX or height < minY) and (height < minX or width < minY):
                raise forms.ValidationError(u'Minimum image size is {}x{} pixels.'.format(minX, minY))

        return img



################################################################################
## Starting out

class StartingForm(forms.ModelForm):

    class Meta:
        model = NewStudentPage
        fields = ['first_name', 'last_name']



################################################################################
## Basic Profile

class ProfileBasicForm(forms.ModelForm):

    title = forms.CharField(
        required=True,
        label='Full Name',
        help_text="Your name in full, as you'd like it to be seen by the public, e.g, Joe Smith",
    )

    profile_image = forms.IntegerField(
        required=False,
        help_text=help_text('rca.NewStudentPage', 'profile_image', default="Self-portrait image, 500x500px"),
        widget=ImageInput,
    )

    def clean_profile_image(self):
        if self.cleaned_data['profile_image']:
            return RcaImage.objects.get(id=self.cleaned_data['profile_image'])
        return None

    def clean_twitter_handle(self):
        if self.cleaned_data.get('twitter_handle'):
            handle = self.cleaned_data.get('twitter_handle', '')
            if handle.startswith('@'):
                return handle[1:]
            else:
                return handle
        else:
            return ''

    class Meta:
        model = NewStudentPage
        fields = ['title', 'first_name', 'last_name', 'twitter_handle', 'profile_image', 'statement']


class EmailForm(forms.Form):
    #saves to NewStudentPageContactsEmail
    email = forms.EmailField(
        required=False,    # because we'll only save those that are there anyway
        help_text=help_text('rca.NewStudentPageContactsEmail', 'email', default="Students can use personal email as well as firstname.surname@network.rca.ac.uk")
    )
EmailFormset = make_formset(EmailForm, 'Email')

class PhoneForm(forms.Form):
    #saves to NewStudentPageContactsPhone
    phone = PhoneNumberField(
        required=False,    # because we'll only save those that are there anyway
        help_text=help_text('rca.NewStudentPageContactsPhone', 'phone', default="UK mobile e.g. 07XXX XXXXXX or overseas landline, e.g. +33 (1) XXXXXXX")
    )
PhoneFormset = make_formset(PhoneForm, 'Phone', 'Enter your phone number(s) in international format with country code: +44 (0) 12345 678910')

class WebsiteForm(forms.Form):
    #saves to NewStudentPageContactsWebsite
    website = forms.URLField(
        required=False,    # because we'll only save those that are there anyway
        error_messages={'invalid': 'Please enter a full URL, including the ‘http://’!'},
        widget=forms.TextInput,
    )

    def clean_website(self):
        website = self.cleaned_data.get('website')
        if not website:
            return None
        if not website.startswith(u'http://') or website.startswith(u'https://'):
            return u'http://' + website
        else:
            return website

WebsiteFormset = make_formset(WebsiteForm, 'Website', 'Paste in the URL of the website in full, including the ‘http://’')


################################################################################
## Academic details

class ProfileAcademicDetailsForm(forms.ModelForm):
    
    class Meta:
        model = NewStudentPage
        fields = ['funding']
    
class PreviousDegreeForm(forms.Form):
    #saves to NewStudentPagePreviousDegree
    degree = forms.CharField(
        required=False,
        help_text=help_text('rca.NewStudentPagePreviousDegree', 'degree', default="Please include the degree level, subject, institution name and year of graduation, separated by commas"),
    )
PreviousDegreesFormset = make_formset(PreviousDegreeForm, 'Previous degrees', u'Include degree level, subject, institution name and year of graduation, separated by commas e.g. BA Fine Art, University of Brighton, 2011')

class ExhibitionForm(forms.Form):
    #saves to NewStudentPageExhibition
    exhibition = forms.CharField(
        required=False,
        help_text=help_text('rca.NewStudentPageExhibition', 'exhibition', default="Please include exhibition title, gallery, city and year, separated by commas"),
    )
ExhibitionsFormset = make_formset(ExhibitionForm, 'Exhibitions', u'Include exhibition title, gallery, city and year, separated by commas')

class ExperienceForm(forms.Form):
    experience = forms.CharField(
        max_length=255, required=False,
        help_text=help_text('rca.NewStudentPageExperience', 'experience', default="Please include job title, company name, city and year(s), separated by commas"),
    )
ExperiencesFormset = make_formset(ExperienceForm, 'Experience', u'Relevant professional experience. Include job title, company name, city and year(s), separated by commas')

class AwardsForm(forms.Form):
    #saves to NewStudentPageAward
    award = forms.CharField(
        required=False,
        help_text=help_text('rca.NewStudentPageAward', 'award', default="Please include prize, award title and year, separated by commas"),
    )
AwardsFormset = make_formset(AwardsForm, 'Awards', help_text('rca.NewStudentPageAward', 'award', default="Please include prize, award title and year, separated by commas"))

class PublicationsForm(forms.Form):
    #saves to NewStudentPagePublication
    name = forms.CharField(
        required=False,
        help_text=help_text('rca.NewStudentPagePublication', 'name', default="Please include author (if not you), title of article, title of publication, issue number, year, pages, separated by commas"),
    )
PublicationsFormset = make_formset(PublicationsForm, 'Publications', u'Include author (if not you), article title, journal title, issue number, year, pages, separated by commas')

class ConferencesForm(forms.Form):
    #saves to NewStudentPageConference
    name = forms.CharField(
        required=False,
        help_text=help_text('rca.NewStudentPageConference', 'name', default="Please include paper, title of conference, institution, date, separated by commas"),
    )
ConferencesFormset = make_formset(ConferencesForm, 'Conferences', u'Include paper title, conference, institution, date, separated by commas')

################################################################################
## postcard upload

class PostcardUploadForm(forms.ModelForm):
    postcard_image = forms.IntegerField(
        label='Postcard image',
        required=False,
        help_text="Image will be used to print a set of postcards with your contact details, for you to use during the Show. The image will not appear in your Show online catalogue. Image must be A6 plus 2mm 'bleed' on each edge (1801 x 1287px, ie. 152 x 109mm @ 300 dpi). This must be uploaded at the correct size and before the deadline for postcards to be printed.",
        widget=ImageInput,
    )

    def clean_postcard_image(self):
        try:
            return RcaImage.objects.get(id=self.cleaned_data.get('postcard_image'))
        except RcaImage.DoesNotExist:
            return None

    class Meta:
        model = NewStudentPage
        fields = [
            'postcard_image',
        ]


################################################################################
## custom school and programme choices for 2015

SCHOOL_CHOICES = (
    ('', '---------'),
    ('schoolofarchitecture', 'School of Architecture'),
    ('schoolofcommunication', 'School of Communication'),
    ('schoolofdesign', 'School of Design'),
    ('schooloffineart', 'School of Fine Art'),
    ('schoolofhumanities', 'School of Humanities'),
    ('schoolofmaterial', 'School of Material'),
)

PROGRAMME_CHOICES_2015 = (('', '---------'), ) + tuple(sorted([
    (
        2015, tuple([
                    (programme, dict(ALL_PROGRAMMES)[programme])
                    for programme
                    in sorted(set(sum(SCHOOL_PROGRAMME_MAP['2014'].values(), [])))
                ])
    )
], reverse=True))


################################################################################
## MA details

class MADetailsForm(forms.ModelForm):

    ma_in_show = forms.BooleanField(
        label='In show',
        required=False,
        help_text="Please tick only if you're in the Show this academic year.",
    )

    ma_graduation_year = forms.IntegerField(
        label='Graduation year',
        min_value=1950, max_value=2050,
        required=False,
        help_text=help_text('rca.NewStudentPage', 'ma_graduation_year'),
    )

    ma_school = forms.ChoiceField(
        label="School", help_text=help_text('rca.NewStudentPage', 'ma_school'),
        choices=SCHOOL_CHOICES,
        required=False,
    )

    ma_programme = forms.ChoiceField(
        label="Programme",
        choices=PROGRAMME_CHOICES_2015,
        required=False,
    )

    def clean_ma_graduation_year(self):
        if self.cleaned_data['ma_graduation_year']:
            return self.cleaned_data['ma_graduation_year']
        else:
            return ''

    class Meta:
        model = NewStudentPage
        fields = [
            'ma_in_show',
            'ma_school', 'ma_programme',
            'ma_graduation_year',
            'ma_specialism',
        ]


class MAShowDetailsForm(forms.ModelForm):

    class Meta:
        model = NewStudentPage
        fields = [
            'show_work_type',
            'show_work_title',
            'show_work_location',
            'show_work_description',
        ]


class MAShowCarouselItemForm(forms.Form):

    item_type = forms.ChoiceField(
        choices = (   
            ('image', 'Image'),    # if you change these values, you must also change the values in the javascript and in the views!
            ('video', 'Video'),
        )
    )

    image_id = forms.IntegerField(   # name is _id because that's what's going to be saved
        label='Image',
        required=False,
        help_text=help_text('rca.CarouselItemFields', 'image', default='Landscape images will display better within the carousel than portrait images. Consider sizing all your images to the same dimension - ideally 2000 x 1125 pixels.'),
        widget=ImageInput,
    )

    # image type fields (there are a lot of them!)
    title = forms.CharField(
        max_length=255, required=False, label='Title',
    )
    title.half = True
    creator = forms.CharField(
        max_length=255, required=False, help_text=help_text('rca.RcaImage', 'creator') + 'If this work was a collaboration with others, list them here after your own name in brackets.',
    )
    creator.half = True
    year = forms.CharField(
        max_length=255, required=False, help_text=help_text('rca.RcaImage', 'year'),
    )
    year.half = True
    medium = forms.CharField(
        max_length=255, required=False, help_text=help_text('rca.RcaImage', 'medium', default='e.g. Bronze, copper wire and plaster'),
    )
    medium.half = True
    dimensions = forms.CharField(
        max_length=255, required=False, help_text=help_text('rca.RcaImage', 'dimensions', default='e.g. 100 cm x 145 cm'),
    )
    dimensions.half = True
    photographer = forms.CharField(
        max_length=255, required=False, help_text=help_text('rca.RcaImage', 'photographer'),
    )
    photographer.half = True

    embedly_url = forms.URLField(
        label='Vimeo URL',
        required=False,
        help_text='Video content must first be uploaded to a Vimeo account. Then simply cut and paste the Vimeo URL in full, e.g. http://vimeo.com/117377525',
    )
    poster_image_id = forms.IntegerField(
        label='Poster image',
        required=False,
        help_text='Add a still image as a placeholder for your video when it is not playing.',
        widget=ImageInput,
    )

    def clean_title(self):
        if self.cleaned_data.get('item_type') == 'image' and self.cleaned_data.get('image_id') and not self.cleaned_data.get('title'):
            raise forms.ValidationError('This field is required.')
        else:
            return self.cleaned_data.get('title', '')
MAShowCarouselItemFormset = make_formset(MAShowCarouselItemForm, max_num=12, validate_max=True)

class MACollaboratorForm(forms.Form):
    #saves to NewStudentPageShowCollaborator
    name = forms.CharField(
        required=False,
        help_text=help_text('rca.NewStudentPageShowCollaborator', 'name', default="Please include collaborator's name and programme (if RCA), separated by commas"),
    )
MACollaboratorFormset = make_formset(MACollaboratorForm, 'Collaborators', help_text('rca.NewStudentPageShowCollaborator', 'name', default="Please include collaborator's name and programme (if RCA)."))

class MASponsorForm(forms.Form):
    #saves to NewStudentPageShowSponsor
    name = forms.CharField(
        required=False,
        help_text=help_text('rca.NewStudentPageShowSponsor', 'name', default="Please list companies and individuals that have provided financial or in kind sponsorship for your final project, separated by commas"),
    )
MASponsorFormset = make_formset(MASponsorForm, 'Sponsors', help_text('rca.NewStudentPageShowSponsor', 'name', default="Please list companies and individuals that have provided financial or in kind sponsorship for your final project."))


# MPhil and PhD forms
class MPhilForm(forms.ModelForm):

    mphil_school = forms.ChoiceField(
        label="School", help_text=help_text('rca.NewStudentPage', 'mphil_school'),
        choices=SCHOOL_CHOICES,
        required=False,
    )

    mphil_programme = forms.ChoiceField(
        label="Programme", help_text=help_text('rca.NewStudentPage', 'mphil_programme'),
        choices=PROGRAMME_CHOICES_2015,
        required=False,
    )

    mphil_start_year = forms.IntegerField(
        label='Start year',
        min_value=1950, max_value=2050,
        required=False,
        help_text=help_text('rca.NewStudentPage', 'mphil_start_year'),
    )
    mphil_graduation_year = forms.IntegerField(
        label='Graduation year',
        min_value=1950, max_value=2050,
        required=False,
        help_text='If unknown, enter current year',
    )

    def clean_mphil_start_year(self):
        if self.cleaned_data['mphil_start_year']:
            return self.cleaned_data['mphil_start_year']
        else:
            return ''
    def clean_mphil_graduation_year(self):
        if self.cleaned_data['mphil_graduation_year']:
            return self.cleaned_data['mphil_graduation_year']
        else:
            return ''


    class Meta:
        model = NewStudentPage
        fields = [
            'mphil_in_show',
            'mphil_school', 'mphil_programme',
            'mphil_start_year',
            'mphil_graduation_year',
            'mphil_status',
            'mphil_degree_type',
        ]


class MPhilShowForm(forms.ModelForm):
    class Meta:
        model = NewStudentPage
        fields = [
            'mphil_dissertation_title',
            'mphil_statement',
            'mphil_work_location',
        ]
# carousel items as above, sponsor and collaborator almost as above

# we create new forms here because the labels and help_texts are slightly different
class MPhilCollaboratorForm(forms.ModelForm):
    class Meta:
        model = NewStudentPageMPhilCollaborator
        fields = ['name']
MPhilCollaboratorFormset = make_formset(
    MPhilCollaboratorForm,
    'Collaborators',
    help_text('rca.NewStudentPageMPhilCollaborator', 'name', default="Please include collaborator's name and programme (if RCA)."),
)

class MPhilSponsorForm(forms.ModelForm):
    class Meta:
        model = NewStudentPageMPhilSponsor
        fields = ['name']
MPhilSponsorFormset = make_formset(
    MPhilSponsorForm,
    'Sponsors',
    help_text('rca.NewStudentPageMPhilSponsor', 'name', default="Please list companies and individuals that have provided financial or in kind sponsorship for your final project.")
)

    
class MPhilSupervisorForm(forms.ModelForm):
    supervisor_type = forms.ChoiceField(
        label='Type',
        choices = (   
            ('internal', 'Internal'),
            ('other', 'Other'),
        )
    )

    supervisor = forms.ModelChoiceField(
        queryset=StaffPage.objects.all().order_by('last_name'),
        required=False,
        help_text=help_text('rca.NewStudentPageMPhilSupervisor', 'supervisor', default="Please select your RCA supervisor's profile page or enter the name of an external supervisor"),
        widget=forms.Select(attrs={'width': '100%', 'class': 'supervisor-select'}),
    )

    class Meta:
        model = NewStudentPageMPhilSupervisor
        fields = ['supervisor', 'supervisor_other']
MPhilSupervisorFormset = make_formset(MPhilSupervisorForm, 'Supervisors')

# and the same once again with PhD instead of MPhil
class PhDForm(forms.ModelForm):

    phd_school = forms.ChoiceField(
        label="School", help_text=help_text('rca.NewStudentPage', 'phd_school'),
        choices=SCHOOL_CHOICES,
        required=False,
    )

    phd_programme = forms.ChoiceField(
        label="Programme", help_text=help_text('rca.NewStudentPage', 'phd_programme'),
        choices=PROGRAMME_CHOICES_2015,
        required=False,
    )

    phd_start_year = forms.IntegerField(
        label='Start year',
        min_value=1950, max_value=2050,
        required=False,
        help_text=help_text('rca.NewStudentPage', 'phd_start_year'),
    )
    phd_graduation_year = forms.IntegerField(
        label='Graduation year',
        min_value=1950, max_value=2050,
        required=False,
        help_text='If unknown, enter current year'
    )

    def clean_phd_start_year(self):
        if self.cleaned_data['phd_start_year']:
            return self.cleaned_data['phd_start_year']
        else:
            return ''
    def clean_phd_graduation_year(self):
        if self.cleaned_data['phd_graduation_year']:
            return self.cleaned_data['phd_graduation_year']
        else:
            return ''

    class Meta:
        model = NewStudentPage
        fields = [
            'phd_in_show',
            'phd_school', 'phd_programme',
            'phd_start_year', 'phd_graduation_year',
            'phd_status',
            'phd_degree_type',
        ]


class PhDShowForm(forms.ModelForm):
    class Meta:
        model = NewStudentPage
        fields = [
            'phd_dissertation_title',
            'phd_statement',
            'phd_work_location',
        ]


class PhDCollaboratorForm(forms.ModelForm):
    class Meta:
        model = NewStudentPagePhDCollaborator
        fields = ['name']
PhDCollaboratorFormset = make_formset(
    PhDCollaboratorForm,
    'Collaborators',
    help_text('rca.NewStudentPagePhDCollaborator', 'name', default="Please include collaborator's name and programme (if RCA).")
)

class PhDSponsorForm(forms.ModelForm):
    class Meta:
        model = NewStudentPagePhDSponsor
        fields = ['name']
PhDSponsorFormset = make_formset(
    PhDSponsorForm,
    'Sponsors',
    help_text('rca.NewStudentPagePhDSponsor', 'name', default="Please list companies and individuals that have provided financial or in kind sponsorship for your final project.")
)

class PhDSupervisorForm(forms.ModelForm):
    supervisor_type = forms.ChoiceField(
        label='Type',
        choices = (   
            ('internal', 'Internal'),
            ('other', 'Other'),
        )
    )
    
    supervisor = forms.ModelChoiceField(
        queryset=StaffPage.objects.all().order_by('last_name'),
        required=False,
        help_text=help_text('rca.NewStudentPagePhDSupervisor', 'supervisor', default="Please select your RCA supervisor's profile page or enter the name of an external supervisor."),
        widget=forms.Select(attrs={'width': '100%', 'class': 'supervisor-select'}),
    )

    class Meta:
        model = NewStudentPagePhDSupervisor
        fields = ['supervisor', 'supervisor_other']
PhDSupervisorFormset = make_formset(PhDSupervisorForm, 'Supervisors')
