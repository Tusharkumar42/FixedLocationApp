
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

LATITUDE = 28.377127992862384
LONGITUDE = 77.33838391152926


class FixedLocationApp(App):

    def build(self):
        Window.clearcolor = (0.06, 0.09, 0.15, 1)

        layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=18
        )

        title = Label(
            text="FIXED LOCATION",
            font_size="26sp",
            bold=True
        )

        self.lat = Label(
            text=f"Latitude: {LATITUDE}",
            font_size="17sp"
        )

        self.lon = Label(
            text=f"Longitude: {LONGITUDE}",
            font_size="17sp"
        )

        self.status = Label(
            text="Status: Ready",
            font_size="18sp"
        )

        start = Button(
            text="START LOCATION",
            size_hint_y=None,
            height=65,
            background_color=(0.1, 0.6, 0.35, 1)
        )
        start.bind(on_press=self.start_location)

        stop = Button(
            text="STOP",
            size_hint_y=None,
            height=65
        )
        stop.bind(on_press=self.stop_location)

        for widget in [
            title, self.lat, self.lon,
            self.status, start, stop
        ]:
            layout.add_widget(widget)

        return layout

    def start_location(self, instance):
        self.status.text = (
            "Profile loaded\n"
            "GPS simulation not connected"
        )

    def stop_location(self, instance):
        self.status.text = "Status: Stopped"


if __name__ == "__main__":
    FixedLocationApp().run()
