XSLTOPTS=

all: 3w 12-30w
3w: 3w.html 3w.pdf
12-30w: 12-30w.html 12-30w.pdf
remote: remoteSense.html remoteSense.xml
charger: batteryCharger.html batteryCharger.xml

%.html: %.xml html.xsl
	xmllint --xinclude $< > resolved.xml
	xsltproc $(XSLTOPTS) --xinclude  --output $@ html.xsl resolved.xml

%.fo: %.xml fo.xsl 
	xsltproc $(XSLTOPTS) --xinclude --output $@ fo.xsl $<

#fop can be got from: http://xmlgraphics.apache.org/fop/download.html
%.pdf: %.fo
	../fop-1.0/fop $< $@

clean:
	rm -f *pdf *html
