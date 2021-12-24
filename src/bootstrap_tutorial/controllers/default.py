# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a controller for the tutorials
# -------------------------------------------------------------------------

# ---- tutorial index page ----
def index():
    response.title = 'Placeholder content'
    
    strapline_text = 'During design and development, dummy content can give the product a look-and-feel.'
    intro_text = 'Lorem ipsum text is commonly used in the layout in web design to draft content. Likewise, placeholder images provide visual content and indicators for the optimum size images that should be used for the actual content.',
    reference_urls = [
            {'name':'Lorem ipsum','url':'https://loremipsum.io/'}, 
            {'name':'Placeholder.com','url':'https://placeholder.com/'}
        ]
    see_more_url = None
    
    return dict(strapline_text=strapline_text, intro_text=intro_text, reference_urls=reference_urls, see_more_url=see_more_url)


def bootstrap_card(): 
    response.title = 'Bootstrap - Card'
     
    strapline_text = 'Bootstrap is a collection of bits of code written in HTML, CSS and JavaScript to quickly build websites'
    intro_text = 'Bootstrap is a free front-end framework constisting of a number of features for creating responsive and dynamic web sites.'
    reference_urls = [
            {'name':'GetBootstrap 4','url':'https://getbootstrap.com/docs/4.6/getting-started/introduction/'}, 
            {'name':'GetBootstrap - Components - Cards','url':'https://getbootstrap.com/docs/4.0/components/card/'}
        ]
    see_more_url = 'https://getbootstrap.com/docs/4.0/components/card/'
    
    return dict(strapline_text=strapline_text, intro_text=intro_text, reference_urls=reference_urls, see_more_url=see_more_url)


def bootstrap_breadcrumb(): 
    response.title = 'Bootstrap - Breadcrumb'
    
    strapline_text = 'Bootstrap is a collection of bits of code written in HTML, CSS and JavaScript to quickly build websites.'
    intro_text = 'Bootstrap is a free front-end framework constisting of a number of features for creating responsive and dynamic web sites.'
    reference_urls = [
            {'name':'GetBootstrap 4','url':'https://getbootstrap.com/docs/4.6/getting-started/introduction/'}, 
            {'name':'GetBootstrap - Components - Breadcrumb','url':'https://getbootstrap.com/docs/4.0/components/breadcrumb/'}
        ]
    see_more_url = 'https://getbootstrap.com/docs/4.0/components/breadcrumb/'

    return dict(strapline_text=strapline_text, intro_text=intro_text, reference_urls=reference_urls, see_more_url=see_more_url)


def bootstrap_button(): 
    response.title = 'Bootstrap - Buttons'
    
    strapline_text = 'Bootstrap is a collection of bits of code written in HTML, CSS and JavaScript to quickly build websites'
    intro_text = 'Bootstrap is a free front-end framework constisting of a number of features for creating responsive and dynamic web sites.'
    reference_urls = [
            {'name':'GetBootstrap 4','url':'https://getbootstrap.com/docs/4.6/getting-started/introduction/'}, 
            {'name':'GetBootstrap - Components - Buttons','url':'https://getbootstrap.com/docs/4.0/components/buttons/'}
        ]
    see_more_url = 'https://getbootstrap.com/docs/4.0/components/buttons/'

    return dict(strapline_text=strapline_text, intro_text=intro_text, reference_urls=reference_urls, see_more_url=see_more_url)


def bootstrap_jumbotron(): 
    response.title = 'Bootstrap - Jumbotron'
     
    main_heading = 'Bootstrap - Jumbotron'
    strapline_text = 'Bootstrap is a collection of bits of code written in HTML, CSS and JavaScript to quickly build websites.'
    intro_text = 'Bootstrap is a free front-end framework constisting of a number of features for creating responsive and dynamic web sites.'
    reference_urls = [
            {'name':'GetBootstrap 4','url':'https://getbootstrap.com/docs/4.6/getting-started/introduction/'}, 
            {'name':'GetBootstrap - Components - Jumbotron','url':'https://getbootstrap.com/docs/4.0/components/jumbotron/'}
        ]
    see_more_url = 'https://getbootstrap.com/docs/4.0/components/jumbotron/'

    return dict(strapline_text=strapline_text, intro_text=intro_text, reference_urls=reference_urls, see_more_url=see_more_url)


def bootstrap_table(): 
    response.title = 'Bootstrap - Table'
    
    strapline_text = 'Bootstrap is a collection of bits of code written in HTML, CSS and JavaScript to quickly build websites.'
    intro_text = 'Bootstrap is a free front-end framework constisting of a number of features for creating responsive and dynamic web sites.'
    reference_urls = [
            {'name':'GetBootstrap 4','url':'https://getbootstrap.com/docs/4.6/getting-started/introduction/'},
            {'name':'GetBootstrap - Content - Table','url':'https://getbootstrap.com/docs/4.6/content/tables/'}
        ]
    see_more_url = 'https://getbootstrap.com/docs/4.6/content/tables/'
    
    return dict(strapline_text=strapline_text, intro_text=intro_text, reference_urls=reference_urls, see_more_url=see_more_url)


def bootstrap_modal(): 
    response.title = 'Bootstrap - Modal (interactive)'
    strapline_text = 'Bootstrap is a collection of bits of code written in HTML, CSS and JavaScript to quickly build websites.'
    intro_text = 'Bootstrap is a free front-end framework constisting of a number of features for creating responsive and dynamic web sites.'
    reference_urls = [
            {'name':'GetBootstrap 4','url':'https://getbootstrap.com/docs/4.6/getting-started/introduction/'}, 
            {'name':'GetBootstrap - Components - Modal','url':'https://getbootstrap.com/docs/4.6/components/modal/'}
        ]
    see_more_url = 'https://getbootstrap.com/docs/4.6/components/modal/'
  
    return dict(strapline_text=strapline_text, intro_text=intro_text, reference_urls=reference_urls, see_more_url=see_more_url)


def bootstrap_carousel(): 
    response.title = 'Bootstrap - Carousel (interactive)'
    
    strapline_text = 'Bootstrap is a collection of bits of code written in HTML, CSS and JavaScript to quickly build websites.'
    intro_text = 'Bootstrap is a free front-end framework constisting of a number of features for creating responsive and dynamic web sites.'
    reference_urls = [
            {'name':'GetBootstrap 4','url':'https://getbootstrap.com/docs/4.6/getting-started/introduction/'}, 
            {'name':'GetBootstrap - Components - Carousel','url':'https://getbootstrap.com/docs/4.6/components/modal/'}
        ]
    see_more_url = 'https://getbootstrap.com/docs/4.6/components/carousel/'
    
    return dict(strapline_text=strapline_text, intro_text=intro_text, reference_urls=reference_urls, see_more_url=see_more_url)


def bootstrap_nav(): 
    response.title = 'Bootstrap - Navigation Menu'

    strapline_text = 'Bootstrap is a collection of bits of code written in HTML, CSS and JavaScript to quickly build websites.'
    intro_text = 'Bootstrap is a free front-end framework constisting of a number of features for creating responsive and dynamic web sites.'
    reference_urls = [
            {'name':'GetBootstrap 4','url':'https://getbootstrap.com/docs/4.6/getting-started/introduction/'}, 
            {'name':'GetBootstrap - Components - Nav','url':'https://getbootstrap.com/docs/4.6/components/navs/'}
        ]
    see_more_url = 'https://getbootstrap.com/docs/4.6/components/navs/'
    
    return dict(strapline_text=strapline_text, intro_text=intro_text, reference_urls=reference_urls, see_more_url=see_more_url)


def bootstrap_pagination(): 
    response.title = 'Bootstrap - Paging'

    strapline_text = 'Bootstrap is a collection of bits of code written in HTML, CSS and JavaScript to quickly build websites.'
    intro_text = 'Bootstrap is a free front-end framework constisting of a number of features for creating responsive and dynamic web sites.'
    reference_urls = [
            {'name':'GetBootstrap 4','url':'https://getbootstrap.com/docs/4.6/getting-started/introduction/'}, 
            {'name':'GetBootstrap - Components - Pagination','url':'https://getbootstrap.com/docs/4.6/components/pagination/'}
        ]
    see_more_url = 'https://getbootstrap.com/docs/4.6/components/pagination/'
    
    return dict(strapline_text=strapline_text, intro_text=intro_text, reference_urls=reference_urls, see_more_url=see_more_url)


def bootstrap_form(): 
    response.title = 'Bootstrap - Form (interactive)'
 
    ''' Default Message '''
    response.message = 'Try this form'
 
    # if form is posted
    if request.post_vars:
        # calls function validatePassword(...) 
        # uses password1 and password2 fields from the request 
        # set the error_message in the response to return to the page
        response.error_message = validatePassword(request.post_vars.password1, request.post_vars.password2)

    strapline_text = 'Bootstrap is a collection of bits of code written in HTML, CSS and JavaScript to quickly build websites.'
    intro_text = 'Bootstrap is a free front-end framework constisting of a number of features for creating responsive and dynamic web sites.'
    reference_urls = [
            {'name':'GetBootstrap 4','url':'https://getbootstrap.com/docs/4.6/getting-started/introduction/'}, 
            {'name':'GetBootstrap - Components - Form','url':'https://getbootstrap.com/docs/4.6/components/forms/'}
        ]
    see_more_url = 'https://getbootstrap.com/docs/4.6/components/forms/'

    return dict(strapline_text=strapline_text, intro_text=intro_text, reference_urls=reference_urls, see_more_url=see_more_url)


def bootstrap_mediaobject(): 
    response.title = 'Bootstrap - Media object'

    strapline_text = 'Bootstrap is a collection of bits of code written in HTML, CSS and JavaScript to quickly build websites'
    intro_text = 'Bootstrap is a free front-end framework constisting of a number of features for creating responsive and dynamic web sites.'
    reference_urls = [
            {'name':'GetBootstrap 4','url':'https://getbootstrap.com/docs/4.6/getting-started/introduction/'}, 
            {'name':'GetBootstrap - Components - Media object','url':'https://getbootstrap.com/docs/4.6/components/media-object/'}
        ]
    see_more_url = 'https://getbootstrap.com/docs/4.6/components/media-object/'

    return dict(strapline_text=strapline_text, intro_text=intro_text, reference_urls=reference_urls, see_more_url=see_more_url)


def validatePassword(password1, password2):
    ''' Validate password on the server.
        1) checks the password is the  valid length 
        2) checks that both password1 and password2 match '''
        
    message = None
    
    if len(password1) < 8:
        message = "password is too weak"
    elif password1 != password2:
        message = "passwords do not match"

    return message
