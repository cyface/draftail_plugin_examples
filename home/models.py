"""
Page Models for Wagtail
"""
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField

from wagtail.core.models import Page


class HomePage(Page):
    """
    HomePage Page model - the body field has the features set to include our custom extensions, as well as bold.
    """
    body = RichTextField(features=['bold', 'underline', 'smallcaption'], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
