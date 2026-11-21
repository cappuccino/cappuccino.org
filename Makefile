#
# ./Makefile
# cappuccino.org
#
# Cappuccino site build and validation orchestration
#
# Created by David Richardson on 2026-11-21.
# Copyright (C) 2026 Cappuccino Project. All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
# USA

HUGO ?= hugo
HUGO_CONFIG ?= hugo.toml
PUBLIC_DIR ?= public
HUGO_FLAGS ?= --config $(HUGO_CONFIG)
SERVER_FLAGS ?= $(HUGO_FLAGS) --buildDrafts --buildFuture --navigateToChanged

.PHONY: all build serve check clean help

help:
	@printf "Targets:\n"
	@printf "  make build  Build the site into %s\n" "$(PUBLIC_DIR)"
	@printf "  make serve  Run the local Hugo development server\n"
	@printf "  make check  Run Hugo build and validation checks\n"
	@printf "  make clean  Remove generated build artifacts (%s and resources)\n" "$(PUBLIC_DIR)"
	@printf "  make help   Show this target summary\n"

all: check

build:
	$(HUGO) $(HUGO_FLAGS) --cleanDestinationDir

serve:
	$(HUGO) server $(SERVER_FLAGS)

check: clean build
	$(HUGO) $(HUGO_FLAGS) --printPathWarnings
	test -d "$(PUBLIC_DIR)"
	test -f "$(PUBLIC_DIR)/index.html"

clean:
	rm -rf "$(PUBLIC_DIR)" resources/_gen
