from app import app, db
from app.models import Category, Product, UserRoleEnum
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import logout_user, current_user
from flask import redirect

admin = Admin(app=app, name='Quản Trị Bán Hàng', template_mode='bootstrap4')


class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class MyCategoryView(AuthenticatedAdmin):
    column_list = ['name', 'products']


class MyProductView(AuthenticatedAdmin):
    column_searchable_list = ['name']
    column_list = ['id', 'name', 'price', 'active']
    column_filters = ['price', 'name']
    can_export = True
    edit_modal = True


class MyStatsView(AuthenticatedUser):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')


class LogOutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view((MyProductView(Product, db.session)))
admin.add_view(MyStatsView(name='Thống kê báo cáo'))
admin.add_view(LogOutView(name='Đăng xuất'))
