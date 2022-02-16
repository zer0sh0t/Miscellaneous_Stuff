#!/usr/bin/bash
set -e
net stop spooler
del %systemroot%\System32\spool\printers\* /Q
net start spooler
