%define version 0.0.14
%define release %mkrel 1

Name:		ggz-docs
Summary:	GGZ Gaming Zone Documents
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Other
Source0:	http://ftp.ggzgamingzone.org/pub/ggz/%{version}/%{name}-%{version}.tar.bz2
Patch1:		%{name}-0.0.9-infoentry.patch
URL:		http://ggzgamingzone.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	docbook-utils
BuildRequires:	openjade
BuildRequires:	lynx
BuildRequires:	texinfo
BuildRequires:	tetex-texi2html
BuildRequires:	docbook-utils-pdf
BuildRequires:	transfig
BuildRequires:	docbook-dtd31-sgml
Requires(post):		info-install
Requires(preun):		info-install

%description
Documents for the GGZ Gaming Zone.

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# move docs back to build dir
rm -rf ./package-docs
mv $RPM_BUILD_ROOT/%{_docdir}/ggz-docs package-docs

%post
%_install_info ggz-game-development-guide.info
%_install_info ggz-hosting-guide.info

%preun
%_remove_install_info ggz-game-development-guide.info
%_remove_install_info ggz-hosting-guide.info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc package-docs/*
%{_infodir}/ggz-game-development-guide.info.*
%{_infodir}/ggz-hosting-guide.info.*


