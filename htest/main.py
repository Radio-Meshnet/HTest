###########################################################################################
#
# ĦTest
#
# Copyright (c) 2024 Hydraledger / hydraledger.tech / GPLv3 License
#
###########################################################################################


__debug_build__ = False
__version__ = "0.0.1"
__version_variant__ = "beta"
__version_date_time__ = "2024-09-29 00:00"
__copyright_short__ = "Copyright (c) 2024 Hydraledger / hydraledger.tech / GPLv3 License"
__copyright_url__ = "https://hydraledger.tech"
__title__ = "ĦTest"
__header__ = "Welcome to ĦTest tool!"
__description__ = "Test tool for the Hydraledger iop-python module"
__author__ = "Hydraledger"
__author_email__ = "info@hydraledger.tech"
__package_domain__ = "tech.hydraledger"
__package_name__ = "htest"


from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from kivy.properties import StringProperty
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.label import MDLabel


import os
import sys
import json
import requests
from mnemonic import Mnemonic


import importlib
if importlib.util.find_spec("iop_python") != None:
    import iop_python as sdk
    iop = sdk.IopPython()


from kivy.logger import Logger, LOG_LEVELS

if __debug_build__:
    Logger.setLevel(LOG_LEVELS["debug"])
else:
    Logger.setLevel(LOG_LEVELS["error"])


KV = """
#: import SlideTransition kivy.uix.screenmanager.SlideTransition

MDNavigationLayout:
    md_bg_color: app.theme_cls.bg_darkest

    ScreenManager:
        id: screen_manager
        transition: SlideTransition()

        MDScreen:
            name: "main"

            BoxLayout:
                orientation: "vertical"

                MDBoxLayout:
                    orientation: "vertical"
                    spacing: dp(0)
                    size_hint_y: None
                    height: dp(20)
                    padding: [dp(10), dp(0), dp(10), dp(0)]
                    md_bg_color: app.theme_cls.primary_color

                    MDLabel:
                        id: header
                        text: ""
                        text_size: self.width, None
                        shorten: True
                        shorten_from: "right"
                        theme_text_color: "Custom"
                        text_color: [1, 1, 1, 1]
                        height: dp(20)
                        bold: True
                        halign: "center"

                MDTopAppBar:
                    id: toolbar
                    title: ""
                    anchor_title: "left"
                    elevation: 0
                    left_action_items:
                        [
                        ["power-standby", lambda x: app.close(), ""],
                        ]
                    right_action_items:
                        [
                        ["clipboard-outline", lambda x: app.log_copy(), ""],
                        ["trash-can", lambda x: app.log_delete(), ""],
                        ]

                MDBottomNavigation:
                    id: tabs
                    selected_color_background: 0, 0, 0, 0
                    transition_duration: 0


                    MDBottomNavigationItem:
                        id: execute_tab
                        name: "execute_tab"
                        text: "Execute"
                        icon: "cogs"

                        ScrollView:
                            effect_cls: "ScrollEffect"
                            size_hint: 1.0, 1.0
                            bar_width: dp(10)
                            bar_color: [.7, .7, .7, .9]
                            bar_inactive_color: [.7, .7, .7, .9]
                            scroll_type: ["bars", "content"]
                            scroll_wheel_distance: dp(100)

                            MDBoxLayout:
                                orientation: "vertical"
                                spacing: dp(15)
                                size_hint_y: None
                                height: self.minimum_height
                                padding: [dp(10), dp(10), dp(10), dp(10)]

                                MDCard:
                                    orientation: "vertical"
                                    spacing: dp(20)
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: [dp(10), dp(10), dp(10), dp(10)]
                                    radius: [0]

                                    MDLabel:
                                        text: "Local iop-python functions"
                                        font_style: "H6"

                                    MDLabel:
                                        markup: True
                                        text: "The following options use the local sdk functionalities."
                                        size_hint_y: None
                                        text_size: self.width, None
                                        height: self.texture_size[1]

                                    MDRectangleFlatButton:
                                        text: "get_hyd_vault"
                                        size_hint: [1.0, None]
                                        on_release: app.get_hyd_vault()

                                    MDRectangleFlatButton:
                                        text: "get_morpheus_vault"
                                        size_hint: [1.0, None]
                                        on_release: app.get_morpheus_vault()

                                    MDRectangleFlatButton:
                                        text: "get_wallet_address"
                                        size_hint: [1.0, None]
                                        on_release: app.get_wallet_address()

                                    MDRectangleFlatButton:
                                        text: "generate_nonce"
                                        size_hint: [1.0, None]
                                        on_release: app.generate_nonce()

                                    MDRectangleFlatButton:
                                        text: "generate_phrase"
                                        size_hint: [1.0, None]
                                        on_release: app.generate_phrase()

                                    MDRectangleFlatButton:
                                        text: "generate_did_by_morpheus"
                                        size_hint: [1.0, None]
                                        on_release: app.generate_did_by_morpheus()

                                    MDRectangleFlatButton:
                                        text: "sign_witness_statement"
                                        size_hint: [1.0, None]
                                        on_release: app.sign_witness_statement()

                                    MDRectangleFlatButton:
                                        text: "verify_signed_statement"
                                        size_hint: [1.0, None]
                                        on_release: app.verify_signed_statement()

                                MDCard:
                                    orientation: "vertical"
                                    spacing: dp(20)
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: [dp(10), dp(10), dp(10), dp(10)]
                                    radius: [0]

                                    MDLabel:
                                        text: "Online API functions"
                                        font_style: "H6"

                                    MDLabel:
                                        markup: True
                                        text: "The following options retrieve data via api from a blockchain server."
                                        size_hint_y: None
                                        text_size: self.width, None
                                        height: self.texture_size[1]

                                    MDRectangleFlatButton:
                                        text: "api_account_get"
                                        size_hint: [1.0, None]
                                        on_release: app.api_account_get()

                                    MDRectangleFlatButton:
                                        text: "api_account_balance_get"
                                        size_hint: [1.0, None]
                                        on_release: app.api_account_balance_get()

                                    MDRectangleFlatButton:
                                        text: "api_nonce_get"
                                        size_hint: [1.0, None]
                                        on_release: app.api_nonce_get()

                                    MDRectangleFlatButton:
                                        text: "api_transactions_get"
                                        size_hint: [1.0, None]
                                        on_release: app.api_transactions_get()

                                    MDRectangleFlatButton:
                                        text: "api_delegates_get"
                                        size_hint: [1.0, None]
                                        on_release: app.api_delegates_get()


                                MDCard:
                                    orientation: "vertical"
                                    spacing: dp(20)
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: [dp(10), dp(10), dp(10), dp(10)]
                                    radius: [0]

                                    MDLabel:
                                        text: "Add a transaction"
                                        font_style: "H6"

                                    MDLabel:
                                        markup: True
                                        text: "Here you can perform a transaction with the local sdk and online api."
                                        size_hint_y: None
                                        text_size: self.width, None
                                        height: self.texture_size[1]

                                    MDBoxLayout:
                                        orientation: "horizontal"
                                        size_hint_y: None
                                        height: self.minimum_height
                                        padding: [dp(0), dp(0), dp(0), dp(0)]

                                        MDTextField:
                                            id: api_transactions_add_address
                                            multiline: True
                                            hint_text: "Destination address"
                                            helper_text: ""
                                            helper_text_mode: "persistent"
                                            text: ""
                                            disabled: False
                                            write_tab: False
                                            text_color_focus: app.theme_cls.text_color
                                            text_color_normal: app.theme_cls.text_color

                                        MDIconButton:
                                            icon: "clipboard-outline"
                                            padding: [dp(0), dp(0), dp(0), dp(0)]
                                            icon_size: dp(24)
                                            on_release: app.api_transactions_add_address_paste()

                                    MDTextField:
                                        id: api_transactions_add_amount
                                        multiline: False
                                        hint_text: "Amount"
                                        helper_text: ""
                                        helper_text_mode: "persistent"
                                        text: "0.001"
                                        disabled: False
                                        write_tab: False
                                        text_color_focus: app.theme_cls.text_color
                                        text_color_normal: app.theme_cls.text_color

                                    MDTextField:
                                        id: api_transactions_add_comment
                                        multiline: True
                                        hint_text: "Comment/Purpose (Optional)"
                                        helper_text: ""
                                        helper_text_mode: "persistent"
                                        text: ""
                                        disabled: False
                                        write_tab: False
                                        text_color_focus: app.theme_cls.text_color
                                        text_color_normal: app.theme_cls.text_color

                                    MDTextField:
                                        id: api_transactions_add_fee
                                        multiline: False
                                        hint_text: "Fee"
                                        helper_text: ""
                                        helper_text_mode: "persistent"
                                        text: "0.01301764"
                                        disabled: False
                                        write_tab: False
                                        text_color_focus: app.theme_cls.text_color
                                        text_color_normal: app.theme_cls.text_color

                                    MDRectangleFlatButton:
                                        text: "api_transactions_add - Sign/Prepare"
                                        size_hint: [1.0, None]
                                        on_release: app.api_transactions_add_sign()

                                    MDRectangleFlatButton:
                                        text: "api_transactions_add - Send/Execute to Blockchain"
                                        size_hint: [1.0, None]
                                        on_release: app.api_transactions_add_send()


                    MDBottomNavigationItem:
                        id: log_tab
                        name: "log_tab"
                        text: "Log"
                        icon: "text"

                        RecycleView:
                            id: log_view
                            viewclass: "LogViewRow"
                            effect_cls: "ScrollEffect"
                            size_hint: 1.0, 1.0
                            bar_width: dp(10)
                            bar_color: [.7, .7, .7, .9]
                            bar_inactive_color: [.7, .7, .7, .9]
                            scroll_type: ["bars", "content"]
                            scroll_wheel_distance: dp(100)
                            RecycleBoxLayout:
                                spacing: dp(0)
                                default_size: None, None
                                default_size_hint: 1, None
                                orientation: "vertical"
                                size_hint_y: None
                                height: self.minimum_height
                                padding: [dp(10), dp(0), dp(10), dp(0)]


                    MDBottomNavigationItem:
                        id: cfg_tab
                        name: "cfg_tab"
                        text: "Config"
                        icon: "tools"

                        ScrollView:
                            effect_cls: "ScrollEffect"
                            size_hint: 1.0, 1.0
                            bar_width: dp(10)
                            bar_color: [.7, .7, .7, .9]
                            bar_inactive_color: [.7, .7, .7, .9]
                            scroll_type: ["bars", "content"]
                            scroll_wheel_distance: dp(100)

                            MDBoxLayout:
                                orientation: "vertical"
                                spacing: dp(20)
                                size_hint_y: None
                                height: self.minimum_height
                                padding: [dp(10), dp(10), dp(10), dp(10)]

                                MDCard:
                                    orientation: "vertical"
                                    spacing: dp(20)
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: [dp(10), dp(10), dp(10), dp(10)]
                                    radius: [0]

                                    MDRectangleFlatButton:
                                        text: "Reset Config"
                                        size_hint: [1.0, None]
                                        on_release: app.cfg_reset()

                                    MDRectangleFlatButton:
                                        text: "Load config"
                                        size_hint: [1.0, None]
                                        on_release: app.cfg_load()

                                    MDRectangleFlatButton:
                                        text: "Save config"
                                        size_hint: [1.0, None]
                                        on_release: app.cfg_save()

                                MDCard:
                                    orientation: "vertical"
                                    spacing: dp(20)
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: [dp(10), dp(10), dp(10), dp(10)]
                                    radius: [0]

                                    MDTextField:
                                        id: cfg_phrase
                                        multiline: True
                                        hint_text: "Restore phrase"
                                        helper_text: "Default: Empty"
                                        helper_text_mode: "persistent"
                                        text: ""
                                        write_tab: False
                                        disabled: False
                                        text_color_focus: app.theme_cls.text_color
                                        text_color_normal: app.theme_cls.text_color

                                    MDRectangleFlatButton:
                                        text: "Generate phrase"
                                        size_hint: [1.0, None]
                                        on_release: app.cfg_phrase_generate()

                                    MDRectangleFlatButton:
                                        text: "Copy phrase"
                                        size_hint: [1.0, None]
                                        on_release: app.cfg_phrase_copy()

                                    MDRectangleFlatButton:
                                        text: "Paste phrase"
                                        size_hint: [1.0, None]
                                        on_release: app.cfg_phrase_paste()

                                MDCard:
                                    orientation: "vertical"
                                    spacing: dp(20)
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: [dp(10), dp(10), dp(10), dp(10)]
                                    radius: [0]

                                    MDTextField:
                                        id: cfg_password
                                        multiline: False
                                        hint_text: "Password"
                                        helper_text: "Default: unlockPassword"
                                        helper_text_mode: "persistent"
                                        text: ""
                                        disabled: False
                                        write_tab: False
                                        text_color_focus: app.theme_cls.text_color
                                        text_color_normal: app.theme_cls.text_color

                                    MDTextField:
                                        id: cfg_idx
                                        multiline: False
                                        hint_text: "Address index"
                                        helper_text: "Default: 0"
                                        helper_text_mode: "persistent"
                                        text: ""
                                        disabled: False
                                        write_tab: False
                                        text_color_focus: app.theme_cls.text_color
                                        text_color_normal: app.theme_cls.text_color

                                    MDTextField:
                                        id: cfg_network
                                        multiline: False
                                        hint_text: "Network (mainnet/devnet/testnet)"
                                        helper_text: "Default: mainnet"
                                        helper_text_mode: "persistent"
                                        text: ""
                                        disabled: False
                                        write_tab: False
                                        text_color_focus: app.theme_cls.text_color
                                        text_color_normal: app.theme_cls.text_color

                                    MDTextField:
                                        id: cfg_server
                                        multiline: False
                                        hint_text: "Server (DNS or IP without Port)"
                                        helper_text: "Default: explorer.hydraledger.tech"
                                        helper_text_mode: "persistent"
                                        text: ""
                                        disabled: False
                                        write_tab: False
                                        text_color_focus: app.theme_cls.text_color
                                        text_color_normal: app.theme_cls.text_color


                    MDBottomNavigationItem:
                        id: infos_tab
                        name: "infos_tab"
                        text: "Infos"
                        icon: "information-variant"
                        on_tab_release: app.infos_action()

                        ScrollView:
                            effect_cls: "ScrollEffect"
                            size_hint: 1.0, 1.0
                            bar_width: dp(10)
                            bar_color: [.7, .7, .7, .9]
                            bar_inactive_color: [.7, .7, .7, .9]
                            scroll_type: ["bars", "content"]
                            scroll_wheel_distance: dp(100)

                            MDBoxLayout:
                                orientation: "vertical"
                                spacing: dp(15)
                                size_hint_y: None
                                height: self.minimum_height
                                padding: [dp(10), dp(10), dp(10), dp(10)]

                                MDCard:
                                    orientation: "vertical"
                                    spacing: dp(20)
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: [dp(10), dp(10), dp(10), dp(10)]
                                    radius: [0]

                                    MDLabel:
                                        id: infos_copyright_title
                                        text: ""
                                        font_style: "H6"

                                    MDLabel:
                                        id: infos_copyright_text
                                        markup: True
                                        text: ""
                                        size_hint_y: None
                                        text_size: self.width, None
                                        height: self.texture_size[1]

                                MDCard:
                                    orientation: "vertical"
                                    spacing: dp(20)
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: [dp(10), dp(10), dp(10), dp(10)]
                                    radius: [0]

                                    MDLabel:
                                        text: "Your current account address"
                                        font_style: "H6"

                                    MDLabel:
                                        id: infos_account
                                        markup: True
                                        text: ""
                                        size_hint_y: None
                                        text_size: self.width, None
                                        height: self.texture_size[1]

                                    MDRectangleFlatButton:
                                        text: "Copy"
                                        size_hint: [1.0, None]
                                        on_release: app.infos_account_copy()

                                MDCard:
                                    orientation: "vertical"
                                    spacing: dp(20)
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: [dp(10), dp(10), dp(10), dp(10)]
                                    radius: [0]

                                    MDLabel:
                                        text: "Your current restore phrase"
                                        font_style: "H6"

                                    MDLabel:
                                        id: infos_phrase
                                        markup: True
                                        text: ""
                                        size_hint_y: None
                                        text_size: self.width, None
                                        height: self.texture_size[1]

                                    MDRectangleFlatButton:
                                        text: "Copy"
                                        size_hint: [1.0, None]
                                        on_release: app.infos_phrase_copy()


<LogViewRow>:
    text: root.text
    markup: True
    size_hint_y: None
    text_size: self.width, None
    height: self.texture_size[1]
"""


class LogViewRow(MDLabel):
    text = StringProperty()


class MainApp(MDApp):
    #################################################
    # Init/Build                                    #
    #################################################


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.log_init()

        self.cfg_init()

        self.api_transactions_add = None


    def on_start(self):
        self.cfg_load()
        self.root.ids.toolbar.title = __title__
        self.root.ids.header.text = __header__


    def build(self):
        return Builder.load_string(KV)


    def close(self):
        self.stop()


    #################################################
    # Execute                                       #
    #################################################


    def get_hyd_vault(self):
        try:
            phrase = self.root.ids.cfg_phrase.text.strip()
            password = self.root.ids.cfg_password.text.strip()
            network = self.root.ids.cfg_network.text.strip()
            account = 0
            result = iop.get_hyd_vault(phrase, password, network, account)
            self.log(result, "get_hyd_vault")
            return result
        except Exception as e:
            self.log_exception(e, "get_hyd_vault")
            return ""


    def get_morpheus_vault(self):
        try:
            phrase = self.root.ids.cfg_phrase.text.strip()
            password = self.root.ids.cfg_password.text.strip()
            result = iop.get_morpheus_vault(phrase, password)
            self.log(result, "get_morpheus_vault")
            return result
        except Exception as e:
            self.log_exception(e, "get_morpheus_vault")
            return ""


    def get_wallet_address(self):
        try:
            phrase = self.root.ids.cfg_phrase.text.strip()
            password = self.root.ids.cfg_password.text.strip()
            network = self.root.ids.cfg_network.text.strip()
            account = 0
            idx = int(self.root.ids.cfg_idx.text.strip())
            vault = iop.get_hyd_vault(phrase, password, network, account)
            result = iop.get_wallet_address(vault, account, idx, network)
            self.log(result, "get_wallet_address")
            return result
        except Exception as e:
            self.log_exception(e, "get_wallet_address")
            return ""


    def generate_nonce(self):
        try:
            result  = iop.generate_nonce()
            self.log(result, "generate_nonce")
            return result
        except Exception as e:
            self.log_exception(e, "generate_nonce")
            return ""


    def generate_phrase(self):
        try:
            result = iop.generate_phrase()
            self.log(result, "generate_phrase")
            return result
        except Exception as e:
            self.log_exception(e, "generate_phrase")
            return ""


    def generate_did_by_morpheus(self):
        try:
            phrase = self.root.ids.cfg_phrase.text.strip()
            password = self.root.ids.cfg_password.text.strip()
            idx = int(self.root.ids.cfg_idx.text.strip())
            morpheus_vault = iop.get_morpheus_vault(phrase, password)
            result = iop.generate_did_by_morpheus(morpheus_vault, password, idx)
            self.log(result, "generate_did_by_morpheus")
            return result
        except Exception as e:
            self.log_exception(e, "generate_did_by_morpheus")
            return ""


    def sign_witness_statement(self):
        try:
            phrase = self.root.ids.cfg_phrase.text.strip()
            password = self.root.ids.cfg_password.text.strip()
            network = self.root.ids.cfg_network.text.strip()
            account = 0
            idx = int(self.root.ids.cfg_idx.text.strip())
            vault = iop.get_hyd_vault(phrase, password, network, account)

            statement = {
                "name": "Max Mustermann",
                "street": "Musterstreet",
                "dob": "01/01/1990",
                "city": "Berlin",
                "country": "Grmany",
                "zipcode": "10178",
            }

            statement = json.dumps(statement)
            result = iop.sign_witness_statement(vault, password, statement, idx)
            self.log(result, "sign_witness_statement")
        except Exception as e:
            self.log_exception(e, "sign_witness_statement")


    def verify_signed_statement(self):
        try:
            signed_statement = {
                "signature": "00987890098776556667788976676787655",
                "claim": {
                    "subject": "did:morpheus:ezbeWGSY2dqcUBqT8K7R14xr",
                    "content": {}
                }
            }

            signed_statement = json.dumps(signed_statement)
            result = iop.verify_signed_statement(signed_statement)
            self.log(result, "verify_signed_statement")
        except Exception as e:
            self.log_exception(e, "verify_signed_statement")


    def api_account_get(self):
        try:
            wallet_address = self.get_wallet_address()
            server = self.root.ids.cfg_server.text.strip()
            url = f"http://{server}:4703/api/v2/wallets/{wallet_address}"
            response = requests.get(url, timeout=2)

            if response.status_code == 200:
                data = response.json()
                self.log(json.dumps(data, indent=4), "api_account_get")
        except Exception as e:
            self.log_exception(e, "api_account_get")


    def api_account_balance_get(self):
        try:
            wallet_address = self.get_wallet_address()
            server = self.root.ids.cfg_server.text.strip()
            url = f"http://{server}:4703/api/v2/wallets/{wallet_address}"
            response = requests.get(url, timeout=2)

            if response.status_code == 200:
                data = response.json()
                text = data["data"]["balance"]+" = "+str(float(int(data["data"]["balance"])/100000000))
                self.log(text, "api_account_balance_get")
                return int(data["data"]["balance"])
        except Exception as e:
            self.log_exception(e, "api_account_balance_get")
            return 0


    def api_nonce_get(self):
        try:
            wallet_address = self.get_wallet_address()
            server = self.root.ids.cfg_server.text.strip()
            url = f"http://{server}:4703/api/v2/wallets/{wallet_address}"
            response = requests.get(url, timeout=2)

            if response.status_code == 200:
                data = response.json()
                self.log(data["data"]["nonce"], "api_nonce_get")
                return int(data["data"]["nonce"])
        except Exception as e:
            self.log_exception(e, "api_nonce_get")
            return 0


    def api_transactions_get(self):
        try:
            wallet_address = self.get_wallet_address()
            server = self.root.ids.cfg_server.text.strip()
            url = f"http://{server}:4703/api/v2/wallets/{wallet_address}/transactions"
            response = requests.get(url, timeout=2)

            if response.status_code == 200:
                data = response.json()
                self.log(json.dumps(data, indent=4), "api_transactions_get")
        except Exception as e:
            self.log_exception(e, "api_transactions_get")


    def api_delegates_get(self):
        try:
            wallet_address = self.get_wallet_address()
            server = self.root.ids.cfg_server.text.strip()
            url = f"http://{server}:4703/api/v2/delegates?page=1&limit=8&orderBy=rank:asc"
            response = requests.get(url, timeout=2)

            if response.status_code == 200:
                data = response.json()
                self.log(json.dumps(data, indent=4), "api_delegates_get")
        except Exception as e:
            self.log_exception(e, "api_delegates_get")


    def api_transactions_add_address_paste(self):
        self.root.ids.api_transactions_add_address.text = Clipboard.paste().strip()
        self.root.ids.header.text = "OK: Address pasted"


    def api_transactions_add_sign(self):
        try:
            address = self.root.ids.api_transactions_add_address.text.strip()
            amount = float(self.root.ids.api_transactions_add_amount.text.strip().replace(",", "."))
            text = str(amount)
            amount = int(amount*100000000)
            text += " = "+str(amount)
            self.root.ids.api_transactions_add_amount.helper_text = text
            nonce = self.api_nonce_get()
            phrase = self.root.ids.cfg_phrase.text.strip()
            password = self.root.ids.cfg_password.text.strip()
            account = 0
            idx = int(self.root.ids.cfg_idx.text.strip())
            network = self.root.ids.cfg_network.text.strip()
            comment = self.root.ids.api_transactions_add_comment.text.strip()
            fee = float(self.root.ids.api_transactions_add_fee.text.strip().replace(",", "."))
            text = str(fee)
            fee = int(fee*100000000)
            text += " = "+str(fee)
            self.root.ids.api_transactions_add_fee.helper_text = text

            result = iop.sign_transaction(
                iop.get_hyd_vault(phrase, password, network, account),
                address,
                amount,
                nonce,
                password,
                account,
                idx,
                network,
                comment if comment else None,
                fee if fee else None
            )
            self.api_transactions_add = result
            self.log(result, "api_transactions_add_sign")
        except Exception as e:
            self.api_transactions_add = None
            self.log_exception(e, "api_transactions_add_sign")


    def api_transactions_add_send(self):
        try:
            server = self.root.ids.cfg_server.text.strip()
            url = f"http://{server}:4703/api/v2/transactions"
            response = requests.post(url, timeout=2, json=json.loads(self.api_transactions_add))

            if response.status_code == 200:
                self.api_transactions_add = None
                data = response.json()
                self.log(json.dumps(data, indent=4), "api_transactions_add_send")
        except Exception as e:
            self.log_exception(e, "api_transactions_add_send")


    #################################################
    # Log                                           #
    #################################################


    def log_init(self):
        self.log_data = []


    def log(self, text="", title=""):
        if title != "":
            print("----"+title+"----")
            self.root.ids.header.text = title
            title = "\n\n[b]"+title+"[/b]\n"
        print(text)
        self.root.ids.log_view.data.append({"text": title+text})


    def log_copy(self):
        self.root.ids.header.text = "OK: Log copied"
        text = "\n".join(item["text"] for item in self.root.ids.log_view.data)
        Clipboard.copy(text)


    def log_delete(self):
        self.root.ids.header.text = "OK: Log deleted"
        self.root.ids.log_view.data = []


    def log_exception(self, e, title=""):
        import traceback
        if type(e).__name__ == "PyIopError":
            text = "An "+str(type(e))+" occurred: "+str(e.args[0].message)
        else:
            text = "An "+str(type(e))+" occurred: "+str(e)
        self.log(text=text, title="ERROR: "+title)
        self.log(text="".join(traceback.TracebackException.from_exception(e).format()))


    #################################################
    # Cfg                                           #
    #################################################


    def cfg_init(self):
        self.cfg = None

        def get_platform():
            if "ANDROID_ARGUMENT" in os.environ:
                return "android"
            elif "ANDROID_ROOT" in os.environ:
                return "android"
            else:
                return sys.platform

        if get_platform() == "android":
            from plyer import storagepath
            self.cfg_dir = storagepath.get_application_dir()+"/"+__package_domain__+"."+__package_name__+"/files"
        elif get_platform() == "darwin":
            from plyer import storagepath
            self.cfg_dir = storagepath.get_home_dir().replace("file://", "")+"/.config/"+__package_name__
        elif get_platform() == "linux":
            from plyer import storagepath
            self.cfg_dir = storagepath.get_home_dir().replace("file://", "")+"/.config/"+__package_name__
        elif str(get_platform()).startswith("win"):
            from plyer import storagepath
            self.cfg_dir = storagepath.get_home_dir().replace("file://", "")+"/.config/"+__package_name__
        else:
            from plyer import storagepath
            self.cfg_dir = storagepath.get_home_dir().replace("file://", "")+"/.config/"+__package_name__

        if not os.path.isdir(self.cfg_dir):
            os.makedirs(self.cfg_dir)

        self.cfg_file = self.cfg_dir+"/config.json"


    def cfg_load(self):
        try:
            if os.path.exists(self.cfg_file):
                with open(self.cfg_file, "r") as fh:
                    self.cfg = json.load(fh)
        except:
            pass

        if not self.cfg or len(self.cfg) == 0:
            self.cfg_reset()

        self.root.ids.cfg_phrase.text = self.cfg["cfg_phrase"].strip()
        self.root.ids.cfg_password.text = self.cfg["cfg_password"].strip()
        self.root.ids.cfg_idx.text = self.cfg["cfg_idx"].strip()
        self.root.ids.cfg_network.text = self.cfg["cfg_network"].strip()
        self.root.ids.cfg_server.text = self.cfg["cfg_server"].strip()

        self.root.ids.header.text = "OK: Config loaded"


    def cfg_reset(self):
        mnemo = Mnemonic("english")

        self.cfg = {
            "cfg_phrase": mnemo.generate(strength=256),
            "cfg_password": "unlockPassword",
            "cfg_idx": "0",
            "cfg_network": "mainnet",
            "cfg_server": "explorer.hydraledger.tech"
        }

        try:
            with open(self.cfg_file, "w") as fh:
                json.dump(self.cfg, fh)
        except:
            pass

        self.cfg_load()

        self.root.ids.header.text = "OK: Config reset"


    def cfg_save(self):
        self.cfg = {
            "cfg_phrase": self.root.ids.cfg_phrase.text.strip(),
            "cfg_password": self.root.ids.cfg_password.text.strip(),
            "cfg_idx": self.root.ids.cfg_idx.text.strip(),
            "cfg_network": self.root.ids.cfg_network.text.strip(),
            "cfg_server": self.root.ids.cfg_server.text.strip()
        }

        try:
            with open(self.cfg_file, "w") as fh:
                json.dump(self.cfg, fh)
        except:
            pass

        self.root.ids.header.text = "OK: Config saved"


    def cfg_phrase_generate(self):
        mnemo = Mnemonic("english")
        self.root.ids.cfg_phrase.text = mnemo.generate(strength=256)
        self.root.ids.header.text = "OK: Phrase generated"


    def cfg_phrase_copy(self):
        Clipboard.copy(self.root.ids.cfg_phrase.text.strip())
        self.root.ids.header.text = "OK: Phrase copied"


    def cfg_phrase_paste(self):
        self.root.ids.cfg_phrase.text = Clipboard.paste().strip()
        self.root.ids.header.text = "OK: Phrase pasted"


    #################################################
    # Infos                                         #
    #################################################


    def infos_action(self):
        self.root.ids.infos_copyright_title.text = __title__+" v"+__version__+" "+__version_variant__
        self.root.ids.infos_copyright_text.text = __copyright_short__

        self.root.ids.infos_account.text = self.get_wallet_address()
        self.root.ids.infos_phrase.text = self.root.ids.cfg_phrase.text.strip()


    def infos_account_copy(self):
        Clipboard.copy(self.root.ids.infos_account.text.strip())
        self.root.ids.header.text = "OK: Account address copied"


    def infos_phrase_copy(self):
        Clipboard.copy(self.root.ids.infos_phrase.text.strip())
        self.root.ids.header.text = "OK: Phrase copied"


#################################################
# Run                                           #
#################################################


from kivy.base import ExceptionManager, ExceptionHandler
class AppExceptionHandler(ExceptionHandler):
    def handle_exception(self, e):
        if isinstance(e, SystemExit):
            return ExceptionManager.RAISE

        import traceback
        print("An unhandled "+str(type(e))+" exception occurred: "+str(e))
        print("".join(traceback.TracebackException.from_exception(e).format()))

        return ExceptionManager.PASS


if __name__ == "__main__":
    MainApp().run()
