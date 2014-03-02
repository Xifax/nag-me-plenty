update:
	pip install -r requirements.txt --use-mirrors

test:
	nosetests tests --nocapture

link-qt:
	cp -r /usr/lib/python2.7/site-packages/sip.so venv/lib/python2.7/site-packages/
	cp -r /usr/lib/python2.7/site-packages/PyQt4/ venv/lib/python2.7/site-packages/
