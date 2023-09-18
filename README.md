# toolkit
A simple tool launcher to organize your various tools, simple but useful.

## Usage

`ToolKit.json` is the configuration file.

- `alias` used to manage your different versions of command line tools, like `java8`, `java11`, `java17`.

- `tools` contains a number of categories, each of which can be added to a number of tools.
  - `name` will be displayed in the interface.
  - `wd` is the working directory of the tool.
  - `cmd` is the main command of the tool, here you can use the previous `alias` configuration.
  - `param` is the parameter that may be needed for the command.
  - Of these above, `name` and `cmd` are required.

- `window` configures the window of the toolkit, the default is `400x300`, and show up to five in a row.

`ToolKit.ico` is the icon of ToolKit.
