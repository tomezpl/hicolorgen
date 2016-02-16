gimp --no-interface -b '(define 
		srcimg (car (gimp-file-load RUN-NONINTERACTIVE "$PATH_TO_SRCIMG" "$PATH_TO_SRCIMG"))
	) 
	(gimp-image-scale srcimg $NEW_WIDTH $NEW_HEIGHT) 
	(define 
		srcdrawable (car (gimp-image-get-active-drawable srcimg)) 
	)
	(gimp-file-save RUN-NONINTERACTIVE srcimg srcdrawable "$PATH_TO_DESTIMG" "$PATH_TO_DESTIMG")' -b '(gimp-quit RUN-NONINTERACTIVE)'
