# -*- coding: utf-8  -*-
import family

# The Uncyclopaedia family, a satirical set of encyclopaedia wikis.
#
# Save this file to families/uncyclopedia_family.py in your pywikibot installation
# The pywikipediabot itself is available for free download from sourceforge.net
# A much more up-to-date version can be retrieved via SVN, with
# svn co http://svn.wikimedia.org/svnroot/pywikipedia/trunk/pywikipedia/ pywikipedia
#
# The latest version of this file can be get at
# http://inciclopedia.wikia.com/wiki/Usuario:Chixpy/uncyclopedia_family.py
#


# Modificado por Chixpy para Inciclopedia
# Updated by Laurusnobilis

class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'uncyclopedia'

        self.langs = {
		'ar': 'beidipedia.wikia.com',
		'ast': 'nunyepedia.wikia.com',
		'bg': 'bg.oxypedia.net',
		'bs': 'bs.neciklopedija.org',
		'ca': 'valenciclopedia.wikia.com',
		'cs': 'necyklopedie.wikia.com',
		'da': 'spademanns.wikia.com',
		'de': 'de.uncyclopedia.org',
		'el': 'frikipaideia.wikia.com',
		'en': 'uncyclopedia.org',
		'eo': 'neciklopedio.wikia.com',
		'es': 'inciclopedia.wikia.com',
		'et': 'uncyclopeedia.org',
		'fa': 'fa.uncyc.org',
		'fi': 'hiki.pedia.ws',
		'fr': 'desencyclopedie.wikia.com',
		'got': 'unsaiklo.pedia.ws',
		'he': 'eincyclopedia.wikia.com',
		'hr': 'hr.neciklopedija.org',
		'hu': 'unciklopedia.org',
		'id': 'tolololpedia.wikia.com',
		'it': 'nonciclopedia.wikia.com',
		'ja': 'ansaikuropedia.org',
		'ko': 'ko.uncyclopedia.info',
		'la': 'uncapaedia.wikia.com',
		'lb': 'lb.uncyc.org',
		'lt': 'juokopedija.org',
		'lv': 'lv.neciklopedija.org',
		'mg': 'hatsiklo.pedia.ws',
		'nl': 'oncyclopedia.net',
		'nn': 'ikkepedia.org',
		'no': 'ikkepedia.wikia.com',
		'pl': 'nonsensopedia.wikia.com',
		'pt': 'desciclo.pedia.ws',
		'ro': 'uncyclopedia.ro',
		'ru': 'absurdopedia.wikia.com',
		'simple': 'uncyclopedia.org',
		'sk': 'necyklopedia.wikia.com',
		'sl': 'butalo.pedija.org',
		'sr': 'sr.neciklopedija.org',
		'sv': 'psyklopedin.org',
		'th': 'th.uncyclopedia.info',
		'tr': 'yansiklopedi.org',
		'uk': 'uk.inciklopedii.org',
		'vi': 'uncyclopedia.org',
		'yi': 'keinziklopedie.wikia.com',
		'zh': 'zh.uncyclopedia.wikia.com',
		'zh-tw': 'uncyclopedia.tw',
#		'common': 'commons.uncyclomedia.org',
#		'info': 'uncyclopedia.info',
#		'meta': 'meta.uncyclomedia.org',
            }
	



        # Most namespaces are inherited from family.Family.
	
	self.namespaces[1] = {
		'_default': u'Talk',
		'ar': u'نقاش',
		'ast': u'Discusión',
		'bg': u'Беседа',
		'bs': u'Razgovor',
		'ca': u'Discussió',
		'cs': u'Diskuse',
		'da': u'Diskussion',
		'de': u'Diskussion',
		'el': u'Συζήτηση',
#		'en': u'Talk',
		'eo': u'Diskuto',
		'es': u'Discusión',
		'et': u'Arutelu',
		'fa': u'بحث',
		'fi': u'Keskustelu',
		'fr': u'Discuter',
		'he': u'שיחה',
		'hr': u'Razgovor',
		'hu': u'Vita',
		'id': u'Pembicaraan',
		'it': u'Discussione',
#		'ja': u'',
		'ko': u'토론',
		'la': u'Disputatio',
		'lb': u'Diskussion',
		'lt': u'Aptarimas',
		'lv': u'Diskusija',
#		'mg': u'',
		'nl': u'Overleg',
		'nn': u'Diskusjon',
		'no': u'Diskusjon',
		'pl': u'Dyskusja',
		'pt': u'Discussão',
		'ro': u'Discuţie',
		'ru': u'Обсуждение',
#		'simple': u'',
		'sk': u'Diskusia',
		'sl': u'Pogovor',
		'sr': u'Разговор',
		'sv': u'Diskussion',
		'th': u'พูดคุย',
		'tr': u'Tartışma',
		'uk': u'Обговорення',
#		'vi': u'',
		'yi': u'רעדן',
#		'zh': u'讨论',
		'zh-tw': u'討論',
	}

        self.namespaces[2] = {
		'_default': u'User',
		'ar': u'مستخدم',
		'ast': u'Usuariu',
		'bg': u'Потребител',
		'bs': u'Korisnik',
		'ca': u'Usuari',
		'cs': u'Uživatel',
		'da': u'Bruger',
		'de': u'Benutzer',
		'el': u'Χρήστης',
#		'en': u'User',
		'eo': u'Vikipediisto',
		'es': u'Usuario',
		'et': u'Kasutaja',
		'fa': u'کاربر',
		'fi': u'Käyttäjä',
		'fr': u'Utilisateur',
		'he': u'משתמש',
		'hr': u'Suradnik',
#		'hu': u'',
		'id': u'Pengguna',
		'it': u'Utente',
		'ja': u'利用者',
		'ko': u'사용자',
		'la': u'Usor',
		'lb': u'Benutzer',
		'lt': u'Naudotojas',
		'lv': u'Lietotājs',
#		'mg': u'',
		'nl': u'Gebruiker',
		'nn': u'Bruker',
		'no': u'Bruker',
		'pl': u'Użytkownik',
		'pt': u'Usuário',
		'ro': u'Utilizator',
		'ru': u'Участник',
#		'simple': u'',
		'sk': u'Redaktor',
		'sl': u'Uporabnik',
		'sr': u'Корисник',
		'sv': u'Användare',
		'th': u'ผู้ใช้',
		'tr': u'Kullanıcı',
		'uk': u'Користувач',
#		'vi': u'',
		'yi': u'באַניצער',
#		'zh': u'用户',
		'zh-tw': u'用戶',
        }

        self.namespaces[3] = {
		'_default': u'User talk',
		'ar': u'نقاش المستخدم',
		'ast': u'Usuariu discusión',
		'bg': u'Потребител беседа',
		'bs': u'Razgovor sa korisnikom',
		'ca': u'Usuari Discussió',
		'cs': u'Uživatel diskuse',
		'da': u'Brugerdiskussion',
		'de': u'Benutzer Diskussion',
		'el': u'Συζήτηση χρήστη',
#		'en': u'User talk',
		'eo': u'Vikipediista diskuto',
		'es': u'Usuario Discusión',
		'et': u'Kasutaja arutelu',
		'fa': u'بحث کاربر',
		'fi': u'Keskustelu käyttäjästä',
		'fr': u'Discussion Utilisateur',
		'he': u'שיחת משתמש',
		'hr': u'Razgovor sa suradnikom',
#		'hu': u'',
		'id': u'Pembicaraan Pengguna',
		'it': u'Discussioni utente',
		'ja': u'利用者‐会話',
		'ko': u'사용자토론',
		'la': u'Disputatio Usoris',
		'lb': u'Benutzer Diskussion',
		'lt': u'Naudotojo aptarimas',
		'lv': u'Lietotāja diskusija',
#		'mg': u'',
		'nl': u'Overleg gebruiker',
		'nn': u'Brukerdiskusjon',
		'no': u'Brukerdiskusjon',
		'pl': u'Dyskusja użytkownika',
		'pt': u'Usuário Discussão',
		'ro': u'Discuţie Utilizator',
		'ru': u'Обсуждение участника',
#		'simple': u'',
		'sk': u'Diskusia s redaktorom',
		'sl': u'Uporabniški pogovor',
		'sr': u'Разговор са корисником',
		'sv': u'Användardiskussion',
		'th': u'คุยกับผู้ใช้',
		'tr': u'Kullanıcı mesaj',
		'uk': u'Обговорення користувача',
#		'vi': u'',
		'yi': u'באַניצער רעדן',
#		'zh': u'用户讨论',
		'zh-tw': u'用戶討論',
        }

        self.namespaces[4] = {
		'_default': u'Uncyclopedia',
		'ar': u'بيضيپيديا',
		'ast': u'Nunyepedia',
		'bg': u'Oxypedia',
		'bs': u'Neciklopedija',
		'ca': u'Valenciclopèdia',
		'cs': u'Necyklopedie',
		'da': u'Spademanns Leksikon',
#		'de': u'Uncyclopedia',
		'el': u'Φρικηπαίδεια',
#		'en': u'Uncyclopedia',
		'eo': u'Neciklopedio',
		'es': u'Inciclopedia',
		'et': u'Ebatsüklopeedia',
#		'fa': u'',
		'fi': u'Hikipedia',
		'fr': u'Désencyclopédie',
		'got': u'Unsaiklopedia',
		'he': u'איןציקלופדיה',
		'hr': u'Neciklopedija',
		'hu': u'Unciklopédia',
		'id': u'Tolololpedia',
		'it': u'Nonciclopedia',
#		'ja': u'',
		'ko': u'백괴사전',
		'la': u'Uncapaedia',
		'lb': u'Kengencyclopedia',
		'lt': u'Juokopediją',
		'lv': u'Neciklopēdija',
		'mg': u'Hatsiklopedia',
		'nl': u'Oncyclopedie',
		'nn': u'Ikkepedia',
		'no': u'Ikkepedia ',
		'pl': u'Nonsensopedia',
		'pt': u'Desciclopédia',
		'ro': u'Unciclopedie',
		'ru': u'Абсурдопедия',
#		'simple': u'',
		'sk': u'Necyklopédia',
		'sl': u'Butalopedija',
		'sr': u'Нециклопедија',
		'sv': u'Psyklopedin',
		'th': u'ไร้สาระนุกรม',
		'tr': u'Yansiklopedi',
		'uk': u'Інциклопедія',
#		'vi': u'',
		'yi': u'קיינציקלאָפעדיע',
		'zh': u'伪基百科',
		'zh-tw': u'偽基百科',
        }

        self.namespaces[5] = {
		'_default': u'Uncyclopedia talk',
		'ar': u'نقاش بيضيپيديا',
		'ast': u'Nunyepedia discusión',
		'bg': u'Oxypedia беседа',
		'bs': u'Razgovor s Neciklopedija',
		'ca': u'Valenciclopèdia Discussió',
		'cs': u'Necyklopedie diskuse',
		'da': u'Spademanns Leksikon-diskussion',
		'de': u'Uncyclopedia Diskussion',
		'el': u'Φρικηπαίδεια συζήτηση',
#		'en': u'Uncyclopedia talk',
		'eo': u'Neciklopedio diskuto',
		'es': u'Inciclopedia Discusión',
		'et': u'Ebatsüklopeedia arutelu',
		'fa': u'بحث Uncyclopedia',
		'fi': u'Keskustelu Hikipediasta',
		'fr': u'Discussion Désencyclopédie',
		'got': u'Unsaiklopedia talk',
		'he': u'שיחת איןציקלופדיה',
		'hr': u'Razgovor Neciklopedija',
		'hu': u'Unciklopédia vita',
		'id': u'Pembicaraan Tolololpedia',
		'it': u'Discussioni Nonciclopedia',
		'ja': u'Uncyclopedia‐ノート',
		'ko': u'백괴사전토론',
		'la': u'Disputatio Uncapaediae',
		'lb': u'Kengencyclopedia Diskussion',
		'lt': u'Juokopediją aptarimas',
		'lv': u'Neciklopēdija diskusija',
		'mg': u'Hatsiklopedia talk',
		'nl': u'Overleg Oncyclopedie',
		'nn': u'Ikkepedia-diskusjon',
		'no': u'Ikkepedia -diskusjon',
		'pl': u'Dyskusja Nonsensopedia',
		'pt': u'Desciclopédia Discussão',
		'ro': u'Discuţie Unciclopedie',
		'ru': u'Обсуждение Абсурдопедии',
#		'simple': u'',
		'sk': u'Diskusia k Necyklopédia',
		'sl': u'Pogovor o Butalopedija',
		'sr': u'Разговор о Нециклопедија',
		'sv': u'Psyklopedindiskussion',
		'th': u'คุยเรื่องไร้สาระนุกรม',
		'tr': u'Yansiklopedi tartışma',
		'uk': u'Обговорення Інциклопедії',
#		'vi': u'',
		'yi': u'קיינציקלאָפעדיע רעדן',
		'zh': u'伪基百科 talk',
		'zh-tw': u'偽基百科討論',
        }

	self.namespaces[6] = {
		'_default': u'Image',
		'ar': u'صورة',
		'ast': u'Imaxen',
		'bg': u'Картинка',
		'bs': u'Slika',
		'ca': u'Imatge',
		'cs': u'Soubor',
		'da': u'Billede',
		'de': u'Bild',
		'el': u'Εικόνα',
#		'en': u'',
		'eo': u'Dosiero',
		'es': u'Imagen',
		'et': u'Pilt',
		'fa': u'تصویر',
		'fi': u'Kuva',
#		'fr': u'',
		'he': u'תמונה',
		'hr': u'Slika',
		'hu': u'Kép',
		'id': u'Berkas',
		'it': u'Immagine',
#		'ja': u'',
		'ko': u'그림',
		'la': u'Imago',
		'lb': u'Bild',
		'lt': u'Vaizdas',
		'lv': u'Attēls',
#		'mg': u'',
		'nl': u'Afbeelding',
		'nn': u'Bilde',
		'no': u'Bilde',
		'pl': u'Grafika',
		'pt': u'Imagem',
		'ro': u'Imagine',
		'ru': u'Изображение',
#		'simple': u'',
		'sk': u'Obrázok',
		'sl': u'Slika',
		'sr': u'Слика',
		'sv': u'Bild',
		'th': u'ภาพ',
		'tr': u'Resim',
		'uk': u'Зображення',
#		'vi': u'',
		'yi': u'בילד',
#		'zh': u'图像',
		'zh-tw': u'圖像',
	}

	self.namespaces[7] = {
		'_default': u'Image talk',
		'ar': u'نقاش الصورة',
		'ast': u'Imaxen discusión',
		'bs': u'Razgovor o slici',
		'bg': u'Картинка беседа',
		'ca': u'Imatge Discussió',
		'cs': u'Soubor diskuse',
		'da': u'Billeddiskussion',
		'de': u'Bild Diskussion',
		'el': u'Συζήτηση εικόνας',
#		'en': u'',
		'eo': u'Dosiera diskuto',
		'es': u'Imagen Discusión',
		'et': u'Pildi arutelu',
		'fa': u'بحث تصویر',
		'fi': u'Keskustelu kuvasta',
		'fr': u'Discussion Image',
		'he': u'שיחת תמונה',
		'hr': u'Razgovor o slici',
		'hu': u'Kep vita',
		'id': u'Pembicaraan Berkas',
		'it': u'Discussioni immagine',
		'ja': u'画像‐ノート',
		'ko': u'그림토론',
		'la': u'Disputatio Imaginis',
		'lb': u'Bild Diskussion',
		'lt': u'Vaizdo aptarimas',
		'lv': u'Attēla diskusija',
#		'mg': u'',
		'nl': u'Overleg afbeelding',
		'nn': u'Bildediskusjon',
		'no': u'Bildediskusjon',
		'pl': u'Dyskusja grafiki',
		'pt': u'Imagem Discussão',
		'ro': u'Discuţie Imagine',
		'ru': u'Обсуждение изображения',
#		'simple': u'',
		'sk': u'Diskusia k obrázku',
		'sl': u'Pogovor o sliki',
		'sr': u'Разговор о слици',
		'sv': u'Bilddiskussion',
		'th': u'คุยเรื่องภาพ',
		'tr': u'Resim tartışma',
		'uk': u'Обговорення зображення',
#		'vi': u'',
		'yi': u'בילד רעדן',
#		'zh': u'图像讨论',
		'zh-tw': u'圖像討論',
	}

        self.namespaces[8] = {
		'_default': u'MediaWiki',
		'ar': u'ميدياويكي',
		'bg': u'МедияУики',
		'bs': u'MedijaViki',
		'fa': u'مدیاویکی',
		'he': u'מדיה ויקי',
		'sr': u'МедијаВики',
		'th': u'มีเดียวิกิ',
		'tr': u'MedyaViki',
		'yi': u'מעדיעװיקי',
		'zh-tw': u'媒體偽基',
	}

        self.namespaces[9] = {
		'_default': u'MediaWiki talk',
		'ar': u'نقاش ميدياويكي',
		'ast': u'MediaWiki discusión',
		'bg': u'МедияУики беседа',
		'bs': u'Razgovor o MedijaVikiju',
		'ca': u'MediaWiki Discussió',
		'cs': u'MediaWiki diskuse',
		'da': u'MediaWiki-diskussion',
		'de': u'MediaWiki Diskussion',
#		'el': u'',
#		'en': u'',
		'eo': u'MediaWiki diskuto',
		'es': u'MediaWiki Discusión',
		'et': u'MediaWiki arutelu',
		'fa': u'بحث مدیاویکی',
		'fi': u'Keskustelu MediaWiki',
		'fr': u'Discussion MediaWiki',
		'he': u'שיחת מדיה ויקי',
		'hr': u'MediaWiki razgovor',
#		'hu': u'',
		'id': u'Pembicaraan MediaWiki',
		'it': u'Discussioni MediaWiki',
		'ja': u'MediaWiki‐ノート',
		'ko': u'MediaWiki토론',
		'la': u'Disputatio MediaWiki',
		'lb': u'MediaWiki Diskussion',
		'lt': u'MediaWiki aptarimas',
		'lv': u'MediaWiki diskusija',
#		'mg': u'',
		'nl': u'Overleg MediaWiki',
		'nn': u'MediaWiki-diskusjon',
		'no': u'MediaWiki-diskusjon',
		'pl': u'Dyskusja MediaWiki',
		'pt': u'MediaWiki Discussão',
		'ro': u'Discuţie MediaWiki',
		'ru': u'Обсуждение MediaWiki',
#		'simple': u'',
		'sk': u'Diskusia k MediaWiki',
		'sl': u'Pogovor o MediaWiki',
		'sr': u'Разговор о МедијаВикију',
		'sv': u'MediaWiki diskussion',
		'th': u'คุยเรื่องมีเดียวิกิ',
		'tr': u'MedyaViki tartışma',
		'uk': u'Обговорення MediaWiki',
#		'vi': u'',
		'yi': u'מעדיעװיקי רעדן',
#		'zh': u'MediaWiki讨论',
		'zh-tw': u'媒體偽基討論',
	}
	
	
	#
        # Custom namespace list
	#
	# NOTA: Estos espacios están entre mezclados entre ellos
	# y por tanto los espacios con el mismo número no son equivalentes
	# siendo los interwikis entre espacios distintos.
        #

#	self.namespaces[numero] = {
#		'_default':u'Espacio/Discusión numero',
#		'ar': u'',
#		'ast': u'',
#		'bg': u'',
#		'bs': u'',
#		'ca': u'',
#		'cs': u'',
#		'da': u'',
#		'de': u'',
#		'el': u'',
#		'en': u'',
#		'eo': u'',
#		'es': u'',
#		'et': u'',
#		'fa': u'',
#		'fi': u'',
#		'fr': u'',
#		'got': u'',
#		'he': u'',
#		'hu': u'',
#		'id': u'',
#		'it': u'',
#		'ja': u'',
#		'ko': u'',
#		'la': u'',
#		'lb': u'',
#		'lt': u'',
#		'lv': u'',
#		'mg': u'',
#		'nl': u'',
#		'nn': u'',
#		'no': u'',
#		'pl': u'',
#		'pt': u'',
#		'ro': u'',
#		'ru': u'',
#		'simple': u'',
#		'sk': u'',
#		'sl': u'',
#		'sr': u'',
#		'sv': u'',
#		'th': u'',
#		'tr': u'',
#		'uk': u'',
#		'vi': u'',
#		'yi': u'',
#		'zh': u'',
#		'zh-tw': u'',
#	}


	self.namespaces[16] = {
		'_default':u'Espacio 16',
		'fi': u'Foorumi',
		'got': u'Forum',
		'ko': u'漢字',
		'nl': u'Portaal',
		'pt': u'Esplanada',
		'th': u'อันไซโคลพีเดีย',
		'zh-tw': u'偽基新聞',		
	}

	self.namespaces[17] = {
		'_default':u'Discusión 17',
		'fi': u'Keskustelu foorumista',
		'got': u'Forum gawaurdja',
		'ko': u'討論',
		'nl': u'Overleg portaal',
		'pt': u'Esplanada Discussão',
		'th': u'คุยเรื่องอันไซโคลพีเดีย',
		'zh-tw': u'偽基新聞討論',		
	}

	self.namespaces[18] = {
		'_default':u'Espacio 18',
		'fi': u'Hikinews',
#		'got': u'',
		'ko': u'백괴나라',
		'nl': u'OnNieuws',
		'pt': u'Fatos',
		'th': u'ไร้ข่าว',
		'zh-tw': u'偽基辭典',		
	}

	self.namespaces[19] = {
		'_default':u'Discusión 19',
		'fi': u'Keskustelu Hikinewseistä',
#		'got': u'',
		'ko': u'백괴나라토론',
		'nl': u'Overleg OnNieuws',
		'pt': u'Fatos Discussão',
		'th': u'คุยเรื่องไร้ข่าว',
		'zh-tw': u'偽基辭典討論',		
	}

	self.namespaces[20] = {
		'_default':u'Espacio 20',
		'fi': u'Hiktionary',
#		'got': u'',
		'nl': u'Onwoordenboek',
		'pt': u'Forum',
		'th': u'ไร้วิทยาลัย',
		'zh-tw': u'動漫遊戲',		
	}
	
	self.namespaces[21] = {
		'_default':u'Discusión 21',
		'fi': u'Keskustelu Hiktionarystä',
#		'got': u'',
		'nl': u'Overleg Onwoordenboek',
		'pt': u'Forum Discussão',
		'th': u'คุยเรื่องไร้วิทยาลัย',
		'zh-tw': u'動漫遊戲討論',
	}

	self.namespaces[22] = {
		'_default':u'Espacio 22',
		'fi': u'Hikikirjasto',
		'nl': u'OnBoeken',
		'th': u'ไร้พจนานุกรม',
		'zh-tw': u'春心蕩漾',
	}
	
	self.namespaces[23] = {
		'_default':u'Discusion 23',
		'fi': u'Keskustelu hikikirjasta',
		'nl': u'Overleg OnBoeken',
		'th': u'คุยเรื่องไร้พจนานุกรม',
		'zh-tw': u'春心蕩漾討論',
	}
	
	self.namespaces[24] = {
		'_default':u'Espacio 24',
		'fi': u'Hikisitaatit',
		'th': u'ไร้ชีวประวัติ',
		'zh-tw': u'主題展館',
	}
	
	self.namespaces[25] = {
		'_default':u'Discusion 25',
		'fi': u'Keskustelu hikisitaatista',
		'th': u'คุยเรื่องไร้ชีวประวัติ',
		'zh-tw': u'主題展館討論',
	}
	
	self.namespaces[26] = {
		'_default':u'Espacio 26',
		'fi': u'Hömppäpedia',
		'th': u'สภาน้ำชา',
		'zh-tw': u'論壇',
	}
	
	self.namespaces[27] = {
		'_default':u'Discusion 27',
		'fi': u'Höpinä hömpästä',
		'th': u'คุยเรื่องสภาน้ำชา',
		'zh-tw': u'論壇討論',
	}
	
	self.namespaces[28] = {
		'_default':u'Espacio 28',
		'fi': u'Hikipeli',
		'nl': u'Ongerijmd',
		'th': u'บอร์ด',
		'zh-tw': u'詞意分道',
	}
	
	self.namespaces[29] = {
		'_default':u'Discusion 29',
		'fi': u'Hihitys Hikipelistä',
		'nl': u'Overleg Ongerijmd',
		'th': u'คุยเรื่องบอร์ด',
		'zh-tw': u'詞意分道討論',
	}
	
	
	self.namespaces[100] = {
		'_default':u'Espacio 100',
		'de': u'UnNews',
		'nn': u'Ikkenytt',
		'pl': u'Cytaty',
		'sv': u'PsykNyheter',
		'tr': u'YanSözlük',
	}

        self.namespaces[101] = {
		'_default':u'Discusión 101',
		'de': u'UnNews Diskussion',
		'nn': u'Ikkenytt-diskusjon',
		'pl': u'Dyskusja cytatów',
		'sv': u'PsykNyheter diskussion',
		'tr': u'YanSözlük tartışma',
	}

        self.namespaces[102] = {
		'_default':u'Espacio 102',
		'de': u'Undictionary',
		'en':u'UnNews',
		'ja': u'UnNews',
		'nn': u'Ikktionary',
		'pl': u'NonNews',
		'simple': u'UnNews',
		'sv': u'Forum',
		'tr': u'YanHaber',
		'vi': u'UnNews',
	}
	
        self.namespaces[103] = {
		'_default':u'Discusión 103',
		'de': u'Undictionary Diskussion',
		'en': u'UnNews talk',
		'ja': u'UnNews talk',
		'nn': u'Ikktionary-diskusjon',
		'pl': u'Dyskusja NonNews',
		'simple': u'UnNews talk',
		'sv': u'Forumdiskussion',
		'tr': u'YanHaber tartışma',
		'vi': u'UnNews talk',
	}
	
        self.namespaces[104] = {
		'_default':u'Espacio 104',
		'de': u'UnBooks',
		'en': u'Undictionary',
		'pl': u'Nonźródła',
		'simple': u'Undictionary',
		'sv': u'Psyktionary',
		'vi': u'Undictionary',
	}
	
        self.namespaces[105] = {
		'_default':u'Discusión 105',
		'de': u'UnBooks Diskussion',
		'en': u'Undictionary talk',
		'pl': u'Dyskusja nonźródeł',
		'simple': u'Undictionary talk',
		'sv': u'Psyktionary diskussion',
		'vi': u'Undictionary talk',
	}
	
        self.namespaces[106] = {
		'_default':u'Espacio 106',
		'en': u'Game',
		'ja': u'Game',
		'pl': u'Słownik',
		'pt': u'Desnotícias',
		'simple': u'Game',
		'sv': u'PsykCitat',
		'vi': u'Game',
	}
	
        self.namespaces[107] = {
		'_default':u'Discusión 107',
		'en': u'Game talk',
		'ja': u'Game talk',
		'pl': u'Dyskusja słownika',
		'pt': u'Desnotícias Discussão',
		'simple': u'Game talk',
		'sv': u'PsykCitat diskussion',
		'vi': u'Game talk',
	}
	
        self.namespaces[108] = {
		'_default':u'Espacio 108',
		'en': u'Babel',
		'pl': u'Gra',
		'pt': u'Jogo',
		'simple': u'Babel',
		'sv': u'Spel',
		'vi': u'Babel',
	}
	
        self.namespaces[109] = {
		'_default':u'Discusión 109',
		'en': u'Babel talk',
		'pl': u'Dyskusja gry',
		'pt': u'Jogo Discussão',
		'simple': u'Babel talk',
		'sv': u'Speldiskussion',
		'vi': u'Babel talk',
	}
	
	#Espacio del Foro en Wikia
        self.namespaces[110] = {
		'_default':u'Forum',
		'pt': u'Descionário',
		'ru': u'Форум',
		'sv': u'PsykBöcker',
		'tr': u'Astroloji',
	}
	
        #Discusión del Foro en wikia
	self.namespaces[111] = {
		'_default':u'Forum talk',
		'da': u'Forumdiskussion',
		'fr': u'Discussion Forum',
		'nn': u'Forum-diskusjon',
		'pl': u'Dyskusja forum',
		'pt': u'Descionário Discussão',
		'ru': u'Обсуждение форума',
		'sv': u'PsykBöckerdiskussion',
		'tr': u'Astroloji tartışma',
	}
	
	#
	# Espacios de las wikis en wikia
	#
	self.namespaces[112] = {
		'_default':u'Espacio 112',
		'en': u'UnTunes',
		'es':u'Incinoticias',
		'fr': u'Désinformation',
		'ja': u'UnTunes',
		'nn': u'Hvordan',
		'pl': u'Portal',
		'pt': u'Descionário Discussão',
		'simple': u'UnTunes',
		'tr': u'Forum',
		'vi': u'UnTunes',
	}

	self.namespaces[113] = {
		'_default':u'Discusión 113',
		'en': u'UnTunes talk',
		'es':u'Incinoticias Discusión',
		'fr': u'Discussion Désinformation',
		'ja': u'UnTunes talk',
		'nn': u'Hvordan-diskusjon',
		'pl': u'Dyskusja portalu',
		'simple': u'UnTunes talk',
		'tr': u'Forum tartışma',
		'vi': u'UnTunes talk',
	}

	self.namespaces[114] = {
		'_default':u'Espacio 114',
		'es':u'Incitables',
		'nn': u'Hvorfor',
		'pl': u'Poradnik',
	}

	self.namespaces[115] = {
		'_default':u'Discusión 115',
		'es':u'Incitables Discusión',
		'nn': u'Hvorfor-diskusjon',
		'pl': u'Dyskusja poradnika',
	}

        # A few selected big languages for things that we do not want to loop over
        # all languages. This is only needed by the titletranslate.py module, so
        # if you carefully avoid the options, you could get away without these
        # for another wiki family.
        self.languages_by_size = ['en', 'pl', 'de', 'es', 'ru', 'fr', 'pt', 'ja', 'fi', 'it']

    def hostname(self,code):
        return self.langs[code]

    def scriptpath(self, code):
        return ''

    def path(self, code):

# 'simple' y 'vi' estan en Babel
        if code=='simple':
           return '/wiki/Babel:Simple'
        if code=='vi':
           return '/wiki/Babel:Vi'
        return '/index.php'

    def version(self, code):
        return "1.12alpha"