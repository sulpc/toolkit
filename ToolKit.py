# -*- coding: utf-8 -*-
'''
a simple tool launcher
- `ToolKit.json`: config file
- `ToolKit.ico`: icon file

layout like:
    *********************************
    * ***** ***** ***** ***** ***** *
    * *   * *   * *   * *   * *   * *
    * *   * *   * *   * *   * *   * *
    * ***** ***** ***** ***** ***** *
    * ***** ***** ***** ***** ***** *
    * *   * *   * *   * *   * *   * *
    * *   * *   * *   * *   * *   * *
    * ***** ***** ***** ***** ***** *
    *********************************
'''

import subprocess
import os
import wx
import json

class MainFrame(wx.Frame):
    def __init__(self, configs: dict):
        width   = configs['window']['width']
        height  = configs['window']['height']

        super().__init__(None, title = "ToolKit", size = (width, height))

        panel        = wx.Panel(self)
        vbox_all     = wx.BoxSizer(wx.VERTICAL)

        tools_list   = []
        row_limit    = configs['window']['row_limit']
        category_num = 0

        for category_name in configs['tools']:
            if category_num % row_limit == 0:                   # max cats in one row
                hbox_tmp = wx.BoxSizer(wx.HORIZONTAL)           # default: wx.HORIZONTAL
                vbox_all.Add(hbox_tmp, flag = wx.EXPAND | wx.ALL, border = 10)

            vbox_tmp = wx.BoxSizer(wx.VERTICAL)                 # a category

            label = wx.StaticText(panel, -1, category_name)
            vbox_tmp.Add(label, flag = wx.CENTER, border = 5)

            tools = configs['tools'][category_name]
            for cfg in tools:
                btn = wx.Button(panel, label = cfg['name'])
                btn.Bind(wx.EVT_BUTTON, lambda event, id=len(tools_list): self.on_clicks(event, id))

                vbox_tmp.Add(btn, flag = wx.EXPAND | wx.ALL, border = 5)
                tools_list.append(cfg)

            hbox_tmp.Add(vbox_tmp, proportion = 1, border = 5)  # proportion: proportion of each block

            category_num += 1

        panel.SetSizer(vbox_all)

        configs['tools'] = tools_list
        self.configs     = configs

    def on_clicks(self, event, id):
        cfg     = self.configs['tools'][id]
        cmd     = cfg['cmd']
        param   = cfg['param']

        if cmd in self.configs['alias']:
            cmd = self.configs['alias'][cmd]

        cmd = '%s %s' % (cmd, param)

        if len(cfg['wd']) != 0:
            wd = cfg['wd']
        else:
            wd = configs['cwd']

        if False:
            print(wd)
            print(cmd)
        else:
            os.chdir(wd)
            subprocess.Popen(cmd)   # , shell=True

if __name__ == '__main__':
    # load config
    with open('ToolKit.json', encoding='utf-8') as file:
        json_str = file.read()
        configs  = json.loads(json_str)

    configs['cwd'] = os.getcwd()

    app = wx.App()
    frame = MainFrame(configs)
    icon  = wx.Icon('ToolKit.ico')
    frame.SetIcon(icon)
    frame.Show()

    app.MainLoop()
