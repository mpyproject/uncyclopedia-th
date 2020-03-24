#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This bot appends some text to all unused images and notifies uploaders.

Parameters:

-always         Don't be asked every time.
-nouserwarning  Do not warn uploader about orphaned file.
-limit          Specify number of pages to work on with "-limit:n" where
                n is the maximum number of articles to work on.
                If not used, all pages are used.
"""
#
# (C) Leonardo Gregianin, 2007
# (C) Filnik, 2008
# (c) xqt, 2011-2019
# (C) Pywikibot team, 2013-2019
#
# Distributed under the terms of the MIT license.
#
from __future__ import absolute_import, division, unicode_literals

import pywikibot
from pywikibot import i18n, pagegenerators
from pywikibot.bot import SingleSiteBot, AutomaticTWSummaryBot, ExistingPageBot
from pywikibot.exceptions import ArgumentDeprecationWarning
from pywikibot.tools import issue_deprecation_warning

#from pandas import Timestamp

template_to_the_image = {
    'meta': '{{Orphan file}}',
    'test': '{{Orphan file}}',
    'it': '{{immagine orfana}}',
    'fa': '{{تصاویر بدون استفاده}}',
    'ur': '{{غیر مستعمل تصاویر}}',
    'th': '{{ไฟล์ไม่ได้ใช้|date={{subst:#time:d F xkY}}|by=[[ผู้ใช้:PatzaBot|กระบวนการอัตโนมัติ]]|timestamp=%(timestamp)s}}',
}

# This template message should use subst:
template_to_the_user = {
    'fa': '\n\n{{جا:اخطار به کاربر برای تصاویر بدون استفاده|%(title)s}}--~~~~',
    'ur': '\n\n{{جا:اطلاع برائے غیر مستعمل تصاویر}}--~~~~',
    'th': '\n\n{{subst:ผู้ใช้:PatzaBot/ไฟล์ไม่ได้ใช้/ผู้ใช้|%(title)s|%(timestamp)s}} — ~~~~',
}


class UnusedFilesBot(SingleSiteBot, AutomaticTWSummaryBot, ExistingPageBot):

    """Unused files bot."""

    summary_key = 'unusedfiles-comment'

    def __init__(self, **kwargs):
        """Initializer."""
        self.availableOptions.update({
            'nouserwarning': False  # do not warn uploader
        })
        super(UnusedFilesBot, self).__init__(**kwargs)

        self.template_image = i18n.translate(self.site,
                                             template_to_the_image)
        self.template_user = i18n.translate(self.site,
                                            template_to_the_user)
        if not (self.template_image
                and (self.template_user or self.getOption('nouserwarning'))):
            raise i18n.TranslationError('This script is not localized for {0} '
                                        'site.'.format(self.site))

    def treat(self, image):
        """Process one image page."""
        # Use fileUrl() and fileIsShared() to confirm it is local media
        # rather than a local page with the same name as shared media.
        if (image.fileUrl() and not image.fileIsShared()
                and 'http://' not in image.text):
            if "{{ไฟล์ไม่ได้ใช้|" in image.text:
                pywikibot.output('{0} done already'
                                 .format(image.title(as_link=True)))
                return
            if "<!-- ไม่สนใจไฟล์ไม่ได้ใช้" in image.text:
                pywikibot.output('{0} ไม่สนใจการเตือน ข้าม'
                                 .format(image.title(as_link=True)))
                return
            if "<!-- IGNOREORPHAN" in image.text:
                pywikibot.output('{0} ไม่สนใจการติดป้าย ข้าม'
                                 .format(image.title(as_link=True)))
                return
            mpyA = image.get_file_history()
            mpyB = list(mpyA.values())
            print(mpyB)
            mpyC = mpyB.pop(0)
            mpyD = mpyC['timestamp']
            self.template_image = self.template_image % {'timestamp': mpyD}
            self.append_text(image, '\n\n' + self.template_image)
            if self.getOption('nouserwarning'):
                return
            if "<!-- USERIGNOREORPHAN" in image.text:
                pywikibot.output('{0} ผู้อัปโหลดไม่สนใจการติดป้าย ข้าม'
                                 .format(image.title(as_link=True)))
                return
            uploader = mpyC['user']
            user = pywikibot.User(image.site, uploader)
            usertalkpage = user.getUserTalkPage()
            msg2uploader = self.template_user % {'title': image.title(),'timestamp': mpyD}
            self.append_text(usertalkpage, msg2uploader)

    def append_text(self, page, apptext):
        """Append apptext to the page."""
        if page.isRedirectPage():
            page = page.getRedirectTarget()
        if page.exists():
            text = page.text
        else:
            if page.isTalkPage():
                text = ''
            else:
                raise pywikibot.NoPage(page)

        text += apptext
        self.current_page = page
        self.put_current(text)

def main(*args):
    """
    Process command line arguments and invoke bot.

    If args is an empty list, sys.argv is used.

    @param args: command line arguments
    @type args: str
    """
    options = {}
    total = None

    local_args = pywikibot.handle_args(args)

    for arg in local_args:
        arg, sep, value = arg.partition(':')
        if arg == '-limit':
            total = value
        elif arg == '-total':
            total = value
            issue_deprecation_warning('The usage of "{0}"'.format(arg),
                                      '-limit', 2, ArgumentDeprecationWarning,
                                      since='20190120')
        else:
            options[arg[1:]] = True

    site = pywikibot.Site()
    gen = pagegenerators.UnusedFilesGenerator(total=total, site=site)
    gen = pagegenerators.PreloadingGenerator(gen)

    bot = UnusedFilesBot(site=site, generator=gen, **options)
    try:
        bot.run()
    except pywikibot.Error as e:
        pywikibot.bot.suggest_help(exception=e)
        return False
    else:
        return True


if __name__ == '__main__':
    main()
