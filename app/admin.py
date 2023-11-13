from app import app, db
from app.models import Category, Product
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView

admin = Admin(app=app, name='Quản Trị Bán Hàng', template_mode='bootstrap4')


class MyCategoryView(ModelView):
    column_list = ['name', 'products']


class MyProductView(ModelView):
    column_searchable_list = ['name']
    column_list = ['id', 'name', 'price', 'active']
    column_filters = ['price', 'name']
    can_export = True
    edit_modal = True


class MyStatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view((MyProductView(Product, db.session)))
admin.add_view(MyStatsView(name='Stats'))
