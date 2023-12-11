from cgi_services.regions.service import RegionsService
from cgi_view.regions.table.table import RegionsTableView
from cgi_view.regions.views.views import RegionsViewsView
from cgi_view.regions.form.formAdd import RegionsFormAddView
from cgi_view.regions.form.formsEdit import RegionsFormsEditView


class RegionsModule:
    def __init__(self):
        self.regions_service = RegionsService()
        self.regions_table_view = RegionsTableView(self)
        self.regions_views_view = RegionsViewsView(self)
        self.regions_form_add_view = RegionsFormAddView(self)
        self.regions_forms_edit_view = RegionsFormsEditView(self)
