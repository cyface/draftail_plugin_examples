"""
Custom Extensions for Wagtail
"""

from wagtail.core.whitelist import attribute_rule
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.core import hooks
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler


@hooks.register('register_rich_text_features')
def register_smallcaption_feature(features):
    """
    Registering the 'smallcaption' Draftail feature which
    adds a span around the selected text
    with its class set to 'small-caption'
    """
    # 1. Set up variables for use below
    feature_name = 'smallcaption'
    type_ = 'SMALLCAPTION'
    # 2. Set up a dictionary to pass to Draftail to configure
    # how it handles this feature in its toolbar.
    # The 'style' attribute controls how Draftail formats that text
    # in the editor - does not affect the final rendered HTML
    # In this case, I am adding similar formatting to what
    # the CSS will do to that 'small-caption' class in the template
    control = {
        'type': type_,
        'label': 'SC',
        'description': 'Small Caption',
        'style': {
            'font-size': '75%',
            'color': '#666'
        }
    }
    # 3. Register the configuration for Draftail to know about.
    # This makes it available to add to editing toolbars,
    # but the RichTextField(features=[]) list has to include it to
    # actually make it appear in the toolbar
    features.register_editor_plugin(
        'draftail',
        feature_name,
        draftail_features.InlineStyleFeature(control)
    )
    # 4.configure the content transform
    # from the DB to the editor and back.
    # The "From" version uses a CSS selector to find spans with
    # a class of 'small-caption'
    # The "To" version adds a span with a class of 'small-caption'
    # surrounding the selected text
    db_conversion = {
        'from_database_format': {
            'span[class="small-caption"]':
                InlineStyleElementHandler(type_)
        },
        'to_database_format': {
            'style_map': {type_: 'span class="small-caption"'}
        },
    }
    # 5. Call register_converter_rule to register
    # the content transformation conversion rule with Draftail
    features.register_converter_rule(
        'contentstate',
        feature_name,
        db_conversion
    )


# 1. Use the register_rich_text_features hook.
@hooks.register('register_rich_text_features')
def register_underline_feature(features):
    """
    Registering the `underline` feature, which uses the `UNDERLINE` Draft.js inline style type,
    and is stored as HTML with an `<s>` tag.
    """
    feature_name = 'underline'
    type_ = 'UNDERLINE'

    # 2. Configure how Draftail handles the feature in its toolbar.
    control = {
        'type': type_,
        'label': 'U',
        'description': 'Underline',
    }

    # 3. Call register_editor_plugin to register the configuration for Draftail.
    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    # 4.configure the content transform from the DB to the editor and back.
    db_conversion = {
        'from_database_format': {'span[style="text-decoration: underline"]': InlineStyleElementHandler(type_)},
        'to_database_format': {'style_map': {type_: 'span style="text-decoration: underline"'}},
    }

    # 5. Call register_converter_rule to register the content transformation conversion.
    features.register_converter_rule('contentstate', feature_name, db_conversion)
