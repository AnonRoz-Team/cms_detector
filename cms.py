#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
G = '\033[0;32m'
C = '\033[0;36m'
W = '\033[0;37m'
R = '\033[0;31m'
Y = '\033[0;33m'
import requests,sys,os
from multiprocessing.pool import ThreadPool
reload(sys)
sys.setdefaultencoding('utf8')
os.system('cls' if os.name == 'nt' else 'clear')
if os.path.isdir("cms_result")==False:os.system("mkdir cms_result")
def scan(site):
	try:
		if "http" in site:
			url = site
		else:
			url = "http://" + site
		r = requests.get(url,timeout=10)
		# 1. CMS WORDPRESS
		if "/wp-content/" in r.text or "/wp-login.php" in r.text or "/wp-admin/" in r.text or "/license.txt" in r.text:
			print("%s[%s✓%s] WORDPRESS %s"%(W,G,W,url))
			open("cms_result/wordpress.txt","a+").write(url + "\n")
		# 2. CMS JOOMLA
		elif "/Joomla!" in r.text or "/index.php?option=com_" in r.text or "/administrator/index.php" in r.text or "/administrator/" in r.text or "/administrator/manifests/files/joomla.xml" in r.text or "/<version>(.*?)<\/version>" in r.text or "/language/en-GB/en-GB.xml" in r.text or "<version>(.*?)<\/version>" in r.text:
			print("%s[%s✓%s] JOOMLA %s"%(W,G,W,url))
			open("cms_result/joomla.txt","a+").write(url + "\n")
		# 3. CMS OPENCART
		elif "/index.php?route=common/home" in r.text:
			print("%s[%s✓%s] OPENCART %s"%(W,G,W,url))
			open("cms_result/opencart.txt","a+").write(url + "\n")
		# 4. CMS DRUPAL
		elif "/sites/default" in r.text:
			print("%s[%s✓%s] DRUPAL %s"%(W,G,W,url))
			open("cms_result/drupal.txt","a+").write(url + "\n")
		# 5. CMS PRESTASHOP
		elif "/prestashop" in r.text or "/PrestaShop" in r.text:
			print("%s[%s✓%s] PRESTASHOP %s"%(W,G,W,url))
			open("cms_result/prestashop.txt","a+").write(url + "\n")
		# 6. CMS OSCOMMERCE
		elif "/osCommerce" in r.text or "/admin/login.php" in r.text or "/admin/images/cal_date_over.gif" in r.text:
			print("%s[%s✓%s] OSCOMMERCE %s"%(W,G,W,url))
			open("cms_result/oscommerce.txt","a+").write(url + "\n")
		# 7. CMS VBULLETIN
		elif "/osCommerce" in r.text or "/admin/login.php" in r.text or "/admin/images/cal_date_over.gif" in r.text:
			print("%s[%s✓%s] VBULLETIN %s"%(W,G,W,url))
			open("cms_result/vbulletin.txt","a+").write(url + "\n")
		# 8. CMS MAGENTO
		elif "/Mage.Cookies" in r.text:
			print("%s[%s✓%s] MAGENTO %s"%(W,G,W,url))
			open("cms_result/magento.txt","a+").write(url + "\n")
		# 9. CMS ZENCART
		elif "/application/configs/application.ini" in r.text:
			print("%s[%s✓%s] ZENCART %s"%(W,G,W,url))
			open("cms_result/zencart.txt","a+").write(url + "\n")
                # 10. CMS SHOPIFY
		elif "/collections/all/Powered by Shopify/cdn.shopify.com/" in r.text or "/all/" in r.text or "/collections/all" in r.text or "/Powered by Shopify/" in r.text or "/cdn.shopify.com" in r.text:
			print("%s[%s✓%s] SHOPIFY %s"%(W,G,W,url))
			open("cms_result/shopify.txt","a+").write(url + "\n")
                # 11. CMS LARAVEL PHP UNIT
		elif "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php" in r.text:
			print("%s[%s✓%s] LARAVEL PHPUNIT %s"%(W,G,W,url))
			open("cms_result/laravel_phpunit.txt","a+").write(url + "\n")
		# 12. CMS SITEFINITY
		elif "/Sitefinity" in r.text or "/sitefinity/UserControls/Dialogs/DocumentEditorDialog.aspx" in r.text:
			print("%s[%s✓%s] SITEFINITY %s"%(W,G,W,url))
			open("cms_result/sitefinity.txt","a+").write(url + "\n")
		# 13. CMS MYBB
		elif "/jscripts/general.js?ver=" in r.text:
			print("%s[%s✓%s] MYBB %s"%(W,G,W,url))
			open("cms_result/mybb.txt","a+").write(url + "\n")
		# 14. CMS UBERCART
		elif "/uc_cart" in r.text:
			print("%s[%s✓%s] UBERCART %s"%(W,G,W,url))
			open("cms_result/ubercart.txt","a+").write(url + "\n")
		# 15. CMS PROTOTYPE
		elif "/sites/default" in r.text or "/prototype.js" in r.text:
			print("%s[%s✓%s] PROTOTYPE %s"%(W,G,W,url))
			open("cms_result/prototype.txt","a+").write(url + "\n")
		# 16. CMS JQUERY FILE UPLOAD
		elif "/assets/global/plugins/jquery-file-upload/server/php/" in r.text or "/jQuery/server/php" in r.text:
			print("%s[%s✓%s] JQUERY FILE UPLOAD %s"%(W,G,W,url))
			open("cms_result/jquery_file_upload.txt","a+").write(url + "\n")
		# 17. CMS JALIOS JCMS
		elif "/Jalios JCMS/" in r.text:
			print("%s[%s✓%s] JALIOS JCMS %s"%(W,G,W,url))
			open("cms_result/jalios_jcms.txt","a+").write(url + "\n")
		# 18. CMS SHAREPOINT
		elif "/SharePoint/" in r.text:
			print("%s[%s✓%s] SHAREPOINT %s"%(W,G,W,url))
			open("cms_result/sharepoint.txt","a+").write(url + "\n")
		# 19. CMS BIGACE
		elif "/BIGACE/" in r.text:
			print("%s[%s✓%s] BIGACE %s"%(W,G,W,url))
			open("cms_result/bigace.txt","a+").write(url + "\n")
		# 20. CMS ZENPHOTO
		elif "/zp-core/js/" in r.text:
			print("%s[%s✓%s] ZENPHOTO %s"%(W,G,W,url))
			open("cms_result/zenphoto.txt","a+").write(url + "\n")
		# 00. CMS NOT FOUND / NOT WORKING
		else:
			print("%s[%sx%s] %sNOT FOUND %s"%(W,R,W,R,url))
			open("cms_result/othercms.txt","a+").write(url + "\n")
	except:
		print("%s[%sx%s] %sNOT WORKING %s"%(W,R,W,R,url))
		pass
try:
	os.system('cls' if os.name == 'nt' else 'clear')
	print '''%s
_________     _____    _________
\_   ___ \   /     \  /   _____/   %sCoded by D4RKSH4D0WS%s
/    \  \/  /  \ /  \ \_____  \    %sFB gg.gg/AnonRoz-Team%s
\     \____/    Y    \/        \   %sIG @anonroz_team%s
 \______  /\____|__  /_______  /   %sCMS DETECTOR%s
        \/         \/        \/ 
	'''%(C,W,C,W,C,W,C,W,C)
	ThreadPool(20).map(scan,open(sys.argv[1]).read().splitlines())
	print '\n%s[%s✓%s] Saved in cms_result'%(W,G,W)
except IndexError:exit('%s[%s!%s] Use : python2 %s target.txt \n    Example: https://target.com/'%(W,R,W,sys.argv[0]))
except IOError:exit('%s[%s!%s] File does not exist'%(W,R,W))
except requests.exceptions.ConnectionError:exit('%s[%s!%s] Check internet'%(W,R,W))
except KeyboardInterrupt:exit('%s[%s!%s] Exit'%(W,R,W))
