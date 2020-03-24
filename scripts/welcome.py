#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Script to welcome new users.

This script works out of the box for Wikis that
have been defined in the script. It is currently used on the Dutch, Norwegian,
Albanian, Italian Wikipedia, Wikimedia Commons and English Wikiquote.

Ensure you have community support before running this bot!

Everything that needs customisation to support additional projects is
indicated by comments.

Description of basic functionality

 * Request a list of new users every period (default: 3600 seconds)
   You can choose to break the script after the first check (see arguments)
 * Check if new user has passed a threshold for a number of edits
   (default: 1 edit)
 * Optional: check username for bad words in the username or if the username
   consists solely of numbers; log this somewhere on the wiki (default: False)
   Update: Added a whitelist (explanation below).
 * If user has made enough edits (it can be also 0), check if user has an empty
   talk page
 * If user has an empty talk page, add a welcome message.
 * Optional: Once the set number of users have been welcomed, add this to the
   configured log page, one for each day (default: True)
 * If no log page exists, create a header for the log page first.

This script (by default not yet implemented) uses two templates that need to
be on the local wiki

* {{WLE}}: contains mark up code for log entries (just copy it from Commons)
* {{welcome}}: contains the information for new users

This script understands the following command-line arguments:

   -edit[:#]       Define how many edits a new user needs to be welcomed
                   (default: 1, max: 50)

   -time[:#]       Define how many seconds the bot sleeps before restart
                   (default: 3600)

   -break          Use it if you don't want that the Bot restart at the end
                   (it will break) (default: False)

   -nlog           Use this parameter if you do not want the bot to log all
                   welcomed users (default: False)

   -limit[:#]      Use this parameter to define how may users should be
                   checked (default:50)

   -offset[:TIME]  Skip the latest new users (those newer than TIME)
                   to give interactive users a chance to welcome the
                   new users (default: now)
                   Timezone is the server timezone, GMT for Wikimedia
                   TIME format : yyyymmddhhmmss or yyyymmdd

   -timeoffset[:#] Skip the latest new users, accounts newer than
                   # minutes

   -numberlog[:#]  The number of users to welcome before refreshing the
                   welcome log (default: 4)

   -filter         Enable the username checks for bad names (default: False)

   -ask            Use this parameter if you want to confirm each possible
                   bad username (default: False)

   -random         Use a random signature, taking the signatures from a wiki
                   page (for instruction, see below).

   -file[:#]       Use a file instead of a wikipage to take the random sign.
                   If you use this parameter, you don't need to use -random.

   -sign           Use one signature from command line instead of the default

   -savedata       This feature saves the random signature index to allow to
                   continue to welcome with the last signature used.

   -sul            Welcome the auto-created users (default: False)

   -quiet          Prevents users without contributions are displayed

********************************* GUIDE ***********************************

*** Report, Bad and white list guide: ***

1)  Set in the code which page it will use to load the badword, the
    whitelist and the report
2)  In these page you have to add a "tuple" with the names that you want to
    add in the two list. For example: ('cat', 'mouse', 'dog')
    You can write also other text in the page, it will work without problem.
3)  What will do the two pages? Well, the Bot will check if a badword is in
    the username and set the "warning" as True. Then the Bot check if a word
    of the whitelist is in the username. If yes it remove the word and
    recheck in the bad word list to see if there are other badword in the
    username.
    Example

        * dio is a badword
        * Claudio is a normal name
        * The username is "Claudio90 fuck!"
        * The Bot finds dio and sets "warning"
        * The Bot finds Claudio and sets "ok"
        * The Bot finds fuck at the end and sets "warning"
        * Result: The username is reported.
4)  When a user is reported you have to check him and do

        * If he's ok, put the {{welcome}}
        * If he's not, block him
        * You can decide to put a "you are blocked, change another username"
          template or not.
        * Delete the username from the page.

        IMPORTANT : The Bot check the user in this order

            * Search if he has a talkpage (if yes, skip)
            * Search if he's blocked, if yes he will be skipped
            * Search if he's in the report page, if yes he will be skipped
            * If no, he will be reported.

*** Random signature guide: ***

Some welcomed users will answer to the one who has signed the welcome message.
When you welcome many new users, you might be overwhelmed with such answers.
Therefore you can define usernames of other users who are willing to receive
some of these messages from newbies.

1) Set the page that the bot will load
2) Add the signatures in this way:

    *<SPACE>SIGNATURE
    <NEW LINE>

Example of signatures:

 <pre>
 * [[User:Filnik|Filnik]]
 * [[User:Rock|Rock]]
 </pre>

NOTE: The white space and <pre></pre> aren't required but I suggest you to
      use them.

******************************** Badwords **********************************

The list of Badwords of the code is opened. If you think that a word is
international and it must be blocked in all the projects feel free to add it.
If also you think that a word isn't so international, feel free to delete it.

However, there is a dinamic-wikipage to load that badwords of your project or
you can add them directly in the source code that you are using without adding
or deleting.

Some words, like "Administrator" or "Dio" (God in italian) or "Jimbo" aren't
badwords at all but can be used for some bad-nickname.
"""
#
# (C) Alfio, 2005
# (C) Kyle/Orgullomoore, 2006-2007
# (C) Siebrand Mazeland, 2006-2009
# (C) Filnik, 2007-2011
# (C) Daniel Herding, 2007
# (C) Alex Shih-Han Lin, 2009-2010
# (C) xqt, 2009-2019
# (C) Pywikibot team, 2008-2019
#
# Distributed under the terms of the MIT license.
#
from __future__ import absolute_import, division, unicode_literals

import codecs
from datetime import timedelta
import locale
import re
from textwrap import fill
import time

from random import choice

import pywikibot

from pywikibot import config, i18n
from pywikibot.bot import SingleSiteBot
from pywikibot.exceptions import HiddenKeyError
from pywikibot.tools.formatter import color_format
from pywikibot.tools import PY2, UnicodeType

if PY2:
    import cPickle as pickle  # noqa: N813
else:
    import pickle

locale.setlocale(locale.LC_ALL, '')

# Script uses the method i18n.translate() to find the right
# page/user/summary/etc so the need to specify language and project have
# been eliminated.
# FIXME: Not all language/project combinations have been defined yet.
#        Add the following strings to customise for a language:
#        logbook, netext, report_page, bad_pag, report_text, random_sign,
#        whitelist_pg, final_new_text_additions, logpage_header

############################################################################

# The page where the bot will save the log (e.g. Wikipedia:Welcome log).
#
# ATTENTION: Projects not listed won't write a log to the wiki.
logbook = {
    'fr': ('Wikipedia:Prise de décision/'
           'Accueil automatique des nouveaux par un robot/log'),
    'ga': 'Project:Log fáilte',
    'ja': '利用者:Alexbot/Welcomebotログ',
    'nl': 'Project:Logboek welkom',
    'no': 'Project:Velkomstlogg',
    'sq': 'Project:Tung log',
    'th': 'ผู้ใช้:PatzaBot/ต้อนรับ/บันทึก',
    'ur': 'Project:نوشتہ خوش آمدید',
    'zh': 'User:Welcomebot/欢迎日志',
    'commons': 'Project:Welcome log',
}
# The text for the welcome message (e.g. {{welcome}}) and %s at the end
# that is your signature (the bot has a random parameter to add different
# sign, so in this way it will change according to your parameters).
netext = {
    'commons': '{{subst:welcome}} %s',
    'wikipedia': {
        'am': '{{subst:Welcome}} %s',
        'ar': '{{subst:ترحيب}} %s',
        'arz': '{{subst:ترحيب}} %s',
        'as': '{{subst:আদৰণি}} %s',
        'ba': '{{Hello}} %s',
        'bn': '{{subst:স্বাগতম/বট}} %s',
        'bs': '{{Dobrodošlica}} %s',
        'da': '{{velkommen|%s}}',
        'en': '{{subst:welcome}} %s',
        'fa': '{{جا:خوشامد}} %s',
        'fr': '{{subst:Discussion Projet:Aide/Bienvenue}} %s',
        'ga': '{{subst:fáilte}} %s',
        'gor': '{{subst:Welcome}} %s',
        'he': '{{ס:ברוך הבא}} %s',
        'hr': '{{subst:dd}} %s',
        'id': '{{subst:sdbot2}}\n%s',
        'it': '<!-- inizio template di benvenuto -->\n{{subst:Benvebot}}\n%s',
        'ja': '{{subst:Welcome/intro}}\n{{subst:welcome|%s}}',
        'ka': '{{ახალი მომხმარებელი}}--%s',
        'kn': '{{subst:ಸುಸ್ವಾಗತ}} %s',
        'ml': '{{ബദൽ:സ്വാഗതം/bot}} %s',
        'my': '{{subst:welcome}} %s',
        'nap': '{{Bemmenuto}}%s',
        'nl': '{{hola|bot|%s}}',
        'no': '{{subst:bruker:jhs/vk}} %s',
        'pdc': '{{subst:Wilkum}}%s',
        'pt': '{{subst:bem vindo}} %s',
        'roa-tara': '{{Bovègne}} %s',
        'ru': '{{Hello}} %s',
        'sd': '{{subst:ڀليڪار}} %s',
        'shn': '{{subst:ႁပ်ႉတွၼ်ႈၽူႈၸႂ်ႉတိုဝ်း}} %s',
        'sq': '{{subst:tung}} %s',
        'sr': '{{Добродошлица}} %s',
        'ur': '{{نقل:خوش آمدید}}%s',
        'vec': '{{subst:Benvegnù|%s}}',
        'vo': '{{benokömö}} %s',
        'zh': '{{subst:welcome|sign=%s}}',
        'zh-yue': '{{歡迎}}--%s',
    },
    'wikibooks': {
        'ar': '{{subst:ترحيب}} %s',
        'bs': '{{Dobrodošlica}} %s',
        'es': '{{subst:bienivenido usuario}} %s',
    },
    'wikinews': {
        'ar': '{{subst:ترحيب}} %s',
        'bs': '{{Dobrodošlica}} %s',
        'fa': '{{خوشامد۲|%s}}',
        'it': '{{subst:benvenuto}}',
        'zh': '{{subst:welcome}} %s',
    },
    'wikisource': {
        'ar': '{{subst:ترحيب}} %s',
        'bn': '{{subst:স্বাগতম}} %s',
        'bs': '{{Dobrodošlica}} %s',
        'kn': '{{subst:ಸುಸ್ವಾಗತ}} %s',
        'mr': '{{subst:Welcome}} %s',
    },
    'wiktionary': {
        'ar': '{{subst:ترحيب}} %s',
        'bn': '{{subst:স্বাগতম|%s}}',
        'bs': '{{Dobrodošlica}} %s',
        'fa': '{{جا:خوشامد|%s}}',
        'kn': '{{subst:ಸುಸ್ವಾಗತ}} %s',
        'it': '{{subst:Utente:Filnik/Benve|firma=%s}}',
        'ur': '{{جا:خوش آمدید}}%s',
    },
    'wikiversity': {
        'ar': '{{subst:ترحيب}} %s',
        'de': '{{subst:Willkommen|%s}}',
        'el': '{{subst:καλωσόρισμα}} %s',
        'en': '{{subst:Welcome}}\n\n{{subst:Talktome}} %s',
        'es': '{{subst:bienvenido usuario}} %s',
        'fr': '{{Bienvenue}} %s',
        'it': '{{subst:Benvenuto}} %s',
    },
    'wikivoyage': {
        'bn': '{{subst:স্বাগতম}} %s',
    },
       'thuncyc': {
        'th': '{{subst:ยินดีต้อนรับ}} <br/>— %s',
    },
       'localwiki': {
        'th': '== ยินดีต้อนรับ คุณ{{subst:ROOTPAGENAME}}==\nยินดีต้อนรับครับ — Patsagorn(<span style="color:green;">superuser</span>)  {\[[user_talk:Patsagorn|คุย]] \}',
    },
}
# The page where the bot will report users with a possibly bad username.
report_page = {
    'commons': ("Project:Administrators'noticeboard/User problems/Usernames"
                'to be checked'),
    'wikipedia': {
        'am': 'User:Beria/Report',
        'ar': 'Project:إخطار الإداريين/أسماء مستخدمين للفحص',
        'da': 'Bruger:Broadbot/Report',
        'en': 'Project:Administrator intervention against vandalism',
        'fa': 'Project:تابلوی اعلانات مدیران/گزارش ربات',
        'ga': 'Project:Log fáilte/Drochainmneacha',
        'it': 'Project:Benvenuto_Bot/Report',
        'ja': '利用者:Alexbot/report',
        'nl': ('Project:Verzoekpagina voor moderatoren'
               '/RegBlok/Te controleren gebruikersnamen'),
        'no': 'Bruker:JhsBot II/Rapport',
        'pdc': 'Benutzer:Xqt/Report',
        'ru': 'Участник:LatitudeBot/Рапорт',
        'sq': 'User:EagleBot/Report',
        'sr': 'User:ZoranBot/Записи',
        'ur': 'Project:تختہ اعلانات برائے منتظمین/صارف نام برائے پڑتال',
        'zh': 'User:Welcomebot/report',
        'zh-yue': 'User:Alexbot/report',
    },
      'thuncyc': {
        'th': 'ผู้ใช้:PatzaBot/ต้อนรับ/รายงาน',
    },
      'localwiki': {
        'th': 'ผู้ใช้:Bot/แจ้ง',
    },
}
# The page where the bot reads the real-time bad words page
# (this parameter is optional).
bad_pag = {
    'commons': 'Project:Welcome log/Bad_names',
    'wikipedia': {
        'am': 'User:Beria/Bad_names',
        'ar': 'Project:سجل الترحيب/أسماء سيئة',
        'en': 'Project:Welcome log/Bad_names',
        'fa': 'Project:سیاهه خوشامد/نام بد',
        'it': 'Project:Benvenuto_Bot/Lista_Badwords',
        'ja': 'Project:不適切な名前の利用者',
        'nl': 'Project:Logboek_welkom/Bad_names',
        'no': 'Bruker:JhsBot/Daarlige ord',
        'ru': 'Участник:LatitudeBot/Чёрный список',
        'sq': 'User:Eagleal/Bad_names',
        'sr': 'User:ZoranBot/лоша корисничка имена',
        'zh': 'User:Welcomebot/badname',
        'zh-yue': 'User:Welcomebot/badname',
    },
    'thuncyc': {
        'th': 'ผู้ใช้:PatzaBot/ต้อนรับ/ชื่อห้ามสร้าง',
    },
    'localwiki': {
        'th': 'ผู้ใช้:Bot/Badname',
    },
}

timeselected = ' ~~~~~'  # Defining the time used after the signature

# The text for reporting a possibly bad username
# e.g. *[[Talk_page:Username|Username]]).
report_text = {
    'commons': '\n*{{user3|%s}}' + timeselected,
    'wikipedia': {
        'am': '\n*[[User talk:%s]]' + timeselected,
        'ar': '\n*{{user13|%s}}' + timeselected,
        'bs': '\n{{Korisnik|%s}}' + timeselected,
        'da': '\n*[[Bruger Diskussion:%s]] ' + timeselected,
        'de': '\n*[[Benutzer Diskussion:%s]] ' + timeselected,
        'en': '\n*{{Userlinks|%s}} ' + timeselected,
        'fa': '\n*{{کاربر|%s}}' + timeselected,
        'fr': '\n*{{u|%s}} ' + timeselected,
        'ga': '\n*[[Plé úsáideora:%s]] ' + timeselected,
        'it': '\n{{Reported|%s|',
        'ja': '\n*{{User2|%s}}' + timeselected,
        'nl': '\n*{{linkgebruiker%s}} ' + timeselected,
        'no': '\n*{{bruker|%s}} ' + timeselected,
        'pdc': '\n*[[Benutzer Diskussion:%s]] ' + timeselected,
        'sq': '\n*[[User:%s]] ' + timeselected,
        'sr': '\n*{{Корисник|%s}}' + timeselected,
        'zh': '\n*{{User|%s}}' + timeselected
    },
    'thuncyc': {
        'th': '\n# {{admincheck|%s}}' + timeselected,
    },
    'localwiki': {
        'th': '\n# [[user:%s]] ' + timeselected,
    },
}
# Set where you load your list of signatures that the bot will load if you use
# the random argument (this parameter is optional).
random_sign = {
    'am': 'User:Beria/Signatures',
    'ar': 'Project:سجل الترحيب/توقيعات',
    'ba': 'Ҡатнашыусы:Salamat bot/Ярҙам',
    'da': 'Wikipedia:Velkommen/Signaturer',
    'en': 'Project:Welcome log/Sign',
    'fa': 'Project:سیاهه خوشامد/امضاها',
    'fr': 'Projet:Service de Parrainage Actif/Signatures',
    'it': 'Project:Benvenuto_Bot/Firme',
    # jawiki: Don't localize. Community discussion oppose to this feature
    # [[ja:Wikipedia:Bot作業依頼/ウェルカムメッセージ貼り付け依頼]]
    'nap': 'User:Cellistbot/Firme',
    'roa-tara': 'Wikipedia:Bovègne Bot/Firme',
    'ru': 'Участник:LatitudeBot/Sign',
    'ur': 'Project:خوش آمدید/دستخطیں',
    'vec': 'Utente:FriBot/Firme',
    'zh': 'User:Welcomebot/欢迎日志/用户',
    'th': 'ผู้ใช้:PatzaBot/ต้อนรับ/สุ่มชื่อต้อนรับ',
}
# The page where the bot reads the real-time whitelist page.
# (this parameter is optional).
whitelist_pg = {
    'ar': 'Project:سجل الترحيب/قائمة بيضاء',
    'en': 'User:Filnik/whitelist',
    'ga': 'Project:Log fáilte/Bánliosta',
    'it': 'Project:Benvenuto_Bot/Lista_Whitewords',
    'ru': 'Участник:LatitudeBot/Белый_список',
    'th': 'ผู้ใช้:Bot/whitelist',
}

# Text after the {{welcome}} template, if you want to add something
# Default (en): nothing.
final_new_text_additions = {
    'it': '\n<!-- fine template di benvenuto -->',
    'zh': '<small>(via ~~~)</small>',
    'th': '\n<!-- ข้อความอัตโนมัตินี้โพสต์โดย PatzaBot -->',
}

#
#
logpage_header = {
    '_default': '{|border="2" cellpadding="4" cellspacing="0" style="margin: '
                '0.5em 0.5em 0.5em 1em; padding: 0.5em; '
                'border: 1px solid black;'
                'font-size: 95%;"',
    'no': '[[Kategori:Velkomstlogg|{{PAGENAME}}]]\n{| class="wikitable"',
    'it': '[[Categoria:Benvenuto log|{{subst:PAGENAME}}]]\n{|border="2" '
          'cellpadding="4" cellspacing="0" style="margin: 0.5em 0.5em 0.5em '
          '1em; padding: 0.5em; background: #bfcda5; border: 1px #b6fd2c '
          'solid; border-collapse: collapse; font-size: 95%;"'
}

# Ok, that's all. What is below, is the rest of code, now the code is fixed
# and it will run correctly in your project ;)
############################################################################

_COLORS = {
    0: 'lightpurple',
    1: 'lightaqua',
    2: 'lightgreen',
    3: 'lightyellow',
    4: 'lightred',
    5: 'lightblue'
}
_MSGS = {
    0: 'ข้อความ',
    1: 'ไม่ทำอะไร',
    2: 'ตรง',
    3: 'ข้ามไป',
    4: 'เตือน',
    5: 'สำเร็จ',
}


class FilenameNotSet(pywikibot.Error):

    """An exception indicating that a signature filename was not specified."""


class Global(object):

    """Container class for global settings."""

    attachEditCount = 0     # จำนวนการแก้ไขน้อยที่สุดเพื่อต้อนรับ (ต่ำกว่า # ครั้งจะไม่ต้อนรับ)
    dumpToLog = 15          # จำนวนผู้ใช้ที่จำเป็นต้องใส่ในบันทึก (บันทึกที่หน้า [[ผู้ใช้:PatzaBot/ต้อนรับ/บันทึก]] )
    offset = None           # ข้ามผู้ใช้นี้เมื่อสร้างหลังจาก yyyymmddhhmmsss
    timeoffset = 0          # ข้ามผู้ใช้ที่มีอายุใหม่กว่า # นาที
    recursive = True        # ให้บอตตรวจสอบว่าบอตส่งข้อความซ้ำหรือไม่
    timeRecur = 300         # ให้บอตอัพเดตทุก ๆ # วินาที (1800 = 30 นาที)
    makeWelcomeLog = True   # บันทึกการยินดีต้อนรับหรือไม่? (บันทึกที่หน้า [[ผู้ใช้:PatzaBot/ต้อนรับ/บันทึก]] )
    confirm = True          # ถามผู้ควบคุมบอตว่าชื่อที่พบเป็นชื่อต้องห้ามหรือไม่
    welcomeAuto = False     # ต้อนรับบัญชีผู้ใช้ที่เป็นการสร้างแบบอัตโนมัติหรือไม่ (Auto-create acc)
    filtBadName = True      # ตรวจว่าชื่อผู้ใช้รับได้หรือไม่ (รายการจะอยู่ที่ [[ผู้ใช้:PatzaBot/ต้อนรับ/ชื่อห้ามสร้าง]])
                            # ถ้าชื่อนั้นตรง จะแจ้งที่[[ผู้ใช้:PatzaBot/ต้อนรับ/รายงาน]]
    randomSign = False      # สุ่มลายเซ็นท้ายข้อความต้อนรับหรือไม่ (สุ่มจาก [[ผู้ใช้:PatzaBot/ต้อนรับ/สุ่มชื่อต้อนรับ]] )
    saveSignIndex = False   # ควรบันทึกว่าลงชื่อผู้ใดหลังสุ่มแล้วหรือไม่
    signFileName = None     # ไฟล์ของรายชื่อ (ผู้ดูแลต้องตั้งค่า โดยปกติเป็น none)
    defaultSign = '[[user:PatzaBot|𝐩𝐚𝐭𝐳𝐚𝐛𝐨𝐭]] [[user:Patzagorn Y?|■]]'    # ลายเซ็นปกติ
    queryLimit = 50         # จำนวนผู้ใช้ที่บอตจะตรวจสอบในหนึ่งครั้งการทำงาน
    quiet = False           # ผู้ใช้ที่ไม่มีในบันทึกการมีส่วนร่วมควรนำออกจากรายการหรือไม่ 


class WelcomeBot(SingleSiteBot):

    """Bot to add welcome messages on User pages."""

    def __init__(self, **kwargs):
        """Initializer."""
        super(WelcomeBot, self).__init__(**kwargs)
        self.check_managed_sites()
        self.bname = {}

        self.welcomed_users = []
        self.log_name = i18n.translate(self.site, logbook)

        if not self.log_name:
            globalvar.makeWelcomeLog = False
        if globalvar.randomSign:
            self.defineSign(True)

    def check_managed_sites(self):
        """Check that site is managed by welcome.py."""
        # Raises KeyError if site is not in netext dict.
        site_netext = i18n.translate(self.site, netext)
        if site_netext is None:
            raise KeyError(
                'welcome.py is not localized for site {0} in netext dict.'
                .format(self.site))
        self.welcome_text = site_netext

    def badNameFilter(self, name, force=False):
        """Check for bad names."""
        if not globalvar.filtBadName:
            return False

        # initialize blacklist
        if not hasattr(self, '_blacklist') or force:
            elenco = [
                ' ano', ' anus', 'anal ', 'babies', 'baldracca', 'balle',
                'bastardo', 'bestiali', 'bestiale', 'bastarda', 'b.i.t.c.h.',
                'bitch', 'boobie', 'bordello', 'breast', 'cacata', 'cacca',
                'cachapera', 'cagata', 'cane', 'cazz', 'cazzo', 'cazzata',
                'chiavare', 'chiavata', 'chick', 'christ ', 'cristo',
                'clitoride', 'coione', 'cojdioonear', 'cojones', 'cojo',
                'coglione', 'coglioni', 'cornuto', 'cula', 'culatone',
                'culattone', 'culo', 'deficiente', 'deficente', 'dio', 'die ',
                'died ', 'ditalino', 'ejackulate', 'enculer', 'eroticunt',
                'fanculo', 'fellatio', 'fica ', 'ficken', 'figa', 'sfiga',
                'fottere', 'fotter', 'fottuto', 'fuck', 'f.u.c.k.', 'funkyass',
                'gay', 'hentai.com', 'horne', 'horney', 'virgin', 'hotties',
                'idiot', '@alice.it', 'incest', 'jesus', 'gesu', 'gesù',
                'kazzo', 'kill', 'leccaculo', 'lesbian', 'lesbica', 'lesbo',
                'masturbazione', 'masturbare', 'masturbo', 'merda', 'merdata',
                'merdoso', 'mignotta', 'minchia', 'minkia', 'minchione',
                'mona', 'nudo', 'nuda', 'nudi', 'oral', 'sex', 'orgasmso',
                'porc', 'pompa', 'pompino', 'porno', 'puttana', 'puzza',
                'puzzone', 'racchia', 'sborone', 'sborrone', 'sborata',
                'sborolata', 'sboro', 'scopata', 'scopare', 'scroto',
                'scrotum', 'sega', 'sesso', 'shit', 'shiz', 's.h.i.t.',
                'sadomaso', 'sodomist', 'stronzata', 'stronzo', 'succhiamelo',
                'succhiacazzi', 'testicol', 'troia', 'universetoday.net',
                'vaffanculo', 'vagina', 'vibrator', 'vacca', 'yiddiot',
                'zoccola',
            ]
            elenco_others = [
                '@', '.com', '.sex', '.org', '.uk', '.en', '.it', 'admin',
                'administrator', 'amministratore', '@yahoo.com', '@alice.com',
                'amministratrice', 'burocrate', 'checkuser', 'developer',
                'http://', 'jimbo', 'mediawiki', 'on wheals', 'on wheal',
                'on wheel', 'planante', 'razinger', 'sysop', 'troll', 'vandal',
                ' v.f. ', 'v. fighter', 'vandal f.', 'vandal fighter',
                'wales jimmy', 'wheels', 'wales', 'www.',
            ]

            # blacklist from wikipage
            badword_page = pywikibot.Page(self.site,
                                          i18n.translate(self.site,
                                                         bad_pag))
            list_loaded = []
            if badword_page.exists():
                pywikibot.output('\nLoading the bad words list from {}...'
                                 .format(self.site))
                list_loaded = load_word_function(badword_page.get())
            else:
                showStatus(4)
                pywikibot.output("The bad word page doesn't exist!")
            self._blacklist = elenco + elenco_others + list_loaded
            del elenco, elenco_others, list_loaded

        if not hasattr(self, '_whitelist') or force:
            # initialize whitelist
            whitelist_default = ['emiliano']
            wtlpg = i18n.translate(self.site, whitelist_pg)
            list_white = []
            if wtlpg:
                whitelist_page = pywikibot.Page(self.site, wtlpg)
                if whitelist_page.exists():
                    pywikibot.output('\nLoading the whitelist from {}...'
                                     .format(self.site))
                    list_white = load_word_function(whitelist_page.get())
                else:
                    showStatus(4)
                    pywikibot.output("The whitelist's page doesn't exist!")
            else:
                showStatus(4)
                pywikibot.warning("The whitelist hasn't been set!")

            # Join the whitelist words.
            self._whitelist = list_white + whitelist_default
            del list_white, whitelist_default

        try:
            for wname in self._whitelist:
                if wname.lower() in str(name).lower():
                    name = name.lower().replace(wname.lower(), '')
                    for bname in self._blacklist:
                        self.bname[name] = bname
                        return bname.lower() in name.lower()
        except UnicodeEncodeError:
            pass
        try:
            for bname in self._blacklist:
                if bname.lower() in str(name).lower():  # bad name positive
                    self.bname[name] = bname
                    return True
        except UnicodeEncodeError:
            pass
        return False

    def reportBadAccount(self, name=None, final=False):
        """Report bad account."""
        # Queue process
        if name:
            if globalvar.confirm:
                answer = pywikibot.input_choice(
                    '{} may have an unwanted username, do you want to report '
                    'this user?'
                    .format(name), [('Yes', 'y'), ('No', 'n'), ('All', 'a')],
                    'n', automatic_quit=False)
                if answer in ['a', 'all']:
                    answer = 'y'
                    globalvar.confirm = False
            else:
                answer = 'y'

            if answer.lower() in ['yes', 'y'] or not globalvar.confirm:
                showStatus()
                pywikibot.output(
                    '{} is possibly an unwanted username. It will be reported.'
                    .format(name))
                if hasattr(self, '_BAQueue'):
                    self._BAQueue.append(name)
                else:
                    self._BAQueue = [name]

        if len(self._BAQueue) >= globalvar.dumpToLog or final:
            rep_text = ''
            # name in queue is max, put detail to report page
            pywikibot.output('อัพเดตบอตเพื่อเข้ากับรายการชื่อห้ามสร้าง')
            rep_page = pywikibot.Page(self.site,
                                      i18n.translate(self.site,
                                                     report_page))
            if rep_page.exists():
                text_get = rep_page.get()
            else:
                text_get = ('หน้านี้มีไว้สำหรับการแจ้งเมื่อพบชิ่อผู้ใช้ไม่เหมาะสม, '
                            'สร้างและแก้ไขอัตโนมัติโดยบอต ~~~ สร้างเมื่อ {{subst:#time:d F ปีxkY, เวลา H:i น.}}\n!== รายการ ==')
            pos = 0
            # The talk page includes "_" between the two names, in this way
            # replace them to " ".
            for usrna in self._BAQueue:
                username = pywikibot.url2link(usrna, self.site, self.site)
                n = re.compile(re.escape(username), re.UNICODE)
                y = n.search(text_get, pos)
                if y:
                    pywikibot.output('{} is already in the report page.'
                                     .format(username))
                else:
                    # Adding the log.
                    rep_text += i18n.translate(self.site,
                                               report_text) % username
                    if self.site.code == 'it':
                        rep_text = '%s%s}}' % (rep_text, self.bname[username])

            com = i18n.twtranslate(self.site, 'welcome-bad_username')
            if rep_text != '':
                rep_page.put(text_get + rep_text, summary=com, force=True,
                             minor=True)
                showStatus(5)
                pywikibot.output('Reported')
            self.BAQueue = []
        else:
            return True

    def makelogpage(self, queue=None):
        """Make log page."""
        if not globalvar.makeWelcomeLog or not queue:
            return False

        if self.site.code == 'it':
            pattern = '%d/%m/%Y'
        else:
            pattern = '%Y/%m' #เฉพาะปีและเดือนพอ
        target = self.log_name + '/' + time.strftime(
            pattern, time.localtime(time.time()))

        log_page = pywikibot.Page(self.site, target)
        if log_page.exists():
            text = log_page.get()
        else:
            # make new log page
            showStatus()
            pywikibot.output(
                'Log page is not exist, getting information for page creation')
            text = i18n.translate(self.site, logpage_header,
                                  fallback=i18n.DEFAULT_FALLBACK)
            text += '\n!' + self.site.namespace(2)
            text += '\n!' + str.capitalize(
                self.site.mediawiki_message('contribslink'))

        # Adding the log... (don't take care of the variable's name...).
        text += '\n'
        text += '\n'.join(
            '{{WLE|user=%s|contribs=%d}}' % (
                user.title(as_url=True, with_ns=False), user.editCount())
            for user in queue)

        # update log page.
        while True:
            try:
                log_page.put(text, i18n.twtranslate(self.site,
                                                    'welcome-updating'))
            except pywikibot.EditConflict:
                pywikibot.output('An edit conflict has occurred. Pausing for '
                                 '10 seconds before continuing.')
                time.sleep(10)
            else:
                break
        return True

    @property
    def generator(self):
        """Retrieve new users."""
        if globalvar.timeoffset != 0:
            start = self.site.server_time() - timedelta(
                minutes=globalvar.timeoffset)
        else:
            start = globalvar.offset
        for ue in self.site.logevents('newusers', total=globalvar.queryLimit,
                                      start=start):
            if ue.action() == 'create' or (
                    ue.action() == 'autocreate' and globalvar.welcomeAuto):
                try:
                    user = ue.page()
                except HiddenKeyError:
                    pywikibot.exception()
                else:
                    yield user

    def defineSign(self, force=False):
        """Setup signature."""
        if hasattr(self, '_randomSignature') and not force:
            return self._randomSignature

        sign_text = ''
        creg = re.compile(r'^\* ?(.*?)$', re.M)
        if not globalvar.signFileName:
            sign_page_name = i18n.translate(self.site, random_sign)
            if not sign_page_name:
                showStatus(4)
                pywikibot.output(
                    "{} doesn't allow random signature, force disable."
                    .format(self.site))
                globalvar.randomSign = False
                return

            sign_page = pywikibot.Page(self.site, sign_page_name)
            if sign_page.exists():
                pywikibot.output('Loading signature list...')
                sign_text = sign_page.get()
            else:
                pywikibot.output('The signature list page does not exist, '
                                 'random signature will be disabled.')
                globalvar.randomSign = False
        else:
            try:
                f = codecs.open(
                    pywikibot.config.datafilepath(globalvar.signFileName), 'r',
                    encoding=config.console_encoding)
            except LookupError:
                f = codecs.open(pywikibot.config.datafilepath(
                    globalvar.signFileName), 'r', encoding='utf-8')
            except IOError:
                pywikibot.error('No fileName!')
                raise FilenameNotSet('No signature filename specified.')

            sign_text = f.read()
            f.close()
        self._randomSignature = creg.findall(sign_text)
        return self._randomSignature

    def skip_page(self, users):
        """Check whether the user is to be skipped."""
        if users.isBlocked():
            showStatus(3)
            pywikibot.output('{} has been blocked!'.format(users.username))

        elif 'bot' in users.groups():
            showStatus(3)
            pywikibot.output('{} is a bot!'.format(users.username))

        elif 'bot' in users.username.lower():
            showStatus(3)
            pywikibot.output('{} might be a global bot!'
                             .format(users.username))

        elif users.editCount() < globalvar.attachEditCount:
            if not users.editCount() == 0:
                showStatus(1)
                pywikibot.output('{0} has only {1} contributions.'
                                 .format(users.username, users.editCount()))
            elif not globalvar.quiet:
                showStatus(1)
                pywikibot.output('{} has no contributions.'
                                 .format(users.username))
        else:
            return super(WelcomeBot, self).skip_page(users)

        return True

    def run(self):
        """Run the bot."""
        while True:
            welcomed_count = 0
            for users in self.generator:
                if self.skip_page(users):
                    continue

                showStatus(2)
                pywikibot.output('{} has enough edits to be welcomed.'
                                 .format(users.username))
                ustp = users.getUserTalkPage()
                if ustp.exists():
                    showStatus(3)
                    pywikibot.output('{} has been already welcomed.'
                                     .format(users.username))
                    continue

                if self.badNameFilter(users.username):
                    self.reportBadAccount(users.username)
                    continue

                welcome_text = self.welcome_text
                if globalvar.randomSign:
                    if self.site.family.name != 'wikinews':
                        welcome_text = welcome_text % choice(self.defineSign())
                    if (self.site.family.name != 'wiktionary'
                            or self.site.code != 'it'):
                        welcome_text += timeselected
                elif self.site.sitename != 'wikinews:it':
                    welcome_text = welcome_text % globalvar.defaultSign

                final_text = i18n.translate(self.site,
                                            final_new_text_additions)
                if final_text:
                    welcome_text += final_text
                welcome_comment = i18n.twtranslate(self.site,
                                                   'welcome-welcome')
                try:
                    # append welcomed, welcome_count++
                    ustp.put(welcome_text, welcome_comment, minor=False)
                except pywikibot.EditConflict:
                    showStatus(4)
                    pywikibot.output(
                        'An edit conflict has occurred, skipping this user.')
                else:
                    self.welcomed_users.append(users)

                welcomed_count = len(self.welcomed_users)
                if globalvar.makeWelcomeLog:
                    showStatus(5)
                    if welcomed_count == 0:
                        count = 'No users have'
                    elif welcomed_count == 1:
                        count = 'One user has'
                    else:
                        count = '{} users have'.format(welcomed_count)
                    pywikibot.output(count + ' been welcomed.')

                    if welcomed_count >= globalvar.dumpToLog:
                        if self.makelogpage(self.welcomed_users):
                            self.welcomed_users = []
                            welcomed_count = 0

            if globalvar.makeWelcomeLog and welcomed_count > 0:
                showStatus()
                if welcomed_count == 1:
                    pywikibot.output('Putting the log of the latest user...')
                else:
                    pywikibot.output(
                        'Putting the log of the latest {} users...'
                        .format(welcomed_count))
                if not self.makelogpage(self.welcomed_users):
                    continue
                self.welcomed_users = []
            if hasattr(self, '_BAQueue'):
                showStatus()
                pywikibot.output('Putting bad name to report page...')
                self.reportBadAccount(None, final=True)
            try:
                if globalvar.recursive:
                    showStatus()
                    if locale.getlocale()[1]:
                        strfstr = time.strftime(
                            '%d %b %Y %H:%M:%S (UTC)', time.gmtime())
                        # py2-py3 compatibility
                        if not isinstance(strfstr, UnicodeType):
                            strfstr = strfstr.decode(locale.getlocale()[1])
                    else:
                        strfstr = time.strftime(
                            '%d %b %Y %H:%M:%S (UTC)', time.gmtime())
                    pywikibot.output('Sleeping {0} seconds before rerun. {1}'
                                     .format(globalvar.timeRecur, strfstr))
                    pywikibot.sleep(globalvar.timeRecur)
                else:
                    raise KeyboardInterrupt
            except KeyboardInterrupt:
                break


def showStatus(n=0):
    """Output colorized status."""
    pywikibot.output(color_format('{color}[{0:5}]{default} ',
                                  _MSGS[n], color=_COLORS[n]), newline=False)


def load_word_function(raw):
    """Load the badword list and the whitelist."""
    page = re.compile(r'(?:\"|\')(.*?)(?:\"|\')(?:, |\))', re.UNICODE)
    list_loaded = page.findall(raw)
    if len(list_loaded) == 0:
        pywikibot.output('There was no input on the real-time page.')
    return list_loaded


globalvar = Global()


def _handle_offset(val):
    """Handle -offset arg."""
    if not val:
        val = pywikibot.input(
            'Which time offset for new users would you like to use? '
            '(yyyymmddhhmmss or yyyymmdd)')
    try:
        globalvar.offset = pywikibot.Timestamp.fromtimestampformat(val)
    except ValueError:
        # upon request, we could check for software version here
        raise ValueError(fill(
            'Mediawiki has changed, -offset:# is not supported anymore, but '
            '-offset:TIMESTAMP is, assuming TIMESTAMP is yyyymmddhhmmss or '
            'yyyymmdd. -timeoffset is now also supported. Please read this '
            'script source header for documentation.'))


def handle_args(args):
    """Process command line arguments.

    If args is an empty list, sys.argv is used.

    @param args: command line arguments
    @type args: str
    """
    mapping = {
        # option: (attribute, value),
        '-break': ('recursive', False),
        '-nlog': ('makeWelcomeLog', False),
        '-ask': ('confirm', True),
        '-filter': ('filtBadName', True),
        '-savedata': ('saveSignIndex', True),
        '-random': ('randomSign', True),
        '-sul': ('welcomeAuto', True),
        '-quiet': ('quiet', True),
    }

    for arg in pywikibot.handle_args(args):
        arg, _, val = arg.partition(':')
        if arg == '-edit':
            globalvar.attachEditCount = int(
                val if val.isdigit() else pywikibot.input(
                    'After how many edits would you like to welcome new users?'
                    ' (0 is allowed)'))
        elif arg == '-timeoffset':
            globalvar.timeoffset = int(
                val if val.isdigit() else pywikibot.input(
                    'Which time offset (in minutes) for new users would you '
                    'like to use?'))
        elif arg == '-time':
            globalvar.timeRecur = int(
                val if val.isdigit() else pywikibot.input(
                    'For how many seconds would you like to bot to sleep '
                    'before checking again?'))
        elif arg == '-offset':
            _handle_offset(val)
        elif arg == '-file':
            globalvar.randomSign = True
            globalvar.signFileName = val or pywikibot.input(
                'Where have you saved your signatures?')
        elif arg == '-sign':
            globalvar.defaultSign = val or pywikibot.input(
                'Which signature to use?')
            globalvar.defaultSign += timeselected
        elif arg == '-limit':
            globalvar.queryLimit = int(
                val if val.isdigit() else pywikibot.input(
                    'How many of the latest new users would you like to '
                    'load?'))
        elif arg == '-numberlog':
            globalvar.dumpToLog = int(
                val if val.isdigit() else pywikibot.input(
                    'After how many welcomed users would you like to update '
                    'the welcome log?'))
        elif arg in mapping:
            setattr(globalvar, *mapping[arg])
        else:
            pywikibot.warning('Unknown option "{}"'.format(arg))


def main(*args):
    """Invoke bot.

    @param args: command line arguments
    @type args: str
    """
    handle_args(args)
    # Filename and Pywikibot path
    # file where is stored the random signature index
    filename = pywikibot.config.datafilepath('welcome-%s-%s.data'
                                             % (pywikibot.Site().family.name,
                                                pywikibot.Site().code))
    if globalvar.offset and globalvar.timeoffset:
        pywikibot.warning(
            'both -offset and -timeoffset were provided, ignoring -offset')
        globalvar.offset = 0

    try:
        bot = WelcomeBot()
    except KeyError as error:
        # site not managed by welcome.py
        pywikibot.bot.suggest_help(exception=error)
        return False

    try:
        bot.run()
    except KeyboardInterrupt:
        if bot.welcomed_users:
            showStatus()
            pywikibot.output('Put welcomed users before quit...')
            bot.makelogpage(bot.welcomed_users)
        pywikibot.output('\nQuitting...')
    finally:
        # If there is the savedata, the script must save the number_user.
        if globalvar.randomSign and globalvar.saveSignIndex and \
           bot.welcomed_users:
            with open(filename, 'wb') as f:
                pickle.dump(bot.welcomed_users, f,
                            protocol=config.pickle_protocol)


if __name__ == '__main__':
    main()
