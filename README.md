# pyinstaller-tutorial
## Usage
1. `pip install PyQt6`
2. Download [QtDesigner](https://build-system.fman.io/qt-designer-download)
3. create a `.ui` file using QtDesigner
4. convert the `.ui`file to `.py`file by: `pyuic6 abc.ui > abc.py` [[example](https://github.com/leoxiang66/pyinstaller-tutorial/blob/desktop-app-1/gui/ui_tempate.py)]
5. inherit this class and implement signal functions [[example](https://github.com/leoxiang66/pyinstaller-tutorial/blob/desktop-app-1/gui/ui.py)]
6. write an entry-script `main.py` [[example](https://github.com/leoxiang66/pyinstaller-tutorial/blob/desktop-app-1/main.py)]
7. pyinstaller: `pyinstaller -F --noconsole main.py`



the binary file is stored in `dist`
