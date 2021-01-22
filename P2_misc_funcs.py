def relative_to_absolute(link, imglink):
    splittedlink = link.split('/')
    splittedimglink = imglink.split('/')
    retour = imglink.count('../')
    del splittedimglink[:retour]
    del splittedlink[-retour - 1:]
    sep = '/'
    return sep.join(splittedlink + splittedimglink)


def relative_to_absolute_list(liste, link):
    newlist = []
    for elem in liste:
        splittedlink = link.split('/')
        retour = elem.count('../')
        splitted = elem.split('/')
        del splitted[:retour]
        del splittedlink[-retour - 1:]
        sep = '/'
        newlist.append(sep.join(splittedlink + splitted))
    return newlist
