
## lib_export

独立成为各个模块之后，需要在当前目录的文件下，自动生成

``` dart

library changshuo_logic_configure;
// configure/names
export 'configs/names/bundle_names.dart';
export 'configs/names/cs_method_names.dart';
export 'configs/names/media_method_names.dart';

```

## 使用

在`User/.zshrc`或`User/.bashrc`中加入

```sh
 ## 自定义python脚本
 alias lib_export='python3 /Users/freedom/Documents/108/code/flutter_tool_kit/lib_export/lib_export.py'
```
刷新配置文件，`source .zshrc(.bashrc)`

进入工程目录后，敲入lib_export即可