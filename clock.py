import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from datetime import datetime
import pytz
import ntplib
import threading

# Set the window size
Window.size = (800, 480)

class ColoredLabel(Label):
    def __init__(self, background_color, **kwargs):
        super(ColoredLabel, self).__init__(**kwargs)
        with self.canvas.before:
            Color(*background_color)  # Set background color
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

class ClockWidget(BoxLayout):
    def __init__(self, city, timezone, time_format_24=True, **kwargs):
        super(ClockWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.city = city
        self.timezone = timezone
        self.time_format_24 = time_format_24

        self.city_label = ColoredLabel(text=city, font_size='30sp', halign='left', valign='middle', size_hint=(1, None), height=75, background_color=(0, 0, 0, 1))
        self.city_label.bind(size=self._update_text_size)
        self.city_label_padding = BoxLayout(size_hint_y=None, height=10)
        self.clock_label = ColoredLabel(font_size='150sp', halign='left', valign='middle', size_hint=(1, None), height=250, background_color=(0, 0, 0, 1))
        self.clock_label.bind(size=self._update_text_size)

        self.add_widget(self.city_label)
        self.add_widget(self.city_label_padding)
        self.add_widget(self.clock_label)

        Clock.schedule_interval(self.update_time, 1)
        Clock.schedule_once(self.print_widget_sizes, 0.1)

    def _update_text_size(self, instance, value):
        instance.text_size = instance.size

    def update_time(self, *args):
        now = datetime.now(pytz.timezone(self.timezone))
        time_format = '%H:%M:%S'  # Always use 24-hour format without AM/PM
        self.clock_label.text = now.strftime(time_format)
    
    def print_widget_sizes(self, *args):
        print(f"City Label Size: {self.city_label.size}, Position: {self.city_label.pos}")
        print(f"Clock Label Size: {self.clock_label.size}, Position: {self.clock_label.pos}")

class DigitalClockApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=(225, 0, 0, 95), spacing=20)

        # Clocks configuration
        clocks_config = [
            ('San Francisco', 'America/Los_Angeles', True),  # 24-hour format
            ('Tokyo', 'Asia/Tokyo', True)                    # 24-hour format
        ]

        for city, timezone, time_format_24 in clocks_config:
            group_layout = BoxLayout(orientation='vertical', spacing=10)
            clock_widget = ClockWidget(city, timezone, time_format_24)
            group_layout.add_widget(clock_widget)
            main_layout.add_widget(group_layout)

        # Sync time with NTP on startup in a separate thread
        threading.Thread(target=self.sync_time_with_ntp).start()

        return main_layout

    def sync_time_with_ntp(self):
        ntp_client = ntplib.NTPClient()
        try:
            response = ntp_client.request('pool.ntp.org')
            offset = response.offset
            self.set_system_time(offset)
        except Exception as e:
            print(f"Failed to sync time: {e}")

    def set_system_time(self, offset):
        # Set the system time (Requires administrative privileges)
        # Note: This code is just a placeholder as setting system time requires platform-specific implementation
        # and typically requires administrative privileges. This functionality is not implemented here.
        pass

if __name__ == '__main__':
    # Example time zones (full list available at https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
    # 'America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney', 'Africa/Johannesburg'
    # 'America/Los_Angeles', 'Europe/Berlin', 'Asia/Shanghai', 'Pacific/Auckland', 'America/Sao_Paulo'
    
    DigitalClockApp().run()
