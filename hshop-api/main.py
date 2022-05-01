import PySimpleGUI as sg

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

    window = sg.Window("HShop API GUI", path_layout, icon=r"hs.ico")
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancel"):
            exit()
        elif event == "Submit":
            folder = values["-DOWNLOAD FOLDER-"]
            break
    window.close()

    search_layout = [
        [sg.Text("Input your search term:")],
        [sg.InputText("", enable_events=True, key="-QUERY-")],
        [sg.Submit("Submit", bind_return_key=True), sg.Cancel("Cancel")],
    ]
    window = sg.Window("HShop API GUI", search_layout, icon=r"hs.ico")
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancel"):
            exit()
        elif event == "Submit":
            query = values["-QUERY-"]
            break
    window.close()
    download_layout = []
    count_dict = {}
    for count, item in enumerate(search(query)):
        im = gen_qr_code(item["id"])
        count_dict[count] = item["id"]
        append_list = [
            sg.Text(f"{item['name']}"),
            sg.Text(f"Region: {item['subcategory']}"),
            sg.Text(f"Category: {item['category']}"),
            sg.Image(im),
            sg.Button("Download", key=count),
        ]
        download_layout.append(append_list)

    window = sg.Window(
        "HShop API GUI",
        [
            [
                sg.Column(
                    download_layout,
                    scrollable=True,
                    vertical_scroll_only=True,
                    element_justification="r",
                )
            ]
        ],
        resizable=True,
        finalize=True,
        icon=r"hs.ico",
    )
    while True:
        event, values = window.read()
        event_int = int(event[len(event) // 2 :])
        if event in (sg.WIN_CLOSED, "Cancel"):
            exit()
        elif event_int in count_dict:
            download(count_dict[event_int], folder)


if __name__ == "__main__":
    main()
