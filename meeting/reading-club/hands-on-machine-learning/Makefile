# @file           Makefile
# @brief          precompile beamer & mv to out
# @author         Kataoka Nagi
# @date           2021-03-14 16:31:05
# $Version:       1.0
# @par            History
#                 add TEX_TARGET
# Copyright (c) 2021 Kataoka Nagi
# - This src is released under the MIT License, see LICENSE.

OUT_DIR := ./out
TEX_TARGET := hands-on-ml_slides_chapter-nn-1st-half

# do all
.PHONY: all
all: $(TEX_TARGET).fmt mv

# precompile beamer preamble
$(TEX_TARGET).fmt: $(TEX_TARGET).tex
	eptex -ini -jobname="$(basename $<)" "&platex" mylatexformat.ltx $<

# move precompiled file to out folder
.PHONY: mv
mv: mvf mvl

.PHONY: mv
mvf: $(TEX_TARGET).fmt
	mv $< $(OUT_DIR)

.PHONY: mvl
mvl: $(TEX_TARGET).log
	mv $< $(OUT_DIR)

# clean precompiled file
.PHONY: cl
cl:
	rm $(OUT_DIR)/*.fmt $(OUT_DIR)/*.log
