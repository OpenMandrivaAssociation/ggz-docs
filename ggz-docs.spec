Name:		ggz-docs
Summary:	GGZ Gaming Zone Documentation
Version:	0.0.14.1
Release:	5
License:	GPL
Group:		Games/Other
URL:		http://ggzgamingzone.org/
Source0:	http://ftp.ggzgamingzone.org/pub/ggz/%{version}/%{name}-%{version}.tar.bz2
Patch1:		ggz-docs-0.0.14-infoentry.patch
Patch2:		ggz-docs-0.0.14-destdir.patch
BuildRequires:	docbook-utils
BuildRequires:	openjade
BuildRequires:	lynx
BuildRequires:	texinfo
BuildRequires:	texi2html
BuildRequires:	texlive
BuildRequires:	docbook-utils-pdf
BuildRequires:	transfig
BuildRequires:	docbook-dtd31-sgml
BuildRequires:	ghostscript
BuildArch:	noarch

%description
Documentation for the GGZ Gaming Zone.

%prep
%setup -q
%patch1 -p1 -b .direntry
%patch2 -p1
autoreconf
find . -name texinfo.tex -exec rm {} \;

%build
# (Abel) no problem for noarch package to not use macros
# in fact it fails to build with macros
%configure \
	--enable-guides \
	--enable-spec \
	--prefix=%{_prefix} \
	--infodir=%{_infodir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# move docs back to build dir
rm -rf ./package-docs
mv %{buildroot}%{_docdir}/ggz-docs package-docs

%files
%doc package-docs/*
%{_infodir}/ggz-game-development-guide.info.*
%{_infodir}/ggz-hosting-guide.info.*



%changelog
* Wed Jun 06 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.0.14.1-5
+ Revision: 802954
- Correct destdir install for some documentation.
- Use %%configure macro.
- Add texlive to build requires.
- Use system wide texinfo.tex file.

  + Andrey Bondrov <abondrov@mandriva.org>
    - Fix BuildRequires
    - Drop some legacy junk, fix patch

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.0.14.1-3mdv2009.0
+ Revision: 245994
- rebuild

* Tue Feb 26 2008 Emmanuel Andry <eandry@mandriva.org> 0.0.14.1-1mdv2008.1
+ Revision: 175575
- New version

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.0.14-2mdv2008.1
+ Revision: 140737
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - convert prereq


* Fri Feb 23 2007 Emmanuel Andry <eandry@mandriva.org> 0.0.14-1mdv2007.0
+ Revision: 125149
- buildrequires docbook-dtd31-sgml
- Buildrequires transfig
- New version 0.0.14
- drop patches 0 and 2
- %%mkrel
- Import ggz-docs

* Thu Dec 02 2004 Abel Cheung <deaddog@mandrake.org> 0.0.9-2mdk
- Fix BuildRequires

* Sat Nov 27 2004 Abel Cheung <deaddog@mandrake.org> 0.0.9-1mdk
- New version
- P0: Fix docbook2html program name detection
- P1: Add info entry to .texi files
- P2: Fix game spec html file building
- Fix postin/un script
- Build guides/spec too

