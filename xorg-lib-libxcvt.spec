Summary:	Library to generate VESA CVT standard timing modelines
Summary(pl.UTF-8):	Biblioteka do generowania linii trybów graficznych z czasami zgodnymi z VESA CVT
Name:		xorg-lib-libxcvt
Version:	0.1.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libxcvt-%{version}.tar.xz
# Source0-md5:	decb371ebd538956441d12f9ef522583
URL:		https://xorg.freedesktop.org/
BuildRequires:	meson >= 0.40.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxcvt is a library providing a standalone version of the X server
implementation of the VESA CVT standard timing modelines generator.

libxcvt also provides a standalone version of the command line tool
cvt copied from the Xorg implementation and is meant to be a direct
replacement to the version provided by the Xorg server.

%description -l pl.UTF-8
libxcvt to biblioteka udostępniająca samodzielną wersję generatora
linii trybów graficznych z czasami zgodnymi ze standardem VESA CVT,
zaimplementowanego w serwerze X.

libxcvt dostarcza także samodzielną wersję narzędzia linii poleceń
cvt, skopiowaną z implementacji Xorg, mającą być bezpośrednim
zamiennikiem polecenia udostępnianego przez serwer Xorg.

%package devel
Summary:	Header files for libxcvt library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxcvt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libxcvt library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libxcvt.

%package tools
Summary:	Tool to generate VESA CTV modelines for X.org server
Summary(pl.UTF-8):	Narzędzie do generowania opisów trybów graficznych (modeline) zgodnych z VESA CVT
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
# cvt tool
Conflicts:	xorg-xserver-server < 1.20.11-4
Conflicts:	xorg-xserver-server-tools < 1.20.12-2

%description tools
Tool to generate modelines for X.org server using VESA Coordinated
Video Timing.

%description tools
Narzędzie do generowania opisów trybów graficznych (modeline) przy
użyciu standardu VESA Coordinated Video Timing.

%prep
%setup -q -n libxcvt-%{version}

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README.md
%attr(755,root,root) %{_bindir}/cvt
%attr(755,root,root) %{_libdir}/libxcvt.so
%{_mandir}/man1/cvt.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/libxcvt
%{_pkgconfigdir}/libxcvt.pc
