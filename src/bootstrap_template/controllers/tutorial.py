# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a controller for the tutorials
# -------------------------------------------------------------------------

# ---- tutorial index page ----
def index():
    main_heading = 'Placeholder content'
    strapline = 'During design and development, dummy content can give the product a look-and-feel.'
    intro = 'Lorem ipsum text is commonly used in the layout in web design to draft content. Likewise, placeholder images provide visual content and indicators for the optimum size images that should be used for the actual content.'

    return dict(main_heading=main_heading, strapline_text=strapline, intro_text=intro)
