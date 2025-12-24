from kivy.resources import resource_find
import shutil
from kivy.utils import platform
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import pandas as pd
import os

# ================= UTIL =================
def ruta_archivo(nombre):
    if platform == "android":
        return os.path.join(App.get_running_app().user_data_dir, nombre)
    else:
        return nombre

def cargar_archivo(nombre):
    if not os.path.exists(nombre):
        return set()
    try:
        with open(nombre, "r", encoding="utf-8") as f:
            return set(l.strip() for l in f if l.strip())
    except Exception:
        return set()

def asegurar_excel():
    destino = ruta_archivo("SK.xlsx")
    if not os.path.exists(destino):
        origen = resource_find("SK.xlsx")
        if origen is None:
            print("¡No se encontró SK.xlsx en recursos!")  # <- ayuda a debug
            raise FileNotFoundError("No se encontró SK.xlsx en recursos")
        shutil.copy(origen, destino)
        except Exception as e:
            return False, f"Error copiando SK.xlsx: {e}"
    return True, ""

def guardar_archivo(nombre, data):
    with open(nombre, "w", encoding="utf-8") as f:
        for x in sorted(data):
            f.write(x + "\n")

# ================= COLORES =================
COLOR_NORMAL = (1, 1, 1, 1)
COLOR_ROJO = (1, 0, 0, 1)

# ================= APP =================
class IngredientesApp(App):
    def build(self):
        # Layout principal de error
        root = BoxLayout(orientation="vertical", padding=20)
        self.error_label = Label(text="", font_size=28)
        root.add_widget(self.error_label)

        # Aseguro Excel
        ok, msg = asegurar_excel()
        if not ok:
            self.error_label.text = msg
            return root

        # Datos
        self.seleccionados = cargar_archivo(ruta_archivo("seleccionados.txt"))
        self.efectos_prohibidos = cargar_archivo(ruta_archivo("efectos_prohibidos.txt"))
        self.ingrediente_base = ""
        self.efecto_base = ""

        try:
            df = pd.read_excel(
                ruta_archivo("SK.xlsx"),
                usecols=[0, 1],
                names=["ingrediente", "efecto"],
                header=0
            )
        except Exception as e:
            self.error_label.text = f"Error leyendo SK.xlsx:\n{e}"
            return root

        df["ingrediente"] = df["ingrediente"].astype(str).str.lower().str.strip()
        df["efecto"] = df["efecto"].astype(str).str.lower().str.strip()
        self.df = df
        self.ingredientes = sorted(df["ingrediente"].unique())

        # Screen Manager
        self.sm = ScreenManager()
        self.sm.add_widget(SeleccionScreen(name="seleccion", app=self))
        self.sm.add_widget(MenuScreen(name="menu", app=self))
        self.sm.add_widget(ElegirIngredienteScreen(name="elige_ingrediente", app=self))
        self.sm.add_widget(ElegirEfectoScreen(name="elige_efecto", app=self))
        self.sm.add_widget(ResultadoIngredienteScreen(name="resultado_ingrediente", app=self))
        self.sm.add_widget(ResultadoEfectoScreen(name="resultado_efecto", app=self))

        return self.sm

# ================= SCREENS =================
class SeleccionScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.filas = {}

        root = BoxLayout(orientation="vertical", padding=20, spacing=20)
        scroll = ScrollView()
        self.lista = BoxLayout(orientation="vertical", size_hint_y=None, spacing=15)
        self.lista.bind(minimum_height=self.lista.setter("height"))
        scroll.add_widget(self.lista)
        root.add_widget(scroll)

        for ing in app.ingredientes:
            fila = BoxLayout(size_hint_y=None, height=110)
            chk = CheckBox(size_hint_x=None, width=90)
            chk.bind(active=lambda chk, val, i=ing: self.toggle(i, val))
            lbl = Label(text=ing, font_size=34, halign="left", valign="middle")
            lbl.bind(size=lbl.setter("text_size"))
            fila.add_widget(chk)
            fila.add_widget(lbl)
            self.lista.add_widget(fila)
            self.filas[ing] = (chk, lbl)

        btn = Button(text="Continuar", height=100, font_size=36, size_hint_y=None)
        btn.bind(on_press=lambda *_: self.continuar())
        root.add_widget(btn)
        self.add_widget(root)

    def on_enter(self):
        prohibidos = self.app.df[self.app.df["efecto"].isin(self.app.efectos_prohibidos)]["ingrediente"].unique()
        for ing, (chk, lbl) in self.filas.items():
            chk.active = ing in self.app.seleccionados
            lbl.color = COLOR_ROJO if ing in prohibidos else COLOR_NORMAL

    def toggle(self, ing, activo):
        if activo:
            self.app.seleccionados.add(ing)
        else:
            self.app.seleccionados.discard(ing)
        guardar_archivo(ruta_archivo("seleccionados.txt"), self.app.seleccionados)

    def continuar(self):
        self.app.sm.current = "menu"

class MenuScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        root = BoxLayout(orientation="vertical", padding=25, spacing=25)
        b1 = Button(text="Buscar por ingrediente", font_size=36, height=110)
        b2 = Button(text="Buscar por efecto", font_size=36, height=110)
        b3 = Button(text="Volver", font_size=32, height=90)
        b1.bind(on_press=lambda *_: self.ir("elige_ingrediente"))
        b2.bind(on_press=lambda *_: self.ir("elige_efecto"))
        b3.bind(on_press=lambda *_: self.ir("seleccion"))
        root.add_widget(b1)
        root.add_widget(b2)
        root.add_widget(b3)
        self.add_widget(root)

    def ir(self, p):
        self.app.sm.current = p

class ElegirIngredienteScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        root = BoxLayout(orientation="vertical", padding=20, spacing=20)
        scroll = ScrollView()
        self.lista = BoxLayout(orientation="vertical", size_hint_y=None, spacing=15)
        self.lista.bind(minimum_height=self.lista.setter("height"))
        scroll.add_widget(self.lista)
        root.add_widget(scroll)
        btn = Button(text="Volver", height=90, font_size=32, size_hint_y=None)
        btn.bind(on_press=lambda *_: self.volver())
        root.add_widget(btn)
        self.add_widget(root)

    def on_enter(self):
        self.lista.clear_widgets()
        prohibidos = self.app.df[self.app.df["efecto"].isin(self.app.efectos_prohibidos)]["ingrediente"].unique()
        for ing in sorted(self.app.seleccionados):
            btn = Button(
                text=ing,
                font_size=34,
                height=110,
                size_hint_y=None,
                color=COLOR_ROJO if ing in prohibidos else COLOR_NORMAL
            )
            btn.bind(on_press=lambda b, i=ing: self.mostrar(i))
            self.lista.add_widget(btn)

    def mostrar(self, ing):
        self.app.ingrediente_base = ing
        self.app.sm.current = "resultado_ingrediente"

    def volver(self):
        self.app.sm.current = "menu"

class ElegirEfectoScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        root = BoxLayout(orientation="vertical", padding=20, spacing=20)
        scroll = ScrollView()
        self.lista = BoxLayout(orientation="vertical", size_hint_y=None, spacing=15)
        self.lista.bind(minimum_height=self.lista.setter("height"))
        scroll.add_widget(self.lista)
        root.add_widget(scroll)
        btn = Button(text="Volver", height=90, font_size=32, size_hint_y=None)
        btn.bind(on_press=lambda *_: self.volver())
        root.add_widget(btn)
        self.add_widget(root)

    def on_enter(self):
        self.lista.clear_widgets()
        efectos = sorted(self.app.df["efecto"].unique())
        for ef in efectos:
            fila = BoxLayout(size_hint_y=None, height=110, spacing=10)
            chk = CheckBox(size_hint_x=None, width=90)
            chk.active = ef in self.app.efectos_prohibidos
            chk.bind(active=lambda chk, val, e=ef: self.toggle_efecto(e, val))
            btn = Button(text=ef, font_size=34, halign="left")
            btn.bind(on_press=lambda b, e=ef: self.mostrar(e))
            fila.add_widget(chk)
            fila.add_widget(btn)
            self.lista.add_widget(fila)

    def toggle_efecto(self, ef, activo):
        if activo:
            self.app.efectos_prohibidos.add(ef)
        else:
            self.app.efectos_prohibidos.discard(ef)
        guardar_archivo(ruta_archivo("efectos_prohibidos.txt"), self.app.efectos_prohibidos)

    def mostrar(self, ef):
        self.app.efecto_base = ef
        self.app.sm.current = "resultado_efecto"

    def volver(self):
        self.app.sm.current = "menu"

class ResultadoIngredienteScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        root = BoxLayout(orientation="vertical", padding=20, spacing=20)
        scroll = ScrollView()
        self.lbl = Label(font_size=30, size_hint_y=None, valign="top")
        self.lbl.bind(texture_size=self.lbl.setter("size"))
        scroll.add_widget(self.lbl)
        root.add_widget(scroll)
        btn = Button(text="Volver", height=90, font_size=32, size_hint_y=None)
        btn.bind(on_press=lambda *_: self.volver())
        root.add_widget(btn)
        self.add_widget(root)

    def on_enter(self):
        base = self.app.ingrediente_base
        sel = self.app.seleccionados
        efectos_base = sorted(self.app.df[self.app.df["ingrediente"] == base]["efecto"].unique())
        texto = [f"Ingrediente seleccionado:\n{base}", "", "Efectos de este ingrediente:"]
        for e in efectos_base:
            texto.append(f"- {e}")
        texto.append("\nOtros ingredientes que comparten al menos uno de estos efectos:\n")
        hay_coincidencias = False
        for ing in sorted(sel):
            if ing == base:
                continue
            efectos_ing = set(self.app.df[self.app.df["ingrediente"] == ing]["efecto"].unique())
            comunes = efectos_ing & set(efectos_base)
            if comunes:
                hay_coincidencias = True
                texto.append(ing)
                for c in sorted(comunes):
                    texto.append(f"  • {c}")
                texto.append("")
        if not hay_coincidencias:
            texto.append("No hay otros ingredientes que compartan estos efectos.")
        self.lbl.text = "\n".join(texto)

    def volver(self):
        self.app.sm.current = "elige_ingrediente"

class ResultadoEfectoScreen(ResultadoIngredienteScreen):
    def on_enter(self):
        ef = self.app.efecto_base
        ing = self.app.df[self.app.df["efecto"] == ef]["ingrediente"].unique()
        self.lbl.text = ef + "\n\n" + "\n".join(ing)

    def volver(self):
        self.app.sm.current = "elige_efecto"

if __name__ == "__main__":
    IngredientesApp().run()
