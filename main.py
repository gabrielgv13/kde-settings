
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction


KCM_MAP = {
    "appearance": "systemsettings kcm_style",
    "application style": "systemsettings kcm_style",
    "colors": "systemsettings kcm_colors",
    "global theme": "systemsettings kcm_lookandfeel",
    "look and feel": "systemsettings kcm_lookandfeel",
    "icons": "systemsettings kcm_icons",
    "cursor theme": "systemsettings kcm_cursortheme",
    "desktop theme": "systemsettings kcm_desktoptheme",
    "splash screen": "systemsettings kcm_splashscreen",
    "sound theme": "systemsettings kcm_soundtheme",
    "wallpaper": "systemsettings kcm_wallpaper",

    "window management": "systemsettings kcm_kwinoptions",
    "window decorations": "systemsettings kcm_kwindecoration",
    "window rules": "systemsettings kcm_kwinrules",
    "window effects": "systemsettings kcm_kwin_effects",
    "desktop effects": "systemsettings kcm_kwin_effects",
    "screen edges": "systemsettings kcm_kwinscreenedges",
    "touchscreen gestures": "systemsettings kcm_kwintouchscreen",
    "alt tab": "systemsettings kcm_kwintabbox",

    "workspace": "systemsettings kcm_workspace",
    "workspace behavior": "systemsettings kcm_workspace",
    "desktop behavior": "systemsettings kcm_workspace",
    "activities": "systemsettings kcm_activities",

    "display": "systemsettings kcm_kscreen",
    "monitors": "systemsettings kcm_kscreen",
    "night light": "systemsettings kcm_nightlight",

    "mouse": "systemsettings kcm_mouse",
    "touchpad": "systemsettings kcm_touchpad",
    "keyboard": "systemsettings kcm_keyboard",
    "keyboard layout": "systemsettings kcm_keyboard",
    "keyboard shortcuts": "systemsettings kcm_keys",
    "shortcuts": "systemsettings kcm_keys",
    "game controller": "systemsettings kcm_gamecontroller",
    "tablet": "systemsettings kcm_tablet",

    "power management": "systemsettings kcm_powerdevilprofilesconfig",
    "battery": "systemsettings kcm_powerdevilprofilesconfig",
    "energy info": "systemsettings kcm_energyinfo",

    "network": "systemsettings kcm_network",
    "network connections": "systemsettings kcm_networkmanagement",
    "wireless": "systemsettings kcm_mobile_wifi",
    "cellular": "systemsettings kcm_cellular_network",
    "hotspot": "systemsettings kcm_mobile_hotspot",
    "firewall": "systemsettings kcm_firewall",

    "audio": "systemsettings kcm_pulseaudio",
    "volume": "systemsettings kcm_pulseaudio",

    "users": "systemsettings kcm_users",
    "about": "systemsettings kcm_about-distro",
    "system info": "systemsettings kcm_about-distro",
    "feedback": "systemsettings kcm_feedback",
    "startup": "systemsettings kcm_autostart",
    "session": "systemsettings kcm_smserver",

    "login manager": "systemsettings kcm_sddm",

    "search": "systemsettings kcm_plasmasearch",
    "file search": "systemsettings kcm_baloofile",

    "notifications": "systemsettings kcm_notifications",
    "recent files": "systemsettings kcm_recentFiles",

    "regional settings": "systemsettings kcm_regionandlang",
    "date and time": "systemsettings kcm_clock",
    "spell checking": "systemsettings kcmspellchecking",

    "wallet": "systemsettings kcm_kwallet5",
    "proxy": "systemsettings kcm_proxy",
    "firmware security": "systemsettings kcm_firmware_security",
    "background services": "systemsettings kcm_kded",
    "screen locking": "systemsettings kcm_screenlocker",

    "cpu info": "systemsettings kcm_cpu",
    "memory info": "systemsettings kcm_memory",
    "opencl": "systemsettings kcm_opencl",
    "pci info": "systemsettings kcm_pci",
    "sensors": "systemsettings kcm_sensors",
    "glx info": "systemsettings kcm_glx",
    "vulkan": "systemsettings kcm_vulkan",
    "wayland info": "systemsettings kcm_wayland",
    "xserver info": "systemsettings kcm_xserver",
}


class KDEListener(EventListener):
    def on_event(self, event, extension):
        query = (event.get_argument() or "").strip().lower()
        results = []

        if not query:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon="icon.png",
                    name="Type to search KDE Settings…",
                    description="Examples: kde appearance, kde display, kde mouse",
                    on_enter=RunScriptAction("systemsettings", None),
                )
            ])

        for name, cmd in KCM_MAP.items():
            if query in name:
                results.append(
                    ExtensionResultItem(
                        icon="icon.png",
                        name=name.title(),
                        description=cmd,
                        on_enter=RunScriptAction(cmd, None)
                    )
                )

        if not results:
            results.append(
                ExtensionResultItem(
                    icon="icon.png",
                    name="System Settings",
                    description="Open KDE System Settings",
                    on_enter=RunScriptAction("systemsettings", None)
                )
            )

        return RenderResultListAction(results)


class KDEExtension(Extension):
    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KDEListener())


if __name__ == "__main__":
    KDEExtension().run()
