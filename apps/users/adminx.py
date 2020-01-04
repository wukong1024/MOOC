import xadmin
from xadmin import views
from .models import *


class BaseSetting(object):  # 设置主题
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):  # 设置标题
    site_title = 'MOOC'
    site_footer = 'Wukong'
    menu_style = 'accordion'  # 折叠目录


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']



class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    # font awesome



xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
