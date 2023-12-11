from cgi_services.regions.service import RegionsService
from cgi_view.regions.table.table import RegionsTableView
from cgi_view.regions.views.views import RegionsViewsView


class RegionsModule:
    def __init__(self):
        self.regions_service = RegionsService()
        self.regions_table_view = RegionsTableView(self)
        self.regions_views_view = RegionsViewsView(self)
