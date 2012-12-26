#!/bin/bash

ORIGNAME=efl
VERSION=1.7.99
SVN_REVISION=81641
NAME=${ORIGNAME}-${VERSION}.svn${SVN_REVISION}

rm -rf ${ORIGNAME}
svn co -r $SVN_REVISION http://svn.enlightenment.org/svn/e/trunk/efl/ >/dev/null
find ${ORIGNAME} -name ".svn" -exec rm -rf {} \; 2>/dev/null
mv ${ORIGNAME} ${NAME}

tar cfJ ${NAME}.tar.xz ${NAME}
rm -rf ${NAME}
