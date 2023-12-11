from services.regions.service import RegionsService
from view.regions.table.table import RegionsTableView
from view.regions.views.views import RegionsViewsView
from view.regions.form.formAdd import RegionsFormAddView
from view.regions.form.formsEdit import RegionsFormsEditView
from controllers.regions.controller import RegionsController


class RegionsModule:
    def __init__(self, app_arg):
        self.regions_service = RegionsService(self)
        self.regions_table_view = RegionsTableView(self)
        self.regions_views_view = RegionsViewsView(self)
        self.regions_form_add_view = RegionsFormAddView(self)
        self.regions_forms_edit_view = RegionsFormsEditView(self)
        self.regions_controller = RegionsController(self,app_arg)
