# Fix invalid keyboard layout typos.

This script takes data from clipboard, determines its language and based on that changes keyboard layout for that data.
Thus you are able to change keyboard layout postfactum.

### Examples:
<i>ghjuhfvvbhjdfybt -> программирование</i>  
<i>ПшеРги -> GitHub</i>  

It works only for english and russian layouts.  

### P.S.  
This is Linux version. It could be cross-platform and simpler using <i>clipboard</i> library but solution is based primarily on Linux cmd to avoid Python dependencies (to easily bind this script to a keyboard shortcut).


