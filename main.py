from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import pandas as pd
import os

# ================= CONFIG =================
ARCH_SEL = "seleccionados.txt"
ARCH_EF = "efectos_prohibidos.txt"

COLOR_NORMAL = (1, 1, 1, 1)
COLOR_ROJO = (1, 0, 0, 1)

# ================= UTIL =================
def cargar_archivo(nombre):
    if not os.path.exists(nombre):
        return set()
    with open(nombre, "r", encoding="utf-8") as f:
        return set(l.strip() for l in f if l.strip())

def guardar_archivo(nombre, data):
    with open(nombre, "w", encoding="utf-8") as f:
        for x in sorted(data):
            f.write(x + "\n")

# ================= DATOS =================
df = pd.read_excel("SK.xlsx", usecols=[0, 1], names=["ingrediente", "efecto"], header=0)
df["ingrediente"] = df["ingrediente"].astype(str).str.lower().str.strip()
df["efecto"] = df["efecto"].astype(str).str.lower().str.strip()

ingredientes = sorted(df["ingrediente"].unique())

def ingredientes_prohibidos(efectos):
    return set(df[df["efecto"].isin(efectos)]["ingrediente"].unique())

# ================= PANTALLA 1 =================
class SeleccionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filas = {}

        root = BoxLayout(orientation="vertical", padding=20, spacing=20)
        scroll = ScrollView()

        self.lista = BoxLayout(orientation="vertical", size_hint_y=None, spacing=15)
        self.lista.bind(minimum_height=self.lista.setter("height"))
        scroll.add_widget(self.lista)
        root.add_widget(scroll)

        for ing in ingredientes:
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
        app = App.get_running_app()
        prohibidos = ingredientes_prohibidos(app.efectos_prohibidos)

        for ing, (chk, lbl) in self.filas.items():
            chk.active = ing in app.seleccionados
            lbl.color = COLOR_ROJO if ing in prohibidos else COLOR_NORMAL

    def toggle(self, ing, activo):
        app = App.get_running_app()
        if activo:
            app.seleccionados.add(ing)
        else:
            app.seleccionados.discard(ing)
        guardar_archivo(ARCH_SEL, app.seleccionados)

    def continuar(self):
        App.get_running_app().sm.current = "menu"

# ================= MENU =================
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
        App.get_running_app().sm.current = p

# ================= ELEGIR INGREDIENTE =================
class ElegirIngredienteScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
        app = App.get_running_app()
        prohibidos = ingredientes_prohibidos(app.efectos_prohibidos)

        for ing in sorted(app.seleccionados):
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
        app = App.get_running_app()
        app.ingrediente_base = ing
        app.sm.current = "resultado_ingrediente"

    def volver(self):
        App.get_running_app().sm.current = "menu"

# ================= ELEGIR EFECTO =================
class ElegirEfectoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical", padding=20, spacing=20)
        scroll = ScrollView()

        self.lista = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            spacing=15
        )
        self.lista.bind(minimum_height=self.lista.setter("height"))
        scroll.add_widget(self.lista)
        root.add_widget(scroll)

        btn = Button(
            text="Volver",
            height=90,
            font_size=32,
            size_hint_y=None
        )
        btn.bind(on_press=lambda *_: self.volver())
        root.add_widget(btn)

        self.add_widget(root)

    def on_enter(self):
        self.lista.clear_widgets()
        app = App.get_running_app()

        efectos = sorted(df["efecto"].unique())

        for ef in efectos:
            fila = BoxLayout(size_hint_y=None, height=110, spacing=10)

            chk = CheckBox(size_hint_x=None, width=90)
            chk.active = ef in app.efectos_prohibidos
            chk.bind(active=lambda chk, val, e=ef: self.toggle_efecto(e, val))

            btn = Button(
                text=ef,
                font_size=34,
                halign="left"
            )
            btn.bind(on_press=lambda b, e=ef: self.mostrar(e))

            fila.add_widget(chk)
            fila.add_widget(btn)
            self.lista.add_widget(fila)

    def toggle_efecto(self, ef, activo):
        app = App.get_running_app()
        if activo:
            app.efectos_prohibidos.add(ef)
        else:
            app.efectos_prohibidos.discard(ef)

        guardar_archivo(ARCH_EF, app.efectos_prohibidos)

    def mostrar(self, ef):
        app = App.get_running_app()
        app.efecto_base = ef
        app.sm.current = "resultado_efecto"

    def volver(self):
        App.get_running_app().sm.current = "menu"

# ================= RESULTADOS =================
class ResultadoIngredienteScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
        app = App.get_running_app()
        base = app.ingrediente_base
        sel = app.seleccionados

        efectos_base = sorted(
            df[df["ingrediente"] == base]["efecto"].unique()
        )

        texto = []
        texto.append("Ingrediente seleccionado:")
        texto.append(base)
        texto.append("")
        texto.append("Efectos de este ingrediente:")
        for e in efectos_base:
            texto.append(f"- {e}")

        texto.append("")
        texto.append("Otros ingredientes que comparten al menos uno de estos efectos:")
        texto.append("")

        hay_coincidencias = False

        for ing in sorted(sel):
            if ing == base:
                continue

            efectos_ing = set(
                df[df["ingrediente"] == ing]["efecto"].unique()
            )
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
        App.get_running_app().sm.current = "elige_ingrediente"

class ResultadoEfectoScreen(ResultadoIngredienteScreen):
    def on_enter(self):
        app = App.get_running_app()
        ef = app.efecto_base
        ing = df[df["efecto"] == ef]["ingrediente"].unique()
        self.lbl.text = ef + "\n\n" + "\n".join(ing)

    def volver(self):
        App.get_running_app().sm.current = "elige_efecto"

# ================= APP =================
class IngredientesApp(App):
    def build(self):
        self.seleccionados = cargar_archivo(ARCH_SEL)
        self.efectos_prohibidos = cargar_archivo(ARCH_EF)
        self.ingrediente_base = ""
        self.efecto_base = ""

        self.sm = ScreenManager()
        self.sm.add_widget(SeleccionScreen(name="seleccion"))
        self.sm.add_widget(MenuScreen(name="menu"))
        self.sm.add_widget(ElegirIngredienteScreen(name="elige_ingrediente"))
        self.sm.add_widget(ElegirEfectoScreen(name="elige_efecto"))
        self.sm.add_widget(ResultadoIngredienteScreen(name="resultado_ingrediente"))
        self.sm.add_widget(ResultadoEfectoScreen(name="resultado_efecto"))

        return self.sm

IngredientesApp().run()
