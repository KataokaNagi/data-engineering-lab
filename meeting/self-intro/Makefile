# @file           Makefile
# @brief          precompile beamer & mv to out
# @author         Kataoka Nagi
# @date           2021-03-14 16:31:05
# $Version:       1.0
# @par            History
#                 New file
# Copyright (c) 2021 Kataoka Nagi
# - This src is released under the MIT License, see LICENSE.

OUT_DIR := ./out

# do all
.PHONY: all
all: *.fmt mv

# precompile beamer preamble
%.fmt: %.tex
	eptex -ini -jobname="$(basename $<)" "&platex" mylatexformat.ltx $<

# move precompiled file to out folder
.PHONY: mv
mv: mvf mvl

.PHONY: mvf
mvf: *.fmt
	mv $< $(OUT_DIR)

.PHONY: mvl
mvl: *.log
	mv $< $(OUT_DIR)

# clean precompiled file
.PHONY: cl
cl:
	rm $(OUT_DIR)/*.fmt $(OUT_DIR)/*.log
