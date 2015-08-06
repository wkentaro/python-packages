#!/bin/sh
julius \
    -C `brew --prefix julius-dictation-kit`/share/main.jconf \
    -C `brew --prefix julius-dictation-kit`/share/am-gmm.jconf \
    -module
