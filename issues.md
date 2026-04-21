Issue 1:

PS C:\temp\QualityThought\qt_customer_support> uv add langgraph
Resolved 32 packages in 1.52s
Prepared 18 packages in 14.27s
░░░░░░░░░░░░░░░░░░░░ [1/31] packaging==26.1                                                                             warning: Failed to hardlink files; falling back to full copy. This may lead to degraded performance.
         If the cache and target directories are on different filesystems, hardlinking may not be supported.
         If this is intentional, set `export UV_LINK_MODE=copy` or use `--link-mode=copy` to suppress this warning.
error: Failed to install: jsonpatch-1.33-py2.py3-none-any.whl (jsonpatch==1.33)
  Caused by: failed to hardlink file from C:\Users\schin\AppData\Local\uv\cache\archive-v0\1CHFFZvYfiVgHAh3ySCQk\jsonpatch-1.33.dist-info\AUTHORS to C:\temp\QualityThought\qt_customer_support\.venv\Lib\site-packages\jsonpatch-1.33.dist-info\AUTHORS: The cloud operation cannot be performed on a file with incompatible hardlinks. (os error 396)

Solution:

echo $env:UV_CACHE_DIR
setx UV_CACHE_DIR c:\uv-cache  #This doesn't set in the current session, so be careful
echo $env:UV_CACHE_DIR

$env:UV_CACHE_DIR="c:\uv-cache"

