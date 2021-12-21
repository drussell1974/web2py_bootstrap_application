# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a controller for the tutorials
# -------------------------------------------------------------------------

# ---- tutorial index page ----
def index():
    response.title = "Placeholder content"
    page_text = {
        'main_heading':'Placeholder content',
        'strapline_text':'During design and development, dummy content can give the product a look-and-feel.',
        'intro_text':'Lorem ipsum text is commonly used in the layout in web design to draft content. Likewise, placeholder images provide visual content and indicators for the optimum size images that should be used for the actual content.',
        'reference_urls': [
            {'name':'Lorem ipsum','url':'https://loremipsum.io/'}, 
            {'name':'Placeholder.com','url':'https://placeholder.com/'}
        ],
        'see_more_url':None
    }

    return page_text


def bootstrap_example(): 
    response.title = "Bootstrap 4"
    page_text = {   
        'main_heading': 'What is Bootstrap?',
        'strapline_text': 'Bootstrap is a collection of bits of code written in HTML, CSS and JavaScript to quickly build websites',
        'intro_text': 'Bootstrap is a free front-end framework constisting of a number of features for creating responsive and dynamic web sites.',
        'reference_urls': [
            {'name':'GetBootstrap 4','url':'https://getbootstrap.com/docs/4.6/getting-started/introduction/'}, 
        ],
        'see_more_url':None
    }

    return page_text


def bootstrap_card(): 
    response.title = "Bootstrap - Card"
    page_text = {   
        'main_heading': 'Bootstrap - Card',
        'strapline_text': 'Bootstrap is a collection of bits of code written in HTML, CSS and JavaScript to quickly build websites',
        'intro_text': 'Bootstrap is a free front-end framework constisting of a number of features for creating responsive and dynamic web sites.',
        'reference_urls': [
            {'name':'GetBootstrap 4','url':'https://getbootstrap.com/docs/4.6/getting-started/introduction/'}, 
            {'name':'GetBootstrap - Components - Cards','url':'https://getbootstrap.com/docs/4.0/components/card/'}
        ],
        'see_more_url':'https://getbootstrap.com/docs/4.0/components/card/'
    }

    return page_text


def bootstrap_breadcrumb(): 
    response.title = "Bootstrap - Breadcrumb"
    page_text = {   
        'main_heading': 'Bootstrap - Breadcrumb',
        'strapline_text': 'Bootstrap is a collection of bits of code written in HTML, CSS and JavaScript to quickly build websites',
        'intro_text': 'Bootstrap is a free front-end framework constisting of a number of features for creating responsive and dynamic web sites.',
        'reference_urls': [
            {'name':'GetBootstrap 4','url':'https://getbootstrap.com/docs/4.6/getting-started/introduction/'}, 
            {'name':'GetBootstrap - Components - Breadcrumb','url':'https://getbootstrap.com/docs/4.0/components/breadcrumb/'}
        ],
        'see_more_url':'https://getbootstrap.com/docs/4.0/components/breadcrumb/'
    }

    return page_text


def bootstrap_button(): 
    response.title = "Bootstrap - Buttons"
    page_text = {   
        'main_heading': 'Bootstrap - Buttons',
        'strapline_text': 'Bootstrap is a collection of bits of code written in HTML, CSS and JavaScript to quickly build websites',
        'intro_text': 'Bootstrap is a free front-end framework constisting of a number of features for creating responsive and dynamic web sites.',
        'reference_urls': [
            {'name':'GetBootstrap 4','url':'https://getbootstrap.com/docs/4.6/getting-started/introduction/'}, 
            {'name':'GetBootstrap - Components - Buttons','url':'https://getbootstrap.com/docs/4.0/components/buttons/'}
        ],
        'see_more_url':'https://getbootstrap.com/docs/4.0/components/buttons/'
    }

    return page_text


def bootstrap_jumbotron(): 
    response.title = "Bootstrap - Jumbotron"
    page_text = {   
        'main_heading': 'Bootstrap - Jumbotron',
        'strapline_text': 'Bootstrap is a collection of bits of code written in HTML, CSS and JavaScript to quickly build websites',
        'intro_text': 'Bootstrap is a free front-end framework constisting of a number of features for creating responsive and dynamic web sites.',
        'reference_urls': [
            {'name':'GetBootstrap 4','url':'https://getbootstrap.com/docs/4.6/getting-started/introduction/'}, 
            {'name':'GetBootstrap - Components - Jumbotron','url':'https://getbootstrap.com/docs/4.0/components/jumbotron/'}
        ],
        'see_more_url':'https://getbootstrap.com/docs/4.0/components/jumbotron/'
    }

    return page_text


def bootstrap_table(): 
    response.title = "Bootstrap - Table"
    page_text = {   
        'main_heading': 'Bootstrap - Table',
        'strapline_text': 'Bootstrap is a collection of bits of code written in HTML, CSS and JavaScript to quickly build websites',
        'intro_text': 'Bootstrap is a free front-end framework constisting of a number of features for creating responsive and dynamic web sites.',
        'reference_urls': [
            {'name':'GetBootstrap 4','url':'https://getbootstrap.com/docs/4.6/getting-started/introduction/'}, 
            {'name':'GetBootstrap - Components - Table','url':'https://getbootstrap.com/docs/4.6/content/tables/'}
        ],
        'see_more_url':'https://getbootstrap.com/docs/4.6/content/tables/'
    }

    return page_text
