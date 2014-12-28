#
# TODO:
# - how to build it?
#
Summary:	Simple filesystem configurator
Summary(pl.UTF-8):	Prosty konfigurator systemu plikïw
Name:		disk-manager
Version:	1.0.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://flomertens.free.fr/disk-manager/download/source/%{name}-%{version}.tar.gz
# Source0-md5:	904f47f2b2d51871fa4d0ee6f9051921
Patch0:     %{name}-pythonver.patch
URL:		http://flomertens.free.fr/disk-manager/
BuildRequires:	gettext-tools
BuildRequires:  intltool
BuildRequires:  python-pygtk-devel >= 2.6.0
#Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Disk manager is a simple filesystem configurator that allows you to:
- Automatically detect new partitions at startup.
- Fully manage configuration of filesystem.
- Enable/disable write support for NTFS.

%description -l pl.UTF-8
Disk manager jest prostym zarządcą systemu plików który pozwala Ci na:
- automatyczne wykrywanie nowych partycji podczas startu,
- kompleksowe zarządzanie konfiguracją systemów plików,
- włączenie/wyłączenie trybu zapisu dla NTFS-a.

%prep
%setup -q
%patch -p1

%build
%{__intltoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
