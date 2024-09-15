import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD_year(self):
        year_list = self._model.get_year()
        for y in year_list:
            self._view.ddyear.options.append(ft.dropdown.Option(y))
        self._view.update_page()

    def fillDD_shape(self, e):
        year = self._view.ddyear.value
        shape_list = self._model.get_shape(year)
        self._view.ddshape.options.clear()
        for s in shape_list:
            if len(s) > 1:
                self._view.ddshape.options.append(ft.dropdown.Option(s))
        self._view.update_page()

    def handle_graph(self, e):
        year = self._view.ddyear.value
        shape = self._view.ddshape.value
        self._model.crea_grafo(year, shape)

    def handle_path(self, e):
        pass
