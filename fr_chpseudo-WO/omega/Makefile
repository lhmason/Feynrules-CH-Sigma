# $Id: Makefile.omega.in 3435 2011-07-24 22:20:34Z cnspeckn $

prefix = /Users/laramason/.whizard
install = /usr/bin/install -c
libpath = /usr/local/lib/omega
ocamlopt = /Users/laramason/.opam/4.06.1/bin/ocamlopt.opt
ocamlflags = 

libdir = $(libpath)/caml

default: all

include Makefile.src

all: $(binaries)

install: all
	$(install) -d -m 755 $(prefix)/bin
	$(install) -m 755 $(binaries) $(prefix)/bin

clean:
	-rm -f $(binaries) *.cmx *.cmi *.o

%.cmi: %.mli
	$(ocamlopt) $(ocamlflags) -I $(libdir) -c $<
%.cmx: %.ml
	$(ocamlopt) $(ocamlflags) -I $(libdir) -c $<

.PHONY: all install clean
