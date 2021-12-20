# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a controller for the tutorials
# -------------------------------------------------------------------------

# ---- tutorial index page ----
def index():
    main_heading = T('Placeholder content')
    strapline = T('During design and development, dummy content can give the product a look-and-feel.')
    content = T('Lorem ipsum text is commonly used in the layout in web design to draft content. Likewise, placeholder images provide visual content and indicators for the optimum size images that should be used for the actual content.')

    return {'main_heading':main_heading, 'strapline':strapline, 'content': content}
