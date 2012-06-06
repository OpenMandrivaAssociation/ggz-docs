Name:		ggz-docs
Summary:	GGZ Gaming Zone Documentation
Version:	0.0.14.1
Release:	5
License:	GPL
Group:		Games/Other
URL:		http://ggzgamingzone.org/
Source0:	http://ftp.ggzgamingzone.org/pub/ggz/%{version}/%{name}-%{version}.tar.bz2
Patch1:		ggz-docs-0.0.14-infoentry.patch
BuildRequires:	docbook-utils
BuildRequires:	openjade
BuildRequires:	lynx
BuildRequires:	texinfo
BuildRequires:	tetex-texi2html
BuildRequires:	docbook-utils-pdf
BuildRequires:	transfig
BuildRequires:	docbook-dtd31-sgml
BuildArch:	noarch

%description
Documentation for the GGZ Gaming Zone.

%prep
%setup -q
%patch1 -p1 -b .direntry

%build
# (Abel) no problem for noarch package to not use macros
# in fact it fails to build with macros
./configure \
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

