1 nocheck (since $DISPLAY is empty string)

since test xproto require a x display env
so bypass test via
%gocheck -d xproto
