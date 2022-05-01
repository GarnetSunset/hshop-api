import io

import PySimpleGUI as sg
from PIL import Image

from functions import *


def main():
    sg.theme("DarkBlue1")

    def text_label(text):
        return sg.Text(text + ":", justification="r", size=(15, 1))

    path_layout = [
        [sg.Text("Choose path to save files to:")],
        [
            text_label("Download Folder"),
            sg.Input(key="-DOWNLOAD FOLDER-"),
            sg.FolderBrowse(target="-DOWNLOAD FOLDER-"),
        ],
        [sg.Submit("Submit", bind_return_key=True), sg.Cancel("Cancel")],
    ]

    # window = sg.Window("HShop API GUI", path_layout, keep_on_top=True, finalize=True)
    # while True:
    #     event, values = window.read()
    #     if event in (sg.WIN_CLOSED, "Cancel"):
    #         exit()
    #     elif event == "Submit":
    #         folder = values["-DOWNLOAD FOLDER-"]
    #         break
    # window.close()

    search_layout = [
        [sg.Text("Input your search term:")],
        [sg.InputText("", enable_events=True, key="-QUERY-")],
        [sg.Submit("Submit", bind_return_key=True), sg.Cancel("Cancel")],
    ]
    window = sg.Window("HShop API GUI", search_layout, keep_on_top=True, finalize=True)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancel"):
            exit()
        elif event == "Submit":
            query = values["-QUERY-"]
            break
    window.close()

    download_layout = []
    for item in search(query):
        im = gen_qr_code(item["id"])
        append_list = [
            [sg.Text(f"{item['name']}")],
            [sg.Text(f"Region: {item['subcategory']}")],
            [sg.Text(f"Category: {item['category']}")],
            [sg.Image(im)],
            [sg.HorizontalSeparator()],
        ]
        download_layout.append(append_list)

    final_download_layout = [
        sg.Column(download_layout, scrollable=True, vertical_scroll_only=True)
    ]

    width, height = sg.Window.get_screen_size()
    window = sg.Window(
        "HShop API GUI",
        final_download_layout,
        keep_on_top=True,
        finalize=True,
        size=(int(width / 4), int(height / 2)),
    )
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancel"):
            exit()
        elif event == "Submit":
            query = values["-INPUT-"]
            break
    window.close()


if __name__ == "__main__":
    main()
