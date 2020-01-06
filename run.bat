ECHO ON
ECHO Running ReMarkable edition add-on software...
cmd /k "cd /d Scripts & activate & remarkable_addons.exe & deactivate & cd /d .. & cd /d temp & del *.svg *.png *.jpg *.pdf"
pause