XSLTOPTS=

all: 3w 12-30w
3w: 3w.html 3w.pdf 3w.resolved.xml
12-30w: 12-30w.html 12-30w.pdf 12-30w.resolved.xml
remote: remoteSense.html remoteSense.xml
charger: batteryCharger.html batteryCharger.xml


%.resolved.xml: %.xml
	xmllint --xinclude $< > $@

%.html: %.resolved.xml html.xsl
	xsltproc $(XSLTOPTS) --output $@ html.xsl $<

%.fo: %.resolved.xml fo.xsl 
	xsltproc $(XSLTOPTS) --output $@ fo.xsl $<

#fop can be got from: http://xmlgraphics.apache.org/fop/download.html
%.pdf: %.fo
	../fop-1.0/fop $< $@

clean:
	rm -f *pdf *html *resolved.xml
