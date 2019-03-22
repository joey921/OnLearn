# _*_ encoding:utf-8 _*_


import xadmin
from users.models import EmailVerifyRecord,Banner,UserProfile
from xadmin import views

# class UserProfileAdmin(object):
#     list_display = ['username','email','mobile','image']

class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']

class BannerAdmin(object):
    list_display = ['title','image','url','index','add_time']
    search_fields = ['title','index','add_time']

class BaseSetting(object):
    enable_themes = True # 将隐藏的主题属性显现
    use_bootswatch = True  # 设置后才有很多主题可用


class GlobalSettings(object):
    site_title = "Online课堂后台"
    site_footer = "2018 上海xx网络科技有限公司      沪ICP备18065824号"
    menu_style = "accordion"  # 将各app的model折叠起来




xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)  # 注册全局设定
