all: ToolKit.exe

ToolKit.exe: ToolKit.py ToolKit.ico
	pyinstaller.exe -F -w -i ToolKit.ico ToolKit.py
	mv dist/ToolKit.exe ./

clean:
	rm -rf build dist ToolKit.spec

clean_all:
	rm -rf build dist ToolKit.spec ToolKit.exe