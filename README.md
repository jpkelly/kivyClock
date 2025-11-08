# kivyClock

A multi-timezone digital clock application built with Kivy for Python. Displays current time for multiple cities simultaneously with NTP time synchronization support.

## Features

- **Multi-Timezone Display**: Shows time for multiple cities/timezones simultaneously
- **24-Hour Format**: Clean, military-style time display (HH:MM:SS)
- **NTP Time Sync**: Automatically syncs with NTP servers on startup
- **Customizable**: Easy to add/remove cities and configure timezones
- **Fixed Window Size**: Optimized for 800x480 displays (e.g., Raspberry Pi touchscreens)

## Requirements

- Python 3.x
- Kivy
- pytz
- ntplib

## Installation

1. Clone this repository:
```bash
git clone https://github.com/jpkelly/kivyClock.git
cd kivyClock
```

2. Install dependencies:
```bash
pip install kivy pytz ntplib
```

## Usage

Run the application:
```bash
python clock.py
```

## Configuration

Edit `clock.py` to customize the displayed timezones. Modify the `clocks_config` list in the `DigitalClockApp.build()` method:

```python
clocks_config = [
    ('San Francisco', 'America/Los_Angeles', True),
    ('Tokyo', 'Asia/Tokyo', True)
]
```

### Available Timezones

Common timezone strings (see [full list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)):
- `America/New_York`
- `America/Los_Angeles`
- `Europe/London`
- `Europe/Berlin`
- `Asia/Tokyo`
- `Asia/Shanghai`
- `Australia/Sydney`
- `Pacific/Auckland`
- `Africa/Johannesburg`
- `America/Sao_Paulo`

## Window Configuration

The default window size is 800x480 pixels. To change it, modify:
```python
Window.size = (width, height)
```

## License

MIT License