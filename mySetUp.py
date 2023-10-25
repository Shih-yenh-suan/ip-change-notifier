from distutils.core import setup
import py2exe

INCLUDES = []

options = {
    "py2exe":
        {
            "compressed": 1,  # 压缩
            "optimize": 2,
            "bundle_files": 1,  # 所有文件打包成一个 exe 文件
            "includes": INCLUDES,
            "dll_excludes": ["MSVCR100.dll"]
        }
}


setup(
    options=options,
    description="detect change in IP",
    console=[{"script": ".\监测IP\监测IP变化并提示.py"}])
