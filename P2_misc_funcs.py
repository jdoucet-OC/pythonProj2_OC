def relative_to_absolute(link, imglink):
    splittedlink = link.split('/')
    splittedimglink = imglink.split('/')
    retour = imglink.count('../')
    del splittedimglink[:retour]
    del splittedlink[-retour - 1:]
    sep = '/'
    return sep.join(splittedlink + splittedimglink)
