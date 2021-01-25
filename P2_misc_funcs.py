#!/usr/bin/env python3

def relative_to_absolute(link, imglink):
    """
    :param link: Lien du site complet
    :param imglink: Lien de l'image incomplet
    :return: Le lien de l'image complète
    """

    splittedlink = link.split('/')
    splittedimglink = imglink.split('/')
    retour = imglink.count('../')
    del splittedimglink[:retour]
    del splittedlink[-retour - 1:]
    sep = '/'
    return sep.join(splittedlink + splittedimglink)


def relative_to_absolute_list(liste, link):
    """
    :param liste: Liste des liens incomplet des
     livre de la catégorie
    :param link: Lien du site
    :return: Liste des liens complet de la page n
        de la catégorie
    """

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
